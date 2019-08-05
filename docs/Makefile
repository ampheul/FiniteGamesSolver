# Minimal makefile for Sphinx documentation
#

# You can set these variables from the command line.
SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = .
BUILDDIR      = ../../FGSDocs

SPHINXAPI     = sphinx-apidoc
APIOPTS       = -f
APISOURCEDIR  = ../source
APIOUTDIR	  = modules
APIFILES      = $(shell find $(APISOURCEDIR) -type f -name "*.py" -print)

# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile api

api:
	@$(SPHINXAPI) -f -o $(APIOUTDIR) $(APISOURCEDIR)

# Catch-all target: route all unknown targets to Sphinx using the new
# "make mode" option.  $(O) is meant as a shortcut for $(SPHINXOPTS).
%: Makefile api
	@$(SPHINXBUILD) -M $@ "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
