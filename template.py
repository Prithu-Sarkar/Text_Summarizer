import os
from pathlib import Path
import logging

# Configure logging with timestamp and custom format for better traceability
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Define the main project name - follows cookiecutter-style project naming
project_name = "textSummarizer"

# Comprehensive list of files and directories to create for the project structure
# Organized following clean architecture patterns with src/, config/, and research/
list_of_files = [
    # GitHub Actions workflow placeholder
    ".github/workflows/.gitkeep",
    
    # Core source code structure
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",  # Business logic components
    f"src/{project_name}/utils/__init__.py",       # Utility functions
    f"src/{project_name}/utils/common.py",         # Common utility functions
    f"src/{project_name}/logging/__init__.py",     # Custom logging setup
    f"src/{project_name}/config/__init__.py",      # Configuration management
    f"src/{project_name}/config/configuration.py", # Main configuration loader
    f"src/{project_name}/pipeline/__init__.py",    # ML/data pipeline components
    f"src/{project_name}/entity/__init__.py",      # Data classes and entities
    f"src/{project_name}/constants/__init__.py",   # Project constants and configs
    
    # Configuration files
    "config/config.yaml",     # Main YAML configuration
    "params.yaml",            # MLflow-style hyperparameters
    
    # Application entry points
    "app.py",                 # Streamlit/Flask app entrypoint
    "main.py",                # CLI/script entrypoint
    
    # Deployment and packaging
    "Dockerfile",             # Docker container configuration
    "requirements.txt",       # Python dependencies
    "setup.py",               # Package installation script
    
    # Research and experimentation
    "research/research.ipynb" # Jupyter notebook for experiments
]

# Iterate through all required files and create directory structure
for filepath in list_of_files:
    # Convert to Path object for better cross-platform compatibility
    filepath = Path(filepath)
    
    # Extract directory path and filename components
    filedir, filename = os.path.split(filepath)
    
    # Create parent directories if they don't exist
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")
    
    # Create empty file if it doesn't exist or is empty (handles __init__.py files)
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Creates empty file
        logging.info(f"Creating empty file: {filepath}")
    
    # File already exists and has content - skip creation
    else:
        logging.info(f"{filename} already exists")
