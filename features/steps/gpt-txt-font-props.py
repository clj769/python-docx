# from behave import given, when, then
# from docx import Document
# from docx.dml.color import ColorFormat
# from docx.enum.text import  WD_UNDERLINE, WD_COLOR_INDEX
# from features.steps.helpers import test_docx
#
#
# @given('a font having {color} highlighting')
# def step_given_font_with_highlight(context, color):
#     doc = Document(test_docx('txt-font-highlight-color'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#     if color != "no":
#         context.font.highlight_color = getattr(WD_COLOR_INDEX, color.upper().replace(" ", "_"))
#
#
# @then('font.highlight_color is {value}')
# def step_then_font_highlight_color_is(context, value):
#     if value == "None":
#         assert context.font.highlight_color is None
#     else:
#         assert context.font.highlight_color == getattr(WD_COLOR_INDEX, value)
#
#
# @when('I assign {value} to font.highlight_color')
# def step_when_assign_to_font_highlight_color(context, value):
#     if value == "None":
#         context.font.highlight_color = None
#     else:
#         context.font.highlight_color = getattr(WD_COLOR_INDEX, value.upper().replace(" ", "_"))
#
#
# @given('a font having typeface name {name}')
# def step_given_font_with_typeface_name(context, name):
#     doc = Document(test_docx('txt-font-props'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#     if name != "not specified":
#         context.font.name = name
#
#
# @then('font.name is {value}')
# def step_then_font_name_is(context, value):
#     value = None if value == 'None' else value
#     assert context.font.name == value
#
#
# @when('I assign {value} to font.name')
# def step_when_assign_to_font_name(context, value):
#     if value == "None":
#         context.font.name = None
#     else:
#         context.font.name = value
#
#
# @given('a font of size {size}')
# def step_given_font_of_size(context, size):
#     doc = Document(test_docx('txt-font-props'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#     if size != "unspecified":
#         context.font.size = int(size.split(" ")[0])
#
#
# @then('font.size is {value}')
# def step_then_font_size_is(context, value):
#     if value == "None":
#         assert context.font.size is None
#     else:
#         assert context.font.size == int(value)
#
#
# @when('I assign {value} to font.size')
# def step_when_assign_to_font_size(context, value):
#     if value == "None":
#         context.font.size = None
#     else:
#         context.font.size = int(value)
#
#
# @given('a font')
# def step_given_a_font(context):
#     doc = Document(test_docx('txt-font-props'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#
#
# @then('font.color is a ColorFormat object')
# def step_then_font_color_is_color_format(context):
#     assert isinstance(context.font.color, ColorFormat)
#
#
# @given('a font having {underline_type} underline')
# def step_given_font_with_underline(context, underline_type):
#     doc = Document(test_docx('txt-font-props'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#     if underline_type == "no":
#         context.font.underline = False
#     elif underline_type == "single":
#         context.font.underline = True
#     elif underline_type == "double":
#         context.font.underline = WD_UNDERLINE.DOUBLE
#
#
# @then('font.underline is {value}')
# def step_then_font_underline_is(context, value):
#     if value == "None":
#         assert context.font.underline is None
#     elif value == "True":
#         assert context.font.underline is True
#     elif value == "False":
#         assert context.font.underline is False
#     else:
#         assert context.font.underline == WD_UNDERLINE.DOUBLE
#
#
# @when('I assign {value} to font.underline')
# def step_when_assign_to_font_underline(context, value):
#     if value == "None":
#         context.font.underline = None
#     elif value == "True":
#         context.font.underline = True
#     elif value == "False":
#         context.font.underline = False
#     else:
#         new_value = {
#             'True': True,
#             'False': False,
#             'None': None,
#             'WD_UNDERLINE.SINGLE': WD_UNDERLINE.SINGLE,
#             'WD_UNDERLINE.DOUBLE': WD_UNDERLINE.DOUBLE,
#         }[value]
#
#         context.font.underline = new_value
#
#
# @given('a font having {vertAlign_state} vertical alignment')
# def step_given_font_with_vertical_alignment(context, vertAlign_state):
#     doc = Document(test_docx('txt-font-props'))
#     run = doc.add_paragraph().add_run()
#     context.font = run.font
#     if vertAlign_state == "subscript":
#         context.font.subscript = True
#     elif vertAlign_state == "superscript":
#         context.font.superscript = True
#
#
# @then('font.{script}script is {value}')
# def step_then_font_script_is(context, script, value):
#     script_value = getattr(context.font, f"{script}script")
#     if value == "None":
#         assert script_value is None
#     elif value == "True":
#         assert script_value is True
#     elif value == "False":
#         assert script_value is False
#
#
# @when('I assign {value} to font.{script}script')
# def step_when_assign_to_font_script(context, value, script):
#     if value == "None":
#         setattr(context.font, f"{script}script", None)
#     elif value == "True":
#         setattr(context.font, f"{script}script", True)
#     elif value == "False":
#         setattr(context.font, f"{script}script", False)
#
#
# @given('a run')
# def step_given_a_run(context):
#     doc = Document()
#     context.run = doc.add_paragraph().add_run()
#
#
# @when('I assign True to its {prop} property')
# def step_when_assign_true_to_run_property(context, prop):
#     setattr(context.run.font, prop, True)
#
#
# @then('the run appears in {prop} unconditionally')
# def step_then_run_appears_in_prop_unconditionally(context, prop):
#     assert getattr(context.run.font, prop) is True
#
#
# @when('I assign False to its {prop} property')
# def step_when_assign_false_to_run_property(context, prop):
#     setattr(context.run.font, prop, False)
#
#
# @then('the run appears without {prop} unconditionally')
# def step_then_run_appears_without_prop_unconditionally(context, prop):
#     assert getattr(context.run.font, prop) is False
#
#
# @given('a run having {prop} set on')
# def step_given_run_with_prop_set_on(context, prop):
#     doc = Document()
#     context.run = doc.add_paragraph().add_run()
#     setattr(context.run.font, prop, True)
#
#
# @when('I assign None to its {prop} property')
# def step_when_assign_none_to_run_property(context, prop):
#     setattr(context.run.font, prop, None)
#
#
# @then('the run appears with its inherited {prop} setting')
# def step_then_run_appears_with_inherited_prop_setting(context, prop):
#     assert getattr(context.run.font, prop) is None
