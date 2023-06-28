# from behave import given, when, then
# from docx import Document
# from docx.enum.text import WD_TAB_ALIGNMENT
# from docx.shared import Inches
# from features.steps.helpers import test_docx
#
#
# @given('a tab_stops having {count:d} tab stops')
# def step_given_a_tab_stops(context, count):
#     document = Document(test_docx('tab-stops'))
#     paragraph = document.add_paragraph()
#     for i in range(count):
#         paragraph.paragraph_format.tab_stops.add_tab_stop(i * 36, WD_TAB_ALIGNMENT.LEFT)
#     context.tab_stops = paragraph.paragraph_format.tab_stops
#
# @then('len(tab_stops) is {count:d}')
# def step_then_len_tab_stops(context, count):
#     assert len(context.tab_stops) == count
#
# @then('I can iterate the TabStops object')
# def step_then_can_iterate_tab_stops(context):
#     for tab_stop in context.tab_stops:
#         pass  # do something with each tab stop
#
# @then('I can access a tab stop by index')
# def step_then_can_access_tab_stop_by_index(context):
#     tab_stop = context.tab_stops[0]
#     assert tab_stop is not None
#
# @when('I add a tab stop')
# def step_when_add_tab_stop(context):
#     context.tab_stops.add_tab_stop(len(context.tab_stops) * 36, WD_TAB_ALIGNMENT.LEFT)
#
# @then('the tab stops are sequenced in position order')
# def step_then_tab_stops_are_sequenced(context):
#     last_pos = 0
#     for tab_stop in context.tab_stops:
#         if last_pos != 0:
#             assert tab_stop.position > last_pos
#         last_pos = tab_stop.position
#
# @when('I remove a tab stop')
# def step_when_remove_tab_stop(context):
#     context.del_tab = context.tab_stops[0]
#     del context.tab_stops[0]
#
# @then('the removed tab stop is no longer present in tab_stops')
# def step_then_removed_tab_stop_is_no_longer_present(context):
#     if context.del_tab != context.tab_stops[0]:
#         assert True
#     else:
#         assert False
#
#
#
# @when('I call tab_stops.clear_all()')
# def step_when_call_tab_stops_clear_all(context):
#     context.tab_stops.clear_all()
