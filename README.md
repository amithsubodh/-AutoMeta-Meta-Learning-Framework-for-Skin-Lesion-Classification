# AutoMeta

AutoMeta is a meta-learning / few-shot learning project with a Streamlit-based interface for running experiments and inspecting results.

## Project structure

- `AutoMeta/src/`: core source code and the Streamlit app
- `AutoMeta/models/`: model definitions and task embeddings
- `AutoMeta/results/`: experiment metrics and analysis outputs (ignored by git)
- `venv/`: local virtual environment (ignored by git)

## Setup

```bash
git clone <this-repo-url>
cd Major
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Running the app

```bash
cd AutoMeta
streamlit run src/streamlit_app.py
```

## Notes

- Large artifacts, results, caches, and the virtual environment are ignored via `.gitignore` so they are not pushed to the public repository.
