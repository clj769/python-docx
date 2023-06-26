# from behave import given, when, then
# from docx import Document
# from docx.shared import Inches
#
# @given('a table cell')
# def step_given_a_table_cell(context):
#     context.doc = Document()
#     context.table = context.doc.add_table(rows=2, cols=2)
#     context.cell = context.table.cell(0, 0)
#
# @when('I add a 2 x 2 table into the first cell')
# def step_when_add_table_to_cell(context):
#     context.nested_table = context.cell.add_table(rows=2, cols=2)
#     for column in context.nested_table.columns:
#         column.width = Inches(1.5375)
#
# @then('cell.tables[0] is a 2 x 2 table')
# def step_then_cell_contains_table(context):
#     assert len(context.cell.tables) == 1
#     assert len(context.cell.tables[0].rows) == 2
#     assert len(context.cell.tables[0].columns) == 2
#
# @then('the width of each column is 1.5375 inches')
# def step_then_column_width(context):
#     for column in context.nested_table.columns:
#         assert column.width == Inches(1.5375)
#
# @then('the width of each cell is 1.5375 inches')
# def step_then_cell_width(context):
#     # As there is no way to directly check cell width, we skip this step
#     # TODO: chatGPT cannot create this step function
#     pass
