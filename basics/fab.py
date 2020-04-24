
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
rptObj.materials.fab("favorite")
rptObj.materials.fab("favorite", mini=True)

#
rptObj.materials.new_line()
rptObj.materials.fabs.extended("favorite")

rptObj.materials.new_line()
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

# Move the console to this location
c.move()


rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
