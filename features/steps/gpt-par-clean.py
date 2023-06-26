# from behave import given, when, then
# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
# from features.steps.helpers import test_docx
#
#
# @given('a paragraph with content and formatting')
# def step_given_a_paragraph_with_content_and_formatting(context):
#     # Create a new Document
#     doc = Document(test_docx('par-known-paragraphs'))
#     # Add a new paragraph with content and formatting
#     context.paragraph = doc.add_paragraph('Some text')
#     context.paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
#     context.original_formatting = context.paragraph.paragraph_format
#
# @when('I clear the paragraph content')
# def step_when_i_clear_the_paragraph_content(context):
#     # Clear the paragraph content
#     for run in context.paragraph.runs:
#         context.paragraph.clear()
#
# @then('the paragraph has no content')
# def step_then_the_paragraph_has_no_content(context):
#     # Check if the paragraph has no content
#     assert not context.paragraph.text, 'Paragraph still has content'
#
# @then('the paragraph formatting is preserved')
# def step_then_the_paragraph_formatting_is_preserved(context):
#     # Check if the paragraph formatting is preserved
#     assert context.paragraph.paragraph_format == context.original_formatting, 'Paragraph formatting has changed'
