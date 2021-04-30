#!/bin/bash
pipeline_base_revision=$1
pipeline_revision=$2

if [ "$pipeline_base_revision" = "" ]; then
  first_commit="$(git log --walk-reflogs "$CIRCLE_BRANCH" --format="%H" | tail -n 2 | head -n 1)"
else
  first_commit=${pipeline_base_revision}
fi

pre-commit install --hook-type pre-commit
pre-commit run --hook-stage manual --from-ref "$first_commit" --to-ref "$pipeline_revision"
cz check --rev-range "$first_commit".."$pipeline_revision"

#7de746b
#6670137
#a4b7b3f
#bin/code_and_commit_linter.sh 6670137 7de746b