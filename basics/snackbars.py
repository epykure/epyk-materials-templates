from epyk_materials.core.Page import Report
import config


rptObj = Report()
snkbar1 = rptObj.materials.texts.snackbar('This is a message')
snkbar2 = rptObj.materials.texts.snackbar('This is a message', type='LEADING')
snkbar3 = rptObj.materials.texts.snackbar('This is a message', type='STACKED')

btn1 = rptObj.ui.buttons.button('test1')
btn2 = rptObj.ui.buttons.button('test2')
btn3 = rptObj.ui.buttons.button('test3')


btn1.click(snkbar1.dom.open())
btn2.click(snkbar2.dom.open())
btn3.click(snkbar3.dom.open())

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)

