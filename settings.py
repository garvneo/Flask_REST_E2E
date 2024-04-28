"""--settings.py
This module is used for deploying the REDIS and background worker.

This works fine locally, but at render.com background worker is a paid
service hence the code is commented.

To run locally one can un comment it and run the redis queue and app.py
parallely using docker.
"""


# import os
# from dotenv import load_dotenv
#
# load_dotenv()
#
# REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
# QUEUES = ["emails", "default"]
