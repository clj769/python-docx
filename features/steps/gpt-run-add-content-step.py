# from behave import given, when, then
# from docx import Document
#
# @given('a run')
# def step_given_a_run(context):
#     doc = Document()
#     para = doc.add_paragraph()
#     context.run = para.add_run()
#
# @when('I add a tab')
# def step_when_i_add_a_tab(context):
#     context.run.add_tab()
#
# @then('the tab appears at the end of the run')
# def step_then_the_tab_appears_at_the_end_of_the_run(context):
#     assert context.run.text.endswith('\t'), \
#         "Expected run text to end with a tab character, but it didn't"
#
# @when('I assign mixed text to the text property')
# def step_when_i_assign_mixed_text_to_the_text_property(context):
#     context.run.text = 'Some text\twith a tab'
#
# @then('the text of the run represents the textual run content')
# def step_then_the_text_of_the_run_represents_the_textual_run_content(context):
#     assert context.run.text == 'Some text\twith a tab', \
#         f"Expected run text to be 'Some text\twith a tab', but got '{context.run.text}'"
