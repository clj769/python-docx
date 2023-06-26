# from behave import given, when, then
# from docx import Document
# from docx.enum.section import WD_ORIENTATION
# from docx.enum.section import WD_SECTION
#
#
# @given('a single-section document having portrait layout')
# def step_given_single_section_document(context):
#     context.doc = Document()
#     section = context.doc.sections[0]
#     section.orientation = WD_ORIENTATION.PORTRAIT
#
# @when('I add an even-page section to the document')
# def step_when_add_even_page_section(context):
#     context.section = context.doc.add_section(WD_SECTION.EVEN_PAGE)
#
# @when('I change the new section layout to landscape')
# def step_when_change_section_layout_to_landscape(context):
#     context.section.orientation = WD_ORIENTATION.LANDSCAPE
#     context.section.page_width, context.section.page_height = context.section.page_height, context.section.page_width
#
# @then('the document has two sections')
# def step_then_document_has_two_sections(context):
#     assert len(context.doc.sections) == 2
#
# @then('the first section is portrait')
# def step_then_first_section_is_portrait(context):
#     assert context.doc.sections[0].orientation == WD_ORIENTATION.PORTRAIT
#
# @then('the second section is landscape')
# def step_then_second_section_is_landscape(context):
#     assert context.doc.sections[1].orientation == WD_ORIENTATION.LANDSCAPE
#
# @given('a single-section Document object with headers and footers as document')
# def step_given_single_section_document_with_headers_footers(context):
#     context.doc = Document()
#     section = context.doc.sections[0]
#     section.header.is_linked_to_previous = True
#     section.even_page_header.is_linked_to_previous = True
#     section.first_page_header.is_linked_to_previous = True
#     section.footer.is_linked_to_previous = True
#     section.even_page_footer.is_linked_to_previous = True
#     section.first_page_footer.is_linked_to_previous = True
#
# @when('I execute section = document.add_section()')
# def step_when_add_section_to_document(context):
#     context.section = context.doc.add_section()
#
# @then('section.header.is_linked_to_previous is True')
# def step_then_section_header_is_linked(context):
#     assert context.section.header.is_linked_to_previous is True
#
# @then('section.even_page_header.is_linked_to_previous is True')
# def step_then_section_even_page_header_is_linked(context):
#     assert context.section.even_page_header.is_linked_to_previous is True
#
# @then('section.first_page_header.is_linked_to_previous is True')
# def step_then_section_first_page_header_is_linked(context):
#     assert context.section.first_page_header.is_linked_to_previous is True
#
# @then('section.footer.is_linked_to_previous is True')
# def step_then_section_footer_is_linked(context):
#     assert context.section.footer.is_linked_to_previous is True
#
# @then('section.even_page_footer.is_linked_to_previous is True')
# def step_then_section_even_page_footer_is_linked(context):
#     assert context.section.even_page_footer.is_linked_to_previous is True
#
# @then('section.first_page_footer.is_linked_to_previous is True')
# def step_then_section_first_page_footer_is_linked(context):
#     assert context.section.first_page_footer.is_linked_to_previous is True
