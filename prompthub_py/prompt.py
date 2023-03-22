from typing import Any, Dict, List
from dataclasses import dataclass

import requests


@dataclass
class Prompt:
    """
    Prompt stores all the information of a single prompt.

    :return: _description_
    :rtype: _type_
    """

    name: str
    tags: List[str]
    meta: Dict[str, str]
    version: str
    text: str
    description: str

    @staticmethod
    def from_json(j: Any):
        """
        Returns a single Prompt created using json.
        """
        return Prompt(
            j["name"], j["tags"], j["meta"], j["version"], j["text"], j["description"]
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
        return Prompt.from_json(res.json())

