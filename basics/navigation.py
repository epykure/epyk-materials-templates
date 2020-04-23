
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()
rptObj.headers._favicon_url = config.FAVICON_URL # Change the Epyk logo

# Console component
c = rptObj.ui.rich.console("* This is a log section for all the events in the different buttons *", options={"timestamp": True})

#
tab1 = rptObj.materials.tabs(["A", "B"])

#
rptObj.materials.navigation.app_bar("Dismissible Drawer")

#
rptObj.materials.drawers(['Inbox', 'Outgoing', 'Drafts'])

#
rptObj.materials.navigation.drawer_app("App Content")

#
rptObj.ui.layouts.new_line()
tab2 = rptObj.materials.tabs(["Tab %s" % i for i in range(10)])

#
rptObj.ui.button("Test").click([
  rptObj.js.console.log(tab1.dom.getScrollPosition()),
  rptObj.js.console.log(tab1.dom.getTabListLength()),
  tab2.dom.setActiveTab(2),
  tab2.dom.deactivateTabAtIndex(3),
  tab2.dom.getTabListLength(),
])

# rptObj.ui.layouts.new_line()
# rptObj.materials.sliders.progressbar(0.6)
#
# rptObj.ui.layouts.new_line()
# bar = rptObj.materials.sliders.progressbar()
#
# rptObj.ui.layouts.new_line()
# rev = rptObj.materials.sliders.progressbar(0.2)

rptObj.ui.layouts.new_line()
rptObj.ui.button("Click").click([
  #bar.dom.setBuffer(0.3),
  #rev.dom.setReverse(True),
])

# Move the console to this location
c.move()

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
