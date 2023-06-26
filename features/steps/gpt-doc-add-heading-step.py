# from behave import given, when, then
# from docx import Document
#
# heading_text = 'Sample Heading'
#
# @given('a document having built-in styles')
# def step_given_a_document_with_styles(context):
#     context.doc = Document()
#
# @when('I add a heading specifying only its text')
# def step_when_add_heading_with_only_text(context):
#     context.doc.add_heading(heading_text)
#
# @then('the style of the last paragraph is \'Heading 1\'')
# def step_then_style_of_last_paragraph_is_heading_1(context):
#     assert context.doc.paragraphs[-1].style.name == 'Heading 1'
#
# @then('the last paragraph contains the heading text')
# def step_then_last_paragraph_contains_heading_text(context):
#     assert context.doc.paragraphs[-1].text == heading_text
#
# @when('I add a heading specifying level={level:d}')
# def step_when_add_heading_with_level(context, level):
#     context.doc.add_heading(heading_text, level=level)
#
# @then('the style of the last paragraph is \'{style}\'')
# def step_then_style_of_last_paragraph_is_given(context, style):
#     assert context.doc.paragraphs[-1].style.name == style
