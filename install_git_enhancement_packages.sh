#!/bin/bash
# isntall packages
pip install pre-commit commitizen black flake8 --quiet

# check installation
pre-commit --version
echo "commitizen $(cz version)"
black --version
flake8 --version

# install hooks to project_root/.git/hooks
# pre-commit: python, terraform, json, yaml and bash linting hooks
pre-commit install --hook-type pre-commit
# commit-msg: conventional commit linting hook
pre-commit install --hook-type commit-msg

