# from behave import given, when, then
# from docx import Document
# from docx.enum.table import WD_ROW_HEIGHT_RULE
# from features.steps.helpers import test_docx
#
#
# def setup_row(height_rule=None, height=None):
#     doc = Document(test_docx('tbl-props'))
#     table = doc.add_table(rows=3, cols=3)
#     row = table.rows[0]
#
#     if height_rule:
#         if height_rule == 'automatic':
#             row.height_rule = WD_ROW_HEIGHT_RULE.AUTO
#         elif height_rule == 'at least':
#             row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
#
#     if height != None:
#         row.height = int(height)
#
#     return row
#
# @given('a table row having height rule {state}')
# def step_given_row_with_height_rule(context, state):
#     context.row = setup_row(height_rule=state)
#
# @given('a table row having height of {state}')
# def step_given_row_with_height(context, state):
#     if state != 'no explicit setting':
#         state = int(state.split()[0]) * 914400
#     else:
#         state = None
#     context.row = setup_row(height=state)
#
# @when('I assign {value} to row.height_rule')
# def step_when_assign_value_to_row_height_rule(context, value):
#     if value == 'AUTO':
#         context.row.height_rule = WD_ROW_HEIGHT_RULE.AUTO
#     elif value == 'AT_LEAST':
#         context.row.height_rule = WD_ROW_HEIGHT_RULE.AT_LEAST
#     else:
#         context.row.height_rule = None
#
# @when('I assign {value} to row.height')
# def step_when_assign_value_to_row_height(context, value):
#     context.row.height = None if value== 'None' else int(value)
#
# @then('row.height_rule is {value}')
# def step_then_row_height_rule_is(context, value):
#     if value == 'None':
#         assert context.row.height_rule is None
#     elif value == 'AUTO':
#         assert context.row.height_rule == WD_ROW_HEIGHT_RULE.AUTO
#     elif value == 'AT_LEAST':
#         assert context.row.height_rule == WD_ROW_HEIGHT_RULE.AT_LEAST
#
# @then('row.height is {value}')
# def step_then_row_height_is(context, value):
#     value = None if value== 'None' else int(value)
#     assert context.row.height == value
