# from behave import given, when, then
# from docx import Document
#
# # blk-add-table-steps ====================================================
#
# @given('a document containing a table')
# def step_given_document_with_table(context):
#     doc = Document()
#     table = doc.add_table(rows=1, cols=1)
#     doc.save('test_table.docx')
#     context.doc_path = 'test_table.docx'
#
# @then('I can access the table')
# def step_then_can_access_table(context):
#     doc = Document(context.doc_path)
#     assert len(doc.tables) > 0
#
# @given('a document')
# def step_given_a_document(context):
#     context.document = Document()
#
# @when('I add a table')
# def step_when_add_a_table(context):
#     context.table = context.document.add_table(rows=1, cols=1)
#
# @then('the new table appears in the document')
# def step_then_table_appears_in_document(context):
#     assert len(context.document.tables) > 0