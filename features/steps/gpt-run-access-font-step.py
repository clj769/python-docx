# from behave import given, when, then
# from docx import Document
#
# @given('a run')
# def step_given_a_run(context):
#     doc = Document()
#     para = doc.add_paragraph()
#     context.run = para.add_run('Test run')
#
# @then('run.font is the Font object for the run')
# def step_then_run_font_is_the_Font_object_for_the_run(context):
#     assert context.run.font is not None, \
#         "Expected run.font to be a Font object, but got None"
#     assert context.run.font.__class__.__name__ == 'Font', \
#         f"Expected run.font to be a Font object, but got {context.run.font.__class__.__name__}"
