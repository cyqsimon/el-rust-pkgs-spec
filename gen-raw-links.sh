#!/usr/bin/env bash

# This script makes submitting builds to COPR via raw URL easier

for SPEC in specs/*.spec; do
    echo "https://raw.githubusercontent.com/cyqsimon/el-rust-pkgs-spec/master/${SPEC}"
done
