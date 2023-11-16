import datetime


class Article:

    def __init__(self, id, submitter, authors, title, comments, journal_ref, doi, report_number, categories,
                 license, abstract, versions, update_date):
        self.id = id
        self.submitter = submitter
        self.submitter_is_preferred = None
        self.authors = authors
        self.authors_is_preferred = None
        self.title = title
        self.title_is_preferred = None
        self.comments = comments
        self.comments_is_preferred = None
        self.journal_ref = journal_ref
        self.journal_ref_is_preferred = None
        self.doi = doi
        self.doi_is_preferred = None
        self.report_number = report_number
        self.report_number_is_preferred = None
        self.categories = categories
        self.categories_is_preferred = None
        self.license = license
        self.license_is_preferred = None
        self.abstract = abstract
        self.abstract_is_preferred = None
        self.versions = versions
        self.versions_is_preferred = None
        self.update_date = update_date
        self.update_date_is_preferred = None
        self.group = None

    def __str__(self):
        return (f'Id: {self.id}, submitter: {self.submitter}, authors: {self.authors}, title: {self.title}, '
                f'comments: {self.comments}, journal_ref: {self.journal_ref}, doi: {self.doi}, '
                f'report_number: {self.report_number}, categories: {self.categories}, license: {self.license}, '
                f'abstract: {self.abstract}, versions: {self.versions}, update_date: {self.update_date}')

    @staticmethod
    def getListOfVariables():
        variables = ['id', 'submitter', 'authors', 'title', 'comments', 'journal_ref', 'doi', 'report_number',
                     'categories', 'license', 'abstract', 'versions', 'update_date']

        return variables

    def to_json(self):
        return {
            "id": self.id,
            "submitter": self.submitter,
            "submitter_is_preferred": self.submitter_is_preferred,
            "authors": self.authors,
            "authors_is_preferred": self.authors_is_preferred,
            "title": self.title,
            "title_is_preferred": self.title_is_preferred,
            "comments": self.comments,
            "comments_is_preferred": self.comments_is_preferred,
            "journal_ref": self.journal_ref,
            "journal_ref_is_preferred": self.journal_ref_is_preferred,
            "doi": self.doi,
            "doi_is_preferred": self.doi_is_preferred,
            "report_number": self.report_number,
            "report_number_is_preferred": self.report_number_is_preferred,
            "categories": self.categories,
            "categories_is_preferred": self.categories_is_preferred,
            "license": self.license,
            "license_is_preferred": self.license_is_preferred,
            "abstract": self.abstract,
            "abstract_is_preferred": self.abstract_is_preferred,
            "versions": self.versions,
            "versions_is_preferred": self.versions_is_preferred,
            "update_date": str(self.update_date),  # NOTE, DATE IS NOW A STRING, VERY BIG NOTE HERE PLS DON'T FORGET
            "update_date_is_preferred": self.update_date_is_preferred,
            "group": self.group
        }
