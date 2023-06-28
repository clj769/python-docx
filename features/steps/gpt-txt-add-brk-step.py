# from behave import given, when, then
# from docx import Document
# from docx.oxml.ns import qn
# from docx.enum.text import WD_BREAK
#
# @given('a run')
# def step_given_a_run(context):
#     doc = Document()
#     para = doc.add_paragraph()
#     context.run = para.add_run()
#
# @when('I add a line break')
# def step_when_add_line_break(context):
#     context.run.add_break(WD_BREAK.LINE)
#
# @when('I add a page break')
# def step_when_add_page_break(context):
#     context.run.add_break(WD_BREAK.PAGE)
#
# @when('I add a column break')
# def step_when_add_column_break(context):
#     context.run.add_break(WD_BREAK.COLUMN)
#
# @then('the last item in the run is a break')
# def step_then_last_item_in_run_is_break(context):
#     last_item = context.run._r[-1]
#     assert last_item.tag.endswith('br')
#
# @then('it is a line break')
# def step_then_it_is_line_break(context):
#     last_item = context.run._r[-1]
#     assert last_item.get('type') == None  # For line break, there is no 'type' attribute.
#
# @then('it is a page break')
# def step_then_it_is_page_break(context):
#     last_item = context.run._r[-1]
#     assert last_item.attrib == {qn('w:type'): 'page'}
#
# @then('it is a column break')
# def step_then_it_is_column_break(context):
#     last_item = context.run._r[-1]
#     assert last_item.tag == '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}br'
