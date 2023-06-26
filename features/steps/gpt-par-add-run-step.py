# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_text
#
#
# @given('a paragraph')
# def step_given_a_paragraph(context):
#     # Create a new Document
#     doc = Document()
#     # Add a new paragraph
#     context.paragraph = doc.add_paragraph()
#
# @when('I add a run specifying its text')
# def step_when_i_add_a_run_specifying_its_text(context):
#     # Add the run with the specified text
#     context.run = context.paragraph.add_run(test_text)
#
# @then('the run contains the text I specified')
# def step_then_the_run_contains_the_text_i_specified(context):
#     # Check if the run contains the specified text
#     assert context.run.text == test_text, 'Run does not contain the specified text'
#
# @when('I add a run specifying the character style Emphasis')
# def step_when_i_add_a_run_specifying_the_character_style_emphasis(context):
#     # Specify the character style
#     context.style = 'Emphasis'
#     # Add the run with the specified style
#     context.run = context.paragraph.add_run(style=context.style)
#
# @then('run.style is styles[\'Emphasis\']')
# def step_then_run_style_is_styles_emphasis(context):
#     # Check if the run's style is the specified style
#     assert context.run.style.name == context.style, 'Run does not have the specified style'
