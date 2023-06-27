# from behave import given, when, then
# from docx import Document
# from docx.enum.style import WD_STYLE_TYPE
# from features.steps.helpers import test_docx, tri_state_vals, bool_vals
#
#
# @given('a style based on {base_style}')
# def step_given_a_style_based_on(context, base_style):
#     if base_style == 'no style':
#         style_name = 'Base'
#     elif base_style == 'Normal':
#         style_name = 'Sub Normal'
#     elif base_style == 'Base':
#         style_name = 'Citation'
#
#     document = Document(test_docx('sty-known-styles'))
#     context.styles = document.styles
#     context.style = document.styles[style_name]
#
# @given('a style having hidden set {setting}')
# def step_given_a_style_with_hidden_set(context, setting):
#     document = Document(test_docx('sty-behav-props'))
#     if setting =='on':
#         style_name = 'Foo'
#     elif setting == 'off':
#         style_name = 'Bar'
#     elif setting =='no setting':
#         style_name = 'Baz'
#     context.style = document.styles[style_name]
#
# @given('a style having locked set {setting}')
# def step_given_a_style_with_locked_set(context, setting):
#     document = Document(test_docx('sty-behav-props'))
#     if setting == 'on':
#         style_name = 'Foo'
#     elif setting == 'off':
#         style_name = 'Bar'
#     elif setting == 'no setting':
#         style_name = 'Baz'
#     context.style = document.styles[style_name]
#
# @given('a style having next paragraph style set to {setting}')
# def step_given_style_next_paragraph_style_set(context, setting):
#
#     # document = Document(test_docx('sty-known-styles'))
#     # if setting == 'Sub Normal': style_name = 'Citation'
#     # elif setting == 'Footbar': style_name = 'Sub Normal'
#     # elif setting == 'Base': style_name = 'Foo'
#     # elif setting == 'no setting': style_name = 'Base'
#     #
#     # context.styles = document.styles
#     # context.style = document.styles[style_name]
#
#     #TODO: UnboundLocalError: local variable 'style_name' referenced before assignment
#     document = Document(test_docx('sty-known-styles'))
#     style_name = {
#         'Sub Normal': 'Citation',
#         'Foobar':     'Sub Normal',
#         'Base':       'Foo',
#         'no setting': 'Base',
#     }[setting]
#     context.styles = document.styles
#     context.style = document.styles[style_name]
#
# @given('a style having priority of {setting}')
# def step_given_style_priority_of(context, setting):
#     document = Document(test_docx('sty-behav-props'))
#     if setting == '42':
#         style_name = 'Foo'
#     elif setting == 'no setting':
#         style_name = 'Baz'
#
#     context.style = document.styles[style_name]
#
# @given('a style having quick-style set {setting}')
# def step_given_style_quick_style_set(context, setting):
#     document = Document(test_docx('sty-behav-props'))
#     if setting == 'on':
#         style_name = 'Foo'
#     elif setting == 'off':
#         style_name = 'Bar'
#     elif setting == 'no setting':
#         style_name = 'Baz'
#     context.style = document.styles[style_name]
#
# @given('a style having a known {attr_name}')
# def given_a_style_having_a_known_attr_name(context, attr_name):
#     docx_path = test_docx('sty-having-styles-part')
#     document = Document(docx_path)
#     context.style = document.styles['Normal']
#
# @given('a style having unhide-when-used set {setting}')
# def step_given_style_unhide_when_used_set(context, setting):
#     document = Document(test_docx('sty-behav-props'))
#     if setting == 'on':
#         style_name = 'Foo'
#     elif setting == 'off':
#         style_name = 'Bar'
#     elif setting == 'no setting':
#         style_name = 'Baz'
#     context.style = document.styles[style_name]
#
# @when('I assign {assigned_value} to style.base_style')
# def step_when_assign_value_to_style_base_style(context, assigned_value):
#     if assigned_value ==  'None': value = None
#     elif assigned_value == 'styles[\'Normal\']': value = context.styles['Normal']
#     elif assigned_value == 'styles[\'Base\']': value = context.styles['Base']
#
#     context.style.base_style = value
#
# @when('I assign {new_value} to style.hidden')
# def step_when_assign_new_value_to_style_hidden(context, new_value):
#     style, new_value = context.style, tri_state_vals[new_value]
#     style.hidden = new_value
#
# @when('I assign {new_value} to style.locked')
# def step_when_assign_new_value_to_style_locked(context, new_value):
#     style, new_value = context.style, bool_vals[new_value]
#     style.locked = new_value
#
# @when('I assign {new_value} to style.next_paragraph_style')
# def step_when_assign_new_value_to_style_next_paragraph_style(context, new_value):
#     styles, style = context.styles, context.style
#     new_value = None if new_value == 'None' else styles[new_value]
#     style.next_paragraph_style = new_value
#
# @when('I assign {new_value} to style.priority')
# def step_when_assign_new_value_to_style_priority(context, new_value):
#     new_value = None if new_value == 'None' else int(new_value)
#     context.style.priority = new_value
#
# @when('I assign {new_value} to style.quick_style')
# def step_when_assign_new_value_to_style_quick_style(context, new_value):
#     context.style.quick_style = bool_vals[new_value]
#
# @when('I assign a new value to style.style_id')
# def step_when_assign_new_value_to_style_style_id(context):
#     context.style.style_id = "Foo42"
#
# @when('I assign a new name to the style')
# def when_I_assign_a_new_name_to_the_style(context):
#     context.style.name = 'Foobar'
#
# @when('I assign {new_value} to style.unhide_when_used')
# def step_when_assign_new_value_to_style_unhide_when_used(context, new_value):
#     context.style.unhide_when_used = bool_vals[new_value]
#
#
# @then('style.base_style is {value}')
# def step_then_style_base_style_is_value(context, value):
#     if value == 'None': expected_value = None
#     elif value == 'styles[\'Normal\']': expected_value = context.styles['Normal']
#     elif value == 'styles[\'Base\']':expected_value =  context.styles['Base']
#     assert context.style.base_style == expected_value
#
# @then('style.hidden is {value}')
# def step_then_style_hidden_is_value(context, value):
#     assert context.style.hidden == tri_state_vals[value]
#
# @then('style.locked is {value}')
# def step_then_style_locked_is_value(context, value):
#     assert context.style.locked == bool_vals[value]
#
# @then('style.next_paragraph_style is {value}')
# def step_then_style_next_paragraph_style_is_value(context, value):
#     assert context.style.next_paragraph_style == context.styles[value]
#
# @then('style.priority is {value}')
# def step_then_style_priority_is_value(context, value):
#     value = None if value == 'None' else int(value)
#     assert context.style.priority == value
#
# @then('style.quick_style is {value}')
# def step_then_style_quick_style_is_value(context, value):
#     assert context.style.quick_style == bool_vals[value]
#
# @then('style.style_id is the {which} style id')
# def then_style_style_id_is_the_which_style_id(context, which):
#     expected_style_id = {
#         'known': 'Normal',
#         'new':   'Foo42',
#     }[which]
#     style = context.style
#     assert style.style_id == expected_style_id
#
# @then('style.name is the {which} name')
# def then_style_name_is_the_which_name(context, which):
#     if which == 'known': expected_name = 'Normal'
#     elif which == 'new': expected_name = 'Foobar'
#     assert context.style.name == expected_name
#
# @then('style.unhide_when_used is {value}')
# def step_then_style_unhide_when_used_is_value(context, value):
#     assert context.style.unhide_when_used == bool_vals[value]
#
# @then('style.type is the known type')
# def then_style_type_is_the_known_type(context):
#     assert context.style.type == WD_STYLE_TYPE.PARAGRAPH