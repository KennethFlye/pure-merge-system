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

    def to_json(a_list):
        return {
            "id": a_list[0],  # id and id preference is skipped
            "submitter": a_list[2],
            "submitter_is_preferred": a_list[3],
            "authors": a_list[4],
            "authors_is_preferred": a_list[5],
            "title": a_list[6],
            "title_is_preferred": a_list[7],
            "comments": a_list[8],
            "comments_is_preferred": a_list[9],
            "journal_ref": a_list[10],
            "journal_ref_is_preferred": a_list[11],
            "doi": a_list[12],
            "doi_is_preferred": a_list[13],
            "report_number": a_list[14],
            "report_number_is_preferred": a_list[15],
            "categories": a_list[16],
            "categories_is_preferred": a_list[17],
            "license": a_list[18],
            "license_is_preferred": a_list[19],
            "abstract": a_list[20],
            "abstract_is_preferred": a_list[21],
            "versions": a_list[22],
            "versions_is_preferred": a_list[23],
            "update_date": a_list[24],  # string?
            "update_date_is_preferred": a_list[25],
            "group": a_list[26]
        }
