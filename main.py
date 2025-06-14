import yaml
from agents.admin_agent import create_admin_agent
from agents.planner_agent import create_planner_agent
from agents.engineer_agent import create_engineer_agent
from agents.executor_agent import create_executor_agent
from agents.writer_agent import create_writer_agent
import autogen

with open("config.yaml") as f:
    config = yaml.safe_load(f)

llm_config = config["llm_config"]
task = config["task"]

admin = create_admin_agent(llm_config)
planner = create_planner_agent(llm_config)
engineer = create_engineer_agent(llm_config)
executor = create_executor_agent(llm_config)
writer = create_writer_agent(llm_config)

groupchat = autogen.GroupChat(
    agents=[admin, engineer, writer, executor, planner],
    messages=[],
    max_round=10
)


manager = autogen.GroupChatManager (
    groupchat=groupchat, llm_config=llm_config
)

result = admin.initiate_chat(manager, message=task)