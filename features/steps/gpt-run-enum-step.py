# from behave import given, when, then
# from docx import Document
# from docx.enum.text import WD_UNDERLINE
#
# # Given
#
# @given('a run having {underline_type} underline')
# def step_given_a_run_having_underline_type_underline(context, underline_type):
#     context.doc = Document()
#     paragraph = context.doc.add_paragraph()
#     context.run = paragraph.add_run('Sample Text')
#     if underline_type == 'single':
#         context.run.underline = True
#     elif underline_type == 'double':
#         context.run.underline = WD_UNDERLINE.DOUBLE
#     elif underline_type == 'no':
#         context.run.underline = False
#     elif underline_type == 'inherited':
#         context.run.underline = None
#
# # When
#
# @when('I set the run underline to {new_underline_value}')
# def step_when_i_set_the_run_underline_to_value(context, new_underline_value):
#     if new_underline_value == 'True':
#         context.run.underline = True
#     elif new_underline_value == 'False':
#         context.run.underline = False
#     elif new_underline_value == 'None':
#         context.run.underline = None
#     elif new_underline_value == 'WD_UNDERLINE.SINGLE':
#         context.run.underline = True
#     elif new_underline_value == 'WD_UNDERLINE.DOUBLE':
#         context.run.underline = WD_UNDERLINE.DOUBLE
#
# # Then
#
# @then('the run underline property value is {expected_underline_value}')
# def step_then_the_run_underline_property_value_is_value(context, expected_underline_value):
#     if expected_underline_value == 'True':
#         assert context.run.underline is True
#     elif expected_underline_value == 'False':
#         assert context.run.underline is False
#     elif expected_underline_value == 'None':
#         assert context.run.underline is None
#     elif expected_underline_value == 'WD_UNDERLINE.DOUBLE':
#         assert context.run.underline == WD_UNDERLINE.DOUBLE
