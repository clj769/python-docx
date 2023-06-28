# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# def setup_table(rows, columns, uniform=True, span_state=None):
#     document = Document(test_docx('tbl-cell-access'))
#     table = document.add_table(rows=rows, cols=columns)
#
#     if uniform:
#         table = document.tables[0]
#     else:
#         if span_state == "horizontal":
#            table = document.tables[1]
#         elif span_state == "vertical":
#             table = document.tables[2]
#
#     return table
#
# def merge_cells(table, origin, other):
#     origin_cell = table.cell(*origin)
#     other_cell = table.cell(*other)
#     merged_cell = origin_cell.merge(other_cell)
#     return merged_cell
#
# @given('a 3x3 table having only uniform cells')
# def step_given_3x3_uniform_cells_table(context):
#     context.table_ = setup_table(3, 3)
#
# @given('a 3x3 table having a horizontal span')
# def step_given_3x3_horizontal_span_table(context):
#     context.table_ = setup_table(3, 3, uniform=False, span_state="horizontal")
#
# @given('a 3x3 table having a vertical span')
# def step_given_3x3_vertical_span_table(context):
#     context.table_ = setup_table(3, 3, uniform=False, span_state="vertical")
#
# @when('I merge from cell {origin} to cell {other}')
# def step_when_merge_cells(context, origin, other):
#     origin = int(origin) - 1
#     other = int(other) - 1
#     context.merged_cell = merge_cells(context.table_, (origin//3, origin%3), (other//3, other%3))
#
# @then('the row cells text is {expected_text}')
# def step_then_row_cells_text_is(context, expected_text):
#     row_texts = ' '.join([cell.text for row in context.table_.rows for cell in row.cells])
#     assert row_texts == expected_text.replace('\\', '\n')
#
# @then('the width of cell {merged} is {width} inches')
# def step_then_merged_cell_width_is(context, merged, width):
#     merged = int(merged) - 1
#     merged_cell = context.table_.cell(merged//3, merged%3)
#     assert merged_cell.width.inches == float(width)
