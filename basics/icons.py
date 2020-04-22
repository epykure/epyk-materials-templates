
from epyk_materials.core.Page import Report
import config


# Create a basic report object
rptObj = Report()

# Create an icon
rptObj.materials.icon('favorite')

rptObj.ui.layouts.new_line()
rptObj.materials.icon('favorite', in_text_field=True)

rptObj.ui.layouts.new_line()
rptObj.materials.icons.text('favorite', 'favorite')

rptObj.ui.layouts.new_line()
rptObj.materials.icons.field('favorite')


# Create a basic icon button
#rptObj.materials.icons.button('favorite')

# Create a basic toggle icon button
#rptObj.materials.icons.toggle('favorite')

rptObj.outs.html_file(path=config.OUTPUT_PATHS_LOCALS_HTML, name=config.OUT_FILENAME)
