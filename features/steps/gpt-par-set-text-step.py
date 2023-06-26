# from behave import given, when, then
# from docx import Document
#
# @given('a paragraph with content and formatting')
# def step_given_a_paragraph_with_content_and_formatting(context):
#     # Create a new Document and add a paragraph with content and formatting
#     context.doc = Document()
#     context.para = context.doc.add_paragraph()
#     context.para.add_run('Some content').bold = True
#     context.original_formatting = context.para.paragraph_format
#
# @when('I set the paragraph text')
# def step_when_i_set_the_paragraph_text(context):
#     # Set the text for the paragraph
#     context.para.text = 'New content'
#
# @then('the paragraph has the text I set')
# def step_then_the_paragraph_has_the_text_i_set(context):
#     # Check if the paragraph has the text I set
#     assert context.para.text == 'New content', 'The paragraph does not have the text I set'
#
# @then('the paragraph formatting is preserved')
# def step_then_the_paragraph_formatting_is_preserved(context):
#     # Check if the paragraph formatting is preserved
#     assert context.para.paragraph_format == context.original_formatting, 'The paragraph formatting is not preserved'
