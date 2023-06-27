# from behave import given, when, then
# from docx import Document
# from docx.enum.section import WD_SECTION, WD_ORIENT
# from docx.section import _Footer, _Header
# from docx.shared import Inches
# from features.steps.helpers import test_docx
#
#
# # Given
#
# @given('a Section object {with_or_without} a distinct first-page header as section')
# def step_given_a_section_object_with_or_without_a_distinct_first_page_header(context, with_or_without):
#     context.doc = Document(test_docx("sct-first-page-hdrftr"))
#     section = context.doc.sections[0]
#     section.different_first_page_header_footer = with_or_without == 'with'
#     context.section = section
#
# @given('a Section object as section')
# def step_given_a_section_object_as_section(context):
#     context.doc = Document(test_docx("sct-section-props"))
#     context.section = context.doc.sections[0]
#
# @given('a section having start type {start_type}')
# def step_given_a_section_having_start_type(context, start_type):
#     context.doc = Document(test_docx('sct-section-props'))
#     section = context.doc.sections[0]
#
#
#     section.start_type = getattr(WD_SECTION, start_type)
#     context.section = section
#
# @given('a section known to have {orientation} orientation')
# def step_given_a_section_known_to_have_orientation(context, orientation):
#     context.doc = Document(test_docx('sct-section-props'))
#     section = context.doc.sections[0]
#     section.orientation = getattr(WD_ORIENT, orientation.upper())
#     context.section = section
#
# @given('a section having known page margins')
# def step_given_a_section_having_known_page_margins(context):
#     context.doc = Document(test_docx('sct-section-props'))
#     context.section = context.doc.sections[0]
#
# @given('a section having known page dimension')
# def step_given_a_section_having_known_page_dimension(context):
#     context.doc = Document(test_docx('sct-section-props'))
#     context.section = context.doc.sections[0]
#     context.section.page_height = Inches(11)
#     context.section.page_width = Inches(8.5)
#
# # When
#
# @when('I assign {value} to section.different_first_page_header_footer')
# def step_when_i_assign_value_to_section_different_first_page_header_footer(context, value):
#     context.section.different_first_page_header_footer = value.lower() == 'true'
#
# @when('I set the section start type to {new_start_type}')
# def step_when_i_set_the_section_start_type_to(context, new_start_type):
#     if new_start_type == 'None':
#         context.section.start_type = None
#     else:
#         context.section.start_type = getattr(WD_SECTION, new_start_type)
#
# @when('I set the section orientation to {new_orientation}')
# def step_when_i_set_the_section_orientation_to(context, new_orientation):
#     if new_orientation == 'None':
#         context.section.orientation = WD_ORIENT.PORTRAIT
#     elif new_orientation == 'WD_ORIENT.LANDSCAPE':
#         context.section.orientation = WD_ORIENT.LANDSCAPE
#     elif new_orientation == 'WD_ORIENT.PORTRAIT':
#         context.section.orientation = WD_ORIENT.PORTRAIT
#
# @when('I set the {margin_type} margin to {length} inches')
# def step_when_i_set_the_margin_type_margin_to_length_inches(context, margin_type, length):
#     if margin_type == 'gutter':
#         context.section.gutter = Inches(float(length))
#     elif margin_type == 'header':
#        context.section.header_distance = Inches(float(length))
#     elif margin_type == 'footer':
#        context.section.footer_distance = Inches(float(length))
#     else:
#         setattr(context.section, margin_type + '_margin', Inches(float(length)))
#
# @when('I set the section page width to {width} inches')
# def step_when_i_set_the_section_page_width_to_width_inches(context, width):
#     context.section.page_width = Inches(float(width))
#
# @when('I set the section page height to {height} inches')
# def step_when_i_set_the_section_page_height_to_height_inches(context, height):
#     context.section.page_height = Inches(float(height))
#
# # Then
#
# @then('section.different_first_page_header_footer is {value}')
# def step_then_section_different_first_page_header_footer_is(context, value):
#     assert context.section.different_first_page_header_footer == (value.lower() == 'true')
#
# @then('the reported section start type is {start_type}')
# def step_then_the_reported_section_start_type_is(context, start_type):
#     assert context.section.start_type == getattr(WD_SECTION, start_type)
#
# @then('the reported page orientation is {reported_orientation}')
# def step_then_the_reported_page_orientation_is(context, reported_orientation):
#     if reported_orientation == 'WD_ORIENT.LANDSCAPE':
#         assert context.section.orientation == WD_ORIENT.LANDSCAPE
#     elif reported_orientation == 'WD_ORIENT.PORTRAIT':
#         assert context.section.orientation == WD_ORIENT.PORTRAIT
#
# @then('the reported {margin_type} margin is {length} inches')
# def step_then_the_reported_margin_type_margin_is_length_inches(context, margin_type, length):
#     if margin_type == 'gutter':
#         assert context.section.gutter == Inches(float(length))
#     elif margin_type == 'header':
#         print(context.section.header_distance, Inches(float(length)))
#         assert context.section.header_distance == Inches(float(length))
#     elif margin_type == 'footer':
#         print(context.section.footer_distance,Inches(float(length)))
#         assert context.section.footer_distance == Inches(float(length))
#     else:
#         assert getattr(context.section, margin_type+'_margin') == Inches(float(length))
#
# @then('the reported page width is {width} inches')
# def step_then_the_reported_page_width_is_width_inches(context, width):
#     assert context.section.page_width == Inches(float(width))
#
# @then('the reported page height is {height} inches')
# def step_then_the_reported_page_height_is_height_inches(context, height):
#     assert context.section.page_height == Inches(float(height))
#
# @then('section.even_page_footer is a _Footer object')
# def step_then_section_even_page_footer_is_a_footer_object(context):
#     assert isinstance(context.section.even_page_footer, _Footer)
#
# @then('section.even_page_header is a _Header object')
# def step_then_section_even_page_header_is_a_header_object(context):
#     assert isinstance(context.section.even_page_header, _Header)
#
# @then('section.first_page_footer is a _Footer object')
# def step_then_section_first_page_footer_is_a_footer_object(context):
#     assert isinstance(context.section.first_page_footer, _Footer)
#
# @then('section.first_page_header is a _Header object')
# def step_then_section_first_page_header_is_a_header_object(context):
#     assert isinstance(context.section.first_page_header, _Header)
#
# @then('section.footer is a _Footer object')
# def step_then_section_footer_is_a_footer_object(context):
#     assert isinstance(context.section.footer, _Footer)
#
# @then('section.header is a _Header object')
# def step_then_section_header_is_a_header_object(context):
#     assert isinstance(context.section.header, _Header)