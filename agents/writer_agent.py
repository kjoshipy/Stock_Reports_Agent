import yaml
import autogen

def load_prompt():
    with open("prompts.yaml") as f:
        return yaml.safe_load(f)

def create_writer_agent(llm_config):
    prompt = load_prompt()
    return autogen.ConversableAgent(
        name="Writer",
        llm_config=llm_config,
        system_message=prompt["writer_system_message"],
        description="Writer."
                    "Write blogs based on the code execution results and take "
                    "feedback from the admin to refine the blog."
    )