bind = 'unix:/var/www/charity/CharityWebsite/gunicorn.sock'  # Adjust the path
workers = 3  # Number of worker processes
worker_class = 'sync'  # Worker class (sync, gevent, eventlet, etc.)
threads = 2  # Number of threads per worker
timeout = 30  # Workers silent for more than this many seconds are killed and restarted
loglevel = 'info'  # Log level (debug, info, warning, error)
accesslog = '/var/www/charity/CharityWebsite/gunicorn-access.log'  # Access log file
errorlog = '/var/www/charity/CharityWebsite/gunicorn-error.log'  # Error log file
