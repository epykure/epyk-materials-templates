
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

#
s = rptObj.materials.buttons.toggle(True)

rptObj.materials.button("favorite", label="Favortie")

rptObj.ui.button("Click").click([
  rptObj.js.console.log(s.dom.checked),
  s.dom.check(True)
])
#


# #
# # rptObj.materials.buttons.toggle()
# #
# #i = rptObj.materials.texts.icon("favorite")
# # rptObj.ui.layouts.new_line(5)
# # s = rptObj.materials.sliders.slider(70)
#
# #n = rptObj.materials.inputs.filled("Test", "Title")
# n = rptObj.materials.inputs.filled("Test", "Title", leading_icon="favorite")
# n = rptObj.materials.inputs.filled("Test", "Title", trailing_icon="visibility")
# rptObj.ui.layouts.new_line(5)
#
# # i = rptObj.ui.input()
# # f.style.mdc.elevation()
#
# #
# # c = rptObj.materials.buttons.toggle(False)
# # c.click([
# #   i.js.toggle.setAttr()
# # ])
# #
# # filled = rptObj.materials.inputs.filled("test", "favorite")
# # filled.click([
# #   filled.val.js.line_ripple.test()
# # ])
#
# #


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
