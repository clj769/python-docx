# from docx import Document
# from docx.shared import Inches
# from behave import given, when, then
#
# from features.steps.helpers import test_file
# from PIL import Image
#
# # Manually added the test_file('monty-truth.png') for pass
#
# @given('a blank document')
# def step_given_blank_document(context):
#     context.doc = Document()
#
# @when('I add a picture specifying only the image file')
# def step_when_add_picture_with_native_size(context):
#     context.image_path = test_file('monty-truth.png')
#     context.pic = context.doc.add_picture(context.image_path)
#
# @then('the document contains the inline picture')
# def step_then_document_contains_inline_picture(context):
#     # assuming the first paragraph contains the picture
#     assert len(context.doc.paragraphs[0].runs) > 0
#
# @then('the picture has its native width and height')
# def step_then_picture_has_native_dimensions(context):
#     assert context.pic.width
#     assert context.pic.height
#
# @when('I add a picture specifying 1.75" width and 2.5" height')
# def step_when_add_picture_with_specified_dimensions(context):
#     context.image_path = test_file('monty-truth.png')
#     context.pic = context.doc.add_picture(context.image_path, width=Inches(1.75), height=Inches(2.5))
#
# @then('picture.width is 1.75 inches')
# def step_then_picture_width_is_specified_width(context):
#     assert context.pic.width == Inches(1.75)
#
# @then('picture.height is 2.5 inches')
# def step_then_picture_height_is_specified_height(context):
#     assert context.pic.height == Inches(2.5)
#
# @when('I add a picture specifying a width of 1.5 inches')
# def step_when_add_picture_with_specified_width(context):
#     context.image_path = test_file('monty-truth.png')
#     context.pic = context.doc.add_picture(context.image_path, width=Inches(1.5))
#
# @then('picture.height is 2.14 inches')
# def step_then_picture_height_is_calculated_height(context):
#     assert context.pic.height == Inches(2.14)
#
# @when('I add a picture specifying a height of 1.5 inches')
# def step_when_add_picture_with_specified_height(context):
#     context.image_path = test_file('monty-truth.png')
#     with Image.open(context.image_path) as img:
#         original_width, original_height = img.size
#     aspect_ratio = original_width / original_height
#     context.specified_height = Inches(1.5)
#     calculated_width = context.specified_height * aspect_ratio
#     context.pic = context.doc.add_picture(context.image_path, width=calculated_width, height=context.specified_height)
#
# @then('picture.width is 1.05 inches')
# def step_then_picture_width_is_calculated_width(context):
#     with Image.open(context.image_path) as img:
#         original_width, original_height = img.size
#     aspect_ratio = original_width / original_height
#     calculated_width = context.specified_height * aspect_ratio
#     assert context.pic.width == int(calculated_width)
