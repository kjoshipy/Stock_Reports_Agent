import yaml
import autogen

def load_prompt():
    with open ("prompts.yam]") as f:
        return yaml.safe_load (f)

def create_engineer_agent(llm_config):
    prompt = load_prompt()
    return autogen.AssistantAgent(
        name="Engineer",
        llm_config=llm_config,
        description="An engineer that writes code based on the plan provided by the planner.",
        system_message=prompt["engineer_system_message"]
    )