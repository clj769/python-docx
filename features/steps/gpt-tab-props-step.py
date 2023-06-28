# from behave import given, when, then
# from docx import Document
# from docx.enum.text import WD_TAB_ALIGNMENT, WD_TAB_LEADER
# from features.steps.helpers import test_docx
#
#
# @given('a tab stop {distance:f} inches {in_or_out} from the paragraph left edge')
# def step_given_a_tab_stop(context, distance, in_or_out):
#     document = Document(test_docx('tab-stops'))
#     paragraph = document.add_paragraph()
#     position = distance * 914400 if in_or_out == 'in' else -distance * 914400
#     paragraph.paragraph_format.tab_stops.add_tab_stop(int(position), WD_TAB_ALIGNMENT.LEFT)
#     context.tab_stops = paragraph.paragraph_format.tab_stops
#     context.tab_stop = paragraph.paragraph_format.tab_stops[0]
#
# @then('tab_stop.position is {position:d}')
# def step_then_tab_stop_position_is(context, position):
#     assert context.tab_stop.position == position
#
# @when('I assign {value:d} to tab_stop.position')
# def step_when_assign_value_to_tab_stop_position(context, value):
#     context.tab_stop.position = value
#
# @given('a tab stop having {alignment} alignment')
# def step_given_a_tab_stop_having_alignment(context, alignment):
#     document = Document(test_docx('tab-stops'))
#     paragraph = document.add_paragraph()
#     align = getattr(WD_TAB_ALIGNMENT, alignment)
#     paragraph.paragraph_format.tab_stops.add_tab_stop(457200, align)
#     context.tab_stop = paragraph.paragraph_format.tab_stops[0]
#
# @then('tab_stop.alignment is {alignment}')
# def step_then_tab_stop_alignment_is(context, alignment):
#     assert context.tab_stop.alignment == getattr(WD_TAB_ALIGNMENT, alignment)
#
# @when('I assign {member} to tab_stop.alignment')
# def step_when_assign_value_to_tab_stop_alignment(context, member):
#     context.tab_stop.alignment = getattr(WD_TAB_ALIGNMENT, member)
#
# @given('a tab stop having {leader} leader')
# def step_given_a_tab_stop_having_leader(context, leader):
#     document = Document(test_docx('tab-stops'))
#     paragraph = document.add_paragraph()
#     leader_type = WD_TAB_LEADER.SPACES if leader == 'no specified' else WD_TAB_LEADER.DOTS
#     paragraph.paragraph_format.tab_stops.add_tab_stop(457200, WD_TAB_ALIGNMENT.LEFT, leader_type)
#     context.tab_stop = paragraph.paragraph_format.tab_stops[0]
#
# @then('tab_stop.leader is {value}')
# def step_then_tab_stop_leader_is(context, value):
#     assert context.tab_stop.leader == getattr(WD_TAB_LEADER, value)
#
# @when('I assign {member} to tab_stop.leader')
# def step_when_assign_value_to_tab_stop_leader(context, member):
#     context.tab_stop.leader = getattr(WD_TAB_LEADER, member)
#
# @then('the tab stops are sequenced in position order')
# def step_then_tab_stops_are_sequenced(context):
#     last_pos = 0
#     for tab_stop in context.tab_stops:
#         if last_pos != 0:
#             assert tab_stop.position > last_pos
#         last_pos = tab_stop.position