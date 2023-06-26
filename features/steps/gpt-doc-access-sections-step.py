# from behave import given, when, then
# from docx import Document
# from docx.section import Section
# from features.steps.helpers import test_docx
#
# context_num_of_sections = 3
#
# @given('a section collection containing 3 sections')
# def step_given_a_section_collection(context):
#     document = Document(test_docx('doc-access-sections'))
#     context.sections = document.sections
#
# @then('len(sections) is 3')
# def step_then_len_sections_is_three(context):
#     assert len(context.sections) == context_num_of_sections
#
# @then('I can iterate over the sections')
# def step_then_can_iterate_over_sections(context):
#     for section in context.sections:
#         assert isinstance(section, Section)
#
# @then('I can access a section by index')
# def step_then_can_access_section_by_index(context):
#     assert isinstance(context.sections[0], Section)
