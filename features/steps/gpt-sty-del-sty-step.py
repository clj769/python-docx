# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# @given('a document having known styles')
# def step_given_document_with_known_styles(context):
#     context.document = Document(test_docx('sty-known-styles'))
#     context.initial_style_count = len(context.document.styles)
#
# @when('I delete a style')
# def step_when_delete_a_style(context):
#     context.deleted_style_name = context.document.styles['No List'].name
#     context.document.styles['No List'].delete()
#
# @then('the document has one fewer styles')
# def step_then_document_has_one_fewer_style(context):
#     assert len(context.document.styles) == context.initial_style_count - 1
#
# @then('the deleted style is not in the styles collection')
# def step_then_deleted_style_not_in_styles(context):
#     assert context.deleted_style_name not in context.document.styles
