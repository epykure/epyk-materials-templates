import PacthRunner

from epyk_materials.core.Page import Report
import config

# Create a basic report object
rptObj = Report()
chk1 = rptObj.materials.inputs.checkbox(True, "test")
chk2 = rptObj.materials.inputs.checkbox(False, "test2")
chk3 = rptObj.materials.inputs.checkbox(False, "test3")
rptObj.js.addOnReady([chk3.dom.setStatus('indeterminate')])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)

