import os
import argparse
import json

from dotenv import load_dotenv
from openai import OpenAI

from functions.get_file_content import get_file_content
from functions.get_files_info import get_files_info
from functions.run_python_file import run_python_file
from functions.write_file import write_file
from call_function import available_functions , call_function


system_prompt = """
You are a helpful AI coding agent.

When a user asks to use a specific function/tool, execute that tool directly without extra exploratory calls.

Available operations:
- List files and directories using get_files_info
- Read file contents using get_file_content
- Write or overwrite files using write_file
- Execute Python files using run_python_file

All paths provided are relative to the working directory. Do not specify working_directory in parameters.
"""

load_dotenv()
api_key = os.environ.get("OPENROUTER_API_KEY")

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

parser = argparse.ArgumentParser(description="Chatbot")
parser.add_argument("user_prompt", type=str, help="User prompt")
parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
args = parser.parse_args()
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": args.user_prompt},
]
itr=20
for i in range(0,itr):
    # call the model, handle responses, etc.


    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        tools=available_functions,
    )

    usage = response.usage
    if args.verbose:
        usage = response.usage
        print(f"User prompt: {args.user_prompt}")
        print(f"Prompt tokens: {usage.prompt_tokens}")
        print(f"Response tokens: {usage.completion_tokens}")

    response_message = response.choices[0].message
    messages.append(response_message)   
    tool_calls = response.choices[0].message.tool_calls
    if tool_calls:
        for tool_call in tool_calls:
            function_args = json.loads(tool_call.function.arguments or "{}")
            result_message = call_function(tool_call, args.verbose)
            if not result_message.get("content"):
                    raise RuntimeError(f"Empty function response for {tool_call.function.name}")
            if args.verbose:
                    print(f"-> {result_message['content']}")
            messages.append(result_message)

    
    else:
     if response_message.content:
            print(response_message.content)
     break


