import os
import csv
from wanted.models import Company, CompanyLang, Tag, TagLang, CompanyTag
from manage import app, db 
# 나중에 코어로 바꾸기
# https://velog.io/@samnaka/sqlalchemy-bulk-insert


def tear_up(db):
    with open('wanted_temp_data.csv','r', encoding='utf-8') as f:
        rdr = csv.reader(f)

        next(rdr, None)
        all_tag = []
        all_taglang_ko = []
        all_taglang_en = []
        all_taglang_jp = []
        for i in range(1,31):
            tag_num = str(i)
            all_tag.append(Tag(id=tag_num))
            all_taglang_ko.append(TagLang(tag_id=tag_num,name="태그_" + tag_num, lang="ko"))
            all_taglang_en.append(TagLang(tag_id=tag_num,name="tag_" + tag_num, lang="en"))
            all_taglang_jp.append(TagLang(tag_id=tag_num,name="タグ_" + tag_num, lang="jp"))
        db.session.bulk_save_objects(all_tag)
        db.session.bulk_save_objects(all_taglang_ko)
        db.session.bulk_save_objects(all_taglang_en)
        db.session.bulk_save_objects(all_taglang_jp)
        db.session.commit()

        all_company = []
        all_company_lang_ko = []
        all_company_lang_en = []
        all_company_lang_jp = []
        all_company_tag = []
        for idx, line in enumerate(rdr):
            line_company_id = str(idx+1)
            all_company.append(Company(id=line_company_id))

            if line[0]:
                all_company_lang_ko.append(CompanyLang(lang="ko", company_id=line_company_id, name=line[0]))

            if line[1]:
                all_company_lang_en.append(CompanyLang(lang="en", company_id=line_company_id, name=line[1]))    

            if line[2]:
                all_company_lang_jp.append(CompanyLang(lang="jp", company_id=line_company_id, name=line[1]))       

            for tag in line[3].split("|"):
                all_company_tag.append(CompanyTag(company_id=line_company_id, tag_id=str(tag[3:])))

        db.session.bulk_save_objects(all_company)
        db.session.bulk_save_objects(all_company_lang_ko)
        db.session.bulk_save_objects(all_company_lang_en)
        db.session.bulk_save_objects(all_company_lang_jp)
        db.session.bulk_save_objects(all_company_tag)
        db.session.commit()
if __name__ == '__main__':
    with app.app_context():
        tear_up(db)
