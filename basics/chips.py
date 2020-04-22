

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

c1 = rptObj.materials.texts.chip("test")

c2 = rptObj.materials.texts.chip(["test %s" % i for i in range(5)])

c3 = rptObj.materials.texts.chip(["test %s" % i for i in range(5)], choice=True)

c4 = rptObj.materials.inputs.chip(["test %s" % i for i in range(5)])

rptObj.ui.button("Test").click([
  c3.dom.selectChipAtIndex(4),
])


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
