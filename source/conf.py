# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Iris'
copyright = '2026, Hikaru'
author = 'Hikaru'
release = '0.1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx.ext.mathjax"]

templates_path = ['_templates']
exclude_patterns = []

mathjax3_config = {
    "loader": {"load": ["[tex]/physics"]},
    "tex": {
        "packages": {"[+]": ["physics"]},
        "macros": {
            "argmax": r"\operatorname*{arg\,max}",
            "argmin": r"\operatorname*{arg\,min}",
        },
    },
}


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
