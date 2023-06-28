# from behave import given, when, then
# from docx import Document
#
#
# def add_cells_with_span_state(table, span_state):
#     texts = [str(i + 1) for i in range(9)]
#     if span_state == 'a horizontal span':
#         texts[4] = '4'
#     elif span_state == 'a vertical span':
#         texts[7] = '5'
#     elif span_state == 'a combined span':
#         texts[3], texts[4], texts[6], texts[7] = '4', '4', '4', '4'
#
#     for i in range(3):
#         cells = table.rows[i].cells
#         for j in range(3):
#             cells[j].text = texts[i * 3 + j]
#
#
# @given('a {rows:d}x{columns:d} table having {span_state}')
# def step_given_a_table_having_span_state(context, rows, columns, span_state):
#     document = Document()
#     table = document.add_table(rows=rows, cols=columns)
#     add_cells_with_span_state(table, span_state)
#     context.table_ = table
#
#
# @then('the row cells text is {expected_text}')
# def step_then_row_cells_text_is(context, expected_text):
#     result = ' '.join([cell.text for row in context.table_.rows for cell in row.cells])
#     assert result == expected_text
#
#
# @then('the column cells text is {expected_text}')
# def step_then_column_cells_text_is(context, expected_text):
#     result = ' '.join([cell.text for column in context.table_.columns for cell in column.cells])
#     assert result == expected_text
#
#
# @then('table.cell({row:d}, {col:d}).text is {expected_text}')
# def step_then_table_cell_text_is(context, row, col, expected_text):
#     assert context.table_.cell(row, col).text == expected_text
