# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

from datetime import datetime
# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
from os.path import dirname, join

with open(join(dirname(__file__), '../../deirokay/__version__.py')) as v:
    __version__ = None
    exec(v.read().strip())


# -- Project information -----------------------------------------------------

project = 'Deirokay'
copyright = f'{datetime.now().year}, Big Data'
author = 'Marcos Bressan'

# The full version, including alpha/beta/rc tags
release = __version__


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.todo',
    'sphinx.ext.napoleon',
    # Link to other project's documentation (see mapping below)
    'sphinx.ext.intersphinx',
    # Add a link to the Python source code for classes, functions etc.
    'sphinx.ext.viewcode',
    # Add a link to another page of the documentation
    'sphinx.ext.autosectionlabel'
]

# napoleon configuration for numpy docstring
todo_include_todos = True
napoleon_use_ivar = True
napoleon_use_google_string = False
napoleon_include_special_with_doc = True

# autosummary
autosummary_generate = True  # Turn on sphinx.ext.autosummary
autoclass_content = "both"  # Add __init__ doc (ie. params) to class summaries
# If no class summary, inherit base class summary
autodoc_inherit_docstrings = True
# Remove 'view source code' from top of page (for html, not python)
html_show_sourcelink = False

# For maths, use mathjax by default and svg if NO_MATHJAX env variable is set
# (useful for viewing the doc offline)
# (include if necessary)
# if os.environ.get('NO_MATHJAX'):
#     extensions.append('sphinx.ext.imgmath')
#     imgmath_image_format = 'svg'
#     mathjax_path = ''
# else:
#     extensions.append('sphinx.ext.mathjax')
#     mathjax_path = ('https://cdn.jsdelivr.net/npm/mathjax@3/es5/'
#                     'tex-chtml.js')

# For PDFs, we could use pdflatex
# TODO: Include specifications for pdflatex work

# I don't know what this does
# (include if necessary)
# autosummary_generate = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en_US'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
exclude_dirs = ['images', 'scripts', 'sandbox']

# The suffix of souce filenames.
source_suffix = '.rst'

# The master toctree document
master_doc = 'index'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static', 'images']

# html_use_smartypants = True

html_theme_options = {
    'logo_only': False,
    'display_version': True,
    'prev_next_buttons_location': 'bottom',
    'style_external_links': False
    # 'vcs_pageview_mode': '',
    # 'style_nav_header_background': 'white',
    # Toc options
    # 'collapse_navigation': True,
    # 'sticky_navigation': True,
    # 'navigation_depth': 4,
    # 'includehidden': True,
    # 'titles_only': False
}

html_logo = "images/bigdatalogo.png"
html_favicon = "images/favicon.ico"

# -- Options for PDF output ---------------------------------------------------
# latex_engine = 'xelatex'

latex_elements = {
    'papersize': 'letterpaper',
    'pointsize': '10pt',
    'figure_align': 'htbp',
    'preamble': r'''
\DeclareUnicodeCharacter{0301}{\'{e}}
''',
}


def setup(app):
    app.add_css_file('stylesheet.css')

# latex_elements = {
#     'papersize': 'letterpaper',
#     'pointsize': '10pt',
#     'figure_align': 'htbp',
#     'preamble': ''' \usepackage{fontspec} \setmainfont{Times New Roman}
#     ''',
#     'inputenc': '',
#     'fncychap': '',
#     'utf8extra': '',
#     'times': '',
#     'babel': '\usepackage{polyglossia}',
#     'cmap': '',
#     'fontenc': '',
#     'releasename': '',
# }
