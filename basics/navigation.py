
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()


rptObj.materials.tabs(["A", "B"])

rptObj.ui.layouts.new_line()
rptObj.materials.sliders.progressbar(0.6)

rptObj.ui.layouts.new_line()
bar = rptObj.materials.sliders.progressbar()

rptObj.ui.layouts.new_line()
rev = rptObj.materials.sliders.progressbar(0.2)

rptObj.ui.button("Click").click([
  bar.js.progress.setBuffer(0.3),
  rev.js.progress.setReverse(True),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
