# from behave import given, then
# from docx import Document
# from docx.text.paragraph import ParagraphFormat
# from features.steps.helpers import test_docx
#
#
# @given('a style of type {style_type}')
# def step_given_style_of_type(context, style_type):
#     context.document = Document(test_docx('sty-known-styles'))
#
#     if style_type == 'WD_STYLE_TYPE.CHARACTER':
#         style = 'Default Paragraph Font'
#     elif style_type == 'WD_STYLE_TYPE.PARAGRAPH':
#         style = 'Normal'
#     elif style_type == 'WD_STYLE_TYPE.LIST':
#         style = 'No List'
#     elif style_type == 'WD_STYLE_TYPE.TABLE':
#         style = 'Normal Table'
#     else:
#         raise ValueError(f"Unsupported style type: {style_type}")
#
#     context.style = context.document.styles[style]
#
# @then('style.paragraph_format is the ParagraphFormat object for the style')
# def step_then_style_paragraph_format_is_paragraph_format_object(context):
#     assert isinstance(context.style.paragraph_format, ParagraphFormat)
