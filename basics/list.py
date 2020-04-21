

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.list(["Test 1", "Test 2"])
rptObj.materials.lists.selections(["Test 1", "Test 2"])
rptObj.materials.lists.radios(["Test 1", "Test 2"])
rptObj.materials.lists.checkbox(["Test 1", "Test 2"])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
