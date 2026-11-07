ADD_TASK = {
    "name": "hcc_add_task",
    "description": "Register a task in Hermes Command Center.",
    "parameters": {
        "type": "object",
        "properties": {
            "title": {"type": "string", "description": "Task title"},
            "details": {"type": "string", "description": "Task details"}
        },
        "required": ["title"]
    }
}

LIST_TASKS = {
    "name": "hcc_list_tasks",
    "description": "List tracked tasks and their statuses.",
    "parameters": {"type": "object", "properties": {}}
}

UPDATE_TASK = {
    "name": "hcc_update_task",
    "description": "Update a tracked task status.",
    "parameters": {
        "type": "object",
        "properties": {
            "task_id": {"type": "integer"},
            "status": {
                "type": "string",
                "enum": ["pending", "running", "completed", "failed"]
            }
        },
        "required": ["task_id", "status"]
    }
}

RECOVERY = {
    "name": "hcc_recovery_advice",
    "description": "Analyze an error and suggest safe recovery steps.",
    "parameters": {
        "type": "object",
        "properties": {
            "error": {"type": "string"}
        },
        "required": ["error"]
    }
}
