# from behave import given, when, then
# from docx import Document
#
# @given('a document containing three paragraphs')
# def step_given_a_document_containing_three_paragraphs(context):
#     # Create a new Document
#     context.doc = Document()
#     # Add three paragraphs
#     for i in range(3):
#         context.doc.add_paragraph(f'Paragraph {i+1}')
#
# @when('I insert a paragraph above the second paragraph')
# def step_when_i_insert_a_paragraph_above_the_second_paragraph(context):
#     # Set the text and style for the new paragraph
#     context.style = 'Heading 1'
#     # Insert the new paragraph
#     context.doc.paragraphs[1].insert_paragraph_before('Test Text', 'Heading1')
#
# @then('the document contains four paragraphs')
# def step_then_the_document_contains_four_paragraphs(context):
#     # Check if the document contains four paragraphs
#     assert len(context.doc.paragraphs) == 4, 'Document does not contain four paragraphs'
#
# @then('the text of the second paragraph matches the text I set')
# def step_then_the_text_of_the_second_paragraph_matches_the_text_i_set(context):
#     # Check if the text of the second paragraph matches the text I set
#     assert context.doc.paragraphs[1].text == 'Test Text', 'Text of the second paragraph does not match the text I set'
#
# @then('the style of the second paragraph matches the style I set')
# def step_then_the_style_of_the_second_paragraph_matches_the_style_i_set(context):
#     # Check if the style of the second paragraph matches the style I set
#     assert context.doc.paragraphs[1].style.name == context.style, 'Style of the second paragraph does not match the style I set'
