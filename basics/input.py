
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
rptObj.materials.inputs.textarea("", "favorite")

rptObj.materials.new_line()
i = rptObj.materials.inputs.input("", "favorite")

# Add a passworkd object
rptObj.materials.new_line()
p = rptObj.materials.inputs.password("", "password", required=True, rules={"minlength": 7})

# Add a [prefilled component
rptObj.materials.new_line()
p = rptObj.materials.inputs.prefilled("data", "password")

#
rptObj.materials.new_line()
i += rptObj.materials.icon("favorite")

#
rptObj.materials.new_line()
rptObj.materials.inputs.outlined("", "favorite")

# Add an outlined input component with leading icon
rptObj.materials.new_line()
text_1 = rptObj.materials.inputs.outlined("Test", "Title", leading_icon="favorite")

# Add an outlined input component with trailing icon
rptObj.materials.new_line()
text_2 = rptObj.materials.inputs.outlined("Test", "Title", trailing_icon="visibility")

# Add a standard button
rptObj.ui.button("Click").click([
  p.dom.setDisabled(True),
  c.dom.write(i.dom.content),
  text_1.dom.setValue(i.dom.content),
])

# Move the console to this location
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
