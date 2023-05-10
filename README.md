# Prompt Hub Python Client

[![PyPI - Version][pypi-badge]][pypi-project] [![Tests][tests-badge]][tests-workflow]

A simple client to fetch prompts from [Prompt Hub][prompt-hub] using its REST API.

## Usage

First step is obviously installation:

```
pip install prompthub-py
```

Then you can import `Prompt`, that class is all you're going to need.

```python
from prompthub_py.prompt import Prompt

# To load from a JSON file
p = Prompt.from_json("./path/to/my/prompt.json")


# To load from a YAML file
p = Prompt.from_yaml("./path/to/my/prompt.yaml")


# To load from Prompt Hub
p = Prompt.fetch("deepset/question-answering")

# To get the prompt text
p.text
```

If you want to use a different Prompt Hub you must set the `PROMPTHUB_MAIN_ENDPOINT` environment variable to your main endpoint.

If the environment variable is not set the default `api.prompthub.deepset.ai` will be used.

## Testing

To run tests locally first install dev dependencies, we use [`poetry`][python-poetry] to manage our dependencies:

```
poetry install --with=dev
```

Run Prompt Hub locally with a set of fake prompts:

```
docker run -p80:80 --volume $PWD/test/fake_prompts:/prompts deepset/prompthub
```

And then run tests:

```
poetry run pytest test
```

[pypi-badge]: https://img.shields.io/pypi/v/prompthub-py.svg
[pypi-project]: https://pypi.org/project/prompthub-py
[prompt-hub]: https://prompthub.deepset.ai/
[python-poetry]: https://python-poetry.org/
[tests-badge]: https://github.com/deepset-ai/prompthub-py/actions/workflows/test.yml/badge.svg
[tests-workflow]: https://github.com/deepset-ai/prompthub-py/actions/workflows/test.yml
