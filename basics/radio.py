

from epyk_materials.core.Page import Report
import config

# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
r1 = rptObj.materials.radio('event', value=1, group_name="group_1")

#
r2 = rptObj.materials.radio('event 2', value=2, group_name="group_1")

#
r3 = rptObj.materials.radio('event 3', value=3, group_name="group_1")

#
rptObj.ui.button("Test").click([
  r2[0].dom.addClass("test"),
  r3[0].dom.setDisabled(),
  rptObj.js.console.log(r1[0].dom.content),
  rptObj.js.console.log(r1[0].dom.value),
  r1[0].dom.check(True),
])

# Move the console to this location
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
