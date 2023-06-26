# from docx import Document
# from behave import given, when, then
#
# from features.steps.helpers import test_docx
#
#
# # Manually add testing files and attributes
#
# @given('a document having a styles part')
# def step_given_document_with_a_styles_state(context):
#     context.doc = Document(test_docx('sty-having-styles-part'))
#
# @given('a document having no styles part')
# def step_given_document_with_no_styles_state(context):
#     context.doc = Document(test_docx('sty-having-no-styles-part'))
#
#
# @then('len(styles) is {style_count}')
# def step_then_len_styles_is_style_count(context, style_count):
#     styles = context.doc.styles
#     assert len(styles) == int(style_count)
#
# @then('I can iterate over its styles')
# def step_then_can_iterate_over_styles(context):
#     styles = context.doc.styles
#     for style in styles:
#         assert style is not None
#
# @then('I can access a style by style id')
# def step_then_can_access_style_by_id(context):
#     styles = context.doc.styles
#     assert styles['DefaultParagraphFont'].style_id is not None
#
# @then('I can access a style by its UI name')
# def step_then_can_access_style_by_ui_name(context):
#     styles = context.doc.styles
#     assert styles['Default Paragraph Font'].name is not None
