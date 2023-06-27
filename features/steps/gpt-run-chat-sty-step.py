# from behave import given, when, then
# from docx import Document
#
# @given('a run having {style} style')
# def step_given_a_run_having_style(context, style):
#     context.doc = doc = Document()
#     para = doc.add_paragraph()
#     if style != 'no explicit':
#         context.run = para.add_run(style=style)
#     else:
#         context.run = para.add_run()
#
# @when('I assign {value} to run.style')
# def step_when_i_assign_value_to_run_style(context, value):
#     if value.startswith('styles['):
#         value = value.split('\'')[1]
#         context.run.style = context.doc.styles[value]
#     elif value == 'None':
#         context.run.style = context.doc.styles['Default Paragraph Font']
#     else:
#         context.run.style = value
#
# @then('run.style is styles[\'{style_name}\']')
# def step_then_run_style_is_styles_style_name(context, style_name):
#     if style_name == 'Default Paragraph Font':
#         assert context.run.style == context.doc.styles['Default Paragraph Font']
#     else:
#         assert context.run.style.name == style_name
