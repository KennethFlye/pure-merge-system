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

    def getListOfVariables(self):
        variables = ['id', 'submitter', 'authors', 'title', 'comments', 'journalRef', 'doi', 'reportNumber',
                     'categories', 'license', 'abstract', 'versions', 'updateDate']

        return variables

