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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'UR High Performance Computing'
copyright = '2021, University of Richmond'
author = 'George Flanagin / Provost Office'
source_encoding = 'utf-8-sig'

version = '1.0'
release = '1.0.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = []


notfound_context = {
    }

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []
latex_elements = {
    'papersize':'letterpaper',
    'pointsize':'11pt'
    }


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'sphinx_documatt_theme'
# html_theme = 'sphinx_celery'
# html_theme = 'bootstrap'
# html_theme = 'sphinx_alabaster_theme'
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'sphinxawesome_theme'
# html_theme = 'insipid'
# html_theme = 'sphinx_typlog_theme'
# html_theme = "furo"
# html_theme = "sphinx_book_theme"
# html_theme = 'guzzle_sphinx_theme'
html_theme = 'sphinx_typo3_theme'

html_last_updated_fmt = '%b %d, %Y at %H:%M'
today_fmt = '%b %d, %Y'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
html_logo = '_static/web.png'
html_favicon = '_static/favicon.ico'

def setup(app):
    app.add_css_file('css/urcolors.css')
