## For development purposes

`puthon manage.py runserv`
1. Automatic reloading of the WSGI application when code changes
2. Serves static files from the `STATIC_DIRS` setting
3. Single-threaded

## For production purposes (Linux/UNIX)
`gunicorn`
1. Stable running of the application
2. Does not serve static files
3. Multi-threaded