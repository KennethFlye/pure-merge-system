import datetime


class Article:

    def __init__(self, id, submitter, authors, title, comments, journalRef, doi, reportNumber, categories, license, abstract, versions, updateDate, authorsParsed):
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
        self.authorsParsed = authorsParsed

    def __str__(self):
        return f'Id: {self.id}, submitter: {self.submitter}, author: {self.author}, title: {self.title}, comments: {self.comments}, journalRef: {self.journalRef}, doi: {self.doi}, reportNumber: {self.reportNumber}, categories: {self.categories}, license: {self.license}, abstract: {self.abstract}, versions: {self.versions}, updateDate: {self.updateDate}, authorsParsed: {self.authorsParsed}'

    def getListOfVariables(self):
        variables = ['id', 'submitter', 'author', 'title', 'comments', 'journalRef', 'doi', 'reportNumber', 'categories', 'license', 'abstract', 'versions', 'updateDate', 'authorsParsed']

        return variables

