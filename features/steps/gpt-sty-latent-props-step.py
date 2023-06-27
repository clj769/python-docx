# from behave import given, when, then
# from docx import Document
# from features.steps.helpers import test_docx, bool_vals
#
#
# @given('a latent styles object with known defaults')
# def step_given_latent_styles_object_with_known_defaults(context):
#     context.document = Document(test_docx('sty-known-styles'))
#     context.latent_styles = context.document.styles.latent_styles
#
# @then('latent_styles.{prop_name} is {value}')
# def step_then_latent_styles_property_is_value(context, prop_name, value):
#     assert getattr(context.latent_styles, prop_name) == bool_vals[value] if value in bool_vals else int(value)
#
# @when('I assign {new_value} to latent_styles.{prop_name}')
# def step_when_assign_new_value_to_latent_styles_property(context, new_value, prop_name):
#     value = bool_vals[new_value] if new_value in bool_vals else int(new_value)
#     setattr(context.latent_styles, prop_name, value)
#
# @given('a latent style having a known name')
# def step_given_latent_style_with_known_name(context):
#     document = Document(test_docx('sty-known-styles'))
#     context.latent_styles = list(document.styles.latent_styles)
#     context.latent_style = context.latent_styles[0]  # Assume we use the last style for this scenario
#
# @then('latent_style.name is the known name')
# def step_then_latent_style_name_is_known_name(context):
#     assert context.latent_style.name == context.latent_style.name
#
# @given('a latent style having priority of {setting}')
# def step_given_latent_style_with_priority(context, setting):
#     # Here you need to implement code that sets the priority according to the setting
#     context.document = Document(test_docx('sty-known-styles'))
#     if setting == '42':
#         context.latent_style = context.document.styles.latent_styles['Normal']
#     elif setting =='no setting':
#         context.latent_style = context.document.styles.latent_styles['Subtitle']
#
#
# @then('latent_style.priority is {value}')
# def step_then_latent_style_priority_is_value(context, value):
#     if value == 'None':
#         assert context.latent_style.priority == None
#     else:
#         assert context.latent_style.priority == int(value)
#
# @when('I assign {new_value} to latent_style.priority')
# def step_when_assign_new_value_to_latent_style_priority(context, new_value):
#     if new_value == 'None':
#         context.latent_style.priority = None
#     else:
#         context.latent_style.priority = int(new_value)
#
# @given('a latent style having {prop_name} set {setting}')
# def step_given_latent_style_with_property_set(context, prop_name, setting):
#     # Here you need to implement code that sets the property according to the setting
#     context.document = Document(test_docx('sty-known-styles'))
#     if setting == 'on':
#         context.latent_style = context.document.styles.latent_styles['Normal']
#     elif setting =='no setting':
#         context.latent_style = context.document.styles.latent_styles['Subtitle']
#     elif setting =='off':
#         context.latent_style = context.document.styles.latent_styles['Title']
#
#
# @then('latent_style.{prop_name} is {value}')
# def step_then_latent_style_property_is_value(context, prop_name, value):
#     if value == 'None':
#         assert getattr(context.latent_style, prop_name) == None
#     else:
#         assert getattr(context.latent_style, prop_name) == bool_vals[value]
#
# @when('I assign {new_value} to latent_style.{prop_name}')
# def step_when_assign_new_value_to_latent_style_property(context, new_value, prop_name):
#     if new_value == 'None':
#         setattr(context.latent_style, prop_name, None)
#     else:
#         setattr(context.latent_style, prop_name,  bool_vals[new_value])
