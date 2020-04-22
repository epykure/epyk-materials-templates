

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

s1 = rptObj.materials.slider()

s2 = rptObj.materials.sliders.discrete(20)

s3 = rptObj.materials.sliders.tracker(20)


rptObj.ui.button("Test").click([
    rptObj.js.console.log(s2.dom.getValue()),
    rptObj.js.console.log(s3.dom.getMax()),
])


#rptObj.materials.selects.outlined("Test")

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
