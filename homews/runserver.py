import os
from app import app
port = os.environ.get("HOMEWS_PORT", 8080)
if __name__ == "__main__":
    app.run(8080)