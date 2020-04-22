
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

#rptObj.materials.inputs.textarea("", "favorite")
#rptObj.materials.inputs.input("", "favorite")
#rptObj.materials.inputs.filled("", "favorite")
#rptObj.materials.inputs.outlined("", "favorite")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
