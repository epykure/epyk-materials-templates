

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

# Add on chip
c1 = rptObj.materials.texts.chip("test")

rptObj.ui.layouts.hr()

# Add a list of chips
c2 = rptObj.materials.texts.chip(["test %s" % i for i in range(5)])

rptObj.ui.layouts.hr()

# Add chip items with a selection
c3 = rptObj.materials.texts.chip(["test %s" % i for i in range(5)], choice=True)

rptObj.ui.layouts.hr()

#
c4 = rptObj.materials.inputs.chip(["test %s" % i for i in range(5)])

rptObj.ui.layouts.hr()

# Add an event
rptObj.ui.button("Test").click([
  c3.dom.selectChipAtIndex(4),
])

c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
