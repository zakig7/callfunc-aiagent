# AI Coding Assistant

This project is a simplified version of AI-powered coding assistants like Cursor/Zed's Agentic Mode or Claude Code. It allows you to interact with an AI agent that can read, write, and execute code within a sandboxed environment.

**Warning:** This is a toy project and is not intended for production use. Even commercial AI coding assistants have security vulnerabilities, so exercise extreme caution when granting the agent access to your files and system.

## Features

* **File System Access:** The AI agent can list files and directories within the project's working directory.
* **File Content Retrieval:** The agent can read the contents of text files.
* **Code Execution:** The agent can execute Python files and receive the output.
* **File Modification:** The agent can create and modify files.

## Security Considerations

This project is for educational and experimental purposes only. It is crucial to understand the security risks associated with AI agents that have access to your file system and code execution capabilities.

* **Sandboxing:** The agent operates within a sandboxed environment to limit its access to the broader system. However, sandboxes are not impenetrable.
* **Limited Scope:** The agent's capabilities are intentionally limited to prevent unintended consequences.
* **No Guarantees:** There are no guarantees of security or stability. Use at your own risk.

## Getting Started

1. Clone this repository.
2. Set up a virtual environment using `uv`.
3. Install the dependencies.
4. Run the `main.py` file to start the AI coding assistant.

## Disclaimer

The author of this project is not responsible for any damages or losses resulting from the use of this software. By using this project, you acknowledge and agree to these terms.
