

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.select("Test")
rptObj.materials.selects.outlined("Test")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
