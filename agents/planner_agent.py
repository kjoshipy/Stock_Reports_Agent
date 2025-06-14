import yaml
import autogen

def load_prompt():
    with open("prompts.yaml") as f:
        return yaml.safe_load(f)

def create_planner_agent (llm_config):
    prompt = load_prompt()
    return autogen.ConversableAgent(
            name="Planner",
            llm_config=llm_config,
            description="Given a task, determine what information is needed to complete the task.",
            system_message=prompt["planner_system_message"]
    )