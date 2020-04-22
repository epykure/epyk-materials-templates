

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.texts.icon("favorite")

rptObj.materials.texts.floating("Hello")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
