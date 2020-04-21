

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.texts.chip("test")
rptObj.materials.texts.chip(["test %s" % i for i in range(5)])

rptObj.materials.texts.chip(["test %s" % i for i in range(5)], choice=True)

rptObj.materials.inputs.chip(["test %s" % i for i in range(5)])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
