import tempfile
from autogen.agent import ConversableAgent
from autogen.coding import DockerCommandLineCodeExecutor


# Step 1: Create a temporary directory to store code files.
temp_dir = tempfile.TemporaryDirectory()

# Step 2: Create a Docker command line code executor.
executor = DockerCommandLineCodeExecutor(
    image="python:3.12-slim",  # The Docker image to use for executing code.
    timeout=10,  # Timeout for code execution in seconds.
    work_dir=temp_dir.name,  # Directory for storing code files.
)

# Step 3: Create an agent that uses the Docker code executor.
code_executor_agent_using_docker = ConversableAgent(
    "code_executor_agent_docker",
    llm_config=False,  # Disable LLM for safety, agent will always take human input.
    code_execution_config={"executor": executor},  # Set up the code execution configuration.
    human_input_mode="ALWAYS",  # Always take human input.
)

# Step 4: Use the agent to execute code (this will depend on your specific implementation).

# Example: Suppose you have code to execute, e.g., a Python script.
code = """
print('Hello from Docker!')
"""

# Step 5: Execute code through the executor.
executor.execute_code(code)

# Step 6: Clean up when no longer needed.
executor.stop()
