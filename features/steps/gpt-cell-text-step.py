# from behave import given, when, then
# from docx import Document
#
# context_string = "Test String"
#
# @given('a table cell')
# def step_given_a_table_cell(context):
#     context.doc = Document()
#     context.table = context.doc.add_table(rows=2, cols=2)
#     context.cell = context.table.cell(0, 0)
#
# @when('I assign a string to the cell text attribute')
# def step_when_assign_string_to_cell_text(context):
#     context.cell.text = context_string
#
# @then('the cell contains the string I assigned')
# def step_then_cell_contains_assigned_string(context):
#     assert context.cell.text == context_string
