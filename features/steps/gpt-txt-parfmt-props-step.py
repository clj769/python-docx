# from behave import given, then, when
# from docx import Document
# from docx.shared import Pt
# from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
# from docx.text.tabstops import TabStops
# from features.steps.helpers import test_docx
#
#
# @given('a paragraph format')
# def step_given_a_paragraph_format(context):
#     doc = Document(test_docx('tab-stops'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#
#
# @then('paragraph_format.tab_stops is a TabStops object')
# def step_then_paragraph_format_tab_stops_is_TabStops(context):
#     assert isinstance(context.paragraph_format.tab_stops, TabStops)
#
#
# @given('a paragraph format having {align_type} alignment')
# def step_given_paragraph_format_with_alignment(context, align_type):
#     doc = Document(test_docx('sty-known-styles'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#     if align_type != "inherited":
#         context.paragraph_format.alignment = getattr(WD_ALIGN_PARAGRAPH, align_type.upper())
#
#
# @then('paragraph_format.alignment is {value}')
# def step_then_paragraph_format_alignment_is_value(context, value):
#     if value == "None":
#         assert context.paragraph_format.alignment is None
#     else:
#         expected_value = {
#             'WD_ALIGN_PARAGRAPH.LEFT': WD_ALIGN_PARAGRAPH.LEFT,
#             'WD_ALIGN_PARAGRAPH.CENTER': WD_ALIGN_PARAGRAPH.CENTER,
#             'WD_ALIGN_PARAGRAPH.RIGHT': WD_ALIGN_PARAGRAPH.RIGHT,
#         }[value]
#         assert context.paragraph_format.alignment == expected_value
#
#
# @when('I assign {new_value} to paragraph_format.alignment')
# def step_when_assign_value_to_paragraph_format_alignment(context, new_value):
#     if new_value == "None":
#         context.paragraph_format.alignment = None
#     else:
#         value = {
#             'WD_ALIGN_PARAGRAPH.CENTER': WD_ALIGN_PARAGRAPH.CENTER,
#             'WD_ALIGN_PARAGRAPH.RIGHT': WD_ALIGN_PARAGRAPH.RIGHT,
#         }[new_value]
#         context.paragraph_format.alignment = value
#
# @given('a paragraph format having {setting} space {side}')
# def step_given_paragraph_format_with_spacing(context, setting, side):
#     doc = Document(test_docx('sty-known-styles'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#     if setting != "inherited":
#         setattr(context.paragraph_format, f"space_{side}", Pt(float(setting.split(" ")[0])))
#
#
# @then('paragraph_format.space_{side} is {value}')
# def step_then_paragraph_format_space_is_value(context, side, value):
#     value = None if value == "None" else int(value)
#     assert getattr(context.paragraph_format, f"space_{side}") == value
#
#
# @when('I assign {new_value} to paragraph_format.space_{side}')
# def step_when_assign_value_to_paragraph_format_space(context, new_value, side):
#     if new_value == "None":
#         setattr(context.paragraph_format, f"space_{side}", None)
#     else:
#         setattr(context.paragraph_format, f"space_{side}", Pt(float(new_value[3:-1])))
#
#
# @given('a paragraph format having {setting} line spacing')
# def step_given_paragraph_format_with_line_spacing(context, setting):
#     doc = Document(test_docx('sty-known-styles'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#     if setting != "inherited":
#         if setting == "double":
#             context.paragraph_format.line_spacing = 2.0
#             context.paragraph_format.line_spacing_rule = WD_LINE_SPACING.DOUBLE
#         else:
#             context.paragraph_format.line_spacing = Pt(float(setting.split(" ")[0]))
#             context.paragraph_format.line_spacing_rule = WD_LINE_SPACING.EXACTLY
#
#
# @then('paragraph_format.line_spacing is {value}')
# def step_then_paragraph_format_line_spacing_is_value(context, value):
#     value = None if value == "None" else float(value) if "." in value else int(value)
#     if value is None or isinstance(value, int):
#         assert context.paragraph_format.line_spacing == value
#     else:
#         assert abs(context.paragraph_format.line_spacing - value) < 0.001
#
#
# @then('paragraph_format.line_spacing_rule is {rule_value}')
# def step_then_paragraph_format_line_spacing_rule_is_value(context, rule_value):
#     expected_value = {
#         'None': None,
#         'WD_LINE_SPACING.EXACTLY': WD_LINE_SPACING.EXACTLY,
#         'WD_LINE_SPACING.MULTIPLE': WD_LINE_SPACING.MULTIPLE,
#         'WD_LINE_SPACING.SINGLE': WD_LINE_SPACING.SINGLE,
#         'WD_LINE_SPACING.DOUBLE': WD_LINE_SPACING.DOUBLE,
#         'WD_LINE_SPACING.AT_LEAST': WD_LINE_SPACING.AT_LEAST,
#         'WD_LINE_SPACING.ONE_POINT_FIVE': WD_LINE_SPACING.ONE_POINT_FIVE,
#     }[rule_value]
#
#     assert context.paragraph_format.line_spacing_rule == expected_value
#
#
# @when('I assign {new_value} to paragraph_format.line_spacing')
# def step_when_assign_value_to_paragraph_format_line_spacing(context, new_value):
#     value = {
#         'Pt(14)': Pt(14),
#         '2': 2,
#     }.get(new_value)
#     value = float(new_value) if value is None else value
#
#     context.paragraph_format.line_spacing = value
#
#
# @when('I assign {new_value} to paragraph_format.line_spacing_rule')
# def step_when_assign_value_to_paragraph_format_line_spacing_rule(context, new_value):
#     if new_value == "None":
#         context.paragraph_format.line_spacing_rule = None
#     else:
#         value = {
#             'None': None,
#             'WD_LINE_SPACING.EXACTLY': WD_LINE_SPACING.EXACTLY,
#             'WD_LINE_SPACING.MULTIPLE': WD_LINE_SPACING.MULTIPLE,
#             'WD_LINE_SPACING.SINGLE': WD_LINE_SPACING.SINGLE,
#             'WD_LINE_SPACING.DOUBLE': WD_LINE_SPACING.DOUBLE,
#             'WD_LINE_SPACING.AT_LEAST': WD_LINE_SPACING.AT_LEAST,
#             'WD_LINE_SPACING.ONE_POINT_FIVE': WD_LINE_SPACING.ONE_POINT_FIVE,
#         }[new_value]
#         context.paragraph_format.line_spacing_rule = value
#
#
# @given('a paragraph format having {type} indent of {setting}')
# def step_given_paragraph_format_with_indent(context, type, setting):
#     doc = Document(test_docx('sty-known-styles'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#     if setting != "inherit":
#         setattr(context.paragraph_format, f"{type}_indent", Pt(float(setting.split(" ")[0])))
#
#
# @then('paragraph_format.{type}_indent is {value}')
# def step_then_paragraph_format_indent_is_value(context, type, value):
#     value = None if value == "None" else int(value)
#     assert getattr(context.paragraph_format, f"{type}_indent") == value
#
#
# @when('I assign {new_value} to paragraph_format.{type}_indent')
# def step_when_assign_value_to_paragraph_format_indent(context, new_value, type):
#     if new_value == "None":
#         setattr(context.paragraph_format, f"{type}_indent", None)
#     else:
#         setattr(context.paragraph_format, f"{type}_indent", Pt(float(new_value.split(" ")[0])))
#
#
# @given('a paragraph format having {prop_name} set {state}')
# def step_given_paragraph_format_with_property(context, prop_name, state):
#     doc = Document(test_docx('sty-known-styles'))
#     context.paragraph_format = doc.add_paragraph().paragraph_format
#     if state != "to inherit":
#         setattr(context.paragraph_format, prop_name, state == "On")
#
#
# @then('paragraph_format.{prop_name} is {value}')
# def step_then_paragraph_format_property_is_value(context, prop_name, value):
#     value = None if value == "None" else value == "True"
#     assert getattr(context.paragraph_format, prop_name) == value
#
#
# @when('I assign {new_value} to paragraph_format.{prop_name}')
# def step_when_assign_value_to_paragraph_format_property(context, new_value, prop_name):
#     if new_value == "None":
#         setattr(context.paragraph_format, prop_name, None)
#     else:
#         setattr(context.paragraph_format, prop_name, new_value == "True")
