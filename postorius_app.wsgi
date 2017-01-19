import os
import site

# project root directory (one above `srv`)
root_dir = os.path.abspath('/app/postorious-standalone')

# prepend root dir to python path
site.addsitedir(root_dir)

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
