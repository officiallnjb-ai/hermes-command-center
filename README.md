# Hermes Command Center (HCC)

Hermes Command Center is an agent task monitoring and safe recovery
recommendation plugin.

## Features

1. Task registration with unique IDs.
2. Task listing and activity history.
3. Task status management:
   pending, running, completed, failed.
4. Error analysis and safe recovery recommendations.

## Registered Tools

- hcc_add_task
- hcc_list_tasks
- hcc_update_task
- hcc_recovery_advice

## Registered Hook

- post_tool_call

## Requirements

The core implementation uses Python standard-library modules.

Install pytest to run the test suite:

    python -m pip install pytest

## Run Tests

    python -m pytest -v

## Project Structure

- tools.py: HCC tool implementations
- schemas.py: Tool definitions and parameters
- plugin.yaml: Plugin configuration
- tests/test_hcc.py: Automated tests
