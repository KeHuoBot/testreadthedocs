# Configuration file for the Sphinx documentation builder.

# path setup
import os
import sys

sys.path.insert(0, os.path.abspath(".."))

# -- Project information
project = "hk debug proj"
copyright = "2022, hk debug"
author = "hk debug"


# -- General configuration
extensions = [
    "sphinx_rtd_theme",
    "recommonmark",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",
    "sphinx_markdown_tables",
    "sphinx.ext.viewcode",
    "sphinx.ext.coverage",
    "sphinx.ext.extlinks",
]

autodoc_default_options = {
    "member-order": "bysource",
    "undoc-members": False,
}


# sphinx supported file extensions.
source_suffix = [".rst", ".md"]


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ["_static"]
# html_logo = "picture.png"


# -- Localization of Documentation.
# https://docs.readthedocs.io/en/stable/localization.html
locale_dirs = ['locale/']
gettext_compact = False
language = 'en'
add_module_names = False
gettext_uuid = True


# Add any paths that contain templates here, relative to this directory.
# templates_path = ["_templates"]


# -- Options for HTML output
html_theme = "sphinx_rtd_theme"


# -- Options for EPUB output
# epub_show_urls = "footnote"
