

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

r1 = rptObj.materials.radio('event', group_name="group_1")
r2 = rptObj.materials.radio('event 2', group_name="group_1")
r3 = rptObj.materials.radio('event 3', group_name="group_1")


rptObj.ui.button("Test").click([

])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
