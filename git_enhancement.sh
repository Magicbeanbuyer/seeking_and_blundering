#!/bin/bash
# default "local" when no argument passed, "circleci" when running in circleci
runtime=${1-local}

pip install pre-commit commitizen --quiet

# check installation
pre-commit --version
echo "commitizen $(cz version)"

# install hooks to project_root/.git/hooks
# pre-commit: python, terraform, json, yaml and bash linting hooks
pre-commit install --hook-type pre-commit

if [ "$runtime" = "local" ]; then
  # commit-msg: conventional commit linting hook
  # only install commit-msg hook via pre-commit locally
  # commitizen won't be called by pre-commit in CircleCI
  pre-commit install --hook-type commit-msg
fi
