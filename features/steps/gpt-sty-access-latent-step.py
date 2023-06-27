# from behave import given, then
# from docx import Document
# from docx.styles.latent import LatentStyles
#
# @given('the style collection of a document')
# def step_given_style_collection_of_document(context):
#     context.document = Document()
#     context.styles = context.document.styles
#
# @then('styles.latent_styles is the LatentStyles object for the document')
# def step_then_latent_styles_object(context):
#     assert isinstance(context.styles.latent_styles, LatentStyles)
#
# @then('len(latent_styles) is 137')
# def step_then_len_latent_styles_is_137(context):
#     assert len(context.styles.latent_styles) == 137
#
# @given('a latent style collection')
# def step_given_latent_style_collection(context):
#     context.document = Document()
#     context.latent_styles = context.document.styles.latent_styles
#
# @then('I can iterate over the latent styles')
# def step_then_iterate_over_latent_styles(context):
#     for latent_style in context.latent_styles:
#         pass  # Do nothing, just iterate
#
# @then('I can access a latent style by name')
# def step_then_access_latent_style_by_name(context):
#     # Assume there's a latent style named 'Normal'
#     latent_style = context.latent_styles['Normal']
#     assert latent_style is not None
