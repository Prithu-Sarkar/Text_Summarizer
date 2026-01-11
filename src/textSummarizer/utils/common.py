import os
from box.exceptions import BoxValueError
import yaml
from src.textSummarizer.logging import logger
from box import ConfigBox
from pathlib import Path
from typing import Any, List


def read_yaml(path_to_yaml: Path) -> ConfigBox:
    """
    Safely reads YAML configuration file and converts to ConfigBox for dot-notation access.

    Args:
        path_to_yaml (Path): File path to YAML configuration

    Raises:
        ValueError: If YAML file is empty
        FileNotFoundError: If YAML file does not exist
        Exception: Any other file reading/parsing errors

    Returns:
        ConfigBox: Enhanced dictionary with dot notation
    """
    try:
        if not path_to_yaml.exists():
            raise FileNotFoundError(f"YAML file not found: {path_to_yaml}")

        with open(path_to_yaml, "r", encoding="utf-8") as yaml_file:
            content = yaml.safe_load(yaml_file)

        if content is None:
            raise ValueError("yaml file is empty")

        logger.info(f"yaml file loaded successfully: {path_to_yaml}")
        return ConfigBox(content)

    except BoxValueError:
        raise ValueError("yaml file is empty")
    except Exception as e:
        raise e


def create_directories(
    path_to_directories: List[Path],
    verbose: bool = True
) -> None:
    """
    Creates multiple directories from a list of paths.

    Args:
        path_to_directories (List[Path]): List of directory paths to create
        verbose (bool): Log each creation
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"created directory at: {path}")
