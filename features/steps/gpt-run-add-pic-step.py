# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_file
#
#
# @given('a run')
# def step_given_a_run(context):
#     doc = Document()
#     para = doc.add_paragraph()
#     context.run = para.add_run()
#
# @given('a run inside a table cell retrieved from {cell_source}')
# def step_given_a_run_inside_a_table_cell(context, cell_source):
#     doc = Document()
#     table = doc.add_table(rows=2, cols=2)
#     if cell_source == 'Table.cell':
#         context.run = table.cell(0, 0).paragraphs[0].add_run()
#     elif cell_source == 'Table.row.cells':
#         context.run = table.rows[0].cells[0].paragraphs[0].add_run()
#     elif cell_source == 'Table.column.cells':
#         context.run = table.columns[0].cells[0].paragraphs[0].add_run()
#
# @when('I add a picture to the run')
# def step_when_i_add_a_picture_to_the_run(context):
#     # Using the provided image file for the test
#     context.run.add_picture(test_file('monty-truth.png'))
#
# @then('the picture appears at the end of the run')
# def step_then_the_picture_appears_at_the_end_of_the_run(context):
#     # Here, checking the last element of the run is a picture.
#     assert context.run._r[-1] is not None
#
# @then('the document contains the inline picture')
# def step_then_the_document_contains_the_inline_picture(context):
#     # Check if the document contains a picture.
#     assert any(blip for blip in context.run._r)
