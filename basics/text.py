

from epyk_materials.core.Page import Report
import config

# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
rptObj.materials.texts.icon("favorite")

#
rptObj.materials.texts.floating("Hello")

# Move the console to this location
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
