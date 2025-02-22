import logging
import threading
from flask import Flask
from .utubebot import UtubeBot
from .config import Config

# Set up logging
logging.basicConfig(level=logging.DEBUG if Config.DEBUG else logging.INFO)
logging.getLogger("pyrogram").setLevel(
    logging.INFO if Config.DEBUG else logging.WARNING
)

# Flask app for health check
app = Flask(__name__)

@app.route("/")
def health_check():
    return "OK", 200  # Koyeb's health check will pass

def start_health_server():
    import os
    port = int(os.environ.get("PORT", 5782))  # Match Koyeb’s health check port
    app.run(host="0.0.0.0", port=port)

# Start Flask health check in a separate thread
threading.Thread(target=start_health_server, daemon=True).start()

# Start the bot
if __name__ == "__main__":
    UtubeBot().run()
