# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import sphinx_rtd_theme
import pydata_sphinx_theme
import nbsphinx
sys.path.insert(0, os.path.abspath('.'))


project = 'cwbplot'
copyright = '2021, CCLiu'
author = 'CCLiu'

# The full version, including alpha/beta/rc tags
release = '0.1.0'

#release = pydata_sphinx_theme.__version__
#version = release.replace("dev0", "")

# -- General configuration ---------------------------------------------------


# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'rainbow_dash'


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [ 'sphinx.ext.autosectionlabel', 'nbsphinx']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'alabaster'
html_theme = "sphinx_rtd_theme"
html_theme = "pydata_sphinx_theme"
#html_theme = "sphinx_book_theme"
#html_title = "My site title"
#html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_logo = './image/cwbrfs-logos_transparent-cut.png'


html_theme_options = {
    "icon_links": [
        {
            # Label for this link
            "name": "GitHub",
            # URL where the link will redirect
            "url": "https://github.com/Liu-CWB/cwbplot/tree/master",  # required
            # Icon class (if "type": "fontawesome"), or path to local image (if "type": "local")
            "icon": "fab fa-github-square",
            # Whether icon should be a FontAwesome class, or a local file
            "type": "fontawesome",  # Default is fontawesome
        }

   ],
   
    "switcher": {
        # "json_url": "/_static/switcher.json",
        "json_url": "https://cwbplot.readthedocs.io/en/dev/_static/switcher.json",
        #"url_template": "https://cwbplot.readthedocs.io/en/v{version}/",
        #"version_match": version,
    },
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_css_files = ['theme-cwbrfs.css']
