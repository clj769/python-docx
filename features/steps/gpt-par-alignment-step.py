# from behave import given, then
# from docx import Document
# from docx.enum.text import WD_ALIGN_PARAGRAPH
#
# @given('a paragraph having {align_type} alignment')
# def step_given_a_paragraph_with_alignment(context, align_type):
#     # Create a new Document
#     doc = Document()
#     # Add a new paragraph
#     paragraph = doc.add_paragraph()
#     # Set paragraph alignment
#     if align_type == 'inherited':
#         pass  # Do nothing, the default alignment is inherited
#     elif align_type == 'left':
#         paragraph.alignment = WD_ALIGN_PARAGRAPH.LEFT
#     elif align_type == 'center':
#         paragraph.alignment = WD_ALIGN_PARAGRAPH.CENTER
#     elif align_type == 'right':
#         paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
#     context.paragraph = paragraph
#
# @then('the paragraph alignment property value is {align_value}')
# def step_then_the_paragraph_alignment_property_value_is(context, align_value):
#     # Map align_value to actual alignment constants
#     alignment_values = {
#         'None': None,
#         'WD_ALIGN_PARAGRAPH.LEFT': WD_ALIGN_PARAGRAPH.LEFT,
#         'WD_ALIGN_PARAGRAPH.CENTER': WD_ALIGN_PARAGRAPH.CENTER,
#         'WD_ALIGN_PARAGRAPH.RIGHT': WD_ALIGN_PARAGRAPH.RIGHT,
#     }
#     # Check if the paragraph alignment is the specified alignment
#     assert context.paragraph.alignment == alignment_values[align_value], 'Paragraph does not have the specified alignment'
