# from behave import given, when, then
# from docx import Document
# from docx.shared import RGBColor
# from docx.enum.dml import MSO_COLOR_TYPE, MSO_THEME_COLOR
# from features.steps.helpers import test_docx
#
#
# @given('a font having {type} color')
# def step_given_a_font_with_color(context, type):
#     doc = Document(test_docx('fnt-color'))
#     para = doc.add_paragraph()
#     run = para.add_run()
#     context.font = run.font
#
#     if type == "no":
#         context.font = doc.paragraphs[0].runs[0].font
#     elif type == "auto":
#         context.font = doc.paragraphs[0].runs[1].font
#     elif type == "an RGB":
#         context.font = doc.paragraphs[0].runs[2].font
#     elif type == "a theme":
#         context.font = doc.paragraphs[0].runs[3].font
#
#
# @when('I assign {value} to font.color.rgb')
# def step_when_assign_rgb_to_font_color(context, value):
#     if value == "None":
#         context.font.color.rgb = None
#     else:
#         context.font.color.rgb = RGBColor.from_string(value)
#
# @when('I assign {value} to font.color.theme_color')
# def step_when_assign_theme_to_font_color(context, value):
#     if value == "None":
#         context.font.color.theme_color = None
#     else:
#         context.font.color.theme_color = getattr(MSO_THEME_COLOR, value)
#
# @then('font.color.type is {value}')
# def step_then_font_color_type_is(context, value):
#     if value == "None":
#         assert context.font.color.type is None
#     else:
#         assert context.font.color.type == getattr(MSO_COLOR_TYPE, value)
#
# @then('font.color.rgb is {value}')
# def step_then_font_color_rgb_is(context, value):
#     if value == "None":
#         assert context.font.color.rgb is None
#     else:
#         assert context.font.color.rgb == RGBColor.from_string(value)
#
#
#
# @then('font.color.theme_color is {value}')
# def step_then_font_color_theme_color_is(context, value):
#     if value == "None":
#         assert context.font.color.theme_color is None
#     else:
#         assert context.font.color.theme_color == getattr(MSO_THEME_COLOR, value)
#
#
