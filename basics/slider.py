

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.slider()

rptObj.materials.sliders.discrete(20)

rptObj.materials.sliders.tracker(20)



#rptObj.materials.selects.outlined("Test")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
