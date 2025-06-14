import autogen


def create_executor_agent(llm_config):
    return autogen.ConversableAgent(
        name="Executor",
        description="Execute the code written by the "
        "engineer and report the result.",
        human_input_mode="NEVER",
        code_execution_config={
            "last_n_messages": 3,
            "work_dir": "coding",
            "use_docker": False,
        },
    )