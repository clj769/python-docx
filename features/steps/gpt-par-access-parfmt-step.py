# from behave import given, then
# from docx import Document
# from docx.text.paragraph import ParagraphFormat
#
# @given('a paragraph')
# def step_given_a_paragraph(context):
#     # Create a new Document
#     doc = Document()
#     # Add a new paragraph
#     context.paragraph = doc.add_paragraph('A sample paragraph.')
#
# @then('paragraph.paragraph_format is its ParagraphFormat object')
# def step_then_paragraph_format_is_its_paragraph_format_object(context):
#     # Ensure paragraph.paragraph_format is ParagraphFormat object
#     assert isinstance(context.paragraph.paragraph_format, ParagraphFormat), "paragraph.paragraph_format is not a ParagraphFormat object"
