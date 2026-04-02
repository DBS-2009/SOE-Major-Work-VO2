# Render Deployment Checklist

1. Ensure all templates are in the `templates/` directory, not the project root.
2. Only one `login.html` should exist: `templates/login.html`.
3. All static files (CSS, JS, images) should be in the `static/` directory.
4. Your Flask app should use the default `templates` and `static` folders.
5. Your `Procfile` should contain:

    web: gunicorn app:app

6. Your `requirements.txt` should list all dependencies (Flask, gunicorn, etc).
7. If you get `TemplateNotFound`, check that the `templates/` folder is deployed and contains all required files.
8. If you get 500 errors, check the logs for missing files or import errors.

## To fix your current error:
- Delete the root-level `login.html` file (keep only `templates/login.html`).
- Redeploy.

This will resolve the `jinja2.exceptions.TemplateNotFound: login.html` error on Render.