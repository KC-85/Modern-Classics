#!/usr/bin/env bash

set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ -x "$ROOT_DIR/venv/bin/python" ]]; then
	PYTHON_BIN="$ROOT_DIR/venv/bin/python"
else
	PYTHON_BIN="python3"
fi

usage() {
	cat <<'EOF'
Usage:
	./scripts/test_automation.sh                 Run all unit tests
	./scripts/test_automation.sh <test-label>    Run a specific app/module/test label
	./scripts/test_automation.sh --keepdb        Reuse test database for faster local runs
	./scripts/test_automation.sh --help          Show this help

Examples:
	./scripts/test_automation.sh
	./scripts/test_automation.sh unit_tests.common
	./scripts/test_automation.sh unit_tests.showroom.test_views --keepdb
EOF
}

if [[ "${1:-}" == "--help" || "${1:-}" == "-h" ]]; then
	usage
	exit 0
fi

TEST_LABELS=()
EXTRA_ARGS=()

i=1
while [[ $i -le $# ]]; do
	arg="${!i}"
	case "$arg" in
		--keepdb|--failfast|--buffer|--reverse|--noinput|--debug-mode)
			EXTRA_ARGS+=("$arg")
			;;
		-v|--verbosity)
			EXTRA_ARGS+=("$arg")
			i=$((i + 1))
			if [[ $i -le $# ]]; then
				EXTRA_ARGS+=("${!i}")
			fi
			;;
		-v*)
			EXTRA_ARGS+=("$arg")
			;;
		*)
			TEST_LABELS+=("$arg")
			;;
	esac
	i=$((i + 1))
done

if [[ ${#TEST_LABELS[@]} -eq 0 ]]; then
	TEST_LABELS=("unit_tests")
fi

echo "Running tests with: $PYTHON_BIN manage.py test ${TEST_LABELS[*]} ${EXTRA_ARGS[*]:-}"
"$PYTHON_BIN" manage.py test "${TEST_LABELS[@]}" "${EXTRA_ARGS[@]}"
