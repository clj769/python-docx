# from behave import given, when, then
# from docx import Document
# from docx.shared import Pt
#
# @given('a paragraph having {style} style')
# def step_given_a_paragraph_with_a_style(context, style):
#
#     if style == 'no specified':
#         expected_value = 'Normal'
#     elif style == 'a missing':
#         expected_value = 'Normal'
#     elif style == 'Heading 1':
#         expected_value = 'Heading 1'
#     elif style == 'Body Text':
#         expected_value = 'Body Text'
#
#     context.doc = Document()
#     context.paragraph = context.doc.add_paragraph(style=expected_value)
#
# @then('paragraph.style is {expected_value}')
# def step_then_paragraph_style_is(context, expected_value):
#     assert context.paragraph.style.name == expected_value, \
#         f"Expected {expected_value}, but got {context.paragraph.style.name}"
#
# @given('a paragraph')
# def step_given_a_paragraph(context):
#     context.doc = Document()
#     context.paragraph = context.doc.add_paragraph()
#
# @when('I assign a {style_spec} to paragraph.style')
# def step_when_i_assign_a_style_to_paragraph(context, style_spec):
#     style = context.style = context.doc.styles['Normal']
#     if style_spec == 'style object':
#         style
#     else:
#         # ensure that the style with this name exists in your document
#         style = 'Normal'  # use an existing style name
#
#     context.paragraph.style = style
#
# @then('the paragraph has the style I set')
# def step_then_paragraph_has_the_style_i_set(context):
#     assert context.paragraph.style == context.style, \
#         f"Expected {context.style}, but got {context.paragraph.style}"
