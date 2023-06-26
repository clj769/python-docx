# from behave import given, when, then
# from docx import Document
# from helpers import test_docx
#
#
# # blk-add-paragraph-steps ====================================================
#
# context_text = "This is a test text"
#
# @given('a document')
# def step_given_a_document(context):
#     context.document = Document()
#
# @when('I add a paragraph')
# def step_when_add_a_paragraph(context):
#     context.paragraph = context.document.add_paragraph()
#
# @when('I add a run to the paragraph')
# def step_when_add_a_run_to_paragraph(context):
#     context.run = context.paragraph.add_run()
#
# @when('I add text to the run')
# def step_when_add_text_to_the_run(context):
#     context.run.text = context_text
#
# @when('I save the document')
# def step_when_save_the_document(context):
#     context.document.save(test_docx('doc-default'))
#
# @then('the document contains the text I added')
# def step_then_document_contains_text(context):
#     doc = Document(test_docx('doc-default'))
#     assert context_text in [p.text for p in doc.paragraphs]