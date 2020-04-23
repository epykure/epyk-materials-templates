

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
rptObj.materials.list(["Test 1", "Test 2"])

#
rptObj.materials.lists.selections(["Test 1", "Test 2"])

#
rptObj.materials.lists.radios(["Test 1", "Test 2"])

#
rptObj.materials.lists.checkbox(["Test 1", "Test 2"])

# Move the console to this location
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
