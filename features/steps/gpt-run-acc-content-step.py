# from behave import given, when, then
# from docx import Document
# from docx.oxml import OxmlElement
#
# @given('a run having mixed text content')
# def step_given_a_run_having_mixed_text_content(context):
#     context.doc = Document()
#     context.para = context.doc.add_paragraph()
#     context.run = context.para.add_run()
#
#     context.run.text = 'Some text'
#     tab = OxmlElement('w:tab')
#     context.run._r.append(tab)
#     context.run.add_text(' more text')
#     br = OxmlElement('w:br')
#     context.run._r.append(br)
#     context.run.add_text(' and some text after a line break')
#
# @then('the text of the run represents the textual run content')
# def step_then_text_of_run_represents_textual_run_content(context):
#     assert context.run.text == 'Some text\t more text\n and some text after a line break', \
#         f"Expected 'Some text\t more text\n and some text after a line break', but got {context.run.text}"
