
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

#
rptObj.materials.fab("favorite")
rptObj.materials.fab("favorite", mini=True)

#
rptObj.ui.layouts.new_line()
rptObj.materials.fabs.extended("favorite")
rptObj.materials.fabs.extended("favorite", "favorite", mini=True)


b = rptObj.materials.fabs.extended("favorite")
b += rptObj.materials.icon("favorite")

#
rptObj.ui.layouts.new_line()
rptObj.materials.button("favorite")

#
rptObj.ui.layouts.new_line()
rptObj.materials.button("favorite", label="Favorites")

rptObj.ui.layouts.new_line()
rptObj.materials.buttons.toggle(False)

rptObj.ui.layouts.new_line()
rptObj.materials.buttons.toggle(True)


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
