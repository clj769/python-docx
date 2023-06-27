# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# @given('an inline shape of known dimensions')
# def step_given_inline_shape_known_dimensions(context):
#     context.document = Document(test_docx('shp-inline-shape-access'))
#
#     # Get the first inline shape which we just added
#     context.inline_shape = context.document.inline_shapes[0]
#
#     # Store the initial dimensions
#     context.initial_width = context.inline_shape.width
#     context.initial_height = context.inline_shape.height
#
# @then('the dimensions of the inline shape match the known values')
# def step_then_dimensions_match_known_values(context):
#     assert context.inline_shape.width == context.initial_width
#     assert context.inline_shape.height == context.initial_height
#
# @when('I change the dimensions of the inline shape')
# def step_when_change_dimensions(context):
#     # Change the width and height
#     context.new_width = context.initial_width * 2
#     context.new_height = context.initial_height * 2
#
#     context.inline_shape.width = context.new_width
#     context.inline_shape.height = context.new_height
#
# @then('the dimensions of the inline shape match the new values')
# def step_then_dimensions_match_new_values(context):
#     assert context.inline_shape.width == context.new_width
#     assert context.inline_shape.height == context.new_height
