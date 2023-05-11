from typing import Dict, List
from dataclasses import dataclass
import json
import os

import yaml
import requests


MAIN_ENDPOINT = os.getenv("PROMPTHUB_MAIN_ENDPOINT", "http://api.prompthub.deepset.ai")


@dataclass
class Prompt:
    """
    Prompt stores all the information of a single prompt.
    """

    name: str
    tags: List[str]
    meta: Dict[str, str]
    version: str
    text: str
    description: str


def from_json(file: str):
    with open(file) as f:
        data = json.load(f)
        return Prompt(
            data["name"],
            data["tags"],
            data["meta"],
            data["version"],
            data["prompt_text"],
            data["description"],
        )


def from_yaml(file: str):
    with open(file) as f:
        data = yaml.safe_load(f)
        return Prompt(
            data["name"],
            data["tags"],
            data["meta"],
            data["version"],
            data["prompt_text"],
            data["description"],
        )


def fetch(name: str, timeout: int = 30):
    """
    Fetches the specified prompt from PromptHUB and
    returns a Prompt instance of it.

    :param name: Name of the prompt to fetch from PromptHUB
    :param timeout: the timeout to use for the request
    :return: An instance of Prompt storing all its info
    """
    url = f"{MAIN_ENDPOINT}/prompts/{name}"
    res = requests.get(url, timeout=timeout)
    j = res.json()
    return Prompt(
        j["name"],
        j["tags"],
        j["meta"],
        j["version"],
        j["prompt_text"],
        j["description"],
    )
