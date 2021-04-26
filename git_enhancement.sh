#!/bin/bash

# install packages
pip install pre-commit commitizen --quiet

# check installation
pre-commit --version
echo "commitizen $(cz version)"

# install hooks to project_root/.git/hooks
# pre-commit: python, terraform, json, yaml and bash linting hooks
# commit-msg: conventional commit linting hook
pre-commit install --hook-type pre-commit,commit-msg

# install hook packages to ~/.cache/pre-commit
# use pre-commit gc once in a while to collect garbage
pre-commit install-hooks
