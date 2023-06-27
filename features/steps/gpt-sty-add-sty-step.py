# from behave import given, when, then
# from docx import Document
# from docx.enum.style import WD_STYLE_TYPE
# from features.steps.helpers import bool_vals, test_docx
#
# style_types = {
#     'WD_STYLE_TYPE.CHARACTER': WD_STYLE_TYPE.CHARACTER,
#     'WD_STYLE_TYPE.PARAGRAPH': WD_STYLE_TYPE.PARAGRAPH,
#     'WD_STYLE_TYPE.LIST':      WD_STYLE_TYPE.LIST,
#     'WD_STYLE_TYPE.TABLE':     WD_STYLE_TYPE.TABLE,
# }
#
# @given('a document having known styles')
# def step_given_document_with_known_styles(context):
#     context.document = Document(test_docx('sty-known-styles'))
#     context.initial_style_count = len(context.document.styles)
#
# @when("I call add_style('{name}', {type}, builtin={builtin})")
# def step_when_call_add_style(context, name, type, builtin):
#     type = style_types[type]
#     builtin = bool_vals[builtin]
#     context.new_style = context.document.styles.add_style(name, type, builtin=builtin)
#
# @then('the document has one additional style')
# def step_then_document_has_one_additional_style(context):
#     assert len(context.document.styles) == context.initial_style_count + 1
#
# @then("styles['{name}'] is a style")
# def step_then_styles_name_is_a_style(context, name):
#     style = context.document.styles[name]
#     assert style == context.new_style
#
# @then('style.type is {type}')
# def step_then_style_type_is(context, type):
#     expected_type = style_types[type]
#     assert context.new_style.type == expected_type
#
# @then('style.builtin is {builtin}')
# def step_then_style_builtin_is(context, builtin):
#     expected_builtin = builtin == 'True'
#     assert context.new_style.builtin == expected_builtin
