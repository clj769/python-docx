# from behave import given, when, then
# from docx import Document
# from docx.shared import Inches
# from features.steps.helpers import test_docx
#
#
# @given('a _Cell object with {state} vertical alignment as cell')
# def step_given_a_cell_with_state(context, state):
#     table_idx = {
#         'inherited': 0,
#         'bottom': 1,
#         'center': 2,
#         'top': 3,
#     }[state]
#     document = Document(test_docx('tbl-props'))
#     table = document.tables[table_idx]
#     context.cell = table.cell(0, 0)
#
# @given('a table cell having a width of {width_setting}')
# def step_given_table_cell_with_width(context, width_setting):
#     table_idx = {'no explicit setting': 0, '1 inch': 1, '2 inches': 2}[width_setting]
#     document = Document(test_docx('tbl-props'))
#     table = document.tables[table_idx]
#     cell = table.cell(0, 0)
#     context.cell = cell
#
# @then('cell.vertical_alignment is {value}')
# def step_then_cell_vertical_alignment_is(context, value):
#     assert context.cell.vertical_alignment == eval(value)
#
# @when('I assign {value} to cell.vertical_alignment')
# def step_when_assign_value_to_cell_vertical_alignment(context, value):
#     context.cell.vertical_alignment = eval(value)
#
#
#
# @then('the reported width of the cell is {reported_width}')
# def step_then_reported_width_of_cell_is(context, reported_width):
#     expected = None if reported_width == 'None' else Inches(int(reported_width.split(' ')[0]))
#     assert context.cell.width == expected
#
# @when('I set the cell width to {new_setting}')
# def step_when_set_cell_width(context, new_setting):
#     context.cell.width = Inches(int(new_setting.split(' ')[0]))
