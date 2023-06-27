# from behave import given, when, then
# from docx.enum.shape import WD_INLINE_SHAPE
# from docx import Document
# from docx.shape import InlineShape
# from features.steps.helpers import test_docx
#
#
# @given('an inline shape collection containing five shapes')
# def step_given_inline_shape_collection(context):
#     # Create a new document
#     context.document = Document(test_docx('shp-inline-shape-access'))
#     context.inline_shapes = context.document.inline_shapes
#
#
# @then('the length of the inline shape collection is 5')
# def step_then_length_of_collection_is_five(context):
#     assert len(context.inline_shapes) == 5
#
#
# @then('I can iterate over the inline shape collection')
# def step_then_iterate_over_collection(context):
#     for shape in context.inline_shapes:
#         pass  # Do nothing, just iterate
#
#
# @then('I can access each inline shape by index')
# def step_then_access_shape_by_index(context):
#     for i in range(len(context.inline_shapes)):
#         shape = context.inline_shapes[i]
#         assert isinstance(shape, InlineShape)
#
#
# @given('an inline shape known to be {shape_type}')
# def step_given_known_inline_shape(context, shape_type):
#     if shape_type == 'an embedded picture':
#         shape = 0
#     elif shape_type == 'a linked picture':
#         shape = 1
#     elif shape_type == 'a link+embed picture':
#         shape = 2
#     elif shape_type == 'a smart art diagram':
#         shape = 3
#     elif shape_type == 'a chart':
#         shape = 4
#
#     context.document = Document(test_docx('shp-inline-shape-access'))
#     context.inline_shape = context.document.inline_shapes[shape]
#
#
# @then('its inline shape type is {shape_type}')
# def step_then_inline_shape_type(context, shape_type):
#     if shape_type == 'WD_INLINE_SHAPE.CHART':
#         expected_type = WD_INLINE_SHAPE.CHART
#     elif shape_type == 'WD_INLINE_SHAPE.LINKED_PICTURE':
#         expected_type = WD_INLINE_SHAPE.LINKED_PICTURE
#     elif shape_type == 'WD_INLINE_SHAPE.PICTURE':
#         expected_type = WD_INLINE_SHAPE.PICTURE
#     elif shape_type == 'WD_INLINE_SHAPE.SMART_ART':
#         expected_type = WD_INLINE_SHAPE.SMART_ART
#
#     assert context.inline_shape.type == expected_type
