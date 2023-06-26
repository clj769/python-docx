# from docx import Document
# from behave import given, when, then
#
# @given('a blank document')
# def step_given_a_blank_document(context):
#     context.doc = Document()
#
# @given('a document')
# def step_given_a_document(context):
#     context.doc = Document()
#     context.doc.add_paragraph('Initial paragraph')
#
# @when('I add a paragraph without specifying text or style')
# def step_when_add_paragraph_without_text_or_style(context):
#     context.para = context.doc.add_paragraph()
#
# @when('I add a paragraph specifying its text')
# def step_when_add_paragraph_with_text(context):
#     context.added_text = "Test Text"  # using 'added_text' instead of 'text'
#     context.para = context.doc.add_paragraph(context.added_text)
#
# @when('I add a paragraph specifying its style as a {style_spec}')
# def step_when_add_paragraph_with_style(context, style_spec):
#     context.style_spec = style_spec
#
#     if style_spec == 'style object':
#         # assuming that you have a style object named 'MyStyle'
#         style = context.doc.styles['Normal']
#     elif style_spec == 'style name':
#         # ensure that the style with this name exists in your document
#         style = 'Normal'  # use an existing style name
#
#     context.style = style
#
#     context.para = context.doc.add_paragraph(style=style)
#
# @then('the last paragraph is the empty paragraph I added')
# def step_then_last_paragraph_is_empty(context):
#     last_para = context.doc.paragraphs[-1]
#     assert last_para.text == ""
#
# @then('the last paragraph contains the text I specified')
# def step_then_last_paragraph_contains_specified_text(context):
#     last_para = context.doc.paragraphs[-1]
#     assert last_para.text == context.added_text  # using 'added_text' instead of 'text'
#
#
# @then('the last paragraph has the style I specified')
# def step_then_last_paragraph_has_specified_style(context):
#     last_para = context.doc.paragraphs[-1]
#
#     if context.style_spec == 'style object':
#         assert last_para.style.name == 'Normal'
#     else:
#         assert last_para.style.name == context.style
