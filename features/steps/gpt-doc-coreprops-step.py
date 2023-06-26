# from datetime import datetime
#
# from docx import Document
# from behave import given, when, then
#
# from features.steps.helpers import test_docx
#
# # Manually added some test file
#
# @given('a document having known core properties')
# def step_given_document_with_known_core_properties(context):
#     context.doc = Document(test_docx('doc-coreprops'))
#
# @then('I can access the core properties object')
# def step_then_access_core_properties_object(context):
#     context.core_properties = context.doc.core_properties
#
# @then('the core property values match the known values')
# def step_then_core_property_values_match_known_values(context):
#     # Replace 'known_values' with the actual values
#     known_values = {
#         'author': 'Steve Canny',
#         'title':  'Title',
#         'subject': 'Subject',
#         'keywords': 'key; word; keyword',
#         'last_modified_by':  'Steve Canny',
#         'created': datetime(2014, 12, 13, 22, 2, 0),
#         'modified': datetime(2014, 12, 13, 22, 6, 0),
#         # Add other known values as necessary
#     }
#     for key, value in known_values.items():
#         assert getattr(context.core_properties, key) == value
#
# @when('I assign new values to the properties')
# def step_when_assign_new_values_to_properties(context):
#     new_values = {
#         'author': 'Lujing Cai',
#         'title': 'New Document',
#         'subject': 'New Testing',
#         'keywords': 'new, docx',
#         'last_modified_by': 'Lujing Cai',
#         'created': datetime(2023, 12, 13, 22, 2, 0),
#         'modified': datetime(2023, 12, 13, 22, 2, 0),
#         # Add other new values as necessary
#     }
#     for key, value in new_values.items():
#         setattr(context.doc.core_properties, key, value)
#
# @then('the core property values match the new values')
# def step_then_core_property_values_match_new_values(context):
#     new_values = {
#         'author': 'Lujing Cai',
#         'title': 'New Document',
#         'subject': 'New Testing',
#         'keywords': 'new, docx',
#         'last_modified_by': 'Lujing Cai',
#         'created': datetime(2023, 12, 13, 22, 2, 0),
#         'modified': datetime(2023, 12, 13, 22, 2, 0),
#         # Add other new values as necessary
#     }
#     for key, value in new_values.items():
#         assert getattr(context.doc.core_properties, key) == value
#
# @given('a document having no core properties part')
# def step_given_document_with_no_core_properties(context):
#     context.doc = Document(test_docx('doc-no-coreprops'))
#
# @when('I access the core properties object')
# def step_when_access_core_properties_object(context):
#     context.core_properties = context.doc.core_properties
#
# @then('a core properties part with default values is added')
# def step_then_core_properties_part_with_default_values_is_added(context):
#     # Check that core properties exist and have default values
#     assert context.core_properties is not None
#     assert context.core_properties.title == 'Word Document'
#     # Check other properties as necessary
