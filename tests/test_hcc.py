import json
import pytest
import tools
from schemas import ADD_TASK, LIST_TASKS, UPDATE_TASK, RECOVERY


@pytest.fixture(autouse=True)
def reset_state():
    tools.TASKS.clear()
    tools.ACTIVITY.clear()
    tools.NEXT_ID = 1


def result(value):
    return json.loads(value)


def test_add_task_success():
    data = result(tools.add_task({"title": "Test task"}))
    assert data["success"] is True
    assert data["task"]["title"] == "Test task"
    assert data["task"]["status"] == "pending"


def test_add_task_trims_title():
    data = result(tools.add_task({"title": "  HCC task  "}))
    assert data["task"]["title"] == "HCC task"


def test_add_task_rejects_empty_title():
    data = result(tools.add_task({"title": "   "}))
    assert data["success"] is False
    assert len(tools.TASKS) == 0


def test_list_tasks():
    tools.add_task({"title": "First task"})
    data = result(tools.list_tasks({}))
    assert data["success"] is True
    assert data["total"] == 1
    assert data["tasks"][0]["title"] == "First task"


def test_update_task_success():
    task = result(tools.add_task({"title": "Update test"}))["task"]
    data = result(tools.update_task({
        "task_id": task["id"],
        "status": "completed"
    }))
    assert data["success"] is True
    assert data["task"]["status"] == "completed"


def test_update_task_rejects_invalid_status():
    task = result(tools.add_task({"title": "Status test"}))["task"]
    data = result(tools.update_task({
        "task_id": task["id"],
        "status": "unknown"
    }))
    assert data["success"] is False
    assert data["error"] == "Invalid status"


def test_update_task_missing_id():
    data = result(tools.update_task({
        "task_id": 999,
        "status": "completed"
    }))
    assert data["success"] is False
    assert data["error"] == "Task not found"


@pytest.mark.parametrize("error,expected", [
    ("Request timeout", "limited retry count"),
    ("Network connection failed", "network connectivity"),
    ("Permission denied", "access permissions"),
    ("Memory exhausted", "memory usage"),
])
def test_recovery_advice(error, expected):
    data = result(tools.recovery_advice({"error": error}))
    assert data["success"] is True
    assert expected in data["recommendation"]
    assert data["automatic_action_taken"] is False


def test_recovery_unknown_error():
    data = result(tools.recovery_advice({"error": "Unknown failure"}))
    assert data["success"] is True
    assert "error logs" in data["recommendation"]


def test_tool_schema_names():
    assert ADD_TASK["name"] == "hcc_add_task"
    assert LIST_TASKS["name"] == "hcc_list_tasks"
    assert UPDATE_TASK["name"] == "hcc_update_task"
    assert RECOVERY["name"] == "hcc_recovery_advice"
