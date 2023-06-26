# from behave import given, then
# from docx import Document
# from features.steps.helpers import test_docx
#
# context_num_of_paragraphs = 3
# context_num_of_tables = 3
#
# @given('a document having inline shapes')
# def step_given_a_document_with_inline_shapes(context):
#     # Here, you should add an inline shape to the document.
#     # Manually adding an inline shapex.
#     context.doc = Document(test_docx('shp-inline-shape-access'))
#
# @given('a document containing three paragraphs')
# def step_given_a_document_with_paragraphs(context):
#     context.doc = Document()
#     for _ in range(context_num_of_paragraphs):
#         context.doc.add_paragraph()
#
# @given('a document having sections')
# def step_given_a_document_with_sections(context):
#     # Here, you should add sections to the document.
#     # Manually adding sections.
#     context.doc = Document(test_docx('doc-access-sections'))
#
# @given('a document having styles')
# def step_given_a_document_with_styles(context):
#     # Here, you should add styles to the document.
#     # Manually adding styles
#     context.doc = Document(test_docx('sty-having-styles-part'))
#
# @given('a document having three tables')
# def step_given_a_document_with_tables(context):
#     context.doc = Document()
#     for _ in range(context_num_of_tables):
#         context.doc.add_table(rows=2, cols=2)
#
# @then('document.inline_shapes is an InlineShapes object')
# def step_then_document_has_inlineshapes(context):
#     assert len(context.doc.inline_shapes) > 0
#
# @then('document.paragraphs is a list containing three paragraphs')
# def step_then_document_has_paragraphs(context):
#     assert len(context.doc.paragraphs) == context_num_of_paragraphs
#
# @then('document.sections is a Sections object')
# def step_then_document_has_sections(context):
#     assert len(context.doc.sections) > 0
#
# @then('document.styles is a Styles object')
# def step_then_document_has_styles(context):
#     assert len(context.doc.styles) > 0
#
# @then('document.tables is a list containing three tables')
# def step_then_document_has_tables(context):
#     assert len(context.doc.tables) == context_num_of_tables
