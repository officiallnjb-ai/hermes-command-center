import logging
from . import schemas, tools

logger = logging.getLogger(__name__)


def on_tool_call(tool_name, args, result, **kwargs):
    logger.info("HCC monitored tool call: %s", tool_name)


def register(ctx):
    ctx.register_tool(
        name="hcc_add_task",
        toolset="hermes_command_center",
        schema=schemas.ADD_TASK,
        handler=tools.add_task
    )

    ctx.register_tool(
        name="hcc_list_tasks",
        toolset="hermes_command_center",
        schema=schemas.LIST_TASKS,
        handler=tools.list_tasks
    )

    ctx.register_tool(
        name="hcc_update_task",
        toolset="hermes_command_center",
        schema=schemas.UPDATE_TASK,
        handler=tools.update_task
    )

    ctx.register_tool(
        name="hcc_recovery_advice",
        toolset="hermes_command_center",
        schema=schemas.RECOVERY,
        handler=tools.recovery_advice
    )

    ctx.register_hook("post_tool_call", on_tool_call)
