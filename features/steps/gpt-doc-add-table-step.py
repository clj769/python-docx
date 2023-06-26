# from docx import Document
# from docx.shared import Inches
# from behave import given, when, then
#
# @given('a blank document')
# def step_given_blank_document(context):
#     context.doc = Document()
#
# @when('I add a 2 x 2 table specifying only row and column count')
# def step_when_add_2x2_table(context):
#     context.table = context.doc.add_table(rows=2, cols=2)
#
# @then('the document contains a 2 x 2 table')
# def step_then_document_contains_2x2_table(context):
#     assert len(context.doc.tables) == 1
#     assert len(context.doc.tables[0].rows) == 2
#     assert len(context.doc.tables[0].columns) == 2
#
# @then('table.style is styles[\'Normal Table\']')
# def step_then_table_style_is_normal_table(context):
#     table, styles = context.doc.tables[-1], context.doc.styles
#     expected_style = context.doc.styles['Normal Table']
#     assert table.style == expected_style
#
# @then('the width of each column is 3.0 inches')
# def step_then_column_width_is_3_inches(context):
#     for column in context.doc.tables[-1].columns:
#         assert column.width == Inches(3.0)
#
# @then('the width of each cell is 3.0 inches')
# def step_then_cell_width_is_3_inches(context):
#     for row in context.doc.tables[-1].rows:
#         for cell in row.cells:
#             assert cell.width == Inches(3.0)
#
# @given('a document having built-in styles')
# def step_given_document_with_built_in_styles(context):
#     context.doc = Document()
#
# @when('I add a 2 x 2 table specifying style \'Table Grid\'')
# def step_when_add_2x2_table_with_style(context):
#     context.table = context.doc.add_table(rows=2, cols=2,style='Table Grid')
#
# @then('table.style is styles[\'Table Grid\']')
# def step_then_table_style_is_table_grid(context):
#     table, styles = context.doc.tables[-1], context.doc.styles
#     expected_style = context.doc.styles['Table Grid']
#     assert table.style == expected_style
