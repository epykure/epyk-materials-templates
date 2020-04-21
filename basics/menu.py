

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

surface = rptObj.materials.menu.surface()

rptObj.materials.menu.anchor("Test", surface)


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
