#!/usr/bin/env bash

# this helper script is needed because it seems like it's not possible
# to run a background process in the .spec file directly

set -e

source ~/.cargo/env

# PostgresQL is needed for some tests
PGDATA="$HOME/.local/share/pgsql/data"
mkdir -p "$PGDATA"
postgres -D "$PGDATA" &> postgres.log &
ss -tupln

cargo test --workspace
cat postgres.log
