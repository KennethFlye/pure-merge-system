import datetime


class Article:

    def __init__(self, id, submitter, authors, title, comments, journalRef, doi, reportNumber, categories, license, abstract, versions, updateDate):
        self.id = id
        self.submitter = submitter
        self.authors = authors
        self.title = title
        self.comments = comments
        self.journalRef = journalRef
        self.doi = doi
        self.reportNumber = reportNumber
        self.categories = categories
        self.license = license
        self.abstract = abstract
        self.versions = versions
        self.updateDate = updateDate

    def __str__(self):
        return (f'Id: {self.id}, submitter: {self.submitter}, authors: {self.authors}, title: {self.title}, '
                f'comments: {self.comments}, journalRef: {self.journalRef}, doi: {self.doi}, '
                f'reportNumber: {self.reportNumber}, categories: {self.categories}, license: {self.license}, '
                f'abstract: {self.abstract}, versions: {self.versions}, updateDate: {self.updateDate}')

    @staticmethod
    def getListOfVariables():
        variables = ['id', 'submitter', 'authors', 'title', 'comments', 'journalRef', 'doi', 'reportNumber',
                     'categories', 'license', 'abstract', 'versions', 'updateDate']

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
