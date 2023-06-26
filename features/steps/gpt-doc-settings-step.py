# from docx import Document
# from behave import given, when, then
#
# from features.steps.helpers import test_docx
#
# # Manually added testing file
#
# @given('a document having {presence} settings part')
# def step_given_document_with_settings_presence(context, presence):
#     if presence == 'a':
#         context.doc = Document(test_docx('doc-word-default-blank'))
#     else:
#         context.doc = Document(test_docx('set-no-settings-part'))
#
# @then('document.settings is a Settings object')
# def step_then_document_settings_is_settings_object(context):
#     assert context.doc.settings is not None
#
# @given('a Settings object {presence} odd and even page headers as settings')
# def step_given_settings_object_with_odd_even_page_headers_presence(context, presence):
#     if presence == 'with':
#         context.settings = Document(test_docx('doc-odd-even-hdrs')).settings
#     else:
#         context.settings = Document(test_docx('sct-section-props')).settings
#
# @then('settings.odd_and_even_pages_header_footer is {value}')
# def step_then_settings_odd_and_even_pages_header_footer_is_value(context, value):
#     expected_value = value.lower() == 'true'
#     assert context.settings.odd_and_even_pages_header_footer == expected_value
#
# @when('I assign {value} to settings.odd_and_even_pages_header_footer')
# def step_when_assign_value_to_settings_odd_and_even_pages_header_footer(context, value):
#     new_value = value.lower() == 'true'
#     context.settings.odd_and_even_pages_header_footer = new_value
