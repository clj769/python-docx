# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx
#
#
# @given('a document having known styles')
# def step_given_document_with_known_styles(context):
#     context.document = Document(test_docx('sty-known-styles'))
#     context.initial_latent_style_count = len(context.document.styles.latent_styles)
#
# @when("I add a latent style named 'Foobar'")
# def step_when_add_latent_style(context):
#     context.new_latent_style = context.document.styles.latent_styles.add_latent_style('Foobar')
#
# @then('the document has one additional latent style')
# def step_then_document_has_one_additional_latent_style(context):
#     assert len(context.document.styles.latent_styles) == context.initial_latent_style_count + 1
#
# @then("latent_styles['Foobar'] is a latent style")
# def step_then_latent_styles_foobar_is_latent_style(context):
#     assert context.new_latent_style == context.document.styles.latent_styles['Foobar']
#
# @when('I delete a latent style')
# def step_when_delete_latent_style(context):
#     # Assuming we have a method delete_latent_style in python-docx (which we don't)
#     context.deleted_latent_style_name = context.document.styles.latent_styles['Normal']
#     context.document.styles.latent_styles['Normal'].delete()
#
# @then('the document has one fewer latent styles')
# def step_then_document_has_one_fewer_latent_style(context):
#     assert len(context.document.styles.latent_styles) == context.initial_latent_style_count - 1
#
# @then('the deleted latent style is not in the latent styles collection')
# def step_then_deleted_latent_style_not_in_latent_styles(context):
#     assert context.deleted_latent_style_name not in context.document.styles.latent_styles
