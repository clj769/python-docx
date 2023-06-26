# from PIL import Image
# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_file
#
#
# @given('the image file \'{filename}\'')
# def step_given_the_image_file(context, filename):
#     context.filename = test_file(filename)
#
# @when('I construct an image using the image path')
# def step_when_i_construct_an_image(context):
#     # Open an image file
#     context.img = Image.open(context.filename)
#     # Get image details
#     context.width, context.height = context.img.size
#     context.mime_type = Image.MIME.get(context.img.format)
#     print(context.img.info)
#     context.horz_dpi, context.vert_dpi = context.img.info.get('dpi', (72, 72))
#
# @then('the image has content type \'{mime_type}\'')
# def step_then_image_has_content_type(context, mime_type):
#     assert context.mime_type == mime_type, f"Expected {mime_type}, but got {context.mime_type}"
#
# @then('the image is {cx} pixels wide')
# def step_then_image_is_pixels_wide(context, cx):
#     assert int(context.width) == int(cx), f"Expected {cx} pixels wide, but got {context.width} pixels wide"
#
# @then('the image is {cy} pixels high')
# def step_then_image_is_pixels_high(context, cy):
#     assert int(context.height) == int(cy), f"Expected {cy} pixels high, but got {context.height} pixels high"
#
# @then('the image has {horz_dpi} horizontal dpi')
# def step_then_image_has_horizontal_dpi(context, horz_dpi):
#     assert int(context.horz_dpi) == int(horz_dpi), f"Expected {horz_dpi} dpi, but got {context.horz_dpi} dpi"
#
# @then('the image has {vert_dpi} vertical dpi')
# def step_then_image_has_vertical_dpi(context, vert_dpi):
#     assert int(context.vert_dpi) == int(vert_dpi), f"Expected {vert_dpi} dpi, but got {context.vert_dpi} dpi"
