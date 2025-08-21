# Chat with Ollama

A simple, interactive command-line chat application that connects to your local Ollama server to chat with the GEMMA language model.

## 🚀 Features

- **Interactive CLI Chat**: Engage in conversations with GEMMA through a command-line interface
- **Multiple Conversations**: Start new conversations without restarting the application
- **Real-time Responses**: Streaming responses for a more chat-like experience
- **Single Configuration File**: All settings managed through one simple `.env` file - no code editing required
- **Graceful Exit**: Type 'exit' or 'quit' to end conversations cleanly
- **Error Handling**: Automatic handling of network errors, server timeouts, and connection issues
- **Smart Context Management**: Rolling message history to maintain relevant context while preventing performance issues
- **Keyboard Interrupt Protection**: Graceful handling of Ctrl+C interruptions

## 📋 Prerequisites

Before running this application, ensure you have:

1. **Python 3.7+** installed on your system
2. **Ollama** installed and running locally
3. **GEMMA model** pulled in Ollama (`ollama pull gemma3:1b-it-q4_K_M`)

## 🛠️ Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/EvenMoreH/chat-w-ollama.git
   cd chat-w-ollama
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure environment**:
   - Copy the example environment file:
     ```bash
     cp .env-example .env
     ```
   - Edit the `.env` file with your configuration:
     ```bash
     URL = "http://localhost:11434"
     MODEL_NAME = "gemma3:1b-it-q4_K_M"
     ```

   > **🎯 One File, All Settings**: Everything is configured in your `.env` file - no need to edit Python code! This keeps your configuration separate from the application logic and makes switching between different setups effortless.

   > **Note**: If your Ollama server is running on a different host or port, update the URL accordingly (e.g., `http://192.168.1.100:11434`)

## 🚀 Usage

1. **Start Ollama** (if not already running):
   ```bash
   ollama serve
   ```

2. **Run the chat application**:
   ```bash
   python app.py
   ```

3. **Start chatting**:
   ```
   Welcome to chat with GEMMA. Type 'exit' or 'quit' to end the chat.

   You: Hello, how are you today?
   GEMMA: Thinking...
   GEMMA: Hello! I'm doing well, thank you for asking. How can I help you today?

   You: Tell me about Python programming
   GEMMA: Thinking...
   GEMMA: Python is a versatile, high-level programming language...
   ```

4. **End conversation**:
   - Type `exit` or `quit` to end the current conversation
   - Choose whether to start a new conversation or exit the application

## 🔧 Configuration

### Environment Variables

The application uses a single `.env` file for all configuration - keeping things simple and organized! Create a `.env` file based on the provided `.env-example`:

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| `URL` | Ollama server base URL | `http://localhost:11434` | Yes |
| `MODEL_NAME` | AI model to use for conversations | `gemma3:1b-it-q4_K_M` | Yes |

> **💡 Why one configuration file?** By keeping both the server URL and model name in your `.env` file, you can easily switch between different setups (local vs remote servers, different models) **without touching any Python code and exposing server URL**. Perfect for testing and development.

### Model Selection

The default **`gemma3:1b-it-q4_K_M`** model is a super small and fast version of GEMMA that's perfect for quick responses and lower resource usage. This makes it ideal for testing and lightweight conversations.

#### Using Different Models

You can easily switch to other Ollama models for different capabilities:

**Popular Model Options:**
- `gemma3:1b-it-q4_K_M` - Ultra-fast, minimal resources (default)
- `gemma3:2b` - Balanced performance and quality
- `llama3.2:3b` - Good general-purpose model
- `llama3.1:8b` - Higher quality responses, more resources
- `codellama:7b` - Specialized for coding tasks
- `mistral:7b` - Excellent instruction following

**To switch models (it's super easy!):**

1. **Pull the desired model** with Ollama:
   ```bash
   ollama pull model-name
   ```

2. **Update your `.env` file**:
   ```bash
   MODEL_NAME = "your-preferred-model"
   ```

3. **Restart the app** - that's it! No code changes needed.

4. **Check available models** on your system:
   ```bash
   ollama list
   ```

> **� Pro tip**: The advantage of having everything in `.env` means you can quickly experiment with different models by just changing one line in your configuration file. Want to try a more powerful model for complex tasks? Just update `MODEL_NAME` and restart.

## 📁 Project Structure

```
chat-w-ollama/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── .env-example       # Environment configuration template
├── .env              # Your environment configuration (create this)
├── LICENSE           # Project license
└── README.md         # This file
```

## 🔍 How It Works

1. **Connection**: The app connects to your local Ollama server using the configured URL
2. **Conversation Loop**: Maintains conversation context by storing message history
3. **Streaming**: Receives responses in real-time using Ollama's streaming API
4. **Session Management**: Each conversation maintains its own message history
5. **Multiple Sessions**: After ending a conversation, you can start fresh without losing the application state
6. **Smart Memory Management**: Automatically manages conversation history with a rolling window (keeps last 30 messages) to maintain performance
7. **Error Recovery**: Handles network issues, server errors, and timeouts gracefully without crashing
8. **Interrupt Handling**: Responds to Ctrl+C with a friendly goodbye message

## 🛠️ Troubleshooting

### Common Issues

**Connection Error**:
- Ensure Ollama is running: `ollama serve`
- Verify the URL in your `.env` file is correct
- Check if the port is accessible
- The app will display a clear error message if the server is unreachable

**Model Not Found**:
- Pull the required model: `ollama pull gemma3:1b-it-q4_K_M`
- Verify the model name in the code matches your available models: `ollama list`
- The app will notify you if the specified model is not available

**Python Dependencies**:
- Install requirements: `pip install -r requirements.txt`
- Consider using a virtual environment for isolation

**Timeout Issues**:
- The app has a built-in 30-second timeout for server requests
- If responses are consistently slow, check your server performance or model size
- For very large models, consider switching to a smaller, faster variant or update the timeout

**Interrupting the Chat**:
- Press `Ctrl+C` at any time to gracefully exit with a friendly goodbye message
- Type `exit` or `quit` during conversation to end the current chat session

### Debug Mode

To see more detailed information about requests, you can modify the code to print the payload being sent to Ollama.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🔗 Related Links

- [Ollama Documentation](https://ollama.ai/)
- [GEMMA Model Information](https://ai.google.dev/gemma)
- [Python dotenv Documentation](https://python-dotenv.readthedocs.io/)

**Enjoy chatting with GEMMA!** 🤖✨