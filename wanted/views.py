import logging
import itertools
from flask import Blueprint, request

from manage import db
from wanted.models import Company, CompanyLang, TagLang, CompanyTag

api = Blueprint('api', __name__)

'''
회사명 자동완성
회사명의 일부만 들어가도 검색이 되어야 합니다.
'''
@api.route('/companies', methods=['GET'])
def search_company():
    result = []

    try:
        request_context = request.args.get('name')
        query = CompanyLang.query.filter(CompanyLang.name.like(f"%{request_context}%")).all()
        for i in query:
            result.append({"company":i.name, "lang":i.lang})
    except Exception as e:
        logging.info(e)

    return {"result": result }, 200

'''
태그명으로 회사 검색
태그로 검색 관련된 회사가 검색되어야 합니다.
다국어로 검색이 가능해야 합니다.
일본어 태그로 검색을 해도 한국 회사가 노출이 되어야 합니다.
タグ_4로 검색 했을 때, 원티드랩 회사 정보가 노출이 되어야 합니다.
동일한 회사는 한번만 노출이 되어야합니다.
'''
def uniq(lst):
    for _, grp in itertools.groupby(lst, lambda d: (d['company_id'])):
        yield list(grp)[0]


@api.route('/companies/tags', methods=['GET'])
def search_company_by_tag():
    result = []

    try:
        request_context = request.args.get('name')

        tag = TagLang.query.filter(TagLang.name == request_context).one()
        companies = CompanyLang.query.join(Company).join(CompanyTag).filter_by(tag_id=tag.tag_id).all()
        for company in companies:
            result.append({'company': company.name, 'company_id': company.company_id})

    except Exception as e:
        logging.info(e)

    return {'result': list(uniq(result))}, 200

'''
회사 태그 정보 추가
'''
@api.route('/companies/<int:company_id>/tags', methods=['POST'])
def add_company_tag(company_id):
    try:
        request_context = dict(request.json)
        tag = request_context['id']
        company_id = int(company_id)
        company_tag = CompanyTag(company_id=company_id, tag_id=tag)
        db.session.add(company_tag)
        db.session.commit()
    except Exception as e:
        logging.info(e)
    # except IntegrityError:
    #     return '', 403
    return 'tag add', 201

'''
회사 태그 정보 삭제
'''
@api.route('/companies/<int:company_id>/tag', methods=['DELETE'])
def remove_company_tag(company_id):
    try:
        tag_id = int(request.args.get('id'))
        company_id = int(company_id)
        CompanyTag.query.filter_by(company_id = company_id, tag_id = tag_id).delete()
        db.session.commit()
    except Exception as e:
        logging.info(e)
    return '', 204