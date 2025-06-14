# Stock_Reports_Agent
This package demonstrates how to use a multi-agent system to generate a stock performance report

## How it works
- **Admin**: Initiates the task and provides feedback.
- **Planner**: Determines what information is needed and how to obtain it.
- **Engineer**: Writes Python code to retrieve the required data.
- **Executor**: Runs the code and reports results.
- **Writer**: Drafts and refines the blog post based on results and feedback.
The agents interact in a group chat, automatically coordinating to complete the task with min

## How to run
1. **Install dependencies**
 ```shell
uv pip install -r <(uv pip compile)
```
2. **Run the project**
```shell
python main.py
```