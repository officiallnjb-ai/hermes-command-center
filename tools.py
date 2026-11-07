import json
from datetime import datetime, timezone

TASKS = []
ACTIVITY = []
NEXT_ID = 1


def record(event):
    ACTIVITY.append({
        "event": event,
        "time": datetime.now(timezone.utc).isoformat()
    })
    del ACTIVITY[:-100]


def add_task(args, **kwargs):
    global NEXT_ID
    try:
        title = str(args.get("title", "")).strip()
        if not title:
            return json.dumps({"success": False, "error": "Title required"})

        task = {
            "id": NEXT_ID,
            "title": title,
            "details": str(args.get("details", "")),
            "status": "pending",
            "created_at": datetime.now(timezone.utc).isoformat()
        }
        TASKS.append(task)
        NEXT_ID += 1
        record(f"Task created: {title}")
        return json.dumps({"success": True, "task": task})
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


def list_tasks(args, **kwargs):
    try:
        return json.dumps({
            "success": True,
            "total": len(TASKS),
            "tasks": TASKS,
            "recent_activity": ACTIVITY[-10:]
        })
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


def update_task(args, **kwargs):
    try:
        task_id = int(args.get("task_id"))
        status = args.get("status")
        allowed = ["pending", "running", "completed", "failed"]

        if status not in allowed:
            return json.dumps({"success": False, "error": "Invalid status"})

        for task in TASKS:
            if task["id"] == task_id:
                task["status"] = status
                record(f"Task {task_id} changed to {status}")
                return json.dumps({"success": True, "task": task})

        return json.dumps({"success": False, "error": "Task not found"})
    except Exception as exc:
        return json.dumps({"success": False, "error": str(exc)})


def recovery_advice(args, **kwargs):
    error = str(args.get("error", "")).lower()

    if "timeout" in error:
        advice = "Check service availability, then retry with a limited retry count."
    elif "network" in error or "connection" in error:
        advice = "Check network connectivity and endpoint availability before retrying."
    elif "permission" in error or "denied" in error:
        advice = "Check access permissions. Do not bypass security restrictions."
    elif "memory" in error:
        advice = "Inspect memory usage and reduce workload before restarting."
    else:
        advice = "Inspect the error logs, identify the cause and test a reversible fix."

    record("Recovery advice requested")
    return json.dumps({
        "success": True,
        "error_analyzed": error,
        "recommendation": advice,
        "automatic_action_taken": False
    })
