import sys
from subprocess import call

FAIL_UNDER = "87"
COV = ["coverage"]
RUN = ["run", "--source=pip_requirements_parser", "--branch", "-m"]
PYTEST = ["pytest", "-vv", "--color=yes", "--tb=long"]
REPORT = ["report", "--show-missing", "--skip-covered", f"--fail-under={FAIL_UNDER}"]

SKIPS = [
    "skeleton_codestyle",
    # https://github.com/conda-forge/pip-requirements-parser-feedstock/pull/4
    "fail_1.txt",
    "invalid_spec-requirements.txt",
    "nikdoof-test-auth-requirements.txt",
]

SKIP_OR = " or ".join(SKIPS)
K = ["-k", f"not ({SKIP_OR})"]


if __name__ == "__main__":
    sys.exit(
        # run the tests
        call([*COV, *RUN, *PYTEST, *K, "tests"])
        # maybe run coverage
        or call([*COV, *REPORT])
    )
