# LangChain Prompts

A beginner-friendly practice project that shows how to talk to an LLM with LangChain: temperature, message types, prompt templates, a chatbot with memory, and a small Streamlit app.

## What is inside

| File | What it shows |
|------|---------------|
| `temperature.py` | How the temperature setting changes how creative the answers are |
| `messages.py` | `SystemMessage`, `HumanMessage` and `AIMessage` in a list |
| `chatbot.py` | A terminal chatbot that remembers the conversation |
| `prompt_template.py` | A reusable prompt with blanks using `PromptTemplate` |
| `chat_prompt_template.py` | A multi-message prompt with blanks using `ChatPromptTemplate` |
| `prompt_generator.py` | Builds a prompt template and saves it to `template.json` |
| `prompt_ui.py` | A Streamlit app that loads `template.json` and explains research papers |
| `template.json` | The saved prompt template used by the app |

## Tech stack

- Python 3.12
- LangChain (`langchain-openai`, `langchain-core`)
- OpenAI API (`gpt-4o-mini`)
- Streamlit
- python-dotenv

## Setup

1. Clone the repo:
```
   git clone https://github.com/surajchaudhary-11/langchain-prompts.git
   cd langchain-prompts
```

2. Create and activate a virtual environment (Windows):
```
   python -m venv venv
   venv\Scripts\activate
```

3. Install the packages:
```
   python -m pip install langchain-openai langchain-core python-dotenv streamlit
```

4. Create a `.env` file in the project folder with your own key:
```
   OPENAI_API_KEY=your_key_here
```
   Never share this file or upload it to GitHub. It is already listed in `.gitignore`.

## How to run

Normal Python files:
```
python temperature.py
python messages.py
python chatbot.py
python prompt_template.py
python chat_prompt_template.py
```

Streamlit app (run the generator first so `template.json` exists):
```
python prompt_generator.py
python -m streamlit run prompt_ui.py
```
Then open `http://localhost:8501` in your browser, choose a paper, style and length, and click **Summarize**.

## Notes

- The files that call the model need credits on your OpenAI account.
- `prompt_template.py`, `chat_prompt_template.py` and `prompt_generator.py` do not call the model, so they run for free.
- In `chatbot.py`, type `exit` to stop the chat.

## What I learned

- How temperature affects the output
- The difference between single messages and a list of messages
- How to build static and dynamic prompts with templates
- How a chatbot keeps memory by storing its message history
- How to save a prompt to JSON and use it in a Streamlit app

## Author

Suraj Chaudhary, [GitHub](https://github.com/surajchaudhary-11)