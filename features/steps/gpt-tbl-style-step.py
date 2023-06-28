# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# def setup_table(style=None):
#     doc = Document(test_docx('tbl-having-applied-style'))
#     table = doc.add_table(rows=3, cols=3)
#
#     if style and style != 'no explicit':
#         if style == 'Light Shading - Accent 1':
#             table.style = 'Light Shading Accent 1'
#         else:
#             table.style = style
#
#     return table, doc.styles
#
#
# @given('a table having {style} style')
# def step_given_table_with_style(context, style):
#     context.table_, context.styles = setup_table(style=style)
#
#
# @when('I assign {value} to table.style')
# def step_when_assign_style_to_table(context, value):
#     if value.startswith("styles['"):
#         value = value[8:-2]  # trim styles[' and ']
#         context.table_.style = context.styles[value]
#     elif value == 'None':
#         context.table_.style = None
#     else:
#         context.table_.style = value
#
#
# @then('table.style is styles[\'{style_name}\']')
# def step_then_table_style_is(context, style_name):
#     assert context.table_.style == context.styles[style_name]
