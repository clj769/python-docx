# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# def setup_table(rows, columns):
#     document = Document(test_docx('blk-containing-table'))
#     table = document.add_table(rows=rows, cols=columns)
#     return table
#
# @given('a table having two rows')
# def step_given_table_with_two_rows(context):
#     context.table_ = setup_table(2, 1)
#
# @then('I can access the row collection of the table')
# def step_then_can_access_row_collection(context):
#     assert len(context.table_.rows) == 2
#
# @then('the length of the row collection is {length}')
# def step_then_length_of_row_collection(context, length):
#     assert len(context.table_.rows) == int(length)
#
# @given('a row collection having two rows')
# def step_given_row_collection_with_two_rows(context):
#     context.rows = setup_table(2, 1).rows
#
# @then('I can iterate over the row collection')
# def step_then_can_iterate_row_collection(context):
#     for row in context.rows:
#         pass
#
# @then('I can access a collection row by index')
# def step_then_can_access_row_by_index(context):
#     assert context.rows[0] is not None
#
# @given('a table having two columns')
# def step_given_table_with_two_columns(context):
#     context.table_ = setup_table(1, 2)
#
# @then('I can access the column collection of the table')
# def step_then_can_access_column_collection(context):
#     assert len(context.table_.columns) == 2
#
# @then('the length of the column collection is {length}')
# def step_then_length_of_column_collection(context, length):
#     assert len(context.table_.columns) == int(length)
#
# @given('a column collection having two columns')
# def step_given_column_collection_with_two_columns(context):
#     context.columns = setup_table(1, 2).columns
#
# @then('I can iterate over the column collection')
# def step_then_can_iterate_column_collection(context):
#     for column in context.columns:
#         pass
#
# @then('I can access a collection column by index')
# def step_then_can_access_column_by_index(context):
#     assert context.columns[0] is not None
