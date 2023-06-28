# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# @given('a table column having a width of {width}')
# def step_given_table_column_with_width(context, width):
#     col_idx = {
#         'no explicit setting': 0,
#         '1440':                1,
#     }[width]
#     docx_path = test_docx('tbl-col-props')
#     document = Document(docx_path)
#     context.column = document.tables[0].columns[col_idx]
#
# @then('the reported column width is {width_emu}')
# def step_then_reported_column_width_is(context, width_emu):
#     expected = None if width_emu == 'None' else int(width_emu)
#     assert context.column.width == expected
#
# @when('I set the column width to {new_width}')
# def step_when_set_column_width(context, new_width):
#     new_width_in_emu = None if new_width == 'None' else int(new_width)
#     context.column.width = new_width_in_emu
#
