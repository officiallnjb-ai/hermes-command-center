try:
    from . import schemas, tools
except ImportError:
    import schemas
    import tools


def _on_post_tool_call(tool_name, args, result, **kwargs):
    tools.record(f"Tool executed: {tool_name}")


def register(ctx):
    toolset = "hermes_command_center"

    ctx.register_tool(
        name="hcc_add_task",
        toolset=toolset,
        schema=schemas.ADD_TASK,
        handler=tools.add_task,
    )

    ctx.register_tool(
        name="hcc_list_tasks",
        toolset=toolset,
        schema=schemas.LIST_TASKS,
        handler=tools.list_tasks,
    )

    ctx.register_tool(
        name="hcc_update_task",
        toolset=toolset,
        schema=schemas.UPDATE_TASK,
        handler=tools.update_task,
    )

    ctx.register_tool(
        name="hcc_recovery_advice",
        toolset=toolset,
        schema=schemas.RECOVERY,
        handler=tools.recovery_advice,
    )

    ctx.register_hook("post_tool_call", _on_post_tool_call)


__all__ = ["schemas", "tools", "register"]
