from typing import Dict, List, Union

from pathlib import Path
from dataclasses import dataclass, asdict
import json
import os

import yaml
import requests


MAIN_ENDPOINT = os.getenv("PROMPTHUB_MAIN_ENDPOINT", "https://api.prompthub.deepset.ai")
PROMPTHUB_CACHE = Path.home() / ".prompthub_cache"
CACHE_ENABLED = bool(os.environ.get("PROMPTHUB_ENABLE_CACHE", True))


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
            data["text"],
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
            data["text"],
            data["description"],
        )
    

def to_yaml(prompt: Prompt, file: str):
    with open(file, 'w') as f:
        yaml.safe_dump(asdict(prompt), f, indent=2)


def fetch(name: str, timeout: float = 30.0, cache: Union[str, Path] = PROMPTHUB_CACHE) -> Prompt:
    """
    Fetches the specified prompt from PromptHUB and returns a Prompt instance of it.

    :param name: Name of the prompt to fetch from PromptHUB
    :param timeout: (optional) How many seconds to wait for the server to send data before giving up.
    :param cache: the path to the prompts cache.
    :return: An instance of Prompt storing all its info
    """
    if CACHE_ENABLED:
        cached_prompt_path = Path(cache) / f"{name}.yaml"
        if cached_prompt_path.exists():
            return from_yaml(cached_prompt_path)

    url = f"{MAIN_ENDPOINT}/prompts/{name}"
    res = requests.get(url, timeout=timeout)
    res.raise_for_status()
    prompt_data = res.json()
    prompt = Prompt(
        prompt_data["name"],
        prompt_data["tags"],
        prompt_data["meta"],
        prompt_data["version"],
        prompt_data["text"],
        prompt_data["description"],
    )

    if CACHE_ENABLED:
        os.makedirs(cached_prompt_path.parent, exist_ok=True)
        to_yaml(prompt, cached_prompt_path)

    return prompt
