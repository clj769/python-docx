# from behave import given, when, then
# from docx import Document
#
# @given('a {rows:d} x {columns:d} table')
# def step_given_a_table(context, rows, columns):
#     document = Document()
#     table = document.add_table(rows=rows, cols=columns)
#     for row in table.rows:
#         for cell in row.cells:
#             cell.width = 914400 * 3
#     context.table_ = table
#
#
# @when('I add a row to the table')
# def step_when_add_a_row_to_table(context):
#     context.row = context.table_.add_row()
#
# @then('the table has {rows:d} rows')
# def step_then_table_has_rows(context, rows):
#     assert len(context.table_.rows) == rows
#
# @then('the new row has {cells:d} cells')
# def step_then_new_row_has_cells(context, cells):
#     assert len(context.table_.rows[-1].cells) == cells
#
# @then('the width of each cell is {width:f} inches')
# def step_then_width_of_each_cell(context, width):
#     for cell in context.table_.rows[-1].cells:
#         assert cell.width == width * 914400  # inches to EMUs
#
# @when('I add a {width:f} inch column to the table')
# def step_when_add_a_column_to_table(context, width):
#     # Currently python-docx does not support adding a column directly.
#     # So we have to add a cell to each row.
#     context.column = context.table_.add_column(int(width) * 914400)
#
# @then('the table has {columns:d} columns')
# def step_then_table_has_columns(context, columns):
#     assert len(context.table_.columns) == columns
#
# @then('the new column has {cells:d} cells')
# def step_then_new_column_has_cells(context, cells):
#     assert len(context.table_.columns[-1].cells) == cells
#
# @then('the new column is {width:f} inches wide')
# def step_then_new_column_is_width(context, width):
#     for cell in context.table_.columns[-1].cells:
#         assert cell.width == width * 914400  # inches to EMUs
