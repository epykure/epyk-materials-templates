

from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

s1 = rptObj.materials.select(["Test", "data"], label="Ok")

s2 = rptObj.materials.selects.outlined(["Test", "data"], label="Ok")


rptObj.ui.button("Test").click([
    rptObj.js.console.log(s1.dom.getValue()),
    s1.dom.setValue("Data"),
    #s1.dom.setDisabled(True),
    rptObj.js.console.log(s1.dom.getSelectedIndex()),
])

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
