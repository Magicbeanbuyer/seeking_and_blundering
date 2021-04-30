#!/bin/bash
pipeline_base_revision=$1

# get the ID of the first commit of the branch
if [ "$pipeline_base_revision" = "" ]; then
  first_commit="$(git log --walk-reflogs "$CIRCLE_BRANCH" --format="%H" | tail -n 2 | head -n 1)"
else
  first_commit="$pipeline_base_revision"
fi

branch_head="$(git rev-parse HEAD)"

#pre-commit install --hook-type pre-commit
pre-commit run --hook-stage manual --from-ref "$first_commit" --to-ref "$branch_head"
cz check --rev-range "$first_commit".."$branch_head"