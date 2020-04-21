
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

#
rptObj.materials.button("favorite")

#
rptObj.materials.buttons.toggle(True)

#
rptObj.materials.button("favorite", label="Favortie")

#
r1 = rptObj.materials.radio('event', group_name="group_1")
r2 = rptObj.materials.radio('event 2', group_name="group_1")
r3 = rptObj.materials.radio('event 3', group_name="group_1")

rptObj.ui.button("Click").click([
  r1[0].js.radio.disabled(True)
])

#
# # rptObj.materials.buttons.icon("favorite")
# #
# # rptObj.materials.buttons.toggle()
# #
# # rptObj.materials.inputs.textarea("", "favorite")
# # rptObj.materials.inputs.input("", "favorite")
# # rptObj.materials.inputs.filled("", "favorite")
# # rptObj.materials.inputs.outlined("", "favorite")
#
#
# #i = rptObj.materials.texts.icon("favorite")
# # rptObj.ui.layouts.new_line(5)
# # s = rptObj.materials.sliders.slider(70)
#
# #n = rptObj.materials.inputs.filled("Test", "Title")
# n = rptObj.materials.inputs.filled("Test", "Title", leading_icon="favorite")
# n = rptObj.materials.inputs.filled("Test", "Title", trailing_icon="visibility")
# rptObj.ui.layouts.new_line(5)
#
# rptObj.materials.inputs.radio(True, group_name="group_1")
# rptObj.materials.inputs.radio(False, group_name="group_1")
#
# rptObj.materials.menus.surface()
#
# #p = rptObj.materials.sliders.progressbar(40, label='Test')
#
# # i = rptObj.ui.input()
# # f = rptObj.materials.texts.floating("Hello")
# # f.style.mdc.elevation()
#
# rptObj.materials.switch(False)
# rptObj.ui.button("Click").click([
#   # s.js.slider.setValue(i.dom.content),
#   # f.js.floating.shake(True)
# ])
# #
# # c = rptObj.materials.buttons.toggle(False)
# # c.click([
# #   i.js.toggle.setAttr()
# # ])
# #
# # rptObj.materials.buttons.toggle(True)
#
# # filled = rptObj.materials.inputs.filled("test", "favorite")
# # filled.click([
# #   filled.val.js.line_ripple.test()
# # ])
# # schema = {"type": 'div', 'children': [
# #   {"type": 'div', 'args': {"htmlObjs": 'youpi 1'}},
# #   {"type": 'div', 'args': {"htmlObjs": 'youpi 2'}}
# # ]}
# #
# # comp = rptObj.ui.composite(schema)
# # comp.click([
# #   comp[1].build("TTTT")
# # ])
#
# # rptObj.materials.sliders.progressbar(39)
# #
# # rptObj.materials.inputs.chips("test")
# # rptObj.materials.icons.icon("favorite")
# # rptObj.materials.icons.clock()
# #
# # r = rptObj.materials.icons.refresh()
# # r.style.css.color = "red"
# # r.style.css.cursor = "pointer"
# # r.click([
# #   rptObj.js.alert("")
# # ])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
