# explorer-ai

Explorer AI: Curiosity-Driven Agents is an innovative project designed to create interactive, curiosity-driven agents using large language models (LLMs) within a ReAct architecture. The project aims to explore the potential of AI-driven conversational systems by allowing users to interact with various LLMs leveraging NVIDIA NIMs, such as Llama 3.1, Llama 3.2 and augmenting these interactions with external tools like search engines.

<b>Interaction flow in Explorer AI:</b>
1.	User Query Input: The user begins by inputting a query into the system via a web-based interface.
2.	Agent Processing: The agent processes the query using their choice of LLM (e.g., Llama 3.1) running on NVIDIA NIMs infrastructure.
3.	Tool Usage & Memory Recall: Depending on the query, the agent may choose to use external tools like the Tavily Search Tool and/or leverage its memory from previous interactions.
4.	Response Generation: The system generates a response that may include additional information retrieved from web searches or previous conversations.
5.	User Interaction Continuation: The user receives the response through the web interface, potentially augmented with links or images, allowing for further interaction.

<b>Key components of Explorer AI:</b>
1. Web Search Function
2. Memory Within Each Chat
3. Persistent Memory Across Sessions
4. Access to Different Models

<b>System is built using several key technologies:</b>
- LangChain: A framework for building applications using large language models (LLMs). It supports multiple LLMs (e.g., OpenAI, NVIDIA, Ollama).
- NVIDIA NIMs: A set of APIs for deploying NVIDIA's LLMs like Llama 3.1 and Phi 3.
- FastHTML and Starlette: For building the web interface and handling HTTP requests.
- SQLite: For persistent storage of chat sessions.
- WebSockets: For real-time communication between the client and server.

# Deploying the app

1.	Set up virtual environment (ensure Python version >= 3.10 is installed)

2.	Install the required packages with pip install -r requirements.txt

3.	Edit the ‘.sample-env’ file in the root directory and add the relevant keys

4.	Edit the name of ‘.sample-env’ to ‘.env’ before running

5.	Run the app with python curiosity.py

