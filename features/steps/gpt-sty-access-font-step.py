# from behave import given, then
# from docx import Document
# from docx.text.font import Font
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
# @then('style.font is the Font object for the style')
# def step_then_style_font_is_font_object(context):
#     assert isinstance(context.style.font, Font)
