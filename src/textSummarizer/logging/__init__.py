import os
import sys
import logging

# Define logs directory and custom logging format with timestamp, level, module, and message
log_dir = "logs"
logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# Create full path for the continuous log file
log_filepath = os.path.join(log_dir, "continuos_logs.log")

# Ensure logs directory exists (creates if missing, does nothing if exists)
os.makedirs(log_dir, exist_ok=True)

# Configure root logger with dual output: file + console
logging.basicConfig(
    level=logging.INFO,                    # Minimum log level (INFO and above)
    format=logging_str,                    # Structured format with module tracing
    
    handlers=[
        logging.FileHandler(log_filepath), # Write logs to rotating log file
        logging.StreamHandler(sys.stdout)  # Also print to console/stdout
    ]
)

# Create named logger for the text summarizer project
# This allows hierarchical logging and easy filtering
logger = logging.getLogger("summarizerlogger")
