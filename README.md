# Autonomous Python AI Agent Framework

An extensible CLI-based AI agent built in Python that leverages Large Language Model (LLM) tool calling (function calling) to autonomously explore directory structures, inspect file contents, write/update code, and execute Python scripts within a secure working directory.

---

## 🌟 Key Features

* **Multi-Turn Agent Loop:** Executes autonomous execution cycles until complex multi-step user prompts are fully resolved.
* **Dynamic Function Dispatcher:** Maps JSON schema tool definitions to Python backend functions dynamically (`call_function.py`).
* **Security Sandboxing:** Enforces relative path boundaries (`WORKING_DIR`) to prevent unauthorized directory traversal.
* **Verbose Inspection Mode:** Real-time feedback showing token consumption (prompt & completion tokens) and step-by-step tool execution parameters (`--verbose`).

---

## 🛠️ Tool Capabilities

The agent is equipped with the following tool schemas:

| Tool Name | Description |
| :--- | :--- |
| `get_files_info` | Lists files and directories with metadata (file size, directory flag). |
| `get_file_content` | Reads and returns text content from a target file. |
| `write_file` | Creates or overwrites files with new text content. |
| `run_python_file` | Executes Python scripts with optional CLI arguments and returns STDOUT/STDERR. |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.10+
* [`uv`](https://github.com/astral-sh/uv) or standard `pip`
* OpenRouter or OpenAI API Key

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/SunayanaDenagama/My_Agent.git](https://github.com/SunayanaDenagama/My_Agent.git)
   cd My_Agent
