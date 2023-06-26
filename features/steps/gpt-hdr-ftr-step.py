# from behave import given, when, then
# from docx import Document
#
# from features.steps.helpers import test_docx, test_file
#
# # Manually add testing file
#
# @given('a _Header object {with_or_no} header definition as header')
# def step_given_header_object_with_def(context, with_or_no):
#     context.doc = Document(test_docx("hdr-header-footer"))
#     if with_or_no == "with a":
#         section = context.doc.sections[0]
#     else:
#         section = context.doc.sections[1]
#     context.header = section.header
#
# @given('a _Footer object {with_or_no} footer definition as footer')
# def step_given_footer_object_with_def(context, with_or_no):
#     context.doc = Document(test_docx("hdr-header-footer"))
#     if with_or_no == "with a":
#         section = context.doc.sections[0]
#     else:
#         section = context.doc.sections[1]
#     context.footer = section.footer
#
# @given('a _Run object from a header as run')
# def step_given_run_object_from_header(context):
#     context.doc = Document(test_docx("hdr-header-footer"))
#     context.run = context.doc.sections[0].header.paragraphs[0].runs[0]
#
# @given('a _Run object from a footer as run')
# def step_given_run_object_from_footer(context):
#     context.doc = Document(test_docx("hdr-header-footer"))
#     context.run = context.doc.sections[0].footer.paragraphs[0].runs[0]
#
# @given('the next _Header object with no header definition as header_2')
# def step_given_next_header_object_no_def(context):
#     context.doc.add_section()
#     section_2 = context.doc.sections[1]
#     context.header_2 = section_2.header
#
# @given('the next _Footer object with no footer definition as footer_2')
# def step_given_next_footer_object_no_def(context):
#     context.doc.add_section()
#     section_2 = context.doc.sections[1]
#     context.footer_2 = section_2.footer
#
# @when('I assign {value} to header.is_linked_to_previous')
# def step_assign_value_to_header(context, value):
#     context.header.is_linked_to_previous = eval(value)
#
# @when('I assign {value} to footer.is_linked_to_previous')
# def step_assign_value_to_footer(context, value):
#     context.footer.is_linked_to_previous = eval(value)
#
# @when('I call run.add_picture()')
# def step_call_add_picture(context):
#     context.run.add_picture(test_file("test.png"))
#
# @when('I assign "{style_name}" to header.paragraphs[0].style')
# def step_assign_style_to_header(context, style_name):
#     context.header.paragraphs[0].style = context.doc.styles[style_name]
#
# @when('I assign "{style_name}" to footer.paragraphs[0].style')
# def step_assign_style_to_footer(context, style_name):
#     context.footer.paragraphs[0].style = context.doc.styles[style_name]
#
# @then('header.is_linked_to_previous is {value}')
# def step_then_header_is_linked(context, value):
#     assert context.header.is_linked_to_previous == eval(value)
#
# @then('footer.is_linked_to_previous is {value}')
# def step_then_footer_is_linked(context, value):
#     assert context.footer.is_linked_to_previous == eval(value)
#
# @then('I can\'t detect the image but no exception is raised')
# def step_then_image_not_detected_no_exception(context):
#     pass  # If we reached this step without errors, then no exception was raised
#
# @then('header_2.paragraphs[0].text == header.paragraphs[0].text')
# def step_then_header2_equals_header(context):
#     assert context.header_2.paragraphs[0].text == context.header.paragraphs[0].text
#
# @then('header_2.is_linked_to_previous is True')
# def step_then_header2_is_linked(context):
#     assert context.header_2.is_linked_to_previous is True
#
# @then('header.paragraphs[0].style.name == "{style_name}"')
# def step_then_header_style_is(context, style_name):
#     assert context.header.paragraphs[0].style.name == style_name
#
# @then('footer_2.paragraphs[0].text == footer.paragraphs[0].text')
# def step_then_footer2_equals_footer(context):
#     assert context.footer_2.paragraphs[0].text == context.footer.paragraphs[0].text
#
# @then('footer_2.is_linked_to_previous is True')
# def step_then_footer2_is_linked(context):
#     assert context.footer_2.is_linked_to_previous is True
#
# @then('footer.paragraphs[0].style.name == "{style_name}"')
# def step_then_footer_style_is(context, style_name):
#     assert context.footer.paragraphs[0].style.name == style_name