# LangGraph Notebooks

This repository contains notebooks and example code using LangGraph and LangChain.

Setup (recommended):

1. Create a Python virtual environment and activate it:

```bash
python -m venv .venv
source .venv/bin/activate   # on Windows: .venv\Scripts\activate
```

2. Copy `.env.example` to `.env` and add your Hugging Face token:

```bash
cp .env.example .env
# edit .env and set HUGGINGFACEHUB_API_TOKEN
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Restart the Jupyter kernel after installing packages and loading `.env`.

Notes:
- The `ai_env/` virtual environment is ignored by `.gitignore` to avoid committing large environment files.
- Do not commit your `.env` file; keep secrets out of the repository.
