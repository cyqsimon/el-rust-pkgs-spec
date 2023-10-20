#!/usr/bin/env bash

# Query the COPR API for build statuses of all packages, then print anything
# that hasn't succeeded (including in-progress, etc.)

set -e

# API documentation is WIP; see https://github.com/fedora-copr/copr/issues/2809
LIST_QUERY='https://copr.fedorainfracloud.org/api_3/package/list?ownername=cyqsimon&projectname=el-rust-pkgs&with_latest_build=1'
BUILD_QUERY_BASE='https://copr.fedorainfracloud.org/coprs/build'

curl -LsSf "$LIST_QUERY" | jq -r --arg BUILD_QUERY_BASE "$BUILD_QUERY_BASE" \
    '.items
    | map({ name, last_build_id: .builds.latest.id, last_build_status: .builds.latest.state })
    | map(select(.last_build_status != "succeeded"))
    | sort_by(.name)
    | map("Build for \"\(.name)\" \(.last_build_status).\n  URL: \($BUILD_QUERY_BASE)/\(.last_build_id)")
    | select(length != 0) // ["All succeeded."]
    | join("\n")'
