import os

import clack

if not os.environ.get('READTHEDOCS', None):
    import sphinx_rtd_theme
    html_theme = 'sphinx_rtd_theme'
    html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

master_doc = 'index'
exclude_patterns = ['_build']

# General information about the project.
project = u'clack'
copyright = u'2014, ' + clack.__author__
version = release = clack.__version__

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc']
autodoc_member_order = 'bysource'
autoclass_content = 'both'
