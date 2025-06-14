import yaml
import autogen

def load_prompt():
    with open("prompts.yaml") as f:
    return yaml.safe_load(f)

def create_admin_agent(llm_config):
    prompt = load_prompt()
    return autogen.ConversableAgent(
        name="Admin",
        system_message=prompt["admin_system_message"],
        code_execution_config=False,
        llm_config=llm_config,
        human_input_mode="ALWAYS",
    )