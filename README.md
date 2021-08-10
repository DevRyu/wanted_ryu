### 실행 방법
- `docker-compose up` 으로 실행합니다.

DB migration, insert 에러시 컨테이너에서 아래 명령어를 치시면 정상 작동합니다.
- `flask db upgrade`
- `python insert_data.py`

### API 명세
```
[회사 검색] [GET]
http://localhost:5000/companies?name :str
required : querystring(name)

[태그명으로 회사 검색] [GET]
http://localhost:5000/companies/tags?name :str
required : querystring(name)


[회사 태그 삭제] [DELETE]
http://localhost:5000/companies/<company_id :int>/tag?id :int
required : resource(company id), querystring(id)

[회사 태그 추가] [POST]
http://localhost:5000/companies/<company_id :int>/tags
json request body
{"tag-id": int}

required : resource(company id), json body(tag-id)

```
예시)
https://documenter.getpostman.com/view/9188758/Tzz4SLGk
위 링크로 접속하시면 됩니다.