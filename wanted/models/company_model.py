from sqlalchemy import func
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class BaseMixIn:
    __table_args__ = {
        'mysql_engine': 'InnoDB',
        'mysql_charset': 'utf8mb4',
        'mysql_collate': 'utf8mb4_general_ci'
    }
    id = db.Column(db.Integer, primary_key=True)

class Company(BaseMixIn, db.Model):
    __tablename__ = "Company"
    created_at = db.Column(db.DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


class CompanyLang(BaseMixIn, db.Model):
    __tablename__ = "CompanyLang"

    lang = db.Column(db.String(50))
    company_id = db.Column(db.Integer, db.ForeignKey('Company.id'))
    name = db.Column(db.String(50), index=True)
    company = db.relationship(
        'Company', backref=('company_lang')
    )


class Tag(BaseMixIn, db.Model):
    __tablename__ = "Tag"
    created_at = db.Column(db.DateTime, nullable=False, default=func.utc_timestamp())
    updated_at = db.Column(db.DateTime, nullable=False, default=func.utc_timestamp(), onupdate=func.utc_timestamp())


class TagLang(BaseMixIn, db.Model):
    __tablename__ = "TagLang"
    tag_id = db.Column(db.Integer, db.ForeignKey('Tag.id'))
    name = db.Column(db.String(50))
    lang = db.Column(db.String(50))
    tag = db.relationship(
        'Tag', backref=('tag_lang')
    )

class CompanyTag(BaseMixIn, db.Model):
    __tablename__ = "CompanyTag"
    company_id = db.Column(db.Integer, db.ForeignKey('Company.id'))
    tag_id = db.Column(db.Integer, db.ForeignKey('Tag.id'), index=True)
    tag = db.relationship(
        'Tag', backref=('compnay_tag')
    )
    company = db.relationship('Company', backref=('company_tag'))
