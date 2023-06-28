# from behave import given, when, then
# from docx import Document
# from docx.enum.table import WD_TABLE_DIRECTION, WD_TABLE_ALIGNMENT
# from features.steps.helpers import test_docx
#
# @given('a table having {alignment} alignment')
# def step_given_table_with_alignment(context, alignment):
#     table_idx = {
#         'inherited': 3,
#         'left': 4,
#         'right': 5,
#         'center': 6,
#     }[alignment]
#     docx_path = test_docx('tbl-props')
#     document = Document(docx_path)
#     context.table_ = document.tables[table_idx]
#
#
# @given('a table having an autofit layout of {autofit_setting}')
# def step_given_table_with_autofit(context, autofit_setting):
#     tbl_idx = {
#         'no explicit setting': 0,
#         'autofit': 1,
#         'fixed': 2,
#     }[autofit_setting]
#     document = Document(test_docx('tbl-props'))
#     context.table_ = document.tables[tbl_idx]
#
#
# @given('a table having table direction set {setting}')
# def step_given_table_with_direction(context, setting):
#     table_idx = [
#         'to inherit',
#         'right-to-left',
#         'left-to-right'
#     ].index(setting)
#     document = Document(test_docx('tbl-on-off-props'))
#     context.table_ = document.tables[table_idx]
#
# @when('I assign {value} to table.alignment')
# def step_when_assign_value_to_alignment(context, value):
#
#     value = {
#         'None': None,
#         'WD_TABLE_ALIGNMENT.LEFT': WD_TABLE_ALIGNMENT.LEFT,
#         'WD_TABLE_ALIGNMENT.RIGHT': WD_TABLE_ALIGNMENT.RIGHT,
#         'WD_TABLE_ALIGNMENT.CENTER': WD_TABLE_ALIGNMENT.CENTER,
#     }[value]
#     table = context.table_
#     table.alignment = value
#
#
# @when('I set the table autofit to {new_setting}')
# def step_when_set_table_autofit(context, new_setting):
#     new_value = {'autofit': True, 'fixed': False}[new_setting]
#     table = context.table_
#     table.autofit = new_value
#
#
# @when('I assign {new_value} to table.table_direction')
# def step_when_assign_value_to_table_direction(context, new_value):
#     new_value = (
#         None if new_value == 'None' else getattr(WD_TABLE_DIRECTION, new_value)
#     )
#     context.table_.table_direction = new_value
#
#
#
# @then('table.alignment is {value}')
# def step_then_table_alignment_is(context, value):
#     value = {
#         'None': None,
#         'WD_TABLE_ALIGNMENT.LEFT': WD_TABLE_ALIGNMENT.LEFT,
#         'WD_TABLE_ALIGNMENT.RIGHT': WD_TABLE_ALIGNMENT.RIGHT,
#         'WD_TABLE_ALIGNMENT.CENTER': WD_TABLE_ALIGNMENT.CENTER,
#     }[value]
#     table = context.table_
#     assert table.alignment == value, 'got %s' % table.alignment
#
#
# @then('the reported autofit setting is {reported_autofit}')
# def step_then_reported_autofit_is(context, reported_autofit):
#     expected_value = {'autofit': True, 'fixed': False}[reported_autofit]
#     table = context.table_
#     assert table.autofit is expected_value
#
#
# @then('table.table_direction is {value}')
# def step_then_table_direction_is(context, value):
#     expected = None if value == 'None' else getattr(WD_TABLE_DIRECTION,value)
#     assert context.table_.table_direction == expected
