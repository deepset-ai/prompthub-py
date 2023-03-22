from typing import Dict, List
from dataclasses import dataclass
import json

import yaml
import requests


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

    @staticmethod
    def from_json(file: str):
        data = json.load(file)
        return Prompt(
            data["name"],
            data["tags"],
            data["meta"],
            data["version"],
            data["prompt_text"],
            data["description"],
        )

    @staticmethod
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

    @staticmethod
    def fetch(name: str):
        """
        Fetches the specified prompt from PromptHUB and
        returns a Prompt instance of it.

        :param prompt_name: Name of the prompt to fetch from PromptHUB
        :return: An instance of Prompt storing all its info
        """
        url = f"https://prompthub.deepset.ai/api/prompts/{name}"
        res = requests.get(url, timeout=30)
        j = res.json()
        return Prompt(
            j["name"],
            j["tags"],
            j["meta"],
            j["version"],
            j["prompt_text"],
            j["description"],
        )
