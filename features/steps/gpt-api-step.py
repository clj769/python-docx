# from behave import given, when, then
# import docx
# from docx import Document
# from helpers import test_docx
# import pkg_resources
#
# # api-steps ====================================================
#
# @given('I have python-docx installed')
# def step_given_python_docx_installed(context):
#     assert pkg_resources.get_distribution('python-docx')
#
# @when('I call docx.Document() with the path of a .docx file')
# def step_when_open_specified_document(context):
#     context.document = Document(test_docx('doc-default'))
#
# @then('document is a Document object')
# def step_then_document_is_a_document_object(context):
#
#     #assert isinstance(context.document, Document)
#     assert isinstance(context.document, docx.document.Document)
# @when('I call docx.Document() with no arguments')
# def step_when_open_default_document(context):
#     context.document = Document()
