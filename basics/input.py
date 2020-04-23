
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

rptObj.materials.inputs.textarea("", "favorite")
i = rptObj.materials.inputs.input("", "favorite")

p = rptObj.materials.inputs.password("", "password", required=True, rules={"minlength": 7})
p = rptObj.materials.inputs.prefilled("data", "password")

i += rptObj.materials.icon("favorite")

#rptObj.materials.inputs.filled("", "favorite")
rptObj.materials.inputs.outlined("", "favorite")
text_1 = rptObj.materials.inputs.outlined("Test", "Title", leading_icon="favorite")
text_2 = rptObj.materials.inputs.outlined("Test", "Title", trailing_icon="visibility")

rptObj.ui.button("Click").click([
  p.dom.setDisabled(True),
  rptObj.js.console.log(i.dom.content),
  text_1.dom.setValue(i.dom.content),
])
rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
