# from behave import given, when, then
# from docx import Document
# from docx.enum.text import WD_BREAK
# from docx.text.run import Run
#
# @given('a blank document')
# def step_given_a_blank_document(context):
#     context.doc = Document()
#
# @when('I add a page break to the document')
# def step_when_add_page_break_to_document(context):
#     doc = context.doc
#     para = doc.add_paragraph()
#     run = para.add_run()
#     run.add_break(WD_BREAK.PAGE)
#
# @then('the last paragraph contains only a page break')
# def step_then_last_paragraph_contains_only_a_page_break(context):
#     doc = context.doc
#     last_paragraph = doc.paragraphs[-1]
#     last_run = last_paragraph.runs[-1]
#     assert isinstance(last_run, Run)
#     assert len(last_run._r.br_lst) == 1  # Check if the run has a page break
