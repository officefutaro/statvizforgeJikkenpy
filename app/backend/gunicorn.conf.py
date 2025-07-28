# Gunicorn configuration file
bind = "0.0.0.0:8000"
workers = 2
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 5
max_requests = 1000
max_requests_jitter = 100
preload_app = True
reload = True  # Development setting
accesslog = "-"
errorlog = "-"
loglevel = "info"