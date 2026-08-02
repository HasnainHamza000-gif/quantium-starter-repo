#!/bin/bash

# 1. Activate the Python virtual environment
source .venv/Scripts/activate

# 2. Execute the pytest suite
pytest test_app.py

# 3. Capture the exit code of pytest (0 = pass, 1+ = fail)
TEST_EXIT_CODE=$?

# 4. Return exit code 0 if all tests passed, or 1 if any failed
if [ $TEST_EXIT_CODE -eq 0 ]; then
    echo "All tests passed successfully!"
    exit 0
else
    echo "Test suite failed!"
    exit 1
fi