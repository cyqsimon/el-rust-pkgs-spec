#!/usr/bin/env bash

# Query the COPR API for build statuses of all packages, then print anything
# that hasn't succeeded (including in-progress, etc.).
# Alternatively, print the newest build of all packages with the `--all` flag.

set -e

# default
MODE=failed

# handle arguments
for ARG in "$@"; do
    case $ARG in
        -a | --all)
            MODE=all
            ;;
        *)
            echo "Unknown argument: \"$ARG\""
            exit 1
            ;;
    esac
done

# API documentation is WIP; see https://github.com/fedora-copr/copr/issues/2809
LIST_QUERY='https://copr.fedorainfracloud.org/api_3/package/list?ownername=cyqsimon&projectname=el-rust-pkgs&with_latest_build=1'
BUILD_QUERY_BASE='https://copr.fedorainfracloud.org/coprs/build'

ALL_STATUS=$(curl -LsSf "$LIST_QUERY" | jq \
    '.items
    | map({ name, build: .builds.latest })
    | sort_by(.name)')

case $MODE in
    failed)
        SELECTED_STATUS=$(jq 'map(select(.build.state != "succeeded"))' <<< "$ALL_STATUS")
        ;;
    all)
        SELECTED_STATUS="$ALL_STATUS"
        ;;
esac

SELECTED_FORMATTED=$(jq --arg BUILD_QUERY_BASE "$BUILD_QUERY_BASE" \
    'map("\(.name)-\(.build.source_package.version // "<TBD>"): \(.build.state)
    URL: \($BUILD_QUERY_BASE)/\(.build.id)")' \
    <<< "$SELECTED_STATUS")

case $MODE in
    failed)
        jq -r 'select(length != 0) // ["All succeeded."] | join("\n")' <<< "$SELECTED_FORMATTED"
        ;;
    all)
        jq -r 'join("\n")' <<< "$SELECTED_FORMATTED"
        ;;
esac
