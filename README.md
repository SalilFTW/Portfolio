
# Salil Portfolio (Simple HTML + CSS)

This folder contains a single-file website (`index.html`) plus an optional Flask wrapper for Python hosting.

## Run locally (no Python required)
- Double-click `index.html` to open in your browser.

## Run locally with Flask
```bash
pip install -r requirements.txt
python app.py
```
Visit http://localhost:5000

## Deploy options
### Netlify (easiest for static)
- Drag & drop this folder on https://app.netlify.com/drop

### GitHub Pages
- Create a repo, upload `index.html`
- In Settings → Pages → set source to `main` (root).

### Render (Flask)
- Push these files to a GitHub repo.
- Create a new Web Service on Render.
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`
- Environment: Python 3.x
- Deploy.
```

