# from behave import given, when, then
# from docx import Document
#
# # Given
#
# @given('a run having known text and formatting')
# def step_given_a_run_having_known_text_and_formatting(context):
#     context.doc = Document()
#     paragraph = context.doc.add_paragraph()
#     context.run = paragraph.add_run('Known text')
#     context.run.bold = True  # Assuming this is part of the 'known formatting'
#
# # When
#
# @when('I clear the run')
# def step_when_i_clear_the_run(context):
#     for item in list(context.run._r):  # Getting list of elements in this run
#         if item.text:  # If it's a text element
#             context.run._r.remove(item)  # Remove it
#
# # Then
#
# @then('the run contains no text')
# def step_then_the_run_contains_no_text(context):
#     assert context.run.text == ""
#
# @then('the run formatting is preserved')
# def step_then_the_run_formatting_is_preserved(context):
#     assert context.run.bold == True
