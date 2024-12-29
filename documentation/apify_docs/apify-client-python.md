Directory structure:
└── apify-apify-client-python/
    ├── docs/
    │   ├── examples.md
    │   └── index.md
    ├── .pre-commit-config.yaml
    ├── tests/
    │   ├── unit/
    │   │   ├── test_client_errors.py
    │   │   └── test_utils.py
    │   └── integration/
    │       ├── conftest.py
    │       ├── test_basic.py
    │       ├── test_request_queue.py
    │       └── test_store.py
    ├── CHANGELOG.md
    ├── scripts/
    │   ├── check_async_docstrings.py
    │   ├── utils.py
    │   └── fix_async_docstrings.py
    ├── .github/
    │   ├── workflows/
    │   │   ├── update_new_issue.yaml
    │   │   ├── _async_docstrings_check.yaml
    │   │   ├── build_and_deploy_docs.yaml
    │   │   ├── run_code_checks.yaml
    │   │   ├── release.yaml
    │   │   ├── check_pr_title.yaml
    │   │   └── pre_release.yaml
    │   └── CODEOWNERS
    ├── renovate.json
    ├── Makefile
    ├── pyproject.toml
    ├── website/
    │   ├── sidebars.js
    │   ├── .eslintrc.json
    │   ├── generate_module_shortcuts.py
    │   ├── transformDocs.js
    │   ├── tools/
    │   │   ├── docs-prettier.config.js
    │   │   └── utils/
    │   │       └── externalLink.js
    │   ├── package.json
    │   ├── babel.config.js
    │   ├── pydoc-markdown.yml
    │   ├── package-lock.json
    │   ├── build_api_reference.sh
    │   ├── docusaurus.config.js
    │   ├── src/
    │   │   └── pages/
    │   │       ├── index.module.css
    │   │       └── index.js
    │   └── static/
    │       └── .nojekyll
    ├── LICENSE
    ├── README.md
    ├── CONTRIBUTING.md
    ├── .markdownlint.yaml
    ├── src/
    │   └── apify_client/
    │       ├── _http_client.py
    │       ├── _utils.py
    │       ├── consts.py
    │       ├── __init__.py
    │       ├── _logging.py
    │       ├── _errors.py
    │       ├── client.py
    │       ├── py.typed
    │       └── clients/
    │           ├── base/
    │           │   ├── base_client.py
    │           │   ├── __init__.py
    │           │   ├── resource_client.py
    │           │   ├── actor_job_base_client.py
    │           │   └── resource_collection_client.py
    │           ├── __init__.py
    │           └── resource_clients/
    │               ├── webhook.py
    │               ├── build.py
    │               ├── schedule_collection.py
    │               ├── actor_version.py
    │               ├── build_collection.py
    │               ├── request_queue.py
    │               ├── store_collection.py
    │               ├── webhook_dispatch_collection.py
    │               ├── request_queue_collection.py
    │               ├── __init__.py
    │               ├── task_collection.py
    │               ├── run_collection.py
    │               ├── actor_env_var_collection.py
    │               ├── webhook_collection.py
    │               ├── actor.py
    │               ├── dataset_collection.py
    │               ├── log.py
    │               ├── actor_version_collection.py
    │               ├── actor_collection.py
    │               ├── schedule.py
    │               ├── task.py
    │               ├── user.py
    │               ├── key_value_store.py
    │               ├── key_value_store_collection.py
    │               ├── dataset.py
    │               ├── webhook_dispatch.py
    │               ├── run.py
    │               └── actor_env_var.py
    └── .editorconfig


Files Content:

(Files content cropped to 300k characters, download full ingest to see more)
================================================
File: /README.md
================================================
# Apify API client for Python

The Apify API Client for Python is the official library to access the [Apify API](https://docs.apify.com/api/v2) from your Python applications.
It provides useful features like automatic retries and convenience functions to improve your experience with the Apify API.

If you want to develop Apify Actors in Python,
check out the [Apify SDK for Python](https://docs.apify.com/sdk/python) instead.

## Installation

Requires Python 3.8+

You can install the package from its [PyPI listing](https://pypi.org/project/apify-client).
To do that, simply run `pip install apify-client` in your terminal.

## Usage

For usage instructions, check the documentation on [Apify Docs](https://docs.apify.com/api/client/python/).

## Quick Start

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Start an Actor and wait for it to finish
actor_call = apify_client.actor('john-doe/my-cool-actor').call()

# Fetch results from the Actor's default dataset
dataset_items = apify_client.dataset(actor_call['defaultDatasetId']).list_items().items
```

## Features

Besides greatly simplifying the process of querying the Apify API, the client provides other useful features.

### Automatic parsing and error handling

Based on the endpoint, the client automatically extracts the relevant data and returns it in the
expected format. Date strings are automatically converted to `datetime.datetime` objects. For exceptions,
we throw an `ApifyApiError`, which wraps the plain JSON errors returned by API and enriches
them with other context for easier debugging.

### Retries with exponential backoff

Network communication sometimes fails. The client will automatically retry requests that
failed due to a network error, an internal error of the Apify API (HTTP 500+) or rate limit error (HTTP 429).
By default, it will retry up to 8 times. First retry will be attempted after ~500ms, second after ~1000ms
and so on. You can configure those parameters using the `max_retries` and `min_delay_between_retries_millis`
options of the `ApifyClient` constructor.

### Support for asynchronous usage

Starting with version 1.0.0, the package offers an asynchronous version of the client, [`ApifyClientAsync`](https://docs.apify.com/api/client/python),
which allows you to work with the Apify API in an asynchronous way, using the standard `async`/`await` syntax.

### Convenience functions and options

Some actions can't be performed by the API itself, such as indefinite waiting for an Actor run to finish
(because of network timeouts). The client provides convenient `call()` and `wait_for_finish()` functions that do that.
Key-value store records can be retrieved as objects, buffers or streams via the respective options, dataset items
can be fetched as individual objects or serialized data and we plan to add better stream support and async iterators.


================================================
File: /docs/examples.md
================================================
---
sidebar_label: Examples
title: 'Code examples'
---

## Passing an input to the Actor

The fastest way to get results from an Actor is to pass input directly to the `call` function.
We can set up the input, pass it to `call` function and get the reference of running Actor (or wait for finish).

```python
from apify_client import ApifyClient

# Client initialization with the API token
apify_client = ApifyClient(token='MY_APIFY_TOKEN')

actor_client = apify_client.actor('apify/instagram-hashtag-scraper')

input_data = { 'hashtags': ['rainbow'], 'resultsLimit': 20 }

# Run the Actor and wait for it to finish up to 60 seconds.
# Input is not persisted for next runs.
run_data = actor_client.call(run_input=input_data, timeout_secs=60)
```

## Manipulating with tasks

To run multiple inputs with the same Actor, most convenient way is to create multiple [tasks](https://docs.apify.com/platform/actors/running/tasks) with different inputs.
Task input is persisted on Apify platform when task is created.

```python

import asyncio

from apify_client import ApifyClientAsync
from apify_client.clients.resource_clients import TaskClientAsync

animal_hashtags = ['zebra', 'lion', 'hippo']


async def run_apify_task(client: TaskClientAsync) -> dict:
    result = await client.call()
    return result or {}


async def main() -> None:
    apify_client = ApifyClientAsync(token='MY_APIFY_TOKEN')

    # Create Apify tasks

    apify_tasks: list[dict] = []
    apify_tasks_client = apify_client.tasks()

    for hashtag in animal_hashtags:
        apify_task = await apify_tasks_client.create(
            name=f'hashtags-{hashtag}',
            actor_id='apify/instagram-hashtag-scraper',
            task_input={'hashtags': [hashtag], 'resultsLimit': 20},
            memory_mbytes=1024,
        )
        apify_tasks.append(apify_task)

    print('Tasks created:', apify_tasks)

    # Create Apify task clients

    apify_task_clients: list[TaskClientAsync] = []

    for apify_task in apify_tasks:
        task_id = apify_task['id']
        apify_task_client = apify_client.task(task_id)
        apify_task_clients.append(apify_task_client)

    print('Task clients created:', apify_task_clients)

    # Execute Apify tasks

    run_apify_tasks = [run_apify_task(client) for client in apify_task_clients]
    task_run_results = await asyncio.gather(*run_apify_tasks)

    print('Task results:', task_run_results)


if __name__ == '__main__':
    asyncio.run(main())
```

## Getting latest data from an Actor, joining datasets

Actor data are stored to [datasets](https://docs.apify.com/platform/storage/dataset). Datasets can be retrieved from Actor runs.
Dataset items can be listed with pagination.
Also, datasets can be merged together to make analysis further on with single file as dataset can be exported to various data format (CSV, JSON, XSLX, XML).
[Integrations](https://docs.apify.com/platform/integrations) can do the trick as well.

```python
from apify_client import ApifyClient

# Client initialization with the API token
apify_client = ApifyClient(token='MY_APIFY_TOKEN')

actor_client = apify_client.actor('apify/instagram-hashtag-scraper')

actor_runs = actor_client.runs()

# See pagination to understand how to get more datasets
actor_datasets = actor_runs.list(limit=20)

merging_dataset = apify_client.datasets().get_or_create(name='merge-dataset')

for dataset_item in actor_datasets.items:
    # Dataset items can be handled here. Dataset items can be paginated
    dataset_items = apify_client.dataset(dataset_id=dataset_item['id']).list_items(limit=1000)

    # Items can be pushed to single dataset
    apify_client.dataset(merging_dataset['id']).push_items(dataset_items.items)

    # ...
```

## Integration with data analysis libraries (Pandas)

The Apify API client for Python can be easily integrated with data analysis libraries.
Following example demonstrates how to load items from the last dataset run and pass them to a Pandas DataFrame for further analysis.
Pandas is a data analysis library that provides data structures and functions to efficiently manipulate large datasets.

```python
from apify_client import ApifyClient
import pandas

# Initialize the Apify client
client = ApifyClient(token="MY_APIFY_TOKEN")

# Load items from last dataset run
dataset_data = client.actor('apify/web-scraper').last_run().dataset().list_items()

# Pass dataset items to Pandas DataFrame
data_frame = pandas.DataFrame(dataset_data.items)

print(data_frame.info)
```


================================================
File: /docs/index.md
================================================
---
sidebar_label: 'Getting started'
title: 'Getting started'
---

# Apify API client for Python

`apify-client` is the official library to access the [Apify REST API](https://docs.apify.com/api/v2) from your Python applications. It provides useful features like automatic retries and convenience functions that improve the experience of using the Apify API. All requests and responses (including errors) are encoded in JSON format with UTF-8 encoding.

## Pre-requisites

`apify-client` requires Python version 3.8 or higher. Python is available for download on the [official website](https://www.python.org/). Check for your current Python version by running:

```bash
python -V
```

## Installation

You can install the client from its [PyPI listing](https://pypi.org/project/apify-client/).
To do that, run:

```bash
pip install apify-client
```

## Authentication and initialization

To use the client, you need an [API token](https://docs.apify.com/platform/integrations/api#api-token). You can find your token under [Integrations](https://console.apify.com/account/integrations) tab in Apify Console. Copy the token and initialize the client by providing the token (`MY-APIFY-TOKEN`) as a parameter to the `ApifyClient` constructor.

```python
# import Apify client
from apify_client import ApifyClient

# Client initialization with the API token
apify_client = ApifyClient('MY-APIFY-TOKEN')
```

:::warning Secure access

The API token is used to authorize your requests to the Apify API. You can be charged for the usage of the underlying services, so do not share your API token with untrusted parties or expose it on the client side of your applications.

:::

## Quick start

One of the most common use cases is starting [Actors](https://docs.apify.com/platform/actors) (serverless programs running in the [Apify cloud](https://docs.apify.com/platform)) and getting results from their [datasets](https://docs.apify.com/platform/storage/dataset) (storage) after they finish the job (usually scraping, automation processes or data processing).

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Start an Actor and waits for it to finish
actor_call = apify_client.actor('username/actor-name').call()

# Get a Actor's dataset
dataset_client = apify_client.dataset(actor_call['defaultDatasetId'])

# Lists items from the Actor's dataset
dataset_items = dataset_client.list_items().items
```

### Running Actors

To start an Actor, you can use the [ActorClient](/reference/class/ActorClient) (`client.actor()`) and pass the Actor's ID (e.g. `john-doe/my-cool-actor`) to define which Actor you want to run. The Actor's ID is a combination of the username and the Actor owner’s username. You can run both your own Actors and [Actors from Apify Store](https://docs.apify.com/platform/actors/running/actors-in-store).

#### Passing input to the Actor

To define the Actor's input, you can pass a run input to the [`call()`](/reference/class/ActorClient#call) method. The input can be any JSON object that the Actor expects (respects the Actor's [input schema](https://docs.apify.com/platform/actors/development/actor-definition/input-schema)).The input is used to pass configuration to the Actor, such as URLs to scrape, search terms, or any other data.

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Define the input for the Actor
actor_input = {
    'some': 'input',
}

# Start an Actor and waits for it to finish
actor_call = apify_client.actor('username/actor-name').call(run_input=actor_input)
```

### Getting results from the dataset

To get the results from the dataset, you can use the [DatasetClient](/reference/class/DatasetClient) (`client.dataset()`) and [`list_items()`](/reference/class/DatasetClient#list_items) method. You need to pass the dataset ID to define which dataset you want to access. You can get the dataset ID from the Actor's run dictionary (represented by `defaultDatasetId`).

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Get dataset
dataset_client = apify_client.dataset('dataset-id')

# Lists items from the Actor's dataset
dataset_items = dataset_client.list_items().items
```

:::note Dataset access

Running an Actor might take time, depending on the Actor's complexity and the amount of data it processes. If you want only to get data and have an immediate response you should access the existing dataset of the finished [Actor run](https://docs.apify.com/platform/actors/running/runs-and-builds#runs).

:::

## Usage concepts

The `ApifyClient` interface follows a generic pattern that applies to all of its components. By calling individual methods of `ApifyClient`, specific clients that target individual API resources are created. There are two types of those clients:

- [`actorClient`](/reference/class/ActorClient): a client for the management of a single resource
- [`actorCollectionClient`](/reference/class/ActorCollectionClient): a client for the collection of resources

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Collection clients do not require a parameter
actor_collection_client = apify_client.actors()

# Create an Actor with the name: my-actor
my_actor = actor_collection_client.create(name='my-actor')

# List all of your Actors
actor_list = actor_collection_client.list().items
```

:::note Resource identification

The resource ID can be either the `id` of the said resource, or a combination of your `username/resource-name`.

:::

```python
# Resource clients accept an ID of the resource
actor_client = apify_client.actor('username/actor-name')

# Fetch the 'username/actor-name' object from the API
my_actor = actor_client.get()

# Start the run of 'username/actor-name' and return the Run object
my_actor_run = actor_client.start()
```

### Nested clients

Sometimes clients return other clients. That's to simplify working with nested collections, such as runs of a given Actor.

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

actor_client = apify_client.actor('username/actor-name')
runs_client = actor_client.runs()

# List the last 10 runs of the Actor
actor_runs = runs_client.list(limit=10, desc=True).items

# Select the last run of the Actor that finished with a SUCCEEDED status
last_succeeded_run_client = actor_client.last_run(status='SUCCEEDED')

# Get dataset
actor_run_dataset_client = last_succeeded_run_client.dataset()

# Fetch items from the run's dataset
dataset_items = actor_run_dataset_client.list_items().items
```

The quick access to `dataset` and other storage directly from the run client can be used with the [`last_run()`](/reference/class/ActorClient#last_run) method.

## Features

Based on the endpoint, the client automatically extracts the relevant data
and returns it in the expected format.
Date strings are automatically converted to `datetime.datetime` objects.
For exceptions, we throw an [`ApifyApiError`](/reference/class/ApifyApiError),
which wraps the plain JSON errors returned by API and enriches them with other context for easier debugging.

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

try:
    # Try to list items from non-existing dataset
    dataset_client = apify_client.dataset('not-existing-dataset-id')
    dataset_items = dataset_client.list_items().items
except Exception as ApifyApiError:
    # The exception is an instance of ApifyApiError
    print(ApifyApiError)
```

### Retries with exponential backoff

Network communication sometimes fails.
The client will automatically retry requests that failed due to a network error,
an internal error of the Apify API (HTTP 500+) or rate limit error (HTTP 429).
By default, it will retry up to 8 times.
First retry will be attempted after ~500ms, second after ~1000ms and so on.
You can configure those parameters using the `max_retries` and `min_delay_between_retries_millis` options
of the [`ApifyClient`](/reference/class/ApifyClient) constructor.

```python
from apify_client import ApifyClient

apify_client = ApifyClient(
    token='MY-APIFY-TOKEN',
    max_retries=8,
    min_delay_between_retries_millis=500, # 0.5s
    timeout_secs=360, # 6 mins
)
```

### Support for asynchronous usage

The package offers an asynchronous version of the client,
[`ApifyClientAsync`](/reference/class/ApifyClientAsync),
which allows you to work with the Apify API in an asynchronous way, using the standard `async`/`await` syntax [offered by Python](https://docs.python.org/3/library/asyncio-task.html).

For example, to run an Actor and asynchronously stream its log while it's running, you can use this snippet:

```python
from apify_client import ApifyClientAsync
apify_client_async = ApifyClientAsync('MY-APIFY-TOKEN')

async def main():
    run = await apify_client_async.actor('my-actor').start()

    async with apify_client_async.run(run['id']).log().stream() as async_log_stream:
        if async_log_stream:
            async for line in async_log_stream.aiter_lines():
                print(line)

asyncio.run(main())
```

### Logging

The library logs some useful debug information to the `apify_client` logger
when sending requests to the Apify API.
To have them printed out to the standard output, you need to add a handler to the logger:

```python
import logging
apify_client_logger = logging.getLogger('apify_client')
apify_client_logger.setLevel(logging.DEBUG)
apify_client_logger.addHandler(logging.StreamHandler())
```

The log records have useful properties added with the `extra` argument,
like `attempt`, `status_code`, `url`, `client_method` and `resource_id`.
To print those out, you'll need to use a custom log formatter.
To learn more about log formatters and how to use them,
please refer to the official Python [documentation on logging](https://docs.python.org/3/howto/logging.html#formatters).

### Convenience functions and options

Some actions can't be performed by the API itself, such as indefinite waiting for an Actor run to finish (because of network timeouts).
The client provides convenient [`call()`](/reference/class/ActorClient#call)
and [`wait_for_finish()`](/reference/class/ActorClient#wait_for_finish) methods that do that.

[Key-value store](https://docs.apify.com/platform/storage/key-value-store) records can be retrieved as objects, buffers or streams via the respective options,
dataset items can be fetched as individual objects or serialized data, or iterated asynchronously.

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Start an Actor and waits for it to finish
finished_actor_run = apify_client.actor('username/actor-name').call()

# Starts an Actor and waits maximum 60s (1 minute) for the finish
actor_run = apify_client.actor('username/actor-name').start(wait_for_finish=60)
```

### Pagination

Most methods named `list` or `list_something` return a [`ListPage`](/reference/class/ListPage) object,
containing properties `items`, `total`, `offset`, `count` and `limit`.
There are some exceptions though, like `list_keys` or `list_head` which paginate differently.
The results you're looking for are always stored under `items` and you can use the `limit`
property to get only a subset of results. Other properties can be available depending on the method.

```python
from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Resource clients accept an ID of the resource
dataset_client = apify_client.dataset('dataset-id')

# Number of items per page
limit = 1000
# Initial offset
offset = 0
# List to store all items
all_items = []

while True:
    response = dataset_client.list_items(limit=limit, offset=offset)
    items = response.items
    total = response.total

    print(f'Fetched {len(items)} items')

    # Merge new items with other already loaded items
    all_items.extend(items)

    # If there are no more items to fetch, exit the loading
    if offset + limit >= total:
        break

    offset += limit

print(f'Overall fetched {len(all_items)} items')
```

### Streaming resources

Some resources (dataset items, key-value store records and logs)
support streaming the resource from the Apify API in parts,
without having to download the whole (potentially huge) resource to memory before processing it.

The methods to stream these resources are
[`DatasetClient.stream_items()`](/reference/class/DatasetClient#stream_items),
[`KeyValueStoreClient.stream_record()`](/reference/class/KeyValueStoreClient#stream_record),
and [`LogClient.stream()`](/reference/class/LogClient#stream).

Instead of the parsed resource, they return a raw, context-managed
[`httpx.Response`](https://www.python-httpx.org/quickstart/#streaming-responses) object,
which has to be consumed using the `with` keyword,
and automatically gets closed once you exit the `with` block, preventing memory leaks and unclosed connections.

For example, to consume an Actor run log in a streaming fashion, you can use this snippet:

```python
with apify_client.run('MY-RUN-ID').log().stream() as log_stream:
    if log_stream:
        for line in log_stream.iter_lines():
            print(line)
```


================================================
File: /.pre-commit-config.yaml
================================================
repos:
  - repo: local
    hooks:
      - id: lint-check
        name: Lint check
        entry: make lint
        language: system
        pass_filenames: false

      - id: type-check
        name: Type check
        entry: make type-check
        language: system
        pass_filenames: false

      - id: async-docstrings-check
        name: Async docstrings check
        entry: make check-async-docstrings
        language: system
        pass_filenames: false


================================================
File: /tests/unit/test_client_errors.py
================================================
import json

import httpx
import pytest
import respx
from respx import MockRouter

from apify_client._errors import ApifyApiError
from apify_client._http_client import HTTPClient, HTTPClientAsync

_TEST_URL = 'http://example.com'
_EXPECTED_MESSAGE = 'some_message'
_EXPECTED_TYPE = 'some_type'
_EXPECTED_DATA = {
    'invalidItems': {'0': ["should have required property 'name'"], '1': ["should have required property 'name'"]}
}


@respx.mock
@pytest.fixture(autouse=True)
def mocked_response(respx_mock: MockRouter) -> None:
    response_content = json.dumps(
        {'error': {'message': _EXPECTED_MESSAGE, 'type': _EXPECTED_TYPE, 'data': _EXPECTED_DATA}}
    )
    respx_mock.get(_TEST_URL).mock(return_value=httpx.Response(400, content=response_content))


def test_client_apify_api_error_with_data() -> None:
    """Test that client correctly throws ApifyApiError with error data from response."""
    client = HTTPClient()

    with pytest.raises(ApifyApiError) as e:
        client.call(method='GET', url=_TEST_URL)

    assert e.value.message == _EXPECTED_MESSAGE
    assert e.value.type == _EXPECTED_TYPE
    assert e.value.data == _EXPECTED_DATA


async def test_async_client_apify_api_error_with_data() -> None:
    """Test that async client correctly throws ApifyApiError with error data from response."""
    client = HTTPClientAsync()

    with pytest.raises(ApifyApiError) as e:
        await client.call(method='GET', url=_TEST_URL)

    assert e.value.message == _EXPECTED_MESSAGE
    assert e.value.type == _EXPECTED_TYPE
    assert e.value.data == _EXPECTED_DATA


================================================
File: /tests/unit/test_utils.py
================================================
import time
from typing import Any, Callable

import pytest
from apify_shared.consts import WebhookEventType

from apify_client._utils import (
    encode_webhook_list_to_base64,
    pluck_data,
    retry_with_exp_backoff,
    retry_with_exp_backoff_async,
    to_safe_id,
)


def test__to_safe_id() -> None:
    assert to_safe_id('abc') == 'abc'
    assert to_safe_id('abc/def') == 'abc~def'
    assert to_safe_id('abc~def') == 'abc~def'


def test_pluck_data() -> None:
    # works correctly when data is present
    assert pluck_data({'data': {}}) == {}
    assert pluck_data({'a': 'b', 'data': {'b': 'c'}}) == {'b': 'c'}

    # throws the right error when it is not
    with pytest.raises(ValueError, match='The "data" property is missing in the response.'):
        pluck_data({'a': 'b'})
    with pytest.raises(ValueError, match='The "data" property is missing in the response.'):
        pluck_data(None)
    with pytest.raises(ValueError, match='The "data" property is missing in the response.'):
        pluck_data('{"a": "b"}')


def test__retry_with_exp_backoff() -> None:
    attempt_counter = 0

    class RetryableError(Exception):
        pass

    class NonRetryableError(Exception):
        pass

    def returns_on_fifth_attempt(_stop_retrying: Callable, attempt: int) -> Any:
        nonlocal attempt_counter
        attempt_counter += 1

        if attempt == 5:
            return 'SUCCESS'
        raise RetryableError

    def bails_on_third_attempt(stop_retrying: Callable, attempt: int) -> Any:
        nonlocal attempt_counter
        attempt_counter += 1

        if attempt == 3:
            stop_retrying()
            raise NonRetryableError
        else:  # noqa: RET506
            raise RetryableError

    # Returns the correct result after the correct time (should take 100 + 200 + 400 + 800 = 1500 ms)
    start = time.time()
    result = retry_with_exp_backoff(
        returns_on_fifth_attempt, backoff_base_millis=100, backoff_factor=2, random_factor=0
    )
    elapsed_time_seconds = time.time() - start
    assert result == 'SUCCESS'
    assert attempt_counter == 5
    assert elapsed_time_seconds > 1.4
    assert elapsed_time_seconds < 2.0

    # Stops retrying when failed for max_retries times
    attempt_counter = 0
    with pytest.raises(RetryableError):
        retry_with_exp_backoff(returns_on_fifth_attempt, max_retries=3, backoff_base_millis=1)
    assert attempt_counter == 4

    # Bails when the bail function is called
    attempt_counter = 0
    with pytest.raises(NonRetryableError):
        retry_with_exp_backoff(bails_on_third_attempt, backoff_base_millis=1)
    assert attempt_counter == 3


async def test__retry_with_exp_backoff_async() -> None:
    attempt_counter = 0

    class RetryableError(Exception):
        pass

    class NonRetryableError(Exception):
        pass

    async def returns_on_fifth_attempt(_stop_retrying: Callable, attempt: int) -> Any:
        nonlocal attempt_counter
        attempt_counter += 1

        if attempt == 5:
            return 'SUCCESS'
        raise RetryableError

    async def bails_on_third_attempt(stop_retrying: Callable, attempt: int) -> Any:
        nonlocal attempt_counter
        attempt_counter += 1

        if attempt == 3:
            stop_retrying()
            raise NonRetryableError
        else:  # noqa: RET506
            raise RetryableError

    # Returns the correct result after the correct time (should take 100 + 200 + 400 + 800 = 1500 ms)
    start = time.time()
    result = await retry_with_exp_backoff_async(
        returns_on_fifth_attempt, backoff_base_millis=100, backoff_factor=2, random_factor=0
    )
    elapsed_time_seconds = time.time() - start
    assert result == 'SUCCESS'
    assert attempt_counter == 5
    assert elapsed_time_seconds > 1.4
    assert elapsed_time_seconds < 2.0

    # Stops retrying when failed for max_retries times
    attempt_counter = 0
    with pytest.raises(RetryableError):
        await retry_with_exp_backoff_async(returns_on_fifth_attempt, max_retries=3, backoff_base_millis=1)
    assert attempt_counter == 4

    # Bails when the bail function is called
    attempt_counter = 0
    with pytest.raises(NonRetryableError):
        await retry_with_exp_backoff_async(bails_on_third_attempt, backoff_base_millis=1)
    assert attempt_counter == 3


def test__encode_webhook_list_to_base64() -> None:
    assert encode_webhook_list_to_base64([]) == 'W10='
    assert (
        encode_webhook_list_to_base64(
            [
                {
                    'event_types': [WebhookEventType.ACTOR_RUN_CREATED],
                    'request_url': 'https://example.com/run-created',
                },
                {
                    'event_types': [WebhookEventType.ACTOR_RUN_SUCCEEDED],
                    'request_url': 'https://example.com/run-succeeded',
                    'payload_template': '{"hello": "world", "resource":{{resource}}}',
                },
            ]
        )
        == 'W3siZXZlbnRUeXBlcyI6IFsiQUNUT1IuUlVOLkNSRUFURUQiXSwgInJlcXVlc3RVcmwiOiAiaHR0cHM6Ly9leGFtcGxlLmNvbS9ydW4tY3JlYXRlZCJ9LCB7ImV2ZW50VHlwZXMiOiBbIkFDVE9SLlJVTi5TVUNDRUVERUQiXSwgInJlcXVlc3RVcmwiOiAiaHR0cHM6Ly9leGFtcGxlLmNvbS9ydW4tc3VjY2VlZGVkIiwgInBheWxvYWRUZW1wbGF0ZSI6ICJ7XCJoZWxsb1wiOiBcIndvcmxkXCIsIFwicmVzb3VyY2VcIjp7e3Jlc291cmNlfX19In1d'  # noqa: E501
    )


================================================
File: /tests/integration/conftest.py
================================================
import os

import pytest

from apify_client import ApifyClient, ApifyClientAsync

TOKEN_ENV_VAR = 'APIFY_TEST_USER_API_TOKEN'
API_URL_ENV_VAR = 'APIFY_INTEGRATION_TESTS_API_URL'


@pytest.fixture
def apify_client() -> ApifyClient:
    api_token = os.getenv(TOKEN_ENV_VAR)
    api_url = os.getenv(API_URL_ENV_VAR)

    if not api_token:
        raise RuntimeError(f'{TOKEN_ENV_VAR} environment variable is missing, cannot run tests!')

    return ApifyClient(api_token, api_url=api_url)


# This fixture can't be session-scoped,
# because then you start getting `RuntimeError: Event loop is closed` errors,
# because `httpx.AsyncClient` in `ApifyClientAsync` tries to reuse the same event loop across requests,
# but `pytest-asyncio` closes the event loop after each test,
# and uses a new one for the next test.
@pytest.fixture
def apify_client_async() -> ApifyClientAsync:
    api_token = os.getenv(TOKEN_ENV_VAR)
    api_url = os.getenv(API_URL_ENV_VAR)

    if not api_token:
        raise RuntimeError(f'{TOKEN_ENV_VAR} environment variable is missing, cannot run tests!')

    return ApifyClientAsync(api_token, api_url=api_url)


================================================
File: /tests/integration/test_basic.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apify_client import ApifyClient, ApifyClientAsync


class TestBasicSync:
    def test_basic(self, apify_client: ApifyClient) -> None:
        me = apify_client.user('me').get()
        assert me is not None
        assert me.get('id') is not None
        assert me.get('username') is not None


class TestBasicAsync:
    async def test_basic(self, apify_client_async: ApifyClientAsync) -> None:
        me = await apify_client_async.user('me').get()
        assert me is not None
        assert me.get('id') is not None
        assert me.get('username') is not None


================================================
File: /tests/integration/test_request_queue.py
================================================
from __future__ import annotations

import secrets
import string
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apify_client import ApifyClient, ApifyClientAsync


def random_string(length: int = 10) -> str:
    return ''.join(secrets.choice(string.ascii_letters) for _ in range(length))


def random_queue_name() -> str:
    return f'python-client-test-queue-{random_string(5)}'


class TestRequestQueueSync:
    def test_request_queue_lock(self, apify_client: ApifyClient) -> None:
        created_queue = apify_client.request_queues().get_or_create(name=random_queue_name())
        queue = apify_client.request_queue(created_queue['id'], client_key=random_string(10))

        # Add requests and check if correct number of requests was locked
        for i in range(15):
            queue.add_request({'url': f'http://test-lock.com/{i}', 'uniqueKey': f'http://test-lock.com/{i}'})
        locked_requests_list = queue.list_and_lock_head(limit=10, lock_secs=10)
        locked_requests = locked_requests_list['items']
        for locked_request in locked_requests:
            assert locked_request['lockExpiresAt'] is not None

        # Check if the delete request works
        queue.delete_request_lock(locked_requests[1]['id'])
        delete_lock_request = queue.get_request(locked_requests[1]['id'])
        assert delete_lock_request is not None
        assert delete_lock_request.get('lockExpiresAt') is None
        queue.delete_request_lock(locked_requests[2]['id'], forefront=True)
        delete_lock_request2 = queue.get_request(locked_requests[2]['id'])
        assert delete_lock_request2 is not None
        assert delete_lock_request2.get('lockExpiresAt') is None

        # Check if the prolong request works
        assert queue.prolong_request_lock(locked_requests[3]['id'], lock_secs=15)['lockExpiresAt'] is not None

        queue.delete()
        assert apify_client.request_queue(created_queue['id']).get() is None

    def test_request_batch_operations(self, apify_client: ApifyClient) -> None:
        created_queue = apify_client.request_queues().get_or_create(name=random_queue_name())
        queue = apify_client.request_queue(created_queue['id'])

        # Add requests to queue and check if they were added
        requests_to_add = [
            {'url': f'http://test-batch.com/{i}', 'uniqueKey': f'http://test-batch.com/{i}'} for i in range(25)
        ]
        added_requests = queue.batch_add_requests(requests_to_add)
        assert len(added_requests.get('processedRequests', [])) > 0
        requests_in_queue = queue.list_requests()
        assert len(requests_in_queue['items']) == len(added_requests['processedRequests'])

        # Delete requests from queue and check if they were deleted
        requests_to_delete = requests_in_queue['items'][:20]
        delete_response = queue.batch_delete_requests(
            [{'uniqueKey': req.get('uniqueKey')} for req in requests_to_delete]
        )
        requests_in_queue2 = queue.list_requests()
        assert len(requests_in_queue2['items']) == 25 - len(delete_response['processedRequests'])

        queue.delete()


class TestRequestQueueAsync:
    async def test_request_queue_lock(self, apify_client_async: ApifyClientAsync) -> None:
        created_queue = await apify_client_async.request_queues().get_or_create(name=random_queue_name())
        queue = apify_client_async.request_queue(created_queue['id'], client_key=random_string(10))

        # Add requests and check if correct number of requests was locked
        for i in range(15):
            await queue.add_request({'url': f'http://test-lock.com/{i}', 'uniqueKey': f'http://test-lock.com/{i}'})
        locked_requests_list = await queue.list_and_lock_head(limit=10, lock_secs=10)
        locked_requests = locked_requests_list['items']
        for locked_request in locked_requests:
            assert locked_request['lockExpiresAt'] is not None

        # Check if the delete request works
        await queue.delete_request_lock(locked_requests[1]['id'])
        delete_lock_request = await queue.get_request(locked_requests[1]['id'])
        assert delete_lock_request is not None
        assert delete_lock_request.get('lockExpiresAt') is None
        await queue.delete_request_lock(locked_requests[2]['id'], forefront=True)
        delete_lock_request2 = await queue.get_request(locked_requests[2]['id'])
        assert delete_lock_request2 is not None
        assert delete_lock_request2.get('lockExpiresAt') is None

        # Check if the prolong request works
        prolonged_request = await queue.prolong_request_lock(locked_requests[3]['id'], lock_secs=15)
        assert prolonged_request['lockExpiresAt'] is not None

        await queue.delete()
        assert await apify_client_async.request_queue(created_queue['id']).get() is None

    async def test_request_batch_operations(self, apify_client_async: ApifyClientAsync) -> None:
        created_queue = await apify_client_async.request_queues().get_or_create(name=random_queue_name())
        queue = apify_client_async.request_queue(created_queue['id'])

        # Add requests to queue and check if they were added
        requests_to_add = [
            {'url': f'http://test-batch.com/{i}', 'uniqueKey': f'http://test-batch.com/{i}'} for i in range(25)
        ]
        added_requests = await queue.batch_add_requests(requests_to_add)
        assert len(added_requests.get('processedRequests', [])) > 0
        requests_in_queue = await queue.list_requests()
        assert len(requests_in_queue['items']) == len(added_requests['processedRequests'])

        # Delete requests from queue and check if they were deleted
        requests_to_delete = requests_in_queue['items'][:20]
        delete_response = await queue.batch_delete_requests(
            [{'uniqueKey': req.get('uniqueKey')} for req in requests_to_delete]
        )
        requests_in_queue2 = await queue.list_requests()
        assert len(requests_in_queue2['items']) == 25 - len(delete_response['processedRequests'])

        await queue.delete()


================================================
File: /tests/integration/test_store.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from apify_client import ApifyClient, ApifyClientAsync


class TestStoreCollectionSync:
    def test_list(self, apify_client: ApifyClient) -> None:
        actors_list = apify_client.store().list()
        assert actors_list is not None
        assert len(actors_list.items) != 0


class TestStoreCollectionAsync:
    async def test_list(self, apify_client_async: ApifyClientAsync) -> None:
        actors_list = await apify_client_async.store().list()
        assert actors_list is not None
        assert len(actors_list.items) != 0


================================================
File: /CHANGELOG.md
================================================
# Changelog

All notable changes to this project will be documented in this file.

<!-- git-cliff-unreleased-start -->
## 1.9.0 - **not yet released**

### 🚀 Features

- Add user.update_limits ([#279](https://github.com/apify/apify-client-python/pull/279)) ([7aed9c9](https://github.com/apify/apify-client-python/commit/7aed9c928958831168ac8d293538d6fd3adbc5e5)) by [@MFori](https://github.com/MFori), closes [#329](https://github.com/apify/apify-client-python/issues/329)
- Add charge method to the run client for &quot;pay per event&quot; ([#304](https://github.com/apify/apify-client-python/pull/304)) ([3bd6bbb](https://github.com/apify/apify-client-python/commit/3bd6bbb86d2b777863f0c3d0459b61da9a7f15ff)) by [@Jkuzz](https://github.com/Jkuzz)
- Add error data to ApifyApiError ([#314](https://github.com/apify/apify-client-python/pull/314)) ([df2398b](https://github.com/apify/apify-client-python/commit/df2398b51d774c5f8653a80f83b320d0f5394dde)) by [@Pijukatel](https://github.com/Pijukatel), closes [#306](https://github.com/apify/apify-client-python/issues/306)


<!-- git-cliff-unreleased-end -->
## [1.8.1](https://github.com/apify/apify-client-python/releases/tags/v1.8.1) (2024-09-17)

### 🐛 Bug Fixes

- Batch add requests can handle more than 25 requests ([#268](https://github.com/apify/apify-client-python/pull/268)) ([9110ee0](https://github.com/apify/apify-client-python/commit/9110ee08954762aed00ac09cd042e802c1d041f7)) by [@vdusek](https://github.com/vdusek), closes [#264](https://github.com/apify/apify-client-python/issues/264)


## [1.8.0](https://github.com/apify/apify-client-python/releases/tags/v1.8.0) (2024-08-30)

- drop support for Python 3.8

### 🚀 Features

- Adds headers_template to webhooks and webhooks_collection ([#239](https://github.com/apify/apify-client-python/pull/239)) ([6dbd781](https://github.com/apify/apify-client-python/commit/6dbd781d24d9deb6a7669193ce4d5a4190fe5026)) by [@jakerobers](https://github.com/jakerobers)
- Add actor standby ([#248](https://github.com/apify/apify-client-python/pull/248)) ([dd4bf90](https://github.com/apify/apify-client-python/commit/dd4bf9072a4caa189af5f90e513e37df325dc929)) by [@jirimoravcik](https://github.com/jirimoravcik)
- Allow passing list of fields to unwind parameter ([#256](https://github.com/apify/apify-client-python/pull/256)) ([036b455](https://github.com/apify/apify-client-python/commit/036b455c51243e0ef81cb74a44fe670abc085ce7)) by [@fnesveda](https://github.com/fnesveda)

## [1.7.1](../../releases/tag/v1.7.1) - 2024-07-11

### Fixed

- fix breaking change (sync -> async) in 1.7.0
- fix getting storages of last run

## [1.7.0](../../releases/tag/v1.7.0) - 2024-05-20

### Fixed

- fix abort of last task run
- fix abort of last Actor run
- `ActorClient`'s and `TaskClient`'s `last_run` methods are asynchronous

## [1.6.4](../../releases/tag/v1.6.4) - 2024-02-27

### Added

- added `monthlyUsage()` and `limits()` methods to `UserClient`

## [1.6.3](../../releases/tag/v1.6.3) - 2023-02-16

### Added

- added `log()` method to `BuildClient`

## [1.6.2](../../releases/tag/v1.6.2) - 2023-01-08

### Internal changes

- Relative imports were replaced for absolute imports

## [1.6.1](../../releases/tag/v1.6.1) - 2023-12-11

### Fixed

- Fixed `_BaseHTTPClient._parse_params()` method to ensure correct conversion of API list parameters

## [1.6.0](../../releases/tag/v1.6.0) - 2023-11-16

### Internal changes

- Migrate from Autopep8 and Flake8 to Ruff

## [1.5.0](../../releases/tag/v1.5.0) - 2023-10-18

### Added

- added support for Python 3.12
- added DELETE to Actor runs
- added DELETE to Actor builds

### Internal changes

- rewrote documentation publication to use Docusaurus
- removed PR Toolkit workflow

## [1.4.1](../../releases/tag/v1.4.1) - 2023-09-06

### Added

- added `StoreCollectionClient` for listing Actors in the Apify Store
- added support for specifying the `max_items` parameter for pay-per result Actors and their runs

### Internal changes

- improved logging of HTTP requests
- removed `pytest-randomly` Pytest plugin

## [1.4.0](../../releases/tag/v1.4.0) - 2023-08-23

### Added

- added `RunClient.reboot` method to reboot Actor runs

### Internal changes

- simplified code via `flake8-simplify`
- unified indentation in configuration files

## [1.3.1](../../releases/tag/v1.3.1) - 2023-07-28

### Internal changes

- started importing general constants and utilities from the `apify-shared` library

## [1.3.0](../../releases/tag/v1.3.0) - 2023-07-24

### Added

- added `list_and_lock_head`, `delete_request_lock`, `prolong_request_lock` methods to `RequestQueueClient`
- added `batch_add_requests`, `batch_delete_requests`, `list_requests` methods `RequestQueueClient`

## [1.2.2](../../releases/tag/v1.2.2) - 2023-05-31

### Fixed

- fixed encoding webhook lists in request parameters

## [1.2.1](../../releases/tag/v1.2.1) - 2023-05-23

### Fixed

- relaxed dependency requirements to improve compatibility with other libraries

## [1.2.0](../../releases/tag/v1.2.0) - 2023-05-23

### Added

- added option to change the build, memory limit and timeout when resurrecting a run

### Internal changes

- updated dependencies

## [1.1.1](../../releases/tag/v1.1.1) - 2023-05-05

### Internal changes

- changed GitHub workflows to use new secrets

## [1.1.0](../../releases/tag/v1.1.0) - 2023-05-05

### Added

- added support for `is_status_message_terminal` flag in Actor run status message update

### Internal changes

- switched from `setup.py` to `pyproject.toml` for specifying project setup

## [1.0.0](../../releases/tag/v1.0.0) - 2023-03-13

### Breaking changes

- dropped support for Python 3.7, added support for Python 3.11
- unified methods for streaming resources
- switched underlying HTTP library from `requests` to `httpx`

### Added

- added support for asynchronous usage via `ApifyClientAsync`
- added configurable socket timeout for requests to the Apify API
- added `py.typed` file to signal type checkers that this package is typed
- added method to update status message for a run
- added option to set up webhooks for Actor builds
- added logger with basic debugging info
- added support for `schema` parameter in `get_or_create` method for datasets and key-value stores
- added support for `title` parameter in task and schedule methods
- added `x-apify-workflow-key` header support
- added support for `flatten` and `view` parameters in dataset items methods
- added support for `origin` parameter in Actor/task run methods
- added clients for Actor version environment variables

### Fixed

- disallowed `NaN` and `Infinity` values in JSONs sent to the Apify API

### Internal changes

- simplified retrying with exponential backoff
- improved checks for "not found" errors
- simplified flake8 config
- updated development dependencies
- simplified development scripts
- updated GitHub Actions versions to fix deprecations
- unified unit test style
- unified preparing resource representation
- updated output management in GitHub Workflows to fix deprecations
- improved type hints across codebase
- added option to manually publish the package with a workflow dispatch
- added `pre-commit` to run code quality checks before committing
- converted `unittest`-style tests to `pytest`-style tests
- backported project setup improvements from `apify-sdk-python`

## [0.6.0](../../releases/tag/v0.6.0) - 2022-06-27

### Removed

- Dropped support for single-file Actors

### Internal changes

- updated dependencies
- fixed some lint issues in shell scripts and `setup.py`
- added Python 3.10 to unit test roster

## [0.5.0](../../releases/tag/v0.5.0) - 2021-09-16

### Changed

- improved retrying broken API server connections

### Fixed

- fixed timeout value in actively waiting for a run to finish

### Internal changes

- updated development dependencies

## [0.4.0](../../releases/tag/v0.4.0) - 2021-09-07

### Changed

- improved handling of `Enum` arguments
- improved support for storing more data types in key-value stores

### Fixed

- fixed values of some `ActorJobStatus` `Enum` members

## [0.3.0](../../releases/tag/v0.3.0) - 2021-08-26

### Added

- added the `test()` method to the webhook client
- added support for indicating the pagination direction in the `ListPage` objects

### Changed

- improved support for storing more data types in datasets

### Fixed

- fixed return type in the `DatasetClient.list_items()` method docs

### Internal changes

- added human-friendly names to the jobs in Github Action workflows
- updated development dependencies

## [0.2.0](../../releases/tag/v0.2.0) - 2021-08-09

### Added

- added the `gracefully` parameter to the "Abort run" method

### Changed

- replaced `base_url` with `api_url` in the client constructor
  to enable easier passing of the API server url from environment variables available to Actors on the Apify platform

### Internal changes

- changed tags for Actor images with this client on Docker Hub to be aligned with the Apify SDK Node.js images
- updated the `requests` dependency to 2.26.0
- updated development dependencies

## [0.1.0](../../releases/tag/v0.1.0) - 2021-08-02

### Changed

- methods using specific option values for arguments now use well-defined and documented `Enum`s for those arguments instead of generic strings
- made the submodule `apify_client.consts` containing those `Enum`s available

### Internal changes

- updated development dependencies
- enforced unified use of single quotes and double quotes
- added repository dispatch to build Actor images with this client when publishing a new version

## [0.0.1](../../releases/tag/v0.0.1) - 2021-05-13

Initial release of the package.

================================================
File: /scripts/check_async_docstrings.py
================================================
#!/usr/bin/env python3

"""Check if async docstrings are the same as sync."""

import re
import sys
from pathlib import Path

from redbaron import RedBaron  # type: ignore[import-untyped]
from utils import sync_to_async_docstring

found_issues = False

# Get the directory of the source files
clients_path = Path(__file__).parent.resolve() / '../src/apify_client'

# Go through every Python file in that directory
for client_source_path in clients_path.glob('**/*.py'):
    with open(client_source_path, encoding='utf-8') as source_file:
        # Read the source file and parse the code using Red Baron
        red = RedBaron(source_code=source_file.read())

        # Find all classes which end with "ClientAsync" (there should be at most 1 per file)
        async_class = red.find('ClassNode', name=re.compile('.*ClientAsync$'))
        if not async_class:
            continue

        # Find the corresponding sync classes (same name, but without -Async)
        sync_class = red.find('ClassNode', name=async_class.name.replace('ClientAsync', 'Client'))

        # Go through all methods in the async class
        for async_method in async_class.find_all('DefNode'):
            # Find corresponding sync method in the sync class
            sync_method = sync_class.find('DefNode', name=async_method.name)

            # Skip methods with @ignore_docs decorator
            if len(async_method.decorators) and str(async_method.decorators[0].value) == 'ignore_docs':
                continue

            # If the sync method has a docstring, check if it matches the async dostring
            if sync_method and isinstance(sync_method.value[0].value, str):
                sync_docstring = sync_method.value[0].value
                async_docstring = async_method.value[0].value
                expected_docstring = sync_to_async_docstring(sync_docstring)

                if not isinstance(async_docstring, str):
                    print(f'Missing docstring for "{async_class.name}.{async_method.name}"!')
                    found_issues = True
                elif expected_docstring != async_docstring:
                    print(
                        f'Docstring for "{async_class.name}.{async_method.name}" is out of sync with "{sync_class.name}.{sync_method.name}"!'  # noqa: E501
                    )
                    found_issues = True

if found_issues:
    print()
    print('Issues with async docstrings found. Please fix them manually or by running `make fix-async-docstrings`.')
    sys.exit(1)
else:
    print('Success: async method docstrings are in sync with sync method docstrings.')


================================================
File: /scripts/utils.py
================================================
import json
import pathlib
import re
from urllib.error import HTTPError
from urllib.request import urlopen

PACKAGE_NAME = 'apify_client'
REPO_ROOT = pathlib.Path(__file__).parent.resolve() / '..'
PYPROJECT_TOML_FILE_PATH = REPO_ROOT / 'pyproject.toml'


# Load the current version number from pyproject.toml
# It is on a line in the format `version = "1.2.3"`
def get_current_package_version() -> str:
    with open(PYPROJECT_TOML_FILE_PATH, encoding='utf-8') as pyproject_toml_file:
        for line in pyproject_toml_file:
            if line.startswith('version = '):
                delim = '"' if '"' in line else "'"
                return line.split(delim)[1]
        else:  # noqa: PLW0120
            raise RuntimeError('Unable to find version string.')


# Write the given version number from pyproject.toml
# It replaces the version number on the line with the format `version = "1.2.3"`
def set_current_package_version(version: str) -> None:
    with open(PYPROJECT_TOML_FILE_PATH, 'r+', encoding='utf-8') as pyproject_toml_file:
        updated_pyproject_toml_file_lines = []
        version_string_found = False
        for line in pyproject_toml_file:
            line_processed = line
            if line.startswith('version = '):
                version_string_found = True
                line_processed = f'version = "{version}"\n'
            updated_pyproject_toml_file_lines.append(line_processed)

        if not version_string_found:
            raise RuntimeError('Unable to find version string.')

        pyproject_toml_file.seek(0)
        pyproject_toml_file.write(''.join(updated_pyproject_toml_file_lines))
        pyproject_toml_file.truncate()


# Generate convert a docstring from a sync resource client method
# into a doctring for its async resource client analogue
def sync_to_async_docstring(docstring: str) -> str:
    substitutions = [(r'Client', r'ClientAsync')]
    res = docstring
    for pattern, replacement in substitutions:
        res = re.sub(pattern, replacement, res, flags=re.MULTILINE)
    return res


# Load the version numbers of the currently published versions from PyPI
def get_published_package_versions() -> list:
    package_info_url = f'https://pypi.org/pypi/{PACKAGE_NAME}/json'
    try:
        package_data = json.load(urlopen(package_info_url))  # noqa: S310
        published_versions = list(package_data['releases'].keys())
    # If the URL returns 404, it means the package has no releases yet (which is okay in our case)
    except HTTPError as e:
        if e.code != 404:
            raise
        published_versions = []
    return published_versions


================================================
File: /scripts/fix_async_docstrings.py
================================================
#!/usr/bin/env python3

import re
from pathlib import Path

from redbaron import RedBaron  # type: ignore[import-untyped]
from utils import sync_to_async_docstring

# Get the directory of the source files
clients_path = Path(__file__).parent.resolve() / '../src/apify_client'

# Go through every Python file in that directory
for client_source_path in clients_path.glob('**/*.py'):
    with open(client_source_path, 'r+', encoding='utf-8') as source_file:
        # Read the source file and parse the code using Red Baron
        red = RedBaron(source_code=source_file.read())

        # Find all classes which end with "ClientAsync" (there should be at most 1 per file)
        async_class = red.find('ClassNode', name=re.compile('.*ClientAsync$'))
        if not async_class:
            continue

        # Find the corresponding sync classes (same name, but without -Async)
        sync_class = red.find('ClassNode', name=async_class.name.replace('ClientAsync', 'Client'))

        # Go through all methods in the async class
        for async_method in async_class.find_all('DefNode'):
            # Find corresponding sync method in the sync class
            sync_method = sync_class.find('DefNode', name=async_method.name)

            # Skip methods with @ignore_docs decorator
            if len(async_method.decorators) and str(async_method.decorators[0].value) == 'ignore_docs':
                continue

            # If the sync method has a docstring, copy it to the async method (with adjustments)
            if isinstance(sync_method.value[0].value, str):
                sync_docstring = sync_method.value[0].value
                async_docstring = async_method.value[0].value

                correct_async_docstring = sync_to_async_docstring(sync_docstring)
                if async_docstring == correct_async_docstring:
                    continue

                # Work around a bug in Red Baron, which indents docstrings too much when you insert them,
                # so we have to un-indent it one level first.
                correct_async_docstring = re.sub('^    ', '', correct_async_docstring, flags=re.MULTILINE)

                if not isinstance(async_docstring, str):
                    print(f'Fixing missing docstring for "{async_class.name}.{async_method.name}"...')
                    async_method.value.insert(0, correct_async_docstring)
                else:
                    async_method.value[0] = correct_async_docstring

        updated_source_code = red.dumps()

        # Work around a bug in Red Baron, which adds indents to docstrings when you insert them (including empty lines),
        # so we have to remove the extra whitespace
        updated_source_code = re.sub('^    $', '', updated_source_code, flags=re.MULTILINE)

        # Work around a bug in Red Baron, which indents `except` and `finally` statements wrong
        # so we have to add some extra whitespace
        updated_source_code = re.sub('^except', '        except', updated_source_code, flags=re.MULTILINE)
        updated_source_code = re.sub('^    except', '        except', updated_source_code, flags=re.MULTILINE)
        updated_source_code = re.sub('^finally', '        finally', updated_source_code, flags=re.MULTILINE)
        updated_source_code = re.sub('^    finally', '        finally', updated_source_code, flags=re.MULTILINE)

        # Work around a bug in Red Baron, which sometimes adds an extra new line to the end of a file
        updated_source_code = updated_source_code.rstrip() + '\n'

        # Save the updated source code back to the file
        source_file.seek(0)
        source_file.write(updated_source_code)
        source_file.truncate()


================================================
File: /.github/workflows/update_new_issue.yaml
================================================
name: Update new issue

on:
  issues:
    types:
      - opened

jobs:
  label_issues:
    name: Label issues
    runs-on: ubuntu-latest
    permissions:
      issues: write

    steps:
      # Add the "t-tooling" label to all new issues
      - uses: actions/github-script@v7
        with:
          script: |
            github.rest.issues.addLabels({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              labels: ["t-tooling"]
            })


================================================
File: /.github/workflows/_async_docstrings_check.yaml
================================================
name: Async docstrings check

on:
  workflow_call:

env:
  PYTHON_VERSION: 3.12

jobs:
  async_docstring_check:
    name: Async docstrings check
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install dependencies
        run: |
          pipx install --python ${{ env.PYTHON_VERSION }} poetry
          make install-dev

      - name: Run async docstrings check
        run: make check-async-docstrings


================================================
File: /.github/workflows/build_and_deploy_docs.yaml
================================================
name: Build and deploy docs

on:
  push:
    branches:
      - master
  workflow_dispatch:

env:
  NODE_VERSION: 20
  PYTHON_VERSION: 3.12

jobs:
  build_and_deploy_docs:
    environment:
      name: github-pages
    permissions:
      contents: write
      pages: write
      id-token: write
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4
        with:
          token: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

      - name: Set up Node
        uses: actions/setup-node@v4
        with:
          node-version: ${{ env.NODE_VERSION }}
          cache: npm
          cache-dependency-path: website/package-lock.json

      - name: Install Node dependencies
        run: |
          npm install
          npm update @apify/docs-theme
        working-directory: ./website

      # We do this as early as possible to prevent conflicts if someone else would push something in the meantime
      - name: Commit the updated package.json and lockfile
        run: |
          git config user.name 'GitHub Actions'
          git config user.email 'github-actions[bot]@users.noreply.github.com'
          git add website/package.json
          git add website/package-lock.json
          git diff-index --quiet HEAD || git commit -m 'chore: Automatic docs theme update [skip ci]' || true
          git push

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: ${{ env.PYTHON_VERSION }}

      - name: Install Python dependencies
        run: |
          pipx install --python ${{ env.PYTHON_VERSION }} poetry
          make install-dev

      - name: Build generated API reference
        run: make build-api-reference

      - name: Build Docusaurus docs
        run: make build-docs

      - name: Set up GitHub Pages
        uses: actions/configure-pages@v5

      - name: Upload GitHub Pages artifact
        uses: actions/upload-pages-artifact@v3
        with:
          path: ./website/build

      - name: Deploy artifact to GitHub Pages
        uses: actions/deploy-pages@v4

      - name: Invalidate CloudFront cache
        run: gh workflow run invalidate.yaml --repo apify/apify-docs-private
        env:
          GITHUB_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}


================================================
File: /.github/workflows/run_code_checks.yaml
================================================
name: Run code checks

on:
  # Trigger code checks on opening a new pull request.
  # Secrets are only made available to the integration tests job, with a manual approval
  # step required for PRs from forks. This prevents their potential exposure.
  pull_request:

jobs:
  lint_check:
    name: Lint check
    uses: apify/workflows/.github/workflows/python_lint_check.yaml@main

  type_check:
    name: Type check
    uses: apify/workflows/.github/workflows/python_type_check.yaml@main

  unit_tests:
    name: Unit tests
    uses: apify/workflows/.github/workflows/python_unit_tests.yaml@main

  async_docstrings:
    name: Async dostrings check
    uses: ./.github/workflows/_async_docstrings_check.yaml

  docs_check:
    name: Docs check
    uses: apify/workflows/.github/workflows/python_docs_check.yaml@main

  integration_tests:
    name: Integration tests
    needs: [lint_check, type_check, unit_tests]
    uses: apify/workflows/.github/workflows/python_integration_tests.yaml@main
    secrets: inherit


================================================
File: /.github/workflows/release.yaml
================================================
name: Create a release

on:
  # Trigger a stable version release via GitHub's UI, with the ability to specify the type of release.
  workflow_dispatch:
    inputs:
      release_type:
        description: Release type
        required: true
        type: choice
        default: auto
        options:
          - auto
          - custom
          - patch
          - minor
          - major
      custom_version:
        description: The custom version to bump to (only for "custom" type)
        required: false
        type: string
        default: ""

jobs:
  release_metadata:
    name: Prepare release metadata
    runs-on: ubuntu-latest
    outputs: 
      version_number: ${{ steps.release_metadata.outputs.version_number }}
      tag_name: ${{ steps.release_metadata.outputs.tag_name }}
      changelog: ${{ steps.release_metadata.outputs.changelog }}
      release_notes: ${{ steps.release_metadata.outputs.release_notes }}
    steps:
      - uses: apify/workflows/git-cliff-release@main
        name: Prepare release metadata
        id: release_metadata
        with:
          release_type: ${{ inputs.release_type }}
          custom_version: ${{ inputs.custom_version }}
          existing_changelog_path: CHANGELOG.md

  lint_check:
    name: Lint check
    uses: apify/workflows/.github/workflows/python_lint_check.yaml@main

  type_check:
    name: Type check
    uses: apify/workflows/.github/workflows/python_type_check.yaml@main

  unit_tests:
    name: Unit tests
    uses: apify/workflows/.github/workflows/python_unit_tests.yaml@main

  async_docstrings:
    name: Async dostrings check
    uses: ./.github/workflows/_async_docstrings_check.yaml

  integration_tests:
    name: Integration tests
    uses: apify/workflows/.github/workflows/python_integration_tests.yaml@main
    secrets: inherit

  update_changelog:
    name: Update changelog
    needs: [release_metadata, lint_check, type_check, unit_tests, integration_tests]
    uses: apify/workflows/.github/workflows/python_bump_and_update_changelog.yaml@main
    with:
      version_number: ${{ needs.release_metadata.outputs.version_number }}
      changelog: ${{ needs.release_metadata.outputs.changelog }}
    secrets: 
      APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

  create_github_release:
    name: Create github release
    needs: [release_metadata, update_changelog]
    runs-on: ubuntu-latest
    env:
      GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
    steps:
      - name: Create release
        uses: softprops/action-gh-release@v2
        with:
          tag_name: ${{ needs.release_metadata.outputs.tag_name }}
          name: ${{ needs.release_metadata.outputs.version_number }}
          target_commitish: ${{ needs.update_changelog.outputs.changelog_commitish }}
          body: ${{ needs.release_metadata.outputs.release_notes }}

  publish_to_pypi:
    name: Publish to PyPI
    needs: [release_metadata, update_changelog]
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: write # Required for OIDC authentication.
    environment:
      name: pypi
      url: https://pypi.org/project/apify-client
    steps:
      - name: Prepare distribution
        uses: apify/workflows/prepare-pypi-distribution@main
        with: 
          package_name: apify-client
          is_prerelease: ""
          version_number: ${{ needs.release_metadata.outputs.version_number }}
          ref: ${{ needs.update_changelog.outputs.changelog_commitish }}
      # Publishes the package to PyPI using PyPA official GitHub action with OIDC authentication.
      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1


================================================
File: /.github/workflows/check_pr_title.yaml
================================================
name: Check PR title

on:
  pull_request_target:
    types: [opened, edited, synchronize]

jobs:
  check_pr_title:
    name: Check PR title
    runs-on: ubuntu-latest
    steps:
      - uses: amannn/action-semantic-pull-request@v5.5.3
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}


================================================
File: /.github/workflows/pre_release.yaml
================================================
name: Create a pre-release

on:
  # Trigger a beta version release (pre-release) on push to the master branch.
  push:
    branches:
      - master
    tags-ignore:
      - "**" # Ignore all tags to prevent duplicate builds when tags are pushed.

jobs:
  release_metadata:
    if: "!startsWith(github.event.head_commit.message, 'docs') && !startsWith(github.event.head_commit.message, 'ci') && startsWith(github.repository, 'apify/')"
    name: Prepare release metadata
    runs-on: ubuntu-latest
    outputs:
      version_number: ${{ steps.release_metadata.outputs.version_number }}
      tag_name: ${{ steps.release_metadata.outputs.tag_name }}
      changelog: ${{ steps.release_metadata.outputs.changelog }}
    steps:
      - uses: apify/workflows/git-cliff-release@main
        id: release_metadata
        name: Prepare release metadata
        with:
          release_type: prerelease
          existing_changelog_path: CHANGELOG.md

  lint_check:
    name: Lint check
    uses: apify/workflows/.github/workflows/python_lint_check.yaml@main

  type_check:
    name: Type check
    uses: apify/workflows/.github/workflows/python_type_check.yaml@main

  unit_tests:
    name: Unit tests
    uses: apify/workflows/.github/workflows/python_unit_tests.yaml@main

  async_docstrings:
    name: Async dostrings check
    uses: ./.github/workflows/_async_docstrings_check.yaml

  integration_tests:
    name: Integration tests
    uses: apify/workflows/.github/workflows/python_integration_tests.yaml@main
    secrets: inherit

  update_changelog:
    name: Update changelog
    needs: [release_metadata, lint_check, type_check, unit_tests, integration_tests]
    uses: apify/workflows/.github/workflows/python_bump_and_update_changelog.yaml@main
    with:
      version_number: ${{ needs.release_metadata.outputs.version_number }}
      changelog: ${{ needs.release_metadata.outputs.changelog }}
    secrets:
      APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN: ${{ secrets.APIFY_SERVICE_ACCOUNT_GITHUB_TOKEN }}

  publish_to_pypi:
    name: Publish to PyPI
    needs: [release_metadata, update_changelog]
    runs-on: ubuntu-latest
    permissions:
      contents: write
      id-token: write # Required for OIDC authentication.
    environment:
      name: pypi
      url: https://pypi.org/project/apify-client
    steps:
      - name: Prepare distribution
        uses: apify/workflows/prepare-pypi-distribution@main
        with: 
          package_name: apify-client
          is_prerelease: "yes"
          version_number: ${{ needs.release_metadata.outputs.version_number }}
          ref: ${{ needs.update_changelog.outputs.changelog_commitish }}
      # Publishes the package to PyPI using PyPA official GitHub action with OIDC authentication.
      - name: Publish package to PyPI
        uses: pypa/gh-action-pypi-publish@release/v1


================================================
File: /.github/CODEOWNERS
================================================
# Documentation codeowner

/docs/*.md @TC-MO
/docs/*.mdx @TC-MO


================================================
File: /renovate.json
================================================
{
    "extends": ["config:base", ":semanticCommitTypeAll(chore)"],
    "pinVersions": false,
    "separateMajorMinor": false,
    "dependencyDashboard": false,
    "semanticCommits": "enabled",
    "lockFileMaintenance": {
        "enabled": true,
        "automerge": true,
        "automergeType": "branch"
    },
    "packageRules": [
        {
            "matchPaths": ["pyproject.toml"],
            "matchDepTypes": ["devDependencies"],
            "matchUpdateTypes": ["major", "minor"],
            "groupName": "major/minor dev dependencies",
            "groupSlug": "dev-dependencies",
            "automerge": true,
            "automergeType": "branch"
        }
    ],
    "schedule": ["before 7am every weekday"],
    "ignoreDeps": ["apify_client", "docusaurus-plugin-typedoc-api"]
}


================================================
File: /Makefile
================================================
.PHONY: clean install-dev build publish-to-pypi lint type-check unit-tests unit-tests-cov \
        integration-tests format check-async-docstrings check-code fix-async-docstrings \
        build-api-reference build-docs run-docs

DIRS_WITH_CODE = src tests scripts

# This is default for local testing, but GitHub workflows override it to a higher value in CI
INTEGRATION_TESTS_CONCURRENCY = 1

clean:
	rm -rf .mypy_cache .pytest_cache .ruff_cache build dist htmlcov .coverage

install-dev:
	poetry install --all-extras
	poetry run pre-commit install

build:
	poetry build --no-interaction -vv

# APIFY_PYPI_TOKEN_CRAWLEE is expected to be set in the environment
publish-to-pypi:
	poetry config pypi-token.pypi "${APIFY_PYPI_TOKEN_CRAWLEE}"
	poetry publish --no-interaction -vv

lint:
	poetry run ruff format --check $(DIRS_WITH_CODE)
	poetry run ruff check $(DIRS_WITH_CODE)

type-check:
	poetry run mypy $(DIRS_WITH_CODE)

unit-tests:
	poetry run pytest --numprocesses=auto --verbose --cov=src/apify_client tests/unit

unit-tests-cov:
	poetry run pytest --numprocesses=auto --verbose --cov=src/apify_client --cov-report=html tests/unit

integration-tests:
	poetry run pytest --numprocesses=$(INTEGRATION_TESTS_CONCURRENCY) tests/integration

format:
	poetry run ruff check --fix $(DIRS_WITH_CODE)
	poetry run ruff format $(DIRS_WITH_CODE)

check-async-docstrings:
	poetry run python scripts/check_async_docstrings.py

# The check-code target runs a series of checks equivalent to those performed by pre-commit hooks
# and the run_checks.yaml GitHub Actions workflow.
check-code: lint type-check unit-tests check-async-docstrings

fix-async-docstrings:
	poetry run python scripts/fix_async_docstrings.py

build-api-reference:
	cd website && poetry run ./build_api_reference.sh

build-docs:
	cd website && npm clean-install && npm run build

run-docs: build-api-reference
	cd website && npm clean-install && npm run start


================================================
File: /pyproject.toml
================================================
[build-system]
requires = ["poetry-core"]
build-backend = "poetry.core.masonry.api"

[tool.poetry]
name = "apify_client"
version = "1.9.0"
description = "Apify API client for Python"
authors = ["Apify Technologies s.r.o. <support@apify.com>"]
license = "Apache-2.0"
readme = "README.md"
packages = [{ include = "apify_client", from = "src" }]
classifiers = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: Apache Software License",
    "Operating System :: OS Independent",
    "Programming Language :: Python :: 3.9",
    "Programming Language :: Python :: 3.10",
    "Programming Language :: Python :: 3.11",
    "Programming Language :: Python :: 3.12",
    "Topic :: Software Development :: Libraries",
]
keywords = [
    "apify",
    "api",
    "client",
    "automation",
    "crawling",
    "scraping",
]

[tool.poetry.urls]
"Homepage" = "https://docs.apify.com/api/client/python/"
"Apify Homepage" = "https://apify.com"
"Changelog" = "https://github.com/apify/apify-client-python/blob/master/CHANGELOG.md"
"Documentation" = "https://docs.apify.com/api/client/python/"
"Issue Tracker" = "https://github.com/apify/apify-client-python/issues"
"Repository" = "https://github.com/apify/apify-client-python"

[tool.poetry.dependencies]
python = "^3.9"
apify-shared = ">=1.1.2"
httpx = ">=0.25"
more_itertools = ">=10.0.0"

[tool.poetry.group.dev.dependencies]
build = "~1.2.0"
griffe = "~1.5.0"
ipdb = "~0.13.0"
mypy = "~1.13.0"
pre-commit = "~4.0.0"
pydoc-markdown = "~4.8.0"
pytest = "~8.3.0"
pytest-asyncio = "~0.25.0"
pytest-cov = "~6.0.0"
pytest-only = "~2.1.0"
pytest-timeout = "~2.3.0"
pytest-xdist = "~3.6.0"
redbaron = "~0.9.0"
respx = "~0.22.0"
ruff = "~0.8.0"
setuptools = "~75.6.0"     # setuptools are used by pytest but not explicitly required

[tool.ruff]
line-length = 120

[tool.ruff.lint]
select = ["ALL"]
ignore = [
    "ANN401",   # Dynamically typed expressions (typing.Any) are disallowed in {filename}
    "ASYNC109", # Async function definition with a `timeout` parameter
    "BLE001",   # Do not catch blind exception
    "C901",     # `{name}` is too complex
    "COM812",   # This rule may cause conflicts when used with the formatter
    "D100",     # Missing docstring in public module
    "D104",     # Missing docstring in public package
    "D107",     # Missing docstring in `__init__`
    "EM",       # flake8-errmsg
    "G004",     # Logging statement uses f-string
    "ISC001",   # This rule may cause conflicts when used with the formatter
    "FIX",      # flake8-fixme
    "PLR0911",  # Too many return statements
    "PLR0913",  # Too many arguments in function definition
    "PLR0915",  # Too many statements
    "PTH",      # flake8-use-pathlib
    "PYI034",   # `__aenter__` methods in classes like `{name}` usually return `self` at runtime
    "PYI036",   # The second argument in `__aexit__` should be annotated with `object` or `BaseException | None`
    "S102",     # Use of `exec` detected
    "S105",     # Possible hardcoded password assigned to
    "S106",     # Possible hardcoded password assigned to argument: "{name}"
    "S301",     # `pickle` and modules that wrap it can be unsafe when used to deserialize untrusted data, possible security issue
    "S303",     # Use of insecure MD2, MD4, MD5, or SHA1 hash function
    "S311",     # Standard pseudo-random generators are not suitable for cryptographic purposes
    "TD002",    # Missing author in TODO; try: `# TODO(<author_name>): ...` or `# TODO @<author_name>: ...
    "TRY003",   # Avoid specifying long messages outside the exception class
]

[tool.ruff.format]
quote-style = "single"
indent-style = "space"

[tool.ruff.lint.per-file-ignores]
"**/__init__.py" = [
    "F401", # Unused imports
]
"**/{scripts}/*" = [
    "D",       # Everything from the pydocstyle
    "INP001",  # File {filename} is part of an implicit namespace package, add an __init__.py
    "PLR2004", # Magic value used in comparison, consider replacing {value} with a constant variable
    "T20",     # flake8-print
]
"**/{tests}/*" = [
    "D",       # Everything from the pydocstyle
    "INP001",  # File {filename} is part of an implicit namespace package, add an __init__.py
    "PLR2004", # Magic value used in comparison, consider replacing {value} with a constant variable
    "S101",    # Use of assert detected
    "SLF001",  # Private member accessed: `{name}`
    "T20",     # flake8-print
    "TRY301",  # Abstract `raise` to an inner function
    "TID252",  # Prefer absolute imports over relative imports from parent modules
]

[tool.ruff.lint.flake8-quotes]
docstring-quotes = "double"
inline-quotes = "single"

[tool.ruff.lint.flake8-builtins]
builtins-ignorelist = ["id"]

[tool.ruff.lint.pydocstyle]
convention = "google"

[tool.ruff.lint.isort]
known-local-folder = ["apify_client"]

[tool.ruff.lint.pylint]
max-branches = 18

[tool.pytest.ini_options]
addopts = "-ra"
asyncio_default_fixture_loop_scope = "function"
asyncio_mode = "auto"
timeout = 1200

[tool.mypy]
python_version = "3.9"
files = ["scripts", "src", "tests"]
check_untyped_defs = true
disallow_incomplete_defs = true
disallow_untyped_calls = true
disallow_untyped_decorators = true
disallow_untyped_defs = true
no_implicit_optional = true
warn_redundant_casts = true
warn_return_any = true
warn_unreachable = true
warn_unused_ignores = true
exclude = []

[tool.basedpyright]
pythonVersion = "3.9"
typeCheckingMode = "standard"
include = ["scripts", "src", "tests"]

[tool.coverage.report]
exclude_lines = [
    "pragma: no cover",
    "if TYPE_CHECKING:",
    "assert_never()",
]

[tool.ipdb]
context = 7


================================================
File: /website/sidebars.js
================================================
module.exports = {
    sidebar: [
        {
            type: 'doc',
            id: 'index',
        },
        {
            type: 'doc',
            id: 'examples',
        },
    ],
};


================================================
File: /website/.eslintrc.json
================================================
{
    "extends": [
        "@apify/eslint-config-ts",
        "plugin:react/recommended",
        "plugin:react-hooks/recommended"
    ],
    "parserOptions": {
        "project": "./tsconfig.eslint.json",
        "ecmaFeatures": {
            "jsx": true
        },
        "ecmaVersion": 2020
    },
    "env": {
        "browser": true
    },
    "settings": {
        "react": {
            "version": "detect"
        }
    },
    "root": true,
    "ignorePatterns": [".docusaurus", "build"],
    "rules": {
        "quote-props": ["error", "consistent"]
    }
}


================================================
File: /website/generate_module_shortcuts.py
================================================
#!/usr/bin/env python3

import importlib
import inspect
import json


def get_module_shortcuts(module, parent_classes=None):
    """Traverse a module and its submodules, and if some class is present in both a module and its submodule, register a shortcut."""
    shortcuts = {}

    if parent_classes is None:
        parent_classes = []
    parent_module_name = '.'.join(module.__name__.split('.')[:-1])
    module_classes = []
    for classname, cls in inspect.getmembers(module, inspect.isclass):
        module_classes.append(cls)
        if cls in parent_classes:
            shortcuts[f'{module.__name__}.{classname}'] = f'{parent_module_name}.{classname}'

    for _, submodule in inspect.getmembers(module, inspect.ismodule):
        if (submodule.__name__.startswith('apify')):
            shortcuts.update(get_module_shortcuts(submodule, module_classes))

    return shortcuts


def resolve_shortcuts(shortcuts):
    """Resolve linked shortcuts.

    For example, if there are shortcuts A -> B and B -> C,
    resolve them to A -> C.
    """
    for source, target in shortcuts.items():
        while target in shortcuts:
            shortcuts[source] = shortcuts[target]
            target = shortcuts[target]


shortcuts = {}
for module_name in ['apify', 'apify_client', 'apify_shared']:
    try:
        module = importlib.import_module(module_name)
        module_shortcuts = get_module_shortcuts(module)
        shortcuts.update(module_shortcuts)
    except ModuleNotFoundError:
        pass

resolve_shortcuts(shortcuts)

with open('module_shortcuts.json', 'w', encoding='utf-8') as shortcuts_file:
    json.dump(shortcuts, shortcuts_file, indent=4, sort_keys=True)


================================================
File: /website/transformDocs.js
================================================
/* eslint-disable */

const fs = require('fs');
const { spawnSync } = require('child_process');

const moduleShortcuts = require('./module_shortcuts.json');

const REPO_ROOT_PLACEHOLDER = 'REPO_ROOT_PLACEHOLDER';

const APIFY_CLIENT_REPO_URL = 'https://github.com/apify/apify-client-python';
const APIFY_SDK_REPO_URL    = 'https://github.com/apify/apify-sdk-python';
const APIFY_SHARED_REPO_URL = 'https://github.com/apify/apify-shared-python';

const REPO_URL_PER_PACKAGE = {
    'apify': APIFY_SDK_REPO_URL,
    'apify_client': APIFY_CLIENT_REPO_URL,
    'apify_shared': APIFY_SHARED_REPO_URL,
};

// For each package, get the installed version, and set the tag to the corresponding version
const TAG_PER_PACKAGE = {};
for (const pkg of ['apify', 'apify_client', 'apify_shared']) {
    const spawnResult = spawnSync('python', ['-c', `import ${pkg}; print(${pkg}.__version__)`]);
    if (spawnResult.status === 0) {
        TAG_PER_PACKAGE[pkg] = `v${spawnResult.stdout.toString().trim()}`;
    }
}

// For the current package, set the tag to 'master'
const thisPackagePyprojectToml = fs.readFileSync('../pyproject.toml', 'utf8');
const thisPackageName = thisPackagePyprojectToml.match(/^name = "(.+)"$/m)[1];
TAG_PER_PACKAGE[thisPackageName] = 'master';


// Taken from https://github.com/TypeStrong/typedoc/blob/v0.23.24/src/lib/models/reflections/kind.ts, modified
const TYPEDOC_KINDS = {
    'class': {
        kind: 128,
        kindString: 'Class',
    },
    'function': {
        kind: 2048,
        kindString: 'Method',
    },
    'data': {
        kind: 1024,
        kindString: 'Property',
    },
    'enum': {
        kind: 8,
        kindString: 'Enumeration',
    },
    'enumValue': {
        kind: 16,
        kindString: 'Enumeration Member',
    },
}

const GROUP_ORDER = [
    'Main Classes',
    'Main Clients',
    'Resource Clients',
    'Async Resource Clients',
    'Helper Classes',
    'Errors',
    'Constructors',
    'Methods',
    'Properties',
    'Constants',
    'Enumeration Members'
];

const groupSort = (g1, g2) => {
    if(GROUP_ORDER.includes(g1) && GROUP_ORDER.includes(g2)){
        return GROUP_ORDER.indexOf(g1) - GROUP_ORDER.indexOf(g2)
    }
    return g1.localeCompare(g2);
};

function getGroupName(object) {
    const groupPredicates = {
        'Errors': (x) => x.name.toLowerCase().includes('error'),
        'Main Classes': (x) => ['Actor', 'Dataset', 'KeyValueStore', 'RequestQueue'].includes(x.name),
        'Main Clients': (x) => ['ApifyClient', 'ApifyClientAsync'].includes(x.name),
        'Async Resource Clients': (x) => x.name.toLowerCase().includes('async'),
        'Resource Clients': (x) => x.kindString === 'Class' && x.name.toLowerCase().includes('client'),
        'Helper Classes': (x) => x.kindString === 'Class',
        'Methods': (x) => x.kindString === 'Method',
        'Constructors': (x) => x.kindString === 'Constructor',
        'Properties': (x) => x.kindString === 'Property',
        'Constants': (x) => x.kindString === 'Enumeration',
        'Enumeration Members': (x) => x.kindString === 'Enumeration Member',
    };

    const [group] = Object.entries(groupPredicates).find(
        ([_, predicate]) => predicate(object)
    );

    return group;
}

// Strips the Optional[] type from the type string, and replaces generic types with just the main type
function getBaseType(type) {
    return type?.replace(/Optional\[(.*)\]/g, '$1').replace('ListPage[Dict]', 'ListPage');
}

// Returns whether a type is a custom class, or a primitive type
function isCustomClass(type) {
    return !['dict', 'list', 'str', 'int', 'float', 'bool'].includes(type.toLowerCase());
}

// Infer the Typedoc type from the docspec type
function inferTypedocType(docspecType) {
    const typeWithoutOptional = getBaseType(docspecType);
    if (!typeWithoutOptional) {
        return undefined;
    }

    // Typically, if a type is a custom class, it will be a reference in Typedoc
    return isCustomClass(typeWithoutOptional) ? {
        type: 'reference',
        name: docspecType
    } : {
        type: 'intrinsic',
        name: docspecType,
    }
}

// Sorts the groups of a Typedoc member, and sorts the children of each group
function sortChildren(typedocMember) {
    for (let group of typedocMember.groups) {
        group.children
            .sort((a, b) => {
                const firstName = typedocMember.children.find(x => x.id === a).name;
                const secondName = typedocMember.children.find(x => x.id === b).name;
                return firstName.localeCompare(secondName);
            });
    }
    typedocMember.groups.sort((a, b) => groupSort(a.title, b.title));
}

// Parses the arguments and return value description of a method from its docstring
function extractArgsAndReturns(docstring) {
    const parameters = (docstring
        .split('Args:')[1] ?? '').split('Returns:')[0] // Get the part between Args: and Returns:
        .split(/(^|\n)\s*([\w]+)\s*\(.*?\)\s*:\s*/) // Magic regex which splits the arguments into an array, and removes the argument types
        .filter(x => x.length > 1) // Remove empty strings
        .reduce((acc, curr, idx, arr) => { // Collect the argument names and types into an object
            if(idx % 2 === 0){
                return {...acc, [curr]: arr[idx+1]} // If the index is even, the current string is an argument name, and the next string is its type
            }
            return acc;
        }, {});

    const returns = (docstring
        .split('Returns:')[1] ?? '').split('Raises:')[0] // Get the part between Returns: and Raises:
        .split(':')[1]?.trim() || undefined; // Split the return value into its type and description, return description


    return { parameters, returns };
}

// Objects with decorators named 'ignore_docs' or with empty docstrings will be ignored
function isHidden(member) {
    return member.decorations?.some(d => d.name === 'ignore_docs') || member.name === 'ignore_docs' || !member.docstring?.content;
}

// Each object in the Typedoc structure has an unique ID,
// we'll just increment it for each object we convert
let oid = 1;

// Converts a docspec object to a Typedoc object, including all its children
function convertObject(obj, parent, module) {
    const rootModuleName = module.name.split('.')[0];
    for (let member of obj.members ?? []) {
        let typedocKind = TYPEDOC_KINDS[member.type];

        if(member.bases?.includes('Enum')) {
            typedocKind = TYPEDOC_KINDS['enum'];
        }

        if (member.decorations?.some(d => d.name === 'dualproperty')) {
            typedocKind = TYPEDOC_KINDS['data'];
        }

        let typedocType = inferTypedocType(member.datatype);

        if(parent.kindString === 'Enumeration') {
            typedocKind = TYPEDOC_KINDS['enumValue'];
            typedocType = {
                type: 'literal',
                value: member.value,
            }
        }

        if(member.type in TYPEDOC_KINDS && !isHidden(member)) {
            // Get the URL of the member in GitHub
            const repoBaseUrl = `${REPO_URL_PER_PACKAGE[rootModuleName]}/blob/${TAG_PER_PACKAGE[rootModuleName]}`;
            const filePathInRepo = member.location.filename.replace(REPO_ROOT_PLACEHOLDER, '');
            const fileGitHubUrl = member.location.filename.replace(REPO_ROOT_PLACEHOLDER, repoBaseUrl);
            const memberGitHubUrl = `${fileGitHubUrl}#L${member.location.lineno}`;

            // Get the module name of the member, and check if it has a shortcut (reexport from an ancestor module)
            const fullName = `${module.name}.${member.name}`;
            let moduleName = module.name;
            if (fullName in moduleShortcuts) {
                moduleName = moduleShortcuts[fullName].replace(`.${member.name}`, '');
            }

            // Create the Typedoc member object
            let typedocMember = {
                id: oid++,
                name: member.name,
                module: moduleName, // This is an extension to the original Typedoc structure, to support showing where the member is exported from
                ...typedocKind,
                flags: {},
                comment: member.docstring ? {
                    summary: [{
                        kind: 'text',
                        text: member.docstring?.content,
                    }],
                } : undefined,
                type: typedocType,
                children: [],
                groups: [],
                sources: [{
                    filename: filePathInRepo,
                    line: member.location.lineno,
                    character: 1,
                    url: memberGitHubUrl,
                }],
            };

            if(typedocMember.kindString === 'Method') {
                const { parameters, returns } = extractArgsAndReturns(member.docstring?.content ?? '');

                typedocMember.signatures = [{
                    id: oid++,
                    name: member.name,
                    modifiers: member.modifiers ?? [],
                    kind: 4096,
                    kindString: 'Call signature',
                    flags: {},
                    comment: member.docstring ? {
                        summary: [{
                            kind: 'text',
                            text: member.docstring?.content
                                .replace(/\**(Args|Arguments|Returns)[\s\S]+/, ''),
                        }],
                        blockTags: returns ? [
                            { tag: '@returns', content: [{ kind: 'text', text: returns }] },
                        ] : undefined,
                    } : undefined,
                    type: inferTypedocType(member.return_type),
                    parameters: member.args.filter((arg) => (arg.name !== 'self' && arg.name !== 'cls')).map((arg) => ({
                        id: oid++,
                        name: arg.name,
                        kind: 32768,
                        kindString: 'Parameter',
                        flags: {
                            isOptional: arg.datatype?.includes('Optional') ? 'true' : undefined,
                            'keyword-only': arg.type === 'KEYWORD_ONLY' ? 'true' : undefined,
                        },
                        type: inferTypedocType(arg.datatype),
                        comment: parameters[arg.name] ? {
                            summary: [{
                                kind: 'text',
                                text: parameters[arg.name]
                            }]
                        } : undefined,
                        defaultValue: arg.default_value,
                    })),
                }];
            }

            if(typedocMember.name === '__init__') {
                typedocMember.kind = 512;
                typedocMember.kindString = 'Constructor';
            }

            convertObject(member, typedocMember, module);

            const groupName = getGroupName(typedocMember);

            const group = parent.groups.find((g) => g.title === groupName);
            if (group) {
                group.children.push(typedocMember.id);
            } else {
                parent.groups.push({
                    title: groupName,
                    children: [typedocMember.id],
                });
            }

            sortChildren(typedocMember);
            parent.children.push(typedocMember);
        }
    }
}

function main() {
    // Root object of the Typedoc structure
    const typedocApiReference = {
        'id': 0,
        'name': 'apify-client',
        'kind': 1,
        'kindString': 'Project',
        'flags': {},
        'originalName': '',
        'children': [],
        'groups': [],
        'sources': [
            {
                'fileName': 'src/index.ts',
                'line': 1,
                'character': 0,
                'url': `http://example.com/blob/123456/src/dummy.py`,
            }
        ]
    };

    // Load the docspec dump files of this module and of apify-shared
    const thisPackageDocspecDump = fs.readFileSync('docspec-dump.jsonl', 'utf8');
    const thisPackageModules = thisPackageDocspecDump.split('\n').filter((line) => line !== '');

    const apifySharedDocspecDump = fs.readFileSync('apify-shared-docspec-dump.jsonl', 'utf8');
    const apifySharedModules = apifySharedDocspecDump.split('\n').filter((line) => line !== '');

    // Convert all the modules, store them in the root object
    for (const module of [...thisPackageModules, ...apifySharedModules]) {
        const parsedModule = JSON.parse(module);
        convertObject(parsedModule, typedocApiReference, parsedModule);
    };

    // Recursively fix references (collect names->ids of all the named entities and then inject those in the reference objects)
    const namesToIds = {};
    function collectIds(obj) {
        for (const child of obj.children ?? []) {
            namesToIds[child.name] = child.id;
            collectIds(child);
        }
    }
    collectIds(typedocApiReference);

    function fixRefs(obj) {
        for (const child of obj.children ?? []) {
            if (child.type?.type === 'reference') {
                child.type.id = namesToIds[child.type.name];
            }
            if (child.signatures) {
                for (const sig of child.signatures) {
                    for (const param of sig.parameters ?? []) {
                        if (param.type?.type === 'reference') {
                            param.type.id = namesToIds[param.type.name];
                        }
                    }
                    if (sig.type?.type === 'reference') {
                        sig.type.id = namesToIds[sig.type.name];
                    }
                }
            }
            fixRefs(child);
        }
    }
    fixRefs(typedocApiReference);

    // Sort the children of the root object
    sortChildren(typedocApiReference);

    // Write the Typedoc structure to the output file
    fs.writeFileSync('./api-typedoc-generated.json', JSON.stringify(typedocApiReference, null, 4));
}

if (require.main === module) {
    main();
}

module.exports = {
    groupSort,
}


================================================
File: /website/tools/docs-prettier.config.js
================================================
/**
 * @type {import('prettier').Options}
 */
module.exports = {
    parser: 'markdown',
    arrowParens: 'avoid',
    trailingComma: 'all',
    singleQuote: true,
    tabWidth: 4,
    printWidth: 150,
    proseWrap: 'always',
};


================================================
File: /website/tools/utils/externalLink.js
================================================
const { parse } = require('url');

const visit = import('unist-util-visit').then((m) => m.visit);

const internalUrls = ['sdk.apify.com'];

/**
 * @param {import('url').UrlWithStringQuery} href
 */
function isInternal(href) {
    return internalUrls.some(
        (internalUrl) => href.host === internalUrl
            || (!href.protocol && !href.host && (href.pathname || href.hash)),
    );
}

/**
 * @type {import('unified').Plugin}
 */
exports.externalLinkProcessor = () => {
    return async (tree) => {
        (await visit)(tree, 'element', (node) => {
            if (
                node.tagName === 'a'
                && node.properties
                && typeof node.properties.href === 'string'
            ) {
                const href = parse(node.properties.href);

                if (!isInternal(href)) {
                    node.properties.target = '_blank';
                    node.properties.rel = 'noopener';
                } else {
                    node.properties.target = null;
                    node.properties.rel = null;
                }
            }
        });
    };
};


================================================
File: /website/package.json
================================================
{
    "name": "apify-client-python",
    "private": "true",
    "scripts": {
        "clean": "rimraf .docusaurus build",
        "build": "npm run clean && docusaurus build",
        "start": "npm run clean && docusaurus start",
        "deploy": "npm run clean && docusaurus deploy",
        "docusaurus": "docusaurus",
        "publish-gh-pages": "docusaurus-publish",
        "rename-version": "docusaurus rename-version",
        "swizzle": "docusaurus swizzle",
        "version": "docusaurus version",
        "write-translations": "docusaurus write-translations",
        "prettify": "prettier --write --config ./tools/docs-prettier.config.js ../docs/*.md ../docs/*.mdx",
        "lint": "npm run lint:md && npm run lint:code",
        "lint:fix": "npm run lint:md:fix && npm run lint:code:fix",
        "lint:md": "markdownlint --config ../.markdownlint.yaml '../docs/**/*.md' '../docs/**/*.mdx' --ignore '../docs/changelog.md'",
        "lint:md:fix": "npm run lint:md -- --fix",
        "lint:code": "eslint .",
        "lint:code:fix": "eslint . --fix"
    },
    "dependencies": {
        "@apify/docs-theme": "^1.0.132",
        "@apify/docusaurus-plugin-typedoc-api": "^4.2.6",
        "@docusaurus/core": "^3.5.2",
        "@docusaurus/plugin-client-redirects": "^3.5.2",
        "@docusaurus/preset-classic": "^3.5.2",
        "clsx": "^2.0.0",
        "docusaurus-gtm-plugin": "^0.0.2",
        "prop-types": "^15.8.1",
        "raw-loader": "^4.0.2",
        "react": "^18.3.1",
        "react-dom": "^18.3.1",
        "unist-util-visit": "^5.0.0"
    },
    "devDependencies": {
        "@apify/eslint-config-ts": "^0.4.0",
        "@apify/tsconfig": "^0.1.0",
        "@types/react": "^18.0.0",
        "@typescript-eslint/eslint-plugin": "^8.0.0",
        "@typescript-eslint/parser": "^8.0.0",
        "eslint": "^9.0.0",
        "eslint-plugin-react": "^7.32.2",
        "eslint-plugin-react-hooks": "^5.0.0",
        "markdownlint": "^0.37.0",
        "markdownlint-cli": "^0.43.0",
        "path-browserify": "^1.0.1",
        "prettier": "^3.0.0",
        "rimraf": "^6.0.0"
    }
}


================================================
File: /website/babel.config.js
================================================
module.exports = {
    presets: [require.resolve('@docusaurus/core/lib/babel/preset')],
};


================================================
File: /website/pydoc-markdown.yml
================================================
loaders:
  - type: python
    search_path: [../src]
processors:
  - type: filter
    skip_empty_modules: true
  - type: crossref
renderer:
  type: docusaurus
  docs_base_path: docs
  relative_output_path: reference
  relative_sidebar_path: sidebar.json
  sidebar_top_level_label: null


================================================
File: /website/build_api_reference.sh
================================================
#!/bin/bash

# On macOS, sed requires a space between -i and '' to specify no backup should be done
# On Linux, sed requires no space between -i and '' to specify no backup should be done
sed_no_backup() {
    if [[ $(uname) = "Darwin" ]]; then
        sed -i '' "$@"
    else
        sed -i'' "$@"
    fi
}

# Create docspec dump of this package's source code through pydoc-markdown
pydoc-markdown --quiet --dump > docspec-dump.jsonl
sed_no_backup "s#${PWD}/..#REPO_ROOT_PLACEHOLDER#g" docspec-dump.jsonl

# Create docpec dump from the right version of the apify-shared package
apify_shared_version=$(python -c "import apify_shared; print(apify_shared.__version__)")
apify_shared_tempdir=$(realpath "$(mktemp -d)")
git clone --quiet https://github.com/apify/apify-shared-python.git "${apify_shared_tempdir}"
cp ./pydoc-markdown.yml "${apify_shared_tempdir}/pydoc-markdown.yml"
sed_no_backup "s#search_path: \[../src\]#search_path: \[./src\]#g" "${apify_shared_tempdir}/pydoc-markdown.yml"

(
    cd "${apify_shared_tempdir}";
    git checkout --quiet "v${apify_shared_version}";
    pydoc-markdown --quiet --dump > ./apify-shared-docspec-dump.jsonl
)

cp "${apify_shared_tempdir}/apify-shared-docspec-dump.jsonl" .
sed_no_backup "s#${apify_shared_tempdir}#REPO_ROOT_PLACEHOLDER#g" apify-shared-docspec-dump.jsonl

rm -rf "${apify_shared_tempdir}"

# Generate import shortcuts from the modules
python generate_module_shortcuts.py

# Transform the docpec dumps into Typedoc-compatible docs tree
node transformDocs.js


================================================
File: /website/docusaurus.config.js
================================================
/* eslint-disable global-require,import/no-extraneous-dependencies */
const { config } = require('@apify/docs-theme');
const { externalLinkProcessor } = require('./tools/utils/externalLink');
const { groupSort } = require('./transformDocs.js');

const { absoluteUrl } = config;

/** @type {Partial<import('@docusaurus/types').DocusaurusConfig>} */
module.exports = {
    title: 'API client for Python | Apify Documentation',
    url: absoluteUrl,
    baseUrl: '/api/client/python',
    trailingSlash: false,
    organizationName: 'apify',
    projectName: 'apify-client-python',
    scripts: ['/js/custom.js'],
    favicon: 'img/favicon.ico',
    onBrokenLinks:
    /** @type {import('@docusaurus/types').ReportingSeverity} */ ('warn'),
    onBrokenMarkdownLinks:
    /** @type {import('@docusaurus/types').ReportingSeverity} */ ('warn'),
    themes: [
        [
            '@apify/docs-theme',
            {
                subNavbar: {
                    title: 'API Client for Python',
                    items: [
                        {
                            to: 'docs',
                            label: 'Docs',
                            position: 'left',
                            activeBaseRegex: '/docs(?!/changelog)',
                        },
                        {
                            to: '/reference',
                            label: 'Reference',
                            position: 'left',
                            activeBaseRegex: '/reference',
                        },
                        {
                            to: 'docs/changelog',
                            label: 'Changelog',
                            position: 'left',
                            activeBaseRegex: '/docs/changelog',
                        },
                        {
                            href: 'https://github.com/apify/apify-client-python',
                            label: 'GitHub',
                            position: 'left',
                        },
                    ],
                },
            },
        ],
    ],
    presets: /** @type {import('@docusaurus/types').PresetConfig[]} */ ([
        [
            '@docusaurus/preset-classic',
            /** @type {import('@docusaurus/preset-classic').Options} */
            ({
                docs: {
                    path: '../docs',
                    sidebarPath: './sidebars.js',
                    rehypePlugins: [externalLinkProcessor],
                    editUrl: 'https://github.com/apify/apify-client-python/blob/master/website/',
                },
            }),
        ],
    ]),
    plugins: [
        [
            '@apify/docusaurus-plugin-typedoc-api',
            {
                projectRoot: '.',
                changelogs: false,
                readmes: false,
                packages: [{ path: '.' }],
                typedocOptions: {
                    excludeExternals: false,
                },
                pathToCurrentVersionTypedocJSON: `${__dirname}/api-typedoc-generated.json`,
                sortSidebar: groupSort,
                routeBasePath: 'reference',
                python: true,
            },
        ],
        ...config.plugins,
    ],
    themeConfig: {
        ...config.themeConfig,
        tableOfContents: {
            ...config.themeConfig.tableOfContents,
            maxHeadingLevel: 5,
        },
    },
    staticDirectories: ['node_modules/@apify/docs-theme/static', 'static'],
};


================================================
File: /website/src/pages/index.module.css
================================================
/**
 * CSS files with the .module.css suffix will be treated as CSS modules
 * and scoped locally.
 */

.buttons {
    display: flex;
    align-items: center;
    justify-content: center;
}

.tagline {
    font-family: 'Lota Grotesque', sans-serif;
    font-size: 64px;
    font-weight: 600;
    line-height: 80px;
    letter-spacing: 0;
    text-align: left;
}

.tagline span {
    color: transparent !important;
}

.relative {
    position: relative;
}

.codeBlock {
    position: absolute;
    top: 40%;
    max-width: 400px;
    width: 100%;
}

.heroBanner {
    padding-top: 100px;
}

.heroBanner h1:nth-child(1) {
    background: linear-gradient(270deg, rgb(235, 40, 75) 0%, rgb(234, 40, 76) 8.07%, rgb(233, 40, 78) 15.54%, rgb(231, 40, 83) 22.5%, rgb(228, 39, 89) 29.04%, rgb(225, 39, 96) 35.26%, rgb(220, 39, 106) 41.25%, rgb(216, 38, 116) 47.1%, rgb(210, 38, 128) 52.9%, rgb(204, 37, 141) 58.75%, rgb(197, 36, 155) 64.74%, rgb(190, 35, 171) 70.96%, rgb(182, 35, 187) 77.5%, rgb(174, 34, 205) 84.46%, rgb(166, 33, 223) 91.93%, rgb(157, 32, 242) 100%),
    linear-gradient(0deg, #41465D, #41465D);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
}

.heroBanner h1:nth-child(2) {
    position: absolute;
    top: 0;
    z-index: 1;
    width: calc(100% - 2rem);
}

.heroBanner h1::selection,
.heroBanner h1 span::selection {
    color: rgb(36, 39, 54) !important;
    -webkit-text-fill-color: rgb(36, 39, 54);
    background: #B4D7FE !important;
    -webkit-background-clip: unset;
    background-clip: unset;
}

html[data-theme='dark'] .heroBanner ::selection {
    color: #fff !important;
    -webkit-text-fill-color: #fff;
    background: #385477 !important;
}

html .heroBanner h2 {
    font-style: normal;
    font-weight: 400;
    font-size: 24px;
    line-height: 40px;
    color: #41465d;
    margin-top: 8px;
    margin-bottom: 24px;
    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', 'Oxygen', 'Ubuntu', 'Cantarell', 'Fira Sans', 'Droid Sans', 'Helvetica Neue', sans-serif;
}

html[data-theme='dark'] .heroBanner h2 {
    color: #b3b8d2;
}

.heroBanner code {
    background: #272c3d;
    padding: 10px 20px;
}

.heroBanner button {
    opacity: 0.4;
    padding: 5px 8px;
    margin-top: -2px;
}

.heroBanner button span {
    width: 16px;
    height: 16px;
    padding: 0;
    margin: 0;
}

.heroBanner code span {
    color: #f2f3fb;
}

.logoBlur {
    position: absolute;
    width: 680px;
    height: 680px;
    top: -120px;
    left: -100px;
    z-index: -1;
}

.heroButtons {
    display: flex;
    align-items: center;
    gap: 1rem;
    margin-bottom: 50px;
}

@media only screen and (max-device-width: 996px) {
    .codeBlock {
        position: relative;
        top: 50px;
    }

    .logoBlur {
        display: none;
    }
}

@media only screen and (max-device-width: 736px) {
    .heroBanner {
        padding-top: 20px;
        padding-bottom: 2rem;
    }

    .tagline {
        font-size: 32px;
        line-height: 48px;
    }

    .tagline br {
        display: none;
    }

    .hideSmall {
        display: none;
    }

    .codeBlock {
        top: 0;
    }
}

@media only screen and (max-device-width: 450px) {
    .codeBlock code {
        font-size: 0.8em;
    }

    .heroButtons {
        flex-direction: column;
        align-items: flex-start !important;
    }

    .heroBanner button {
        opacity: 0;
    }
}

@media only screen and (max-device-width: 350px) {
    .codeBlock code {
        font-size: 0.7em;
    }
}

.tagline span {
    color: var(--ifm-color-primary);
}

.getStarted {
    font-size: 18px;
    line-height: 28px;
    padding: 12px 24px;
    background: #7717b5;
    border-radius: 8px;
    color: white;
    font-weight: 600;
}

.getStarted:hover {
    color: white;
    background: #931ce0;
}

html[data-theme='dark'] .getStarted {
    border-color: #585e76;
}

.try {
    padding-top: 20px;
}

.try, .features {
    color: #41465d;
}

.try > * {
    margin-left: 0;
    margin-right: 0;
}

html[data-theme='dark'] .try,
html[data-theme='dark'] .features {
    color: #b3b8d2;
}

.features > * {
    margin: 2em 0;
}

.bottomLogo {
    height: 40px;
}
/*.bottomLogo path:nth-child(1) {*/
/*    fill: url(#gradient-1) !important;*/
/*    stroke: url(#gradient-1) !important;*/
/*}*/


================================================
File: /website/src/pages/index.js
================================================
import React from 'react';
import clsx from 'clsx';
import Layout from '@theme/Layout';
import Link from '@docusaurus/Link';
import CodeBlock from '@theme/CodeBlock';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import useBaseUrl from '@docusaurus/useBaseUrl';
import styles from './index.module.css';

function Hero() {
    return (
        <header className={clsx('container', styles.heroBanner)}>
            <div className="row padding-horiz--md">
                <div className="col col--7">
                    <div className={clsx(styles.relative, 'row')}>
                        <div className="col">
                            <h1 className={styles.tagline}>
                                Apify API client for Python
                            </h1>
                            <h1 className={styles.tagline}>
                                {/* eslint-disable-next-line max-len */}
                                <span>Apify API client</span> for Python.
                            </h1>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col">
                            <h2></h2>
                            <h2>
                                The Apify API Client for Python is the official library to access Apify API from your Python applications.
                                It provides useful features like automatic retries and convenience functions to improve your experience with the Apify API.
                            </h2>
                        </div>
                    </div>
                    <div className="row">
                        <div className="col">
                            <div className={styles.heroButtons}>
                                <Link to="docs" className={styles.getStarted}>Get Started</Link>
                                <iframe src="https://ghbtns.com/github-btn.html?user=apify&repo=apify-client-python&type=star&count=true&size=large" width="170" height="30" title="GitHub"></iframe>
                            </div>
                        </div>
                    </div>
                </div>
                <div className={clsx(styles.relative, 'col', 'col--5')}>
                    <div className={styles.logoBlur}>
                        <img src={useBaseUrl('img/logo-blur.png')} className={clsx(styles.hideSmall)} />
                    </div>
                    <div className={styles.codeBlock}>
                        <CodeBlock className="language-bash">
                            pip install apify-client
                        </CodeBlock>
                    </div>
                </div>
            </div>
        </header>
    );
}

export default function Home() {
    const { siteConfig } = useDocusaurusContext();
    return (
        <Layout
            description={siteConfig.description}>
            <Hero />
            <div>
                <div className="container">
                    <div className="row padding-horiz--md" >
                        <div className="col col--4">
                            <p style={{ lineHeight: '200%' }}>
                            For example, the Apify API Client for Python makes it easy to run your own Actors or Actors from the <a href='https://apify.com/store'>Apify Store</a>
                                {' '}by simply using the <code>.call()</code> method to start an Actor and wait for it to finish.
                            </p>
                        </div>
                        <div className="col col--8">
                            <CodeBlock language='python'>{`from apify_client import ApifyClient

apify_client = ApifyClient('MY-APIFY-TOKEN')

# Start an Actor and wait for it to finish
actor_call = apify_client.actor('john-doe/my-cool-actor').call()

# Fetch results from the Actor run's default dataset
dataset_items = apify_client.dataset(actor_call['defaultDatasetId']).list_items().items`}</CodeBlock>
                        </div>
                    </div>
                </div>
            </div>
        </Layout>
    );
}


================================================
File: /LICENSE
================================================
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "{}"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2023 Apify Technologies s.r.o.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.


================================================
File: /CONTRIBUTING.md
================================================
# Development

Here you'll find a contributing guide to get started with development.

## Environment

For local development, it is required to have Python 3.9 (or a later version) installed.

We use [Poetry](https://python-poetry.org/) for project management. Install it and set up your IDE accordingly.

## Dependencies

To install this package and its development dependencies, run:

```sh
make install-dev
```

## Code checking

To execute all code checking tools together, run:

```sh
make check-code
```

### Linting

We utilize [ruff](https://docs.astral.sh/ruff/) for linting, which analyzes code for potential issues and enforces consistent style. Refer to `pyproject.toml` for configuration details.

To run linting:

```sh
make lint
```

### Formatting

Our automated code formatting also leverages [ruff](https://docs.astral.sh/ruff/), ensuring uniform style and addressing fixable linting issues. Configuration specifics are outlined in `pyproject.toml`.

To run formatting:

```sh
make format
```

### Type checking

Type checking is handled by [mypy](https://mypy.readthedocs.io/), verifying code against type annotations. Configuration settings can be found in `pyproject.toml`.

To run type checking:

```sh
make type-check
```

### Unit tests

We employ pytest as our testing framework, equipped with various plugins. Check pyproject.toml for configuration details and installed plugins.

We use [pytest](https://docs.pytest.org/) as a testing framework with many plugins. Check `pyproject.toml` for configuration details and installed plugins.

To run unit tests:

```sh
make unit-tests
```

To run unit tests with HTML coverage report:

```sh
make unit-tests-cov
```

## Integration tests

We have integration tests which build and run Actors using the Python SDK on the Apify Platform. To run these tests,
you need to set the `APIFY_TEST_USER_API_TOKEN` environment variable to the API token of the Apify user you want to
use for the tests, and then start them with `make integration-tests`.

If you want to run the integration tests on a different environment than the main Apify Platform, you need to set
the `APIFY_INTEGRATION_TESTS_API_URL` environment variable to the right URL to the Apify API you want to use.

## Documentation

We adhere to the [Google docstring format](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html) for documenting our codebase. Every user-facing class or method is documented. Documentation standards are enforced using [Ruff](https://docs.astral.sh/ruff/).

Our API documentation is generated from these docstrings using [pydoc-markdown](https://pypi.org/project/pydoc-markdown/) with additional post-processing. Markdown files in the `docs/` folder complement the autogenerated content. Final documentation is rendered using [Docusaurus](https://docusaurus.io/) and published to GitHub Pages.

To run the documentation locally, you need to have Node.js version 20 or higher installed. Once you have the correct version of Node.js, follow these steps:

Navigate to the `website/` directory:

```sh
cd website/
```

Enable Corepack, which installs Yarn automatically:

```sh
corepack enable
```

Build the API reference:

```sh
./build_api_reference.sh
```

Install the necessary dependencies:

```sh
yarn
```

Start the project in development mode with Hot Module Replacement (HMR):

```sh
yarn start
```

Or using `make`:

```sh
make run-doc
```

## Release process

Publishing new versions to [PyPI](https://pypi.org/project/apify_client) is automated through GitHub Actions.

- **Beta releases**: On each commit to the master branch, a new beta release is automatically published. The version number is determined based on the latest release and conventional commits. The beta version suffix is incremented by 1 from the last beta release on PyPI.
- **Stable releases**: A stable version release may be created by triggering the `release` GitHub Actions workflow. The version number is determined based on the latest release and conventional commits (`auto` release type), or it may be overriden using the `custom` release type.

### Publishing to PyPI manually

1. **Do not do this unless absolutely necessary.** In all conceivable scenarios, you should use the `release` workflow instead.
2. **Make sure you know what you're doing.**

3. Update the version number:

- Modify the `version` field under `tool.poetry` in `pyproject.toml`.

```toml
[tool.poetry]
name = "apify_client"
version = "x.z.y"
```

4. Generate the distribution archives for the package:

```shell
poetry build
```

5. Set up the PyPI API token for authentication:

```shell
poetry config pypi-token.pypi YOUR_API_TOKEN
```

6. Upload the package to PyPI:

```shell
poetry publish
```


================================================
File: /.markdownlint.yaml
================================================
default: true
line-length:
  line_length: 150
ul-style: dash
no-inline-html: false


================================================
File: /src/apify_client/_http_client.py
================================================
from __future__ import annotations

import gzip
import json as jsonlib
import logging
import os
import sys
from http import HTTPStatus
from importlib import metadata
from typing import TYPE_CHECKING, Any, Callable

import httpx
from apify_shared.utils import ignore_docs, is_content_type_json, is_content_type_text, is_content_type_xml

from apify_client._errors import ApifyApiError, InvalidResponseBodyError, is_retryable_error
from apify_client._logging import log_context, logger_name
from apify_client._utils import retry_with_exp_backoff, retry_with_exp_backoff_async

if TYPE_CHECKING:
    from apify_shared.types import JSONSerializable


DEFAULT_BACKOFF_EXPONENTIAL_FACTOR = 2
DEFAULT_BACKOFF_RANDOM_FACTOR = 1

logger = logging.getLogger(logger_name)


class _BaseHTTPClient:
    @ignore_docs
    def __init__(
        self,
        *,
        token: str | None = None,
        max_retries: int = 8,
        min_delay_between_retries_millis: int = 500,
        timeout_secs: int = 360,
    ) -> None:
        self.max_retries = max_retries
        self.min_delay_between_retries_millis = min_delay_between_retries_millis
        self.timeout_secs = timeout_secs

        headers = {'Accept': 'application/json, */*'}

        workflow_key = os.getenv('APIFY_WORKFLOW_KEY')
        if workflow_key is not None:
            headers['X-Apify-Workflow-Key'] = workflow_key

        is_at_home = 'APIFY_IS_AT_HOME' in os.environ
        python_version = '.'.join([str(x) for x in sys.version_info[:3]])
        client_version = metadata.version('apify-client')

        user_agent = f'ApifyClient/{client_version} ({sys.platform}; Python/{python_version}); isAtHome/{is_at_home}'
        headers['User-Agent'] = user_agent

        if token is not None:
            headers['Authorization'] = f'Bearer {token}'

        self.httpx_client = httpx.Client(headers=headers, follow_redirects=True, timeout=timeout_secs)
        self.httpx_async_client = httpx.AsyncClient(headers=headers, follow_redirects=True, timeout=timeout_secs)

    @staticmethod
    def _maybe_parse_response(response: httpx.Response) -> Any:
        if response.status_code == HTTPStatus.NO_CONTENT:
            return None

        content_type = ''
        if 'content-type' in response.headers:
            content_type = response.headers['content-type'].split(';')[0].strip()

        try:
            if is_content_type_json(content_type):
                return response.json()
            elif is_content_type_xml(content_type) or is_content_type_text(content_type):  # noqa: RET505
                return response.text
            else:
                return response.content
        except ValueError as err:
            raise InvalidResponseBodyError(response) from err

    @staticmethod
    def _parse_params(params: dict | None) -> dict | None:
        if params is None:
            return None

        parsed_params: dict = {}
        for key, value in params.items():
            # Our API needs boolean parameters passed as 0 or 1
            if isinstance(value, bool):
                parsed_params[key] = int(value)
            # Our API needs lists passed as comma-separated strings
            elif isinstance(value, list):
                parsed_params[key] = ','.join(value)
            elif value is not None:
                parsed_params[key] = value

        return parsed_params

    def _prepare_request_call(
        self,
        headers: dict | None = None,
        params: dict | None = None,
        data: Any = None,
        json: JSONSerializable | None = None,
    ) -> tuple[dict, dict | None, Any]:
        if json and data:
            raise ValueError('Cannot pass both "json" and "data" parameters at the same time!')

        if not headers:
            headers = {}

        # dump JSON data to string, so they can be gzipped
        if json:
            data = jsonlib.dumps(json, ensure_ascii=False, allow_nan=False, default=str).encode('utf-8')
            headers['Content-Type'] = 'application/json'

        if isinstance(data, (str, bytes, bytearray)):
            if isinstance(data, str):
                data = data.encode('utf-8')
            data = gzip.compress(data)
            headers['Content-Encoding'] = 'gzip'

        return (
            headers,
            self._parse_params(params),
            data,
        )


class HTTPClient(_BaseHTTPClient):
    def call(
        self,
        *,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: Any = None,
        json: JSONSerializable | None = None,
        stream: bool | None = None,
        parse_response: bool | None = True,
    ) -> httpx.Response:
        log_context.method.set(method)
        log_context.url.set(url)

        if stream and parse_response:
            raise ValueError('Cannot stream response and parse it at the same time!')

        headers, params, content = self._prepare_request_call(headers, params, data, json)

        httpx_client = self.httpx_client

        def _make_request(stop_retrying: Callable, attempt: int) -> httpx.Response:
            log_context.attempt.set(attempt)
            logger.debug('Sending request')
            try:
                request = httpx_client.build_request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    content=content,
                )
                response = httpx_client.send(
                    request=request,
                    stream=stream or False,
                )

                # If response status is < 300, the request was successful, and we can return the result
                if response.status_code < 300:  # noqa: PLR2004
                    logger.debug('Request successful', extra={'status_code': response.status_code})
                    if not stream:
                        _maybe_parsed_body = (
                            self._maybe_parse_response(response) if parse_response else response.content
                        )
                        setattr(response, '_maybe_parsed_body', _maybe_parsed_body)  # noqa: B010

                    return response

            except Exception as e:
                logger.debug('Request threw exception', exc_info=e)
                if not is_retryable_error(e):
                    logger.debug('Exception is not retryable', exc_info=e)
                    stop_retrying()
                raise

            # We want to retry only requests which are server errors (status >= 500) and could resolve on their own,
            # and also retry rate limited requests that throw 429 Too Many Requests errors
            logger.debug('Request unsuccessful', extra={'status_code': response.status_code})
            if response.status_code < 500 and response.status_code != HTTPStatus.TOO_MANY_REQUESTS:  # noqa: PLR2004
                logger.debug('Status code is not retryable', extra={'status_code': response.status_code})
                stop_retrying()
            raise ApifyApiError(response, attempt)

        return retry_with_exp_backoff(
            _make_request,
            max_retries=self.max_retries,
            backoff_base_millis=self.min_delay_between_retries_millis,
            backoff_factor=DEFAULT_BACKOFF_EXPONENTIAL_FACTOR,
            random_factor=DEFAULT_BACKOFF_RANDOM_FACTOR,
        )


class HTTPClientAsync(_BaseHTTPClient):
    async def call(
        self,
        *,
        method: str,
        url: str,
        headers: dict | None = None,
        params: dict | None = None,
        data: Any = None,
        json: JSONSerializable | None = None,
        stream: bool | None = None,
        parse_response: bool | None = True,
    ) -> httpx.Response:
        log_context.method.set(method)
        log_context.url.set(url)

        if stream and parse_response:
            raise ValueError('Cannot stream response and parse it at the same time!')

        headers, params, content = self._prepare_request_call(headers, params, data, json)

        httpx_async_client = self.httpx_async_client

        async def _make_request(stop_retrying: Callable, attempt: int) -> httpx.Response:
            log_context.attempt.set(attempt)
            logger.debug('Sending request')
            try:
                request = httpx_async_client.build_request(
                    method=method,
                    url=url,
                    headers=headers,
                    params=params,
                    content=content,
                )
                response = await httpx_async_client.send(
                    request=request,
                    stream=stream or False,
                )

                # If response status is < 300, the request was successful, and we can return the result
                if response.status_code < 300:  # noqa: PLR2004
                    logger.debug('Request successful', extra={'status_code': response.status_code})
                    if not stream:
                        _maybe_parsed_body = (
                            self._maybe_parse_response(response) if parse_response else response.content
                        )
                        setattr(response, '_maybe_parsed_body', _maybe_parsed_body)  # noqa: B010

                    return response

            except Exception as e:
                logger.debug('Request threw exception', exc_info=e)
                if not is_retryable_error(e):
                    logger.debug('Exception is not retryable', exc_info=e)
                    stop_retrying()
                raise

            # We want to retry only requests which are server errors (status >= 500) and could resolve on their own,
            # and also retry rate limited requests that throw 429 Too Many Requests errors
            logger.debug('Request unsuccessful', extra={'status_code': response.status_code})
            if response.status_code < 500 and response.status_code != HTTPStatus.TOO_MANY_REQUESTS:  # noqa: PLR2004
                logger.debug('Status code is not retryable', extra={'status_code': response.status_code})
                stop_retrying()
            raise ApifyApiError(response, attempt)

        return await retry_with_exp_backoff_async(
            _make_request,
            max_retries=self.max_retries,
            backoff_base_millis=self.min_delay_between_retries_millis,
            backoff_factor=DEFAULT_BACKOFF_EXPONENTIAL_FACTOR,
            random_factor=DEFAULT_BACKOFF_RANDOM_FACTOR,
        )


================================================
File: /src/apify_client/_utils.py
================================================
from __future__ import annotations

import asyncio
import base64
import json
import random
import time
from http import HTTPStatus
from typing import TYPE_CHECKING, Any, Callable, TypeVar, cast

from apify_shared.utils import is_file_or_bytes, maybe_extract_enum_member_value

if TYPE_CHECKING:
    from collections.abc import Awaitable

    from apify_client._errors import ApifyApiError

PARSE_DATE_FIELDS_MAX_DEPTH = 3
PARSE_DATE_FIELDS_KEY_SUFFIX = 'At'

RECORD_NOT_FOUND_EXCEPTION_TYPES = ['record-not-found', 'record-or-token-not-found']

T = TypeVar('T')
StopRetryingType = Callable[[], None]


def to_safe_id(id: str) -> str:
    # Identificators of resources in the API are either in the format `resource_id` or `username/resource_id`.
    # Since the `/` character has a special meaning in URL paths,
    # we replace it with `~` for proper route parsing on the API, where after parsing the URL it's replaced back to `/`.
    return id.replace('/', '~')


def pluck_data(parsed_response: Any) -> dict:
    if isinstance(parsed_response, dict) and 'data' in parsed_response:
        return cast(dict, parsed_response['data'])

    raise ValueError('The "data" property is missing in the response.')


def pluck_data_as_list(parsed_response: Any) -> list:
    if isinstance(parsed_response, dict) and 'data' in parsed_response:
        return cast(list, parsed_response['data'])

    raise ValueError('The "data" property is missing in the response.')


def retry_with_exp_backoff(
    func: Callable[[StopRetryingType, int], T],
    *,
    max_retries: int = 8,
    backoff_base_millis: int = 500,
    backoff_factor: float = 2,
    random_factor: float = 1,
) -> T:
    random_factor = min(max(0, random_factor), 1)
    backoff_factor = min(max(1, backoff_factor), 10)
    swallow = True

    def stop_retrying() -> None:
        nonlocal swallow
        swallow = False

    for attempt in range(1, max_retries + 1):
        try:
            return func(stop_retrying, attempt)
        except Exception:
            if not swallow:
                raise

        random_sleep_factor = random.uniform(1, 1 + random_factor)
        backoff_base_secs = backoff_base_millis / 1000
        backoff_exp_factor = backoff_factor ** (attempt - 1)

        sleep_time_secs = random_sleep_factor * backoff_base_secs * backoff_exp_factor
        time.sleep(sleep_time_secs)

    return func(stop_retrying, max_retries + 1)


async def retry_with_exp_backoff_async(
    async_func: Callable[[StopRetryingType, int], Awaitable[T]],
    *,
    max_retries: int = 8,
    backoff_base_millis: int = 500,
    backoff_factor: float = 2,
    random_factor: float = 1,
) -> T:
    random_factor = min(max(0, random_factor), 1)
    backoff_factor = min(max(1, backoff_factor), 10)
    swallow = True

    def stop_retrying() -> None:
        nonlocal swallow
        swallow = False

    for attempt in range(1, max_retries + 1):
        try:
            return await async_func(stop_retrying, attempt)
        except Exception:
            if not swallow:
                raise

        random_sleep_factor = random.uniform(1, 1 + random_factor)
        backoff_base_secs = backoff_base_millis / 1000
        backoff_exp_factor = backoff_factor ** (attempt - 1)

        sleep_time_secs = random_sleep_factor * backoff_base_secs * backoff_exp_factor
        await asyncio.sleep(sleep_time_secs)

    return await async_func(stop_retrying, max_retries + 1)


def catch_not_found_or_throw(exc: ApifyApiError) -> None:
    is_not_found_status = exc.status_code == HTTPStatus.NOT_FOUND
    is_not_found_type = exc.type in RECORD_NOT_FOUND_EXCEPTION_TYPES
    if not (is_not_found_status and is_not_found_type):
        raise exc


def encode_webhook_list_to_base64(webhooks: list[dict]) -> str:
    """Encode a list of dictionaries representing webhooks to their base64-encoded representation for the API."""
    data = []
    for webhook in webhooks:
        webhook_representation = {
            'eventTypes': [maybe_extract_enum_member_value(event_type) for event_type in webhook['event_types']],
            'requestUrl': webhook['request_url'],
        }
        if 'payload_template' in webhook:
            webhook_representation['payloadTemplate'] = webhook['payload_template']
        data.append(webhook_representation)

    return base64.b64encode(json.dumps(data).encode('utf-8')).decode('ascii')


def encode_key_value_store_record_value(value: Any, content_type: str | None = None) -> tuple[Any, str]:
    if not content_type:
        if is_file_or_bytes(value):
            content_type = 'application/octet-stream'
        elif isinstance(value, str):
            content_type = 'text/plain; charset=utf-8'
        else:
            content_type = 'application/json; charset=utf-8'

    if 'application/json' in content_type and not is_file_or_bytes(value) and not isinstance(value, str):
        value = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False, default=str).encode('utf-8')

    return (value, content_type)


================================================
File: /src/apify_client/consts.py
================================================
from __future__ import annotations

import warnings
from typing import Any

from apify_shared.consts import ActorJobStatus as _ActorJobStatus  # noqa: F401
from apify_shared.consts import ActorSourceType as _ActorSourceType  # noqa: F401
from apify_shared.consts import MetaOrigin as _MetaOrigin  # noqa: F401
from apify_shared.consts import WebhookEventType as _WebhookEventType  # noqa: F401

DEPRECATED_NAMES = [
    'ActorJobStatus',
    'ActorSourceType',
    'MetaOrigin',
    'WebhookEventType',
]


# The following piece of code is highly inspired by the example in https://peps.python.org/pep-0562.
# The else branch is missing intentionally! Check the following discussion for details:
# https://github.com/apify/apify-client-python/pull/132#discussion_r1277294315.
def __getattr__(name: str) -> Any:
    if name in DEPRECATED_NAMES:
        warnings.warn(
            (
                f'Importing "{name}" from "apify_client.consts" is deprecated and will be removed in the future. '
                'Please use "apify_shared" library instead.'
            ),
            category=DeprecationWarning,
            stacklevel=2,
        )
        return globals()[f'_{name}']
    raise AttributeError(f'module {__name__!r} has no attribute {name!r}')


================================================
File: /src/apify_client/__init__.py
================================================
from importlib import metadata

from .client import ApifyClient, ApifyClientAsync

__version__ = metadata.version('apify-client')

__all__ = ['ApifyClient', 'ApifyClientAsync', '__version__']


================================================
File: /src/apify_client/_logging.py
================================================
from __future__ import annotations

import functools
import inspect
import json
import logging
from contextvars import ContextVar
from typing import TYPE_CHECKING, Any, Callable, NamedTuple

# Conditional import only executed when type checking, otherwise we'd get circular dependency issues
if TYPE_CHECKING:
    from apify_client.clients.base.base_client import _BaseBaseClient

# Name of the logger used throughout the library
logger_name = __name__.split('.')[0]

# Logger used throughout the library
logger = logging.getLogger(logger_name)


# Context containing the details of the request and the resource client making the request
class LogContext(NamedTuple):
    attempt: ContextVar[int | None]
    client_method: ContextVar[str | None]
    method: ContextVar[str | None]
    resource_id: ContextVar[str | None]
    url: ContextVar[str | None]


log_context = LogContext(
    attempt=ContextVar('attempt', default=None),
    client_method=ContextVar('client_method', default=None),
    method=ContextVar('method', default=None),
    resource_id=ContextVar('resource_id', default=None),
    url=ContextVar('url', default=None),
)


# Metaclass for resource clients which wraps all their public methods
# With injection of their details to the log context vars
class WithLogDetailsClient(type):
    def __new__(cls, name: str, bases: tuple, attrs: dict) -> WithLogDetailsClient:
        for attr_name, attr_value in attrs.items():
            if not attr_name.startswith('_') and inspect.isfunction(attr_value):
                attrs[attr_name] = _injects_client_details_to_log_context(attr_value)

        return type.__new__(cls, name, bases, attrs)


# Wraps an unbound method so that its call will inject the details
# of the resource client (which is the `self` argument of the method)
# to the log context vars
def _injects_client_details_to_log_context(fun: Callable) -> Callable:
    if inspect.iscoroutinefunction(fun):

        @functools.wraps(fun)
        async def async_wrapper(resource_client: _BaseBaseClient, *args: Any, **kwargs: Any) -> Any:
            log_context.client_method.set(fun.__qualname__)
            log_context.resource_id.set(resource_client.resource_id)

            return await fun(resource_client, *args, **kwargs)

        return async_wrapper
    elif inspect.isasyncgenfunction(fun):  # noqa: RET505

        @functools.wraps(fun)
        async def async_generator_wrapper(resource_client: _BaseBaseClient, *args: Any, **kwargs: Any) -> Any:
            log_context.client_method.set(fun.__qualname__)
            log_context.resource_id.set(resource_client.resource_id)

            async for item in fun(resource_client, *args, **kwargs):
                yield item

        return async_generator_wrapper
    else:

        @functools.wraps(fun)
        def wrapper(resource_client: _BaseBaseClient, *args: Any, **kwargs: Any) -> Any:
            log_context.client_method.set(fun.__qualname__)
            log_context.resource_id.set(resource_client.resource_id)

            return fun(resource_client, *args, **kwargs)

        return wrapper


# A filter which lets every log record through,
# but adds the current logging context to the record
class _ContextInjectingFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.client_method = log_context.client_method.get()
        record.resource_id = log_context.resource_id.get()
        record.method = log_context.method.get()
        record.url = log_context.url.get()
        record.attempt = log_context.attempt.get()
        return True


logger.addFilter(_ContextInjectingFilter())


# Log formatter useful for debugging of the client
# Will print out all the extra fields added to the log record
class _DebugLogFormatter(logging.Formatter):
    empty_record = logging.LogRecord('dummy', 0, 'dummy', 0, 'dummy', None, None)

    # Gets the extra fields from the log record which are not present on an empty record
    def _get_extra_fields(self, record: logging.LogRecord) -> dict:
        extra_fields: dict = {}
        for key, value in record.__dict__.items():
            if key not in self.empty_record.__dict__:
                extra_fields[key] = value  # noqa: PERF403

        return extra_fields

    def format(self, record: logging.LogRecord) -> str:
        extra = self._get_extra_fields(record)

        log_string = super().format(record)
        if extra:
            log_string = f'{log_string} ({json.dumps(extra)})'
        return log_string


================================================
File: /src/apify_client/_errors.py
================================================
from __future__ import annotations

import httpx
from apify_shared.utils import ignore_docs


class ApifyClientError(Exception):
    """Base class for errors specific to the Apify API Client."""


class ApifyApiError(ApifyClientError):
    """Error specific to requests to the Apify API.

    An `ApifyApiError` is thrown for successful HTTP requests that reach the API, but the API responds with
    an error response. Typically, those are rate limit errors and internal errors, which are automatically retried,
    or validation errors, which are thrown immediately, because a correction by the user is needed.
    """

    @ignore_docs
    def __init__(self, response: httpx.Response, attempt: int) -> None:
        """A default constructor.

        Args:
            response: The response to the failed API call.
            attempt: Which attempt was the request that failed.
        """
        self.message: str | None = None
        self.type: str | None = None
        self.data = dict[str, str]()

        self.message = f'Unexpected error: {response.text}'
        try:
            response_data = response.json()
            if 'error' in response_data:
                self.message = response_data['error']['message']
                self.type = response_data['error']['type']
                if 'data' in response_data['error']:
                    self.data = response_data['error']['data']
        except ValueError:
            pass

        super().__init__(self.message)

        self.name = 'ApifyApiError'
        self.status_code = response.status_code
        self.attempt = attempt
        self.http_method = response.request.method

        # TODO: self.client_method   # noqa: TD003
        # TODO: self.original_stack  # noqa: TD003
        # TODO: self.path  # noqa: TD003
        # TODO: self.stack  # noqa: TD003


class InvalidResponseBodyError(ApifyClientError):
    """Error caused by the response body failing to be parsed.

    This error exists for the quite common situation, where only a partial JSON response is received and an attempt
    to parse the JSON throws an error. In most cases this can be resolved by retrying the request. We do that by
    identifying this error in the HTTPClient.
    """

    @ignore_docs
    def __init__(self, response: httpx.Response) -> None:
        """A default constructor.

        Args:
            response: The response which failed to be parsed.
        """
        super().__init__('Response body could not be parsed')

        self.name = 'InvalidResponseBodyError'
        self.code = 'invalid-response-body'
        self.response = response


def is_retryable_error(exc: Exception) -> bool:
    """Check if the given error is retryable."""
    return isinstance(
        exc,
        (
            InvalidResponseBodyError,
            httpx.NetworkError,
            httpx.TimeoutException,
            httpx.RemoteProtocolError,
        ),
    )


================================================
File: /src/apify_client/client.py
================================================
from __future__ import annotations

from apify_shared.utils import ignore_docs

from apify_client._http_client import HTTPClient, HTTPClientAsync
from apify_client.clients import (
    ActorClient,
    ActorClientAsync,
    ActorCollectionClient,
    ActorCollectionClientAsync,
    BuildClient,
    BuildClientAsync,
    BuildCollectionClient,
    BuildCollectionClientAsync,
    DatasetClient,
    DatasetClientAsync,
    DatasetCollectionClient,
    DatasetCollectionClientAsync,
    KeyValueStoreClient,
    KeyValueStoreClientAsync,
    KeyValueStoreCollectionClient,
    KeyValueStoreCollectionClientAsync,
    LogClient,
    LogClientAsync,
    RequestQueueClient,
    RequestQueueClientAsync,
    RequestQueueCollectionClient,
    RequestQueueCollectionClientAsync,
    RunClient,
    RunClientAsync,
    RunCollectionClient,
    RunCollectionClientAsync,
    ScheduleClient,
    ScheduleClientAsync,
    ScheduleCollectionClient,
    ScheduleCollectionClientAsync,
    StoreCollectionClient,
    StoreCollectionClientAsync,
    TaskClient,
    TaskClientAsync,
    TaskCollectionClient,
    TaskCollectionClientAsync,
    UserClient,
    UserClientAsync,
    WebhookClient,
    WebhookClientAsync,
    WebhookCollectionClient,
    WebhookCollectionClientAsync,
    WebhookDispatchClient,
    WebhookDispatchClientAsync,
    WebhookDispatchCollectionClient,
    WebhookDispatchCollectionClientAsync,
)

DEFAULT_API_URL = 'https://api.apify.com'
API_VERSION = 'v2'


class _BaseApifyClient:
    http_client: HTTPClient | HTTPClientAsync

    @ignore_docs
    def __init__(
        self,
        token: str | None = None,
        *,
        api_url: str | None = None,
        max_retries: int | None = 8,
        min_delay_between_retries_millis: int | None = 500,
        timeout_secs: int | None = 360,
    ) -> None:
        """A default constructor.

        Args:
            token: The Apify API token.
            api_url: The URL of the Apify API server to which to connect to. Defaults to https://api.apify.com.
            max_retries: How many times to retry a failed request at most.
            min_delay_between_retries_millis: How long will the client wait between retrying requests
                (increases exponentially from this value).
            timeout_secs: The socket timeout of the HTTP requests sent to the Apify API.
        """
        self.token = token
        api_url = (api_url or DEFAULT_API_URL).rstrip('/')
        self.base_url = f'{api_url}/{API_VERSION}'
        self.max_retries = max_retries or 8
        self.min_delay_between_retries_millis = min_delay_between_retries_millis or 500
        self.timeout_secs = timeout_secs or 360

    def _options(self) -> dict:
        return {
            'root_client': self,
            'base_url': self.base_url,
            'http_client': self.http_client,
        }


class ApifyClient(_BaseApifyClient):
    """The Apify API client."""

    http_client: HTTPClient

    def __init__(
        self,
        token: str | None = None,
        *,
        api_url: str | None = None,
        max_retries: int | None = 8,
        min_delay_between_retries_millis: int | None = 500,
        timeout_secs: int | None = 360,
    ) -> None:
        """A default constructor.

        Args:
            token: The Apify API token.
            api_url: The URL of the Apify API server to which to connect to. Defaults to https://api.apify.com.
            max_retries: How many times to retry a failed request at most.
            min_delay_between_retries_millis: How long will the client wait between retrying requests
                (increases exponentially from this value).
            timeout_secs: The socket timeout of the HTTP requests sent to the Apify API.
        """
        super().__init__(
            token,
            api_url=api_url,
            max_retries=max_retries,
            min_delay_between_retries_millis=min_delay_between_retries_millis,
            timeout_secs=timeout_secs,
        )

        self.http_client = HTTPClient(
            token=token,
            max_retries=self.max_retries,
            min_delay_between_retries_millis=self.min_delay_between_retries_millis,
            timeout_secs=self.timeout_secs,
        )

    def actor(self, actor_id: str) -> ActorClient:
        """Retrieve the sub-client for manipulating a single Actor.

        Args:
            actor_id: ID of the Actor to be manipulated.
        """
        return ActorClient(resource_id=actor_id, **self._options())

    def actors(self) -> ActorCollectionClient:
        """Retrieve the sub-client for manipulating Actors."""
        return ActorCollectionClient(**self._options())

    def build(self, build_id: str) -> BuildClient:
        """Retrieve the sub-client for manipulating a single Actor build.

        Args:
            build_id: ID of the Actor build to be manipulated.
        """
        return BuildClient(resource_id=build_id, **self._options())

    def builds(self) -> BuildCollectionClient:
        """Retrieve the sub-client for querying multiple builds of a user."""
        return BuildCollectionClient(**self._options())

    def run(self, run_id: str) -> RunClient:
        """Retrieve the sub-client for manipulating a single Actor run.

        Args:
            run_id: ID of the Actor run to be manipulated.
        """
        return RunClient(resource_id=run_id, **self._options())

    def runs(self) -> RunCollectionClient:
        """Retrieve the sub-client for querying multiple Actor runs of a user."""
        return RunCollectionClient(**self._options())

    def dataset(self, dataset_id: str) -> DatasetClient:
        """Retrieve the sub-client for manipulating a single dataset.

        Args:
            dataset_id: ID of the dataset to be manipulated.
        """
        return DatasetClient(resource_id=dataset_id, **self._options())

    def datasets(self) -> DatasetCollectionClient:
        """Retrieve the sub-client for manipulating datasets."""
        return DatasetCollectionClient(**self._options())

    def key_value_store(self, key_value_store_id: str) -> KeyValueStoreClient:
        """Retrieve the sub-client for manipulating a single key-value store.

        Args:
            key_value_store_id: ID of the key-value store to be manipulated.
        """
        return KeyValueStoreClient(resource_id=key_value_store_id, **self._options())

    def key_value_stores(self) -> KeyValueStoreCollectionClient:
        """Retrieve the sub-client for manipulating key-value stores."""
        return KeyValueStoreCollectionClient(**self._options())

    def request_queue(self, request_queue_id: str, *, client_key: str | None = None) -> RequestQueueClient:
        """Retrieve the sub-client for manipulating a single request queue.

        Args:
            request_queue_id: ID of the request queue to be manipulated.
            client_key: A unique identifier of the client accessing the request queue.
        """
        return RequestQueueClient(resource_id=request_queue_id, client_key=client_key, **self._options())

    def request_queues(self) -> RequestQueueCollectionClient:
        """Retrieve the sub-client for manipulating request queues."""
        return RequestQueueCollectionClient(**self._options())

    def webhook(self, webhook_id: str) -> WebhookClient:
        """Retrieve the sub-client for manipulating a single webhook.

        Args:
            webhook_id: ID of the webhook to be manipulated.
        """
        return WebhookClient(resource_id=webhook_id, **self._options())

    def webhooks(self) -> WebhookCollectionClient:
        """Retrieve the sub-client for querying multiple webhooks of a user."""
        return WebhookCollectionClient(**self._options())

    def webhook_dispatch(self, webhook_dispatch_id: str) -> WebhookDispatchClient:
        """Retrieve the sub-client for accessing a single webhook dispatch.

        Args:
            webhook_dispatch_id: ID of the webhook dispatch to access.
        """
        return WebhookDispatchClient(resource_id=webhook_dispatch_id, **self._options())

    def webhook_dispatches(self) -> WebhookDispatchCollectionClient:
        """Retrieve the sub-client for querying multiple webhook dispatches of a user."""
        return WebhookDispatchCollectionClient(**self._options())

    def schedule(self, schedule_id: str) -> ScheduleClient:
        """Retrieve the sub-client for manipulating a single schedule.

        Args:
            schedule_id: ID of the schedule to be manipulated.
        """
        return ScheduleClient(resource_id=schedule_id, **self._options())

    def schedules(self) -> ScheduleCollectionClient:
        """Retrieve the sub-client for manipulating schedules."""
        return ScheduleCollectionClient(**self._options())

    def log(self, build_or_run_id: str) -> LogClient:
        """Retrieve the sub-client for retrieving logs.

        Args:
            build_or_run_id: ID of the Actor build or run for which to access the log.
        """
        return LogClient(resource_id=build_or_run_id, **self._options())

    def task(self, task_id: str) -> TaskClient:
        """Retrieve the sub-client for manipulating a single task.

        Args:
            task_id: ID of the task to be manipulated.
        """
        return TaskClient(resource_id=task_id, **self._options())

    def tasks(self) -> TaskCollectionClient:
        """Retrieve the sub-client for manipulating tasks."""
        return TaskCollectionClient(**self._options())

    def user(self, user_id: str | None = None) -> UserClient:
        """Retrieve the sub-client for querying users.

        Args:
            user_id: ID of user to be queried. If None, queries the user belonging to the token supplied to the client.
        """
        return UserClient(resource_id=user_id, **self._options())

    def store(self) -> StoreCollectionClient:
        """Retrieve the sub-client for Apify store."""
        return StoreCollectionClient(**self._options())


class ApifyClientAsync(_BaseApifyClient):
    """The asynchronous version of the Apify API client."""

    http_client: HTTPClientAsync

    def __init__(
        self,
        token: str | None = None,
        *,
        api_url: str | None = None,
        max_retries: int | None = 8,
        min_delay_between_retries_millis: int | None = 500,
        timeout_secs: int | None = 360,
    ) -> None:
        """A default constructor.

        Args:
            token: The Apify API token.
            api_url: The URL of the Apify API server to which to connect to. Defaults to https://api.apify.com.
            max_retries: How many times to retry a failed request at most.
            min_delay_between_retries_millis: How long will the client wait between retrying requests
                (increases exponentially from this value).
            timeout_secs: The socket timeout of the HTTP requests sent to the Apify API.
        """
        super().__init__(
            token,
            api_url=api_url,
            max_retries=max_retries,
            min_delay_between_retries_millis=min_delay_between_retries_millis,
            timeout_secs=timeout_secs,
        )

        self.http_client = HTTPClientAsync(
            token=token,
            max_retries=self.max_retries,
            min_delay_between_retries_millis=self.min_delay_between_retries_millis,
            timeout_secs=self.timeout_secs,
        )

    def actor(self, actor_id: str) -> ActorClientAsync:
        """Retrieve the sub-client for manipulating a single Actor.

        Args:
            actor_id: ID of the Actor to be manipulated.
        """
        return ActorClientAsync(resource_id=actor_id, **self._options())

    def actors(self) -> ActorCollectionClientAsync:
        """Retrieve the sub-client for manipulating Actors."""
        return ActorCollectionClientAsync(**self._options())

    def build(self, build_id: str) -> BuildClientAsync:
        """Retrieve the sub-client for manipulating a single Actor build.

        Args:
            build_id: ID of the Actor build to be manipulated.
        """
        return BuildClientAsync(resource_id=build_id, **self._options())

    def builds(self) -> BuildCollectionClientAsync:
        """Retrieve the sub-client for querying multiple builds of a user."""
        return BuildCollectionClientAsync(**self._options())

    def run(self, run_id: str) -> RunClientAsync:
        """Retrieve the sub-client for manipulating a single Actor run.

        Args:
            run_id: ID of the Actor run to be manipulated.
        """
        return RunClientAsync(resource_id=run_id, **self._options())

    def runs(self) -> RunCollectionClientAsync:
        """Retrieve the sub-client for querying multiple Actor runs of a user."""
        return RunCollectionClientAsync(**self._options())

    def dataset(self, dataset_id: str) -> DatasetClientAsync:
        """Retrieve the sub-client for manipulating a single dataset.

        Args:
            dataset_id: ID of the dataset to be manipulated.
        """
        return DatasetClientAsync(resource_id=dataset_id, **self._options())

    def datasets(self) -> DatasetCollectionClientAsync:
        """Retrieve the sub-client for manipulating datasets."""
        return DatasetCollectionClientAsync(**self._options())

    def key_value_store(self, key_value_store_id: str) -> KeyValueStoreClientAsync:
        """Retrieve the sub-client for manipulating a single key-value store.

        Args:
            key_value_store_id: ID of the key-value store to be manipulated.
        """
        return KeyValueStoreClientAsync(resource_id=key_value_store_id, **self._options())

    def key_value_stores(self) -> KeyValueStoreCollectionClientAsync:
        """Retrieve the sub-client for manipulating key-value stores."""
        return KeyValueStoreCollectionClientAsync(**self._options())

    def request_queue(self, request_queue_id: str, *, client_key: str | None = None) -> RequestQueueClientAsync:
        """Retrieve the sub-client for manipulating a single request queue.

        Args:
            request_queue_id: ID of the request queue to be manipulated.
            client_key: A unique identifier of the client accessing the request queue.
        """
        return RequestQueueClientAsync(resource_id=request_queue_id, client_key=client_key, **self._options())

    def request_queues(self) -> RequestQueueCollectionClientAsync:
        """Retrieve the sub-client for manipulating request queues."""
        return RequestQueueCollectionClientAsync(**self._options())

    def webhook(self, webhook_id: str) -> WebhookClientAsync:
        """Retrieve the sub-client for manipulating a single webhook.

        Args:
            webhook_id: ID of the webhook to be manipulated.
        """
        return WebhookClientAsync(resource_id=webhook_id, **self._options())

    def webhooks(self) -> WebhookCollectionClientAsync:
        """Retrieve the sub-client for querying multiple webhooks of a user."""
        return WebhookCollectionClientAsync(**self._options())

    def webhook_dispatch(self, webhook_dispatch_id: str) -> WebhookDispatchClientAsync:
        """Retrieve the sub-client for accessing a single webhook dispatch.

        Args:
            webhook_dispatch_id: ID of the webhook dispatch to access.
        """
        return WebhookDispatchClientAsync(resource_id=webhook_dispatch_id, **self._options())

    def webhook_dispatches(self) -> WebhookDispatchCollectionClientAsync:
        """Retrieve the sub-client for querying multiple webhook dispatches of a user."""
        return WebhookDispatchCollectionClientAsync(**self._options())

    def schedule(self, schedule_id: str) -> ScheduleClientAsync:
        """Retrieve the sub-client for manipulating a single schedule.

        Args:
            schedule_id: ID of the schedule to be manipulated.
        """
        return ScheduleClientAsync(resource_id=schedule_id, **self._options())

    def schedules(self) -> ScheduleCollectionClientAsync:
        """Retrieve the sub-client for manipulating schedules."""
        return ScheduleCollectionClientAsync(**self._options())

    def log(self, build_or_run_id: str) -> LogClientAsync:
        """Retrieve the sub-client for retrieving logs.

        Args:
            build_or_run_id: ID of the Actor build or run for which to access the log.
        """
        return LogClientAsync(resource_id=build_or_run_id, **self._options())

    def task(self, task_id: str) -> TaskClientAsync:
        """Retrieve the sub-client for manipulating a single task.

        Args:
            task_id: ID of the task to be manipulated.
        """
        return TaskClientAsync(resource_id=task_id, **self._options())

    def tasks(self) -> TaskCollectionClientAsync:
        """Retrieve the sub-client for manipulating tasks."""
        return TaskCollectionClientAsync(**self._options())

    def user(self, user_id: str | None = None) -> UserClientAsync:
        """Retrieve the sub-client for querying users.

        Args:
            user_id: ID of user to be queried. If None, queries the user belonging to the token supplied to the client.
        """
        return UserClientAsync(resource_id=user_id, **self._options())

    def store(self) -> StoreCollectionClientAsync:
        """Retrieve the sub-client for Apify store."""
        return StoreCollectionClientAsync(**self._options())


================================================
File: /src/apify_client/clients/base/base_client.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs

from apify_client._logging import WithLogDetailsClient
from apify_client._utils import to_safe_id

# Conditional import only executed when type checking, otherwise we'd get circular dependency issues
if TYPE_CHECKING:
    from apify_client import ApifyClient, ApifyClientAsync
    from apify_client._http_client import HTTPClient, HTTPClientAsync


class _BaseBaseClient(metaclass=WithLogDetailsClient):
    resource_id: str | None
    url: str
    params: dict
    http_client: HTTPClient | HTTPClientAsync
    root_client: ApifyClient | ApifyClientAsync

    def _url(self, path: str | None = None) -> str:
        if path is not None:
            return f'{self.url}/{path}'
        return self.url

    def _params(self, **kwargs: Any) -> dict:
        return {
            **self.params,
            **kwargs,
        }

    def _sub_resource_init_options(self, **kwargs: Any) -> dict:
        options = {
            'base_url': self.url,
            'http_client': self.http_client,
            'params': self.params,
            'root_client': self.root_client,
        }

        return {
            **options,
            **kwargs,
        }


@ignore_docs
class BaseClient(_BaseBaseClient):
    """Base class for sub-clients."""

    http_client: HTTPClient
    root_client: ApifyClient

    @ignore_docs
    def __init__(
        self,
        *,
        base_url: str,
        root_client: ApifyClient,
        http_client: HTTPClient,
        resource_id: str | None = None,
        resource_path: str,
        params: dict | None = None,
    ) -> None:
        """A default constructor.

        Args:
            base_url: Base URL of the API server.
            root_client: The ApifyClient instance under which this resource client exists.
            http_client: The HTTPClient instance to be used in this client.
            resource_id: ID of the manipulated resource, in case of a single-resource client.
            resource_path: Path to the resource's endpoint on the API server.
            params: Parameters to include in all requests from this client.
        """
        if resource_path.endswith('/'):
            raise ValueError('resource_path must not end with "/"')

        self.base_url = base_url
        self.root_client = root_client
        self.http_client = http_client
        self.params = params or {}
        self.resource_path = resource_path
        self.resource_id = resource_id
        self.url = f'{self.base_url}/{self.resource_path}'
        if self.resource_id is not None:
            self.safe_id = to_safe_id(self.resource_id)
            self.url = f'{self.url}/{self.safe_id}'


@ignore_docs
class BaseClientAsync(_BaseBaseClient):
    """Base class for async sub-clients."""

    http_client: HTTPClientAsync
    root_client: ApifyClientAsync

    @ignore_docs
    def __init__(
        self,
        *,
        base_url: str,
        root_client: ApifyClientAsync,
        http_client: HTTPClientAsync,
        resource_id: str | None = None,
        resource_path: str,
        params: dict | None = None,
    ) -> None:
        """A default constructor.

        Args:
            base_url: Base URL of the API server.
            root_client: The ApifyClientAsync instance under which this resource client exists.
            http_client: The HTTPClientAsync instance to be used in this client.
            resource_id: ID of the manipulated resource, in case of a single-resource client.
            resource_path: Path to the resource's endpoint on the API server.
            params: Parameters to include in all requests from this client.
        """
        if resource_path.endswith('/'):
            raise ValueError('resource_path must not end with "/"')

        self.base_url = base_url
        self.root_client = root_client
        self.http_client = http_client
        self.params = params or {}
        self.resource_path = resource_path
        self.resource_id = resource_id
        self.url = f'{self.base_url}/{self.resource_path}'
        if self.resource_id is not None:
            self.safe_id = to_safe_id(self.resource_id)
            self.url = f'{self.url}/{self.safe_id}'


================================================
File: /src/apify_client/clients/base/__init__.py
================================================
from .actor_job_base_client import ActorJobBaseClient, ActorJobBaseClientAsync
from .base_client import BaseClient, BaseClientAsync
from .resource_client import ResourceClient, ResourceClientAsync
from .resource_collection_client import ResourceCollectionClient, ResourceCollectionClientAsync

__all__ = [
    'ActorJobBaseClient',
    'ActorJobBaseClientAsync',
    'BaseClient',
    'BaseClientAsync',
    'ResourceClient',
    'ResourceClientAsync',
    'ResourceCollectionClient',
    'ResourceCollectionClientAsync',
]


================================================
File: /src/apify_client/clients/base/resource_client.py
================================================
from __future__ import annotations

from apify_shared.utils import ignore_docs, parse_date_fields

from apify_client._errors import ApifyApiError
from apify_client._utils import catch_not_found_or_throw, pluck_data
from apify_client.clients.base.base_client import BaseClient, BaseClientAsync


@ignore_docs
class ResourceClient(BaseClient):
    """Base class for sub-clients manipulating a single resource."""

    def _get(self) -> dict | None:
        try:
            response = self.http_client.call(
                url=self.url,
                method='GET',
                params=self._params(),
            )

            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    def _update(self, updated_fields: dict) -> dict:
        response = self.http_client.call(
            url=self._url(),
            method='PUT',
            params=self._params(),
            json=updated_fields,
        )

        return parse_date_fields(pluck_data(response.json()))

    def _delete(self) -> None:
        try:
            self.http_client.call(
                url=self._url(),
                method='DELETE',
                params=self._params(),
            )

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)


@ignore_docs
class ResourceClientAsync(BaseClientAsync):
    """Base class for async sub-clients manipulating a single resource."""

    async def _get(self) -> dict | None:
        try:
            response = await self.http_client.call(
                url=self.url,
                method='GET',
                params=self._params(),
            )

            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    async def _update(self, updated_fields: dict) -> dict:
        response = await self.http_client.call(
            url=self._url(),
            method='PUT',
            params=self._params(),
            json=updated_fields,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def _delete(self) -> None:
        try:
            await self.http_client.call(
                url=self._url(),
                method='DELETE',
                params=self._params(),
            )

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)


================================================
File: /src/apify_client/clients/base/actor_job_base_client.py
================================================
from __future__ import annotations

import asyncio
import math
import time
from datetime import datetime, timezone

from apify_shared.consts import ActorJobStatus
from apify_shared.utils import ignore_docs, parse_date_fields

from apify_client._errors import ApifyApiError
from apify_client._utils import catch_not_found_or_throw, pluck_data
from apify_client.clients.base.resource_client import ResourceClient, ResourceClientAsync

DEFAULT_WAIT_FOR_FINISH_SEC = 999999

# After how many seconds we give up trying in case job doesn't exist
DEFAULT_WAIT_WHEN_JOB_NOT_EXIST_SEC = 3


@ignore_docs
class ActorJobBaseClient(ResourceClient):
    """Base sub-client class for Actor runs and Actor builds."""

    def _wait_for_finish(self, wait_secs: int | None = None) -> dict | None:
        started_at = datetime.now(timezone.utc)
        should_repeat = True
        job: dict | None = None
        seconds_elapsed = 0

        while should_repeat:
            wait_for_finish = DEFAULT_WAIT_FOR_FINISH_SEC
            if wait_secs is not None:
                wait_for_finish = wait_secs - seconds_elapsed

            try:
                response = self.http_client.call(
                    url=self._url(),
                    method='GET',
                    params=self._params(waitForFinish=wait_for_finish),
                )
                job = parse_date_fields(pluck_data(response.json()))

                seconds_elapsed = math.floor((datetime.now(timezone.utc) - started_at).total_seconds())
                if ActorJobStatus(job['status']).is_terminal or (
                    wait_secs is not None and seconds_elapsed >= wait_secs
                ):
                    should_repeat = False

                if not should_repeat:
                    # Early return here so that we avoid the sleep below if not needed
                    return job

            except ApifyApiError as exc:
                catch_not_found_or_throw(exc)

                # If there are still not found errors after DEFAULT_WAIT_WHEN_JOB_NOT_EXIST_SEC, we give up
                # and return None. In such case, the requested record probably really doesn't exist.
                if seconds_elapsed > DEFAULT_WAIT_WHEN_JOB_NOT_EXIST_SEC:
                    return None

            # It might take some time for database replicas to get up-to-date so sleep a bit before retrying
            time.sleep(0.25)

        return job

    def _abort(self, gracefully: bool | None = None) -> dict:
        response = self.http_client.call(
            url=self._url('abort'),
            method='POST',
            params=self._params(gracefully=gracefully),
        )
        return parse_date_fields(pluck_data(response.json()))


@ignore_docs
class ActorJobBaseClientAsync(ResourceClientAsync):
    """Base async sub-client class for Actor runs and Actor builds."""

    async def _wait_for_finish(self, wait_secs: int | None = None) -> dict | None:
        started_at = datetime.now(timezone.utc)
        should_repeat = True
        job: dict | None = None
        seconds_elapsed = 0

        while should_repeat:
            wait_for_finish = DEFAULT_WAIT_FOR_FINISH_SEC
            if wait_secs is not None:
                wait_for_finish = wait_secs - seconds_elapsed

            try:
                response = await self.http_client.call(
                    url=self._url(),
                    method='GET',
                    params=self._params(waitForFinish=wait_for_finish),
                )
                job = parse_date_fields(pluck_data(response.json()))

                seconds_elapsed = math.floor((datetime.now(timezone.utc) - started_at).total_seconds())
                if ActorJobStatus(job['status']).is_terminal or (
                    wait_secs is not None and seconds_elapsed >= wait_secs
                ):
                    should_repeat = False

                if not should_repeat:
                    # Early return here so that we avoid the sleep below if not needed
                    return job

            except ApifyApiError as exc:
                catch_not_found_or_throw(exc)

                # If there are still not found errors after DEFAULT_WAIT_WHEN_JOB_NOT_EXIST_SEC, we give up
                # and return None. In such case, the requested record probably really doesn't exist.
                if seconds_elapsed > DEFAULT_WAIT_WHEN_JOB_NOT_EXIST_SEC:
                    return None

            # It might take some time for database replicas to get up-to-date so sleep a bit before retrying
            await asyncio.sleep(0.25)

        return job

    async def _abort(self, gracefully: bool | None = None) -> dict:
        response = await self.http_client.call(
            url=self._url('abort'),
            method='POST',
            params=self._params(gracefully=gracefully),
        )
        return parse_date_fields(pluck_data(response.json()))


================================================
File: /src/apify_client/clients/base/resource_collection_client.py
================================================
from __future__ import annotations

from typing import Any

from apify_shared.models import ListPage
from apify_shared.utils import ignore_docs, parse_date_fields

from apify_client._utils import pluck_data
from apify_client.clients.base.base_client import BaseClient, BaseClientAsync


@ignore_docs
class ResourceCollectionClient(BaseClient):
    """Base class for sub-clients manipulating a resource collection."""

    def _list(self, **kwargs: Any) -> ListPage:
        response = self.http_client.call(
            url=self._url(),
            method='GET',
            params=self._params(**kwargs),
        )

        return ListPage(parse_date_fields(pluck_data(response.json())))

    def _create(self, resource: dict) -> dict:
        response = self.http_client.call(
            url=self._url(),
            method='POST',
            params=self._params(),
            json=resource,
        )

        return parse_date_fields(pluck_data(response.json()))

    def _get_or_create(self, name: str | None = None, resource: dict | None = None) -> dict:
        response = self.http_client.call(
            url=self._url(),
            method='POST',
            params=self._params(name=name),
            json=resource,
        )

        return parse_date_fields(pluck_data(response.json()))


@ignore_docs
class ResourceCollectionClientAsync(BaseClientAsync):
    """Base class for async sub-clients manipulating a resource collection."""

    async def _list(self, **kwargs: Any) -> ListPage:
        response = await self.http_client.call(
            url=self._url(),
            method='GET',
            params=self._params(**kwargs),
        )

        return ListPage(parse_date_fields(pluck_data(response.json())))

    async def _create(self, resource: dict) -> dict:
        response = await self.http_client.call(
            url=self._url(),
            method='POST',
            params=self._params(),
            json=resource,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def _get_or_create(
        self,
        name: str | None = None,
        resource: dict | None = None,
    ) -> dict:
        response = await self.http_client.call(
            url=self._url(),
            method='POST',
            params=self._params(name=name),
            json=resource,
        )

        return parse_date_fields(pluck_data(response.json()))


================================================
File: /src/apify_client/clients/__init__.py
================================================
from .base import (
    ActorJobBaseClient,
    ActorJobBaseClientAsync,
    BaseClient,
    BaseClientAsync,
    ResourceClient,
    ResourceClientAsync,
    ResourceCollectionClient,
    ResourceCollectionClientAsync,
)
from .resource_clients import (
    ActorClient,
    ActorClientAsync,
    ActorCollectionClient,
    ActorCollectionClientAsync,
    ActorEnvVarClient,
    ActorEnvVarClientAsync,
    ActorEnvVarCollectionClient,
    ActorEnvVarCollectionClientAsync,
    ActorVersionClient,
    ActorVersionClientAsync,
    ActorVersionCollectionClient,
    ActorVersionCollectionClientAsync,
    BuildClient,
    BuildClientAsync,
    BuildCollectionClient,
    BuildCollectionClientAsync,
    DatasetClient,
    DatasetClientAsync,
    DatasetCollectionClient,
    DatasetCollectionClientAsync,
    KeyValueStoreClient,
    KeyValueStoreClientAsync,
    KeyValueStoreCollectionClient,
    KeyValueStoreCollectionClientAsync,
    LogClient,
    LogClientAsync,
    RequestQueueClient,
    RequestQueueClientAsync,
    RequestQueueCollectionClient,
    RequestQueueCollectionClientAsync,
    RunClient,
    RunClientAsync,
    RunCollectionClient,
    RunCollectionClientAsync,
    ScheduleClient,
    ScheduleClientAsync,
    ScheduleCollectionClient,
    ScheduleCollectionClientAsync,
    StoreCollectionClient,
    StoreCollectionClientAsync,
    TaskClient,
    TaskClientAsync,
    TaskCollectionClient,
    TaskCollectionClientAsync,
    UserClient,
    UserClientAsync,
    WebhookClient,
    WebhookClientAsync,
    WebhookCollectionClient,
    WebhookCollectionClientAsync,
    WebhookDispatchClient,
    WebhookDispatchClientAsync,
    WebhookDispatchCollectionClient,
    WebhookDispatchCollectionClientAsync,
)

__all__ = [
    'ActorClient',
    'ActorClientAsync',
    'ActorCollectionClient',
    'ActorCollectionClientAsync',
    'ActorEnvVarClient',
    'ActorEnvVarClientAsync',
    'ActorEnvVarCollectionClient',
    'ActorEnvVarCollectionClientAsync',
    'ActorJobBaseClient',
    'ActorJobBaseClientAsync',
    'ActorVersionClient',
    'ActorVersionClientAsync',
    'ActorVersionCollectionClient',
    'ActorVersionCollectionClientAsync',
    'BaseClient',
    'BaseClientAsync',
    'BuildClient',
    'BuildClientAsync',
    'BuildCollectionClient',
    'BuildCollectionClientAsync',
    'DatasetClient',
    'DatasetClientAsync',
    'DatasetCollectionClient',
    'DatasetCollectionClientAsync',
    'KeyValueStoreClient',
    'KeyValueStoreClientAsync',
    'KeyValueStoreCollectionClient',
    'KeyValueStoreCollectionClientAsync',
    'LogClient',
    'LogClientAsync',
    'RequestQueueClient',
    'RequestQueueClientAsync',
    'RequestQueueCollectionClient',
    'RequestQueueCollectionClientAsync',
    'ResourceClient',
    'ResourceClientAsync',
    'ResourceCollectionClient',
    'ResourceCollectionClientAsync',
    'RunClient',
    'RunClientAsync',
    'RunCollectionClient',
    'RunCollectionClientAsync',
    'ScheduleClient',
    'ScheduleClientAsync',
    'ScheduleCollectionClient',
    'ScheduleCollectionClientAsync',
    'StoreCollectionClient',
    'StoreCollectionClientAsync',
    'TaskClient',
    'TaskClientAsync',
    'TaskCollectionClient',
    'TaskCollectionClientAsync',
    'UserClient',
    'UserClientAsync',
    'WebhookClient',
    'WebhookClientAsync',
    'WebhookCollectionClient',
    'WebhookCollectionClientAsync',
    'WebhookDispatchClient',
    'WebhookDispatchClientAsync',
    'WebhookDispatchCollectionClient',
    'WebhookDispatchCollectionClientAsync',
]


================================================
File: /src/apify_client/clients/resource_clients/webhook.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import (
    filter_out_none_values_recursively,
    ignore_docs,
    maybe_extract_enum_member_value,
    parse_date_fields,
)

from apify_client._errors import ApifyApiError
from apify_client._utils import catch_not_found_or_throw, pluck_data
from apify_client.clients.base import ResourceClient, ResourceClientAsync
from apify_client.clients.resource_clients.webhook_dispatch_collection import (
    WebhookDispatchCollectionClient,
    WebhookDispatchCollectionClientAsync,
)

if TYPE_CHECKING:
    from apify_shared.consts import WebhookEventType


def get_webhook_representation(
    *,
    event_types: list[WebhookEventType] | None = None,
    request_url: str | None = None,
    payload_template: str | None = None,
    headers_template: str | None = None,
    actor_id: str | None = None,
    actor_task_id: str | None = None,
    actor_run_id: str | None = None,
    ignore_ssl_errors: bool | None = None,
    do_not_retry: bool | None = None,
    idempotency_key: str | None = None,
    is_ad_hoc: bool | None = None,
) -> dict:
    """Prepare webhook dictionary representation for clients."""
    webhook: dict = {
        'requestUrl': request_url,
        'payloadTemplate': payload_template,
        'headersTemplate': headers_template,
        'ignoreSslErrors': ignore_ssl_errors,
        'doNotRetry': do_not_retry,
        'idempotencyKey': idempotency_key,
        'isAdHoc': is_ad_hoc,
        'condition': {
            'actorRunId': actor_run_id,
            'actorTaskId': actor_task_id,
            'actorId': actor_id,
        },
    }

    if actor_run_id is not None:
        webhook['isAdHoc'] = True

    if event_types is not None:
        webhook['eventTypes'] = [maybe_extract_enum_member_value(event_type) for event_type in event_types]

    return webhook


class WebhookClient(ResourceClient):
    """Sub-client for manipulating a single webhook."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhooks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def get(self) -> dict | None:
        """Retrieve the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/get-webhook

        Returns:
            The retrieved webhook, or None if it does not exist.
        """
        return self._get()

    def update(
        self,
        *,
        event_types: list[WebhookEventType] | None = None,
        request_url: str | None = None,
        payload_template: str | None = None,
        headers_template: str | None = None,
        actor_id: str | None = None,
        actor_task_id: str | None = None,
        actor_run_id: str | None = None,
        ignore_ssl_errors: bool | None = None,
        do_not_retry: bool | None = None,
        is_ad_hoc: bool | None = None,
    ) -> dict:
        """Update the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/update-webhook

        Args:
            event_types: List of event types that should trigger the webhook. At least one is required.
            request_url: URL that will be invoked once the webhook is triggered.
            payload_template: Specification of the payload that will be sent to request_url.
            headers_template: Headers that will be sent to the request_url.
            actor_id: Id of the Actor whose runs should trigger the webhook.
            actor_task_id: Id of the Actor task whose runs should trigger the webhook.
            actor_run_id: Id of the Actor run which should trigger the webhook.
            ignore_ssl_errors: Whether the webhook should ignore SSL errors returned by request_url.
            do_not_retry: Whether the webhook should retry sending the payload to request_url upon failure.
            is_ad_hoc: Set to True if you want the webhook to be triggered only the first time the condition
                is fulfilled. Only applicable when actor_run_id is filled.

        Returns:
            The updated webhook.
        """
        webhook_representation = get_webhook_representation(
            event_types=event_types,
            request_url=request_url,
            payload_template=payload_template,
            headers_template=headers_template,
            actor_id=actor_id,
            actor_task_id=actor_task_id,
            actor_run_id=actor_run_id,
            ignore_ssl_errors=ignore_ssl_errors,
            do_not_retry=do_not_retry,
            is_ad_hoc=is_ad_hoc,
        )

        return self._update(filter_out_none_values_recursively(webhook_representation))

    def delete(self) -> None:
        """Delete the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/delete-webhook
        """
        return self._delete()

    def test(self) -> dict | None:
        """Test a webhook.

        Creates a webhook dispatch with a dummy payload.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-test/test-webhook

        Returns:
            The webhook dispatch created by the test.
        """
        try:
            response = self.http_client.call(
                url=self._url('test'),
                method='POST',
                params=self._params(),
            )

            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    def dispatches(self) -> WebhookDispatchCollectionClient:
        """Get dispatches of the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/dispatches-collection/get-collection

        Returns:
            A client allowing access to dispatches of this webhook using its list method.
        """
        return WebhookDispatchCollectionClient(
            **self._sub_resource_init_options(resource_path='dispatches'),
        )


class WebhookClientAsync(ResourceClientAsync):
    """Async sub-client for manipulating a single webhook."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhooks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def get(self) -> dict | None:
        """Retrieve the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/get-webhook

        Returns:
            The retrieved webhook, or None if it does not exist.
        """
        return await self._get()

    async def update(
        self,
        *,
        event_types: list[WebhookEventType] | None = None,
        request_url: str | None = None,
        payload_template: str | None = None,
        headers_template: str | None = None,
        actor_id: str | None = None,
        actor_task_id: str | None = None,
        actor_run_id: str | None = None,
        ignore_ssl_errors: bool | None = None,
        do_not_retry: bool | None = None,
        is_ad_hoc: bool | None = None,
    ) -> dict:
        """Update the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/update-webhook

        Args:
            event_types: List of event types that should trigger the webhook. At least one is required.
            request_url: URL that will be invoked once the webhook is triggered.
            payload_template: Specification of the payload that will be sent to request_url.
            headers_template: Headers that will be sent to the request_url.
            actor_id: Id of the Actor whose runs should trigger the webhook.
            actor_task_id: Id of the Actor task whose runs should trigger the webhook.
            actor_run_id: Id of the Actor run which should trigger the webhook.
            ignore_ssl_errors: Whether the webhook should ignore SSL errors returned by request_url.
            do_not_retry: Whether the webhook should retry sending the payload to request_url upon failure.
            is_ad_hoc: Set to True if you want the webhook to be triggered only the first time the condition
                is fulfilled. Only applicable when actor_run_id is filled.

        Returns:
            The updated webhook.
        """
        webhook_representation = get_webhook_representation(
            event_types=event_types,
            request_url=request_url,
            payload_template=payload_template,
            headers_template=headers_template,
            actor_id=actor_id,
            actor_task_id=actor_task_id,
            actor_run_id=actor_run_id,
            ignore_ssl_errors=ignore_ssl_errors,
            do_not_retry=do_not_retry,
            is_ad_hoc=is_ad_hoc,
        )

        return await self._update(filter_out_none_values_recursively(webhook_representation))

    async def delete(self) -> None:
        """Delete the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/delete-webhook
        """
        return await self._delete()

    async def test(self) -> dict | None:
        """Test a webhook.

        Creates a webhook dispatch with a dummy payload.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-test/test-webhook

        Returns:
            The webhook dispatch created by the test.
        """
        try:
            response = await self.http_client.call(
                url=self._url('test'),
                method='POST',
                params=self._params(),
            )

            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    def dispatches(self) -> WebhookDispatchCollectionClientAsync:
        """Get dispatches of the webhook.

        https://docs.apify.com/api/v2#/reference/webhooks/dispatches-collection/get-collection

        Returns:
            A client allowing access to dispatches of this webhook using its list method.
        """
        return WebhookDispatchCollectionClientAsync(
            **self._sub_resource_init_options(resource_path='dispatches'),
        )


================================================
File: /src/apify_client/clients/resource_clients/build.py
================================================
from __future__ import annotations

from typing import Any

from apify_shared.utils import ignore_docs

from apify_client.clients.base import ActorJobBaseClient, ActorJobBaseClientAsync
from apify_client.clients.resource_clients.log import LogClient, LogClientAsync


class BuildClient(ActorJobBaseClient):
    """Sub-client for manipulating a single Actor build."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-builds')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def get(self) -> dict | None:
        """Return information about the Actor build.

        https://docs.apify.com/api/v2#/reference/actor-builds/build-object/get-build

        Returns:
            The retrieved Actor build data.
        """
        return self._get()

    def delete(self) -> None:
        """Delete the build.

        https://docs.apify.com/api/v2#/reference/actor-builds/delete-build/delete-build
        """
        return self._delete()

    def abort(self) -> dict:
        """Abort the Actor build which is starting or currently running and return its details.

        https://docs.apify.com/api/v2#/reference/actor-builds/abort-build/abort-build

        Returns:
            The data of the aborted Actor build.
        """
        return self._abort()

    def wait_for_finish(self, *, wait_secs: int | None = None) -> dict | None:
        """Wait synchronously until the build finishes or the server times out.

        Args:
            wait_secs: How long does the client wait for build to finish. None for indefinite.

        Returns:
            The Actor build data. If the status on the object is not one of the terminal statuses (SUCEEDED, FAILED,
                TIMED_OUT, ABORTED), then the build has not yet finished.
        """
        return self._wait_for_finish(wait_secs=wait_secs)

    def log(self) -> LogClient:
        """Get the client for the log of the Actor build.

        https://docs.apify.com/api/v2/#/reference/actor-builds/build-log/get-log

        Returns:
            A client allowing access to the log of this Actor build.
        """
        return LogClient(
            **self._sub_resource_init_options(resource_path='log'),
        )


class BuildClientAsync(ActorJobBaseClientAsync):
    """Async sub-client for manipulating a single Actor build."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-builds')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def get(self) -> dict | None:
        """Return information about the Actor build.

        https://docs.apify.com/api/v2#/reference/actor-builds/build-object/get-build

        Returns:
            The retrieved Actor build data.
        """
        return await self._get()

    async def abort(self) -> dict:
        """Abort the Actor build which is starting or currently running and return its details.

        https://docs.apify.com/api/v2#/reference/actor-builds/abort-build/abort-build

        Returns:
            The data of the aborted Actor build.
        """
        return await self._abort()

    async def delete(self) -> None:
        """Delete the build.

        https://docs.apify.com/api/v2#/reference/actor-builds/delete-build/delete-build
        """
        return await self._delete()

    async def wait_for_finish(self, *, wait_secs: int | None = None) -> dict | None:
        """Wait synchronously until the build finishes or the server times out.

        Args:
            wait_secs: How long does the client wait for build to finish. None for indefinite.

        Returns:
            The Actor build data. If the status on the object is not one of the terminal statuses (SUCEEDED, FAILED,
                TIMED_OUT, ABORTED), then the build has not yet finished.
        """
        return await self._wait_for_finish(wait_secs=wait_secs)

    def log(self) -> LogClientAsync:
        """Get the client for the log of the Actor build.

        https://docs.apify.com/api/v2/#/reference/actor-builds/build-log/get-log

        Returns:
            A client allowing access to the log of this Actor build.
        """
        return LogClientAsync(
            **self._sub_resource_init_options(resource_path='log'),
        )


================================================
File: /src/apify_client/clients/resource_clients/schedule_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync
from apify_client.clients.resource_clients.schedule import _get_schedule_representation

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class ScheduleCollectionClient(ResourceCollectionClient):
    """Sub-client for manipulating schedules."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'schedules')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available schedules.

        https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/get-list-of-schedules

        Args:
            limit: How many schedules to retrieve.
            offset: What schedules to include as first when retrieving the list.
            desc: Whether to sort the schedules in descending order based on their modification date.

        Returns:
            The list of available schedules matching the specified filters.
        """
        return self._list(limit=limit, offset=offset, desc=desc)

    def create(
        self,
        *,
        cron_expression: str,
        is_enabled: bool,
        is_exclusive: bool,
        name: str | None = None,
        actions: list[dict] | None = None,  # type: ignore[valid-type]
        description: str | None = None,
        timezone: str | None = None,
        title: str | None = None,
    ) -> dict:
        """Create a new schedule.

        https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/create-schedule

        Args:
            cron_expression: The cron expression used by this schedule.
            is_enabled: True if the schedule should be enabled.
            is_exclusive: When set to true, don't start Actor or Actor task if it's still running from the previous
                schedule.
            name: The name of the schedule to create.
            actions: Actors or tasks that should be run on this schedule. See the API documentation for exact structure.
            description: Description of this schedule.
            timezone: Timezone in which your cron expression runs (TZ database name from
                https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
            title: Title of this schedule.

        Returns:
            The created schedule.
        """
        if not actions:
            actions = []

        schedule_representation = _get_schedule_representation(
            cron_expression=cron_expression,
            is_enabled=is_enabled,
            is_exclusive=is_exclusive,
            name=name,
            actions=actions,
            description=description,
            timezone=timezone,
            title=title,
        )

        return self._create(filter_out_none_values_recursively(schedule_representation))


class ScheduleCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for manipulating schedules."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'schedules')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available schedules.

        https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/get-list-of-schedules

        Args:
            limit: How many schedules to retrieve.
            offset: What schedules to include as first when retrieving the list.
            desc: Whether to sort the schedules in descending order based on their modification date.

        Returns:
            The list of available schedules matching the specified filters.
        """
        return await self._list(limit=limit, offset=offset, desc=desc)

    async def create(
        self,
        *,
        cron_expression: str,
        is_enabled: bool,
        is_exclusive: bool,
        name: str | None = None,
        actions: list[dict] | None = None,  # type: ignore[valid-type]
        description: str | None = None,
        timezone: str | None = None,
        title: str | None = None,
    ) -> dict:
        """Create a new schedule.

        https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/create-schedule

        Args:
            cron_expression: The cron expression used by this schedule.
            is_enabled: True if the schedule should be enabled.
            is_exclusive: When set to true, don't start Actor or Actor task if it's still running from the previous
                schedule.
            name: The name of the schedule to create.
            actions: Actors or tasks that should be run on this schedule. See the API documentation for exact structure.
            description: Description of this schedule.
            timezone: Timezone in which your cron expression runs (TZ database name from
                https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).
            title: Title of this schedule.

        Returns:
            The created schedule.
        """
        if not actions:
            actions = []

        schedule_representation = _get_schedule_representation(
            cron_expression=cron_expression,
            is_enabled=is_enabled,
            is_exclusive=is_exclusive,
            name=name,
            actions=actions,
            description=description,
            timezone=timezone,
            title=title,
        )

        return await self._create(filter_out_none_values_recursively(schedule_representation))


================================================
File: /src/apify_client/clients/resource_clients/actor_version.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs, maybe_extract_enum_member_value

from apify_client.clients.base import ResourceClient, ResourceClientAsync
from apify_client.clients.resource_clients.actor_env_var import ActorEnvVarClient, ActorEnvVarClientAsync
from apify_client.clients.resource_clients.actor_env_var_collection import (
    ActorEnvVarCollectionClient,
    ActorEnvVarCollectionClientAsync,
)

if TYPE_CHECKING:
    from apify_shared.consts import ActorSourceType


def _get_actor_version_representation(
    *,
    version_number: str | None = None,
    build_tag: str | None = None,
    env_vars: list[dict] | None = None,
    apply_env_vars_to_build: bool | None = None,
    source_type: ActorSourceType | None = None,
    source_files: list[dict] | None = None,
    git_repo_url: str | None = None,
    tarball_url: str | None = None,
    github_gist_url: str | None = None,
) -> dict:
    return {
        'versionNumber': version_number,
        'buildTag': build_tag,
        'envVars': env_vars,
        'applyEnvVarsToBuild': apply_env_vars_to_build,
        'sourceType': maybe_extract_enum_member_value(source_type),
        'sourceFiles': source_files,
        'gitRepoUrl': git_repo_url,
        'tarballUrl': tarball_url,
        'gitHubGistUrl': github_gist_url,
    }


class ActorVersionClient(ResourceClient):
    """Sub-client for manipulating a single Actor version."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'versions')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def get(self) -> dict | None:
        """Return information about the Actor version.

        https://docs.apify.com/api/v2#/reference/actors/version-object/get-version

        Returns:
            The retrieved Actor version data.
        """
        return self._get()

    def update(
        self,
        *,
        build_tag: str | None = None,
        env_vars: list[dict] | None = None,
        apply_env_vars_to_build: bool | None = None,
        source_type: ActorSourceType | None = None,
        source_files: list[dict] | None = None,
        git_repo_url: str | None = None,
        tarball_url: str | None = None,
        github_gist_url: str | None = None,
    ) -> dict:
        """Update the Actor version with specified fields.

        https://docs.apify.com/api/v2#/reference/actors/version-object/update-version

        Args:
            build_tag: Tag that is automatically set to the latest successful build of the current version.
            env_vars: Environment variables that will be available to the Actor run process, and optionally
                also to the build process. See the API docs for their exact structure.
            apply_env_vars_to_build: Whether the environment variables specified for the Actor run will also
                be set to the Actor build process.
            source_type: What source type is the Actor version using.
            source_files: Source code comprised of multiple files, each an item of the array. Required when
                `source_type` is `ActorSourceType.SOURCE_FILES`. See the API docs for the exact structure.
            git_repo_url: The URL of a Git repository from which the source code will be cloned.
                Required when `source_type` is `ActorSourceType.GIT_REPO`.
            tarball_url: The URL of a tarball or a zip archive from which the source code will be downloaded.
                Required when `source_type` is `ActorSourceType.TARBALL`.
            github_gist_url: The URL of a GitHub Gist from which the source will be downloaded.
                Required when `source_type` is `ActorSourceType.GITHUB_GIST`.

        Returns:
            The updated Actor version.
        """
        actor_version_representation = _get_actor_version_representation(
            build_tag=build_tag,
            env_vars=env_vars,
            apply_env_vars_to_build=apply_env_vars_to_build,
            source_type=source_type,
            source_files=source_files,
            git_repo_url=git_repo_url,
            tarball_url=tarball_url,
            github_gist_url=github_gist_url,
        )

        return self._update(filter_out_none_values_recursively(actor_version_representation))

    def delete(self) -> None:
        """Delete the Actor version.

        https://docs.apify.com/api/v2#/reference/actors/version-object/delete-version
        """
        return self._delete()

    def env_vars(self) -> ActorEnvVarCollectionClient:
        """Retrieve a client for the environment variables of this Actor version."""
        return ActorEnvVarCollectionClient(**self._sub_resource_init_options())

    def env_var(self, env_var_name: str) -> ActorEnvVarClient:
        """Retrieve the client for the specified environment variable of this Actor version.

        Args:
            env_var_name: The name of the environment variable for which to retrieve the resource client.

        Returns:
            The resource client for the specified Actor environment variable.
        """
        return ActorEnvVarClient(**self._sub_resource_init_options(resource_id=env_var_name))


class ActorVersionClientAsync(ResourceClientAsync):
    """Async sub-client for manipulating a single Actor version."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'versions')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def get(self) -> dict | None:
        """Return information about the Actor version.

        https://docs.apify.com/api/v2#/reference/actors/version-object/get-version

        Returns:
            The retrieved Actor version data.
        """
        return await self._get()

    async def update(
        self,
        *,
        build_tag: str | None = None,
        env_vars: list[dict] | None = None,
        apply_env_vars_to_build: bool | None = None,
        source_type: ActorSourceType | None = None,
        source_files: list[dict] | None = None,
        git_repo_url: str | None = None,
        tarball_url: str | None = None,
        github_gist_url: str | None = None,
    ) -> dict:
        """Update the Actor version with specified fields.

        https://docs.apify.com/api/v2#/reference/actors/version-object/update-version

        Args:
            build_tag: Tag that is automatically set to the latest successful build of the current version.
            env_vars: Environment variables that will be available to the Actor run process, and optionally
                also to the build process. See the API docs for their exact structure.
            apply_env_vars_to_build: Whether the environment variables specified for the Actor run will also
                be set to the Actor build process.
            source_type: What source type is the Actor version using.
            source_files: Source code comprised of multiple files, each an item of the array. Required when
                `source_type` is `ActorSourceType.SOURCE_FILES`. See the API docs for the exact structure.
            git_repo_url: The URL of a Git repository from which the source code will be cloned.
                Required when `source_type` is `ActorSourceType.GIT_REPO`.
            tarball_url: The URL of a tarball or a zip archive from which the source code will be downloaded.
                Required when `source_type` is `ActorSourceType.TARBALL`.
            github_gist_url: The URL of a GitHub Gist from which the source will be downloaded.
                Required when `source_type` is `ActorSourceType.GITHUB_GIST`.

        Returns:
            The updated Actor version.
        """
        actor_version_representation = _get_actor_version_representation(
            build_tag=build_tag,
            env_vars=env_vars,
            apply_env_vars_to_build=apply_env_vars_to_build,
            source_type=source_type,
            source_files=source_files,
            git_repo_url=git_repo_url,
            tarball_url=tarball_url,
            github_gist_url=github_gist_url,
        )

        return await self._update(filter_out_none_values_recursively(actor_version_representation))

    async def delete(self) -> None:
        """Delete the Actor version.

        https://docs.apify.com/api/v2#/reference/actors/version-object/delete-version
        """
        return await self._delete()

    def env_vars(self) -> ActorEnvVarCollectionClientAsync:
        """Retrieve a client for the environment variables of this Actor version."""
        return ActorEnvVarCollectionClientAsync(**self._sub_resource_init_options())

    def env_var(self, env_var_name: str) -> ActorEnvVarClientAsync:
        """Retrieve the client for the specified environment variable of this Actor version.

        Args:
            env_var_name: The name of the environment variable for which to retrieve the resource client.

        Returns:
            The resource client for the specified Actor environment variable.
        """
        return ActorEnvVarClientAsync(**self._sub_resource_init_options(resource_id=env_var_name))


================================================
File: /src/apify_client/clients/resource_clients/build_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class BuildCollectionClient(ResourceCollectionClient):
    """Sub-client for listing Actor builds."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-builds')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List all Actor builds.

        List all Actor builds, either of a single Actor, or all user's Actors, depending on where this client
        was initialized from.

        https://docs.apify.com/api/v2#/reference/actors/build-collection/get-list-of-builds
        https://docs.apify.com/api/v2#/reference/actor-builds/build-collection/get-user-builds-list

        Args:
            limit: How many builds to retrieve.
            offset: What build to include as first when retrieving the list.
            desc: Whether to sort the builds in descending order based on their start date.

        Returns:
            The retrieved Actor builds.
        """
        return self._list(limit=limit, offset=offset, desc=desc)


class BuildCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for listing Actor builds."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-builds')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List all Actor builds.

        List all Actor builds, either of a single Actor, or all user's Actors, depending on where this client
        was initialized from.

        https://docs.apify.com/api/v2#/reference/actors/build-collection/get-list-of-builds
        https://docs.apify.com/api/v2#/reference/actor-builds/build-collection/get-user-builds-list

        Args:
            limit: How many builds to retrieve.
            offset: What build to include as first when retrieving the list.
            desc: Whether to sort the builds in descending order based on their start date.

        Returns:
            The retrieved Actor builds.
        """
        return await self._list(limit=limit, offset=offset, desc=desc)


================================================
File: /src/apify_client/clients/resource_clients/request_queue.py
================================================
from __future__ import annotations

import asyncio
import logging
import math
from dataclasses import dataclass
from datetime import timedelta
from queue import Queue
from time import sleep
from typing import TYPE_CHECKING, Any, TypedDict

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs, parse_date_fields
from more_itertools import constrained_batches

from apify_client._errors import ApifyApiError
from apify_client._utils import catch_not_found_or_throw, pluck_data
from apify_client.clients.base import ResourceClient, ResourceClientAsync

if TYPE_CHECKING:
    from collections.abc import Iterable

logger = logging.getLogger(__name__)

_RQ_MAX_REQUESTS_PER_BATCH = 25
_MAX_PAYLOAD_SIZE_BYTES = 9 * 1024 * 1024  # 9 MB
_SAFETY_BUFFER_PERCENT = 0.01 / 100  # 0.01%


class BatchAddRequestsResult(TypedDict):
    """Result of the batch add requests operation.

    Args:
        processedRequests: List of successfully added requests.
        unprocessedRequests: List of requests that failed to be added.
    """

    processedRequests: list[dict]
    unprocessedRequests: list[dict]


@dataclass
class AddRequestsBatch:
    """Batch of requests to add to the request queue.

    Args:
        requests: List of requests to be added to the request queue.
        num_of_retries: Number of times this batch has been retried.
    """

    requests: Iterable[dict]
    num_of_retries: int = 0


class RequestQueueClient(ResourceClient):
    """Sub-client for manipulating a single request queue."""

    @ignore_docs
    def __init__(  # noqa: D417
        self,
        *args: Any,
        client_key: str | None = None,
        **kwargs: Any,
    ) -> None:
        """A default constructor.

        Args:
            client_key: A unique identifier of the client accessing the request queue.
        """
        resource_path = kwargs.pop('resource_path', 'request-queues')
        super().__init__(*args, resource_path=resource_path, **kwargs)
        self.client_key = client_key

    def get(self) -> dict | None:
        """Retrieve the request queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/get-request-queue

        Returns:
            The retrieved request queue, or None, if it does not exist.
        """
        return self._get()

    def update(self, *, name: str | None = None) -> dict:
        """Update the request queue with specified fields.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/update-request-queue

        Args:
            name: The new name for the request queue.

        Returns:
            The updated request queue.
        """
        updated_fields = {
            'name': name,
        }

        return self._update(filter_out_none_values_recursively(updated_fields))

    def delete(self) -> None:
        """Delete the request queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/delete-request-queue
        """
        return self._delete()

    def list_head(self, *, limit: int | None = None) -> dict:
        """Retrieve a given number of requests from the beginning of the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-head/get-head

        Args:
            limit: How many requests to retrieve.

        Returns:
            The desired number of requests from the beginning of the queue.
        """
        request_params = self._params(limit=limit, clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url('head'),
            method='GET',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    def list_and_lock_head(self, *, lock_secs: int, limit: int | None = None) -> dict:
        """Retrieve a given number of unlocked requests from the beginning of the queue and lock them for a given time.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-head-with-locks/get-head-and-lock

        Args:
            lock_secs: How long the requests will be locked for, in seconds.
            limit: How many requests to retrieve.

        Returns:
            The desired number of locked requests from the beginning of the queue.
        """
        request_params = self._params(lockSecs=lock_secs, limit=limit, clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url('head/lock'),
            method='POST',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    def add_request(self, request: dict, *, forefront: bool | None = None) -> dict:
        """Add a request to the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request-collection/add-request

        Args:
            request: The request to add to the queue.
            forefront: Whether to add the request to the head or the end of the queue.

        Returns:
            The added request.
        """
        request_params = self._params(forefront=forefront, clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url('requests'),
            method='POST',
            json=request,
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    def get_request(self, request_id: str) -> dict | None:
        """Retrieve a request from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/get-request

        Args:
            request_id: ID of the request to retrieve.

        Returns:
            The retrieved request, or None, if it did not exist.
        """
        try:
            response = self.http_client.call(
                url=self._url(f'requests/{request_id}'),
                method='GET',
                params=self._params(),
            )
            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    def update_request(self, request: dict, *, forefront: bool | None = None) -> dict:
        """Update a request in the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/update-request

        Args:
            request: The updated request.
            forefront: Whether to put the updated request in the beginning or the end of the queue.

        Returns:
            The updated request.
        """
        request_id = request['id']

        request_params = self._params(forefront=forefront, clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url(f'requests/{request_id}'),
            method='PUT',
            json=request,
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    def delete_request(self, request_id: str) -> None:
        """Delete a request from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/delete-request

        Args:
            request_id: ID of the request to delete.
        """
        request_params = self._params(
            clientKey=self.client_key,
        )

        self.http_client.call(
            url=self._url(f'requests/{request_id}'),
            method='DELETE',
            params=request_params,
        )

    def prolong_request_lock(
        self,
        request_id: str,
        *,
        forefront: bool | None = None,
        lock_secs: int,
    ) -> dict:
        """Prolong the lock on a request.

        https://docs.apify.com/api/v2#/reference/request-queues/request-lock/prolong-request-lock

        Args:
            request_id: ID of the request to prolong the lock.
            forefront: Whether to put the request in the beginning or the end of the queue after lock expires.
            lock_secs: By how much to prolong the lock, in seconds.
        """
        request_params = self._params(clientKey=self.client_key, forefront=forefront, lockSecs=lock_secs)

        response = self.http_client.call(
            url=self._url(f'requests/{request_id}/lock'),
            method='PUT',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    def delete_request_lock(self, request_id: str, *, forefront: bool | None = None) -> None:
        """Delete the lock on a request.

        https://docs.apify.com/api/v2#/reference/request-queues/request-lock/delete-request-lock

        Args:
            request_id: ID of the request to delete the lock.
            forefront: Whether to put the request in the beginning or the end of the queue after the lock is deleted.
        """
        request_params = self._params(clientKey=self.client_key, forefront=forefront)

        self.http_client.call(
            url=self._url(f'requests/{request_id}/lock'),
            method='DELETE',
            params=request_params,
        )

    def batch_add_requests(
        self,
        requests: list[dict],
        *,
        forefront: bool = False,
        max_parallel: int = 1,
        max_unprocessed_requests_retries: int = 3,
        min_delay_between_unprocessed_requests_retries: timedelta = timedelta(milliseconds=500),
    ) -> BatchAddRequestsResult:
        """Add requests to the request queue in batches.

        Requests are split into batches based on size and processed in parallel.

        https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/add-requests

        Args:
            requests: List of requests to be added to the queue.
            forefront: Whether to add requests to the front of the queue.
            max_parallel: Specifies the maximum number of parallel tasks for API calls. This is only applicable
                to the async client. For the sync client, this value must be set to 1, as parallel execution
                is not supported.
            max_unprocessed_requests_retries: Number of retry attempts for unprocessed requests.
            min_delay_between_unprocessed_requests_retries: Minimum delay between retry attempts for unprocessed
                requests.

        Returns:
            Result containing lists of processed and unprocessed requests.
        """
        if max_parallel != 1:
            raise NotImplementedError('max_parallel is only supported in async client')

        request_params = self._params(clientKey=self.client_key, forefront=forefront)

        # Compute the payload size limit to ensure it doesn't exceed the maximum allowed size.
        payload_size_limit_bytes = _MAX_PAYLOAD_SIZE_BYTES - math.ceil(_MAX_PAYLOAD_SIZE_BYTES * _SAFETY_BUFFER_PERCENT)

        # Split the requests into batches, constrained by the max payload size and max requests per batch.
        batches = constrained_batches(
            requests,
            max_size=payload_size_limit_bytes,
            max_count=_RQ_MAX_REQUESTS_PER_BATCH,
        )

        # Put the batches into the queue for processing.
        queue = Queue[AddRequestsBatch]()

        for b in batches:
            queue.put(AddRequestsBatch(b))

        processed_requests = list[dict]()
        unprocessed_requests = list[dict]()

        # Process all batches in the queue sequentially.
        while not queue.empty():
            batch = queue.get()

            # Send the batch to the API.
            response = self.http_client.call(
                url=self._url('requests/batch'),
                method='POST',
                params=request_params,
                json=list(batch.requests),
            )

            # Retry if the request failed and the retry limit has not been reached.
            if not response.is_success and batch.num_of_retries < max_unprocessed_requests_retries:
                batch.num_of_retries += 1
                sleep(min_delay_between_unprocessed_requests_retries.total_seconds())
                queue.put(batch)

            # Otherwise, add the processed/unprocessed requests to their respective lists.
            else:
                response_parsed = parse_date_fields(pluck_data(response.json()))
                processed_requests.extend(response_parsed.get('processedRequests', []))
                unprocessed_requests.extend(response_parsed.get('unprocessedRequests', []))

        return {
            'processedRequests': processed_requests,
            'unprocessedRequests': unprocessed_requests,
        }

    def batch_delete_requests(self, requests: list[dict]) -> dict:
        """Delete given requests from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/delete-requests

        Args:
            requests: List of the requests to delete.
        """
        request_params = self._params(clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url('requests/batch'),
            method='DELETE',
            params=request_params,
            json=requests,
        )

        return parse_date_fields(pluck_data(response.json()))

    def list_requests(
        self,
        *,
        limit: int | None = None,
        exclusive_start_id: str | None = None,
    ) -> dict:
        """List requests in the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request-collection/list-requests

        Args:
            limit: How many requests to retrieve.
            exclusive_start_id: All requests up to this one (including) are skipped from the result.
        """
        request_params = self._params(limit=limit, exclusive_start_id=exclusive_start_id, clientKey=self.client_key)

        response = self.http_client.call(
            url=self._url('requests'),
            method='GET',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))


class RequestQueueClientAsync(ResourceClientAsync):
    """Async sub-client for manipulating a single request queue."""

    @ignore_docs
    def __init__(  # noqa: D417
        self,
        *args: Any,
        client_key: str | None = None,
        **kwargs: Any,
    ) -> None:
        """A default constructor.

        Args:
            client_key: A unique identifier of the client accessing the request queue.
        """
        resource_path = kwargs.pop('resource_path', 'request-queues')
        super().__init__(*args, resource_path=resource_path, **kwargs)
        self.client_key = client_key

    async def get(self) -> dict | None:
        """Retrieve the request queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/get-request-queue

        Returns:
            The retrieved request queue, or None, if it does not exist.
        """
        return await self._get()

    async def update(self, *, name: str | None = None) -> dict:
        """Update the request queue with specified fields.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/update-request-queue

        Args:
            name: The new name for the request queue.

        Returns:
            The updated request queue.
        """
        updated_fields = {
            'name': name,
        }

        return await self._update(filter_out_none_values_recursively(updated_fields))

    async def delete(self) -> None:
        """Delete the request queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue/delete-request-queue
        """
        return await self._delete()

    async def list_head(self, *, limit: int | None = None) -> dict:
        """Retrieve a given number of requests from the beginning of the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-head/get-head

        Args:
            limit: How many requests to retrieve.

        Returns:
            The desired number of requests from the beginning of the queue.
        """
        request_params = self._params(limit=limit, clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url('head'),
            method='GET',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def list_and_lock_head(self, *, lock_secs: int, limit: int | None = None) -> dict:
        """Retrieve a given number of unlocked requests from the beginning of the queue and lock them for a given time.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-head-with-locks/get-head-and-lock

        Args:
            lock_secs: How long the requests will be locked for, in seconds.
            limit: How many requests to retrieve.

        Returns:
            The desired number of locked requests from the beginning of the queue.
        """
        request_params = self._params(lockSecs=lock_secs, limit=limit, clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url('head/lock'),
            method='POST',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def add_request(self, request: dict, *, forefront: bool | None = None) -> dict:
        """Add a request to the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request-collection/add-request

        Args:
            request: The request to add to the queue.
            forefront: Whether to add the request to the head or the end of the queue.

        Returns:
            The added request.
        """
        request_params = self._params(forefront=forefront, clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url('requests'),
            method='POST',
            json=request,
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def get_request(self, request_id: str) -> dict | None:
        """Retrieve a request from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/get-request

        Args:
            request_id: ID of the request to retrieve.

        Returns:
            The retrieved request, or None, if it did not exist.
        """
        try:
            response = await self.http_client.call(
                url=self._url(f'requests/{request_id}'),
                method='GET',
                params=self._params(),
            )
            return parse_date_fields(pluck_data(response.json()))

        except ApifyApiError as exc:
            catch_not_found_or_throw(exc)

        return None

    async def update_request(self, request: dict, *, forefront: bool | None = None) -> dict:
        """Update a request in the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/update-request

        Args:
            request: The updated request.
            forefront: Whether to put the updated request in the beginning or the end of the queue.

        Returns:
            The updated request.
        """
        request_id = request['id']

        request_params = self._params(forefront=forefront, clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url(f'requests/{request_id}'),
            method='PUT',
            json=request,
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def delete_request(self, request_id: str) -> None:
        """Delete a request from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request/delete-request

        Args:
            request_id: ID of the request to delete.
        """
        request_params = self._params(clientKey=self.client_key)

        await self.http_client.call(
            url=self._url(f'requests/{request_id}'),
            method='DELETE',
            params=request_params,
        )

    async def prolong_request_lock(
        self,
        request_id: str,
        *,
        forefront: bool | None = None,
        lock_secs: int,
    ) -> dict:
        """Prolong the lock on a request.

        https://docs.apify.com/api/v2#/reference/request-queues/request-lock/prolong-request-lock

        Args:
            request_id: ID of the request to prolong the lock.
            forefront: Whether to put the request in the beginning or the end of the queue after lock expires.
            lock_secs: By how much to prolong the lock, in seconds.
        """
        request_params = self._params(clientKey=self.client_key, forefront=forefront, lockSecs=lock_secs)

        response = await self.http_client.call(
            url=self._url(f'requests/{request_id}/lock'),
            method='PUT',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))

    async def delete_request_lock(
        self,
        request_id: str,
        *,
        forefront: bool | None = None,
    ) -> None:
        """Delete the lock on a request.

        https://docs.apify.com/api/v2#/reference/request-queues/request-lock/delete-request-lock

        Args:
            request_id: ID of the request to delete the lock.
            forefront: Whether to put the request in the beginning or the end of the queue after the lock is deleted.
        """
        request_params = self._params(clientKey=self.client_key, forefront=forefront)

        await self.http_client.call(
            url=self._url(f'requests/{request_id}/lock'),
            method='DELETE',
            params=request_params,
        )

    async def _batch_add_requests_worker(
        self,
        queue: asyncio.Queue[AddRequestsBatch],
        request_params: dict,
        max_unprocessed_requests_retries: int,
        min_delay_between_unprocessed_requests_retries: timedelta,
    ) -> BatchAddRequestsResult:
        """Worker function to process a batch of requests.

        This worker will process batches from the queue, retrying requests that fail until the retry limit is reached.

        Returns result containing lists of processed and unprocessed requests by the worker.
        """
        processed_requests = list[dict]()
        unprocessed_requests = list[dict]()

        while True:
            # Get the next batch from the queue.
            try:
                batch = await queue.get()
            except asyncio.CancelledError:
                break

            try:
                # Send the batch to the API.
                response = await self.http_client.call(
                    url=self._url('requests/batch'),
                    method='POST',
                    params=request_params,
                    json=list(batch.requests),
                )

                response_parsed = parse_date_fields(pluck_data(response.json()))

                # Retry if the request failed and the retry limit has not been reached.
                if not response.is_success and batch.num_of_retries < max_unprocessed_requests_retries:
                    batch.num_of_retries += 1
                    await asyncio.sleep(min_delay_between_unprocessed_requests_retries.total_seconds())
                    await queue.put(batch)

                # Otherwise, add the processed/unprocessed requests to their respective lists.
                else:
                    processed_requests.extend(response_parsed.get('processedRequests', []))
                    unprocessed_requests.extend(response_parsed.get('unprocessedRequests', []))

            except Exception as exc:
                logger.warning(f'Error occurred while processing a batch of requests: {exc}')

            finally:
                # Mark the batch as done whether it succeeded or failed.
                queue.task_done()

        return {
            'processedRequests': processed_requests,
            'unprocessedRequests': unprocessed_requests,
        }

    async def batch_add_requests(
        self,
        requests: list[dict],
        *,
        forefront: bool = False,
        max_parallel: int = 5,
        max_unprocessed_requests_retries: int = 3,
        min_delay_between_unprocessed_requests_retries: timedelta = timedelta(milliseconds=500),
    ) -> BatchAddRequestsResult:
        """Add requests to the request queue in batches.

        Requests are split into batches based on size and processed in parallel.

        https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/add-requests

        Args:
            requests: List of requests to be added to the queue.
            forefront: Whether to add requests to the front of the queue.
            max_parallel: Specifies the maximum number of parallel tasks for API calls. This is only applicable
                to the async client. For the sync client, this value must be set to 1, as parallel execution
                is not supported.
            max_unprocessed_requests_retries: Number of retry attempts for unprocessed requests.
            min_delay_between_unprocessed_requests_retries: Minimum delay between retry attempts for unprocessed
                requests.

        Returns:
            Result containing lists of processed and unprocessed requests.
        """
        tasks = set[asyncio.Task]()
        queue: asyncio.Queue[AddRequestsBatch] = asyncio.Queue()
        request_params = self._params(clientKey=self.client_key, forefront=forefront)

        # Compute the payload size limit to ensure it doesn't exceed the maximum allowed size.
        payload_size_limit_bytes = _MAX_PAYLOAD_SIZE_BYTES - math.ceil(_MAX_PAYLOAD_SIZE_BYTES * _SAFETY_BUFFER_PERCENT)

        # Split the requests into batches, constrained by the max payload size and max requests per batch.
        batches = constrained_batches(
            requests,
            max_size=payload_size_limit_bytes,
            max_count=_RQ_MAX_REQUESTS_PER_BATCH,
        )

        for batch in batches:
            await queue.put(AddRequestsBatch(batch))

        # Start a required number of worker tasks to process the batches.
        for i in range(max_parallel):
            coro = self._batch_add_requests_worker(
                queue,
                request_params,
                max_unprocessed_requests_retries,
                min_delay_between_unprocessed_requests_retries,
            )
            task = asyncio.create_task(coro, name=f'batch_add_requests_worker_{i}')
            tasks.add(task)

        # Wait for all batches to be processed.
        await queue.join()

        # Send cancellation signals to all worker tasks and wait for them to finish.
        for task in tasks:
            task.cancel()

        results: list[BatchAddRequestsResult] = await asyncio.gather(*tasks)

        # Combine the results from all workers and return them.
        processed_requests = []
        unprocessed_requests = []

        for result in results:
            processed_requests.extend(result['processedRequests'])
            unprocessed_requests.extend(result['unprocessedRequests'])

        return {
            'processedRequests': processed_requests,
            'unprocessedRequests': unprocessed_requests,
        }

    async def batch_delete_requests(self, requests: list[dict]) -> dict:
        """Delete given requests from the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/delete-requests

        Args:
            requests: List of the requests to delete.
        """
        request_params = self._params(clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url('requests/batch'),
            method='DELETE',
            params=request_params,
            json=requests,
        )
        return parse_date_fields(pluck_data(response.json()))

    async def list_requests(
        self,
        *,
        limit: int | None = None,
        exclusive_start_id: str | None = None,
    ) -> dict:
        """List requests in the queue.

        https://docs.apify.com/api/v2#/reference/request-queues/request-collection/list-requests

        Args:
            limit: How many requests to retrieve.
            exclusive_start_id: All requests up to this one (including) are skipped from the result.
        """
        request_params = self._params(limit=limit, exclusive_start_id=exclusive_start_id, clientKey=self.client_key)

        response = await self.http_client.call(
            url=self._url('requests'),
            method='GET',
            params=request_params,
        )

        return parse_date_fields(pluck_data(response.json()))


================================================
File: /src/apify_client/clients/resource_clients/store_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class StoreCollectionClient(ResourceCollectionClient):
    """Sub-client for Apify store."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'store')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        sort_by: str | None = None,
        category: str | None = None,
        username: str | None = None,
        pricing_model: str | None = None,
    ) -> ListPage[dict]:
        """List Actors in Apify store.

        https://docs.apify.com/api/v2/#/reference/store/store-actors-collection/get-list-of-actors-in-store

        Args:
            limit: How many Actors to list.
            offset: What Actor to include as first when retrieving the list.
            search: String to search by. The search runs on the following fields: title, name, description, username,
                readme.
            sort_by: Specifies the field by which to sort the results.
            category: Filter by this category.
            username: Filter by this username.
            pricing_model: Filter by this pricing model.

        Returns:
            The list of available tasks matching the specified filters.
        """
        return self._list(
            limit=limit,
            offset=offset,
            search=search,
            sortBy=sort_by,
            category=category,
            username=username,
            pricingModel=pricing_model,
        )


class StoreCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for Apify store."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'store')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        search: str | None = None,
        sort_by: str | None = None,
        category: str | None = None,
        username: str | None = None,
        pricing_model: str | None = None,
    ) -> ListPage[dict]:
        """List Actors in Apify store.

        https://docs.apify.com/api/v2/#/reference/store/store-actors-collection/get-list-of-actors-in-store

        Args:
            limit: How many Actors to list.
            offset: What Actor to include as first when retrieving the list.
            search: String to search by. The search runs on the following fields: title, name, description, username,
                readme.
            sort_by: Specifies the field by which to sort the results.
            category: Filter by this category.
            username: Filter by this username.
            pricing_model: Filter by this pricing model.

        Returns:
            The list of available tasks matching the specified filters.
        """
        return await self._list(
            limit=limit,
            offset=offset,
            search=search,
            sortBy=sort_by,
            category=category,
            username=username,
            pricingModel=pricing_model,
        )


================================================
File: /src/apify_client/clients/resource_clients/webhook_dispatch_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class WebhookDispatchCollectionClient(ResourceCollectionClient):
    """Sub-client for listing webhook dispatches."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhook-dispatches')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List all webhook dispatches of a user.

        https://docs.apify.com/api/v2#/reference/webhook-dispatches/webhook-dispatches-collection/get-list-of-webhook-dispatches

        Args:
            limit: How many webhook dispatches to retrieve.
            offset: What webhook dispatch to include as first when retrieving the list.
            desc: Whether to sort the webhook dispatches in descending order based on the date of their creation.

        Returns:
            The retrieved webhook dispatches of a user.
        """
        return self._list(limit=limit, offset=offset, desc=desc)


class WebhookDispatchCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for listing webhook dispatches."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhook-dispatches')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List all webhook dispatches of a user.

        https://docs.apify.com/api/v2#/reference/webhook-dispatches/webhook-dispatches-collection/get-list-of-webhook-dispatches

        Args:
            limit: How many webhook dispatches to retrieve.
            offset: What webhook dispatch to include as first when retrieving the list.
            desc: Whether to sort the webhook dispatches in descending order based on the date of their creation.

        Returns:
            The retrieved webhook dispatches of a user.
        """
        return await self._list(limit=limit, offset=offset, desc=desc)


================================================
File: /src/apify_client/clients/resource_clients/request_queue_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class RequestQueueCollectionClient(ResourceCollectionClient):
    """Sub-client for manipulating request queues."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'request-queues')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        unnamed: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available request queues.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/get-list-of-request-queues

        Args:
            unnamed: Whether to include unnamed request queues in the list.
            limit: How many request queues to retrieve.
            offset: What request queue to include as first when retrieving the list.
            desc: Whether to sort therequest queues in descending order based on their modification date.

        Returns:
            The list of available request queues matching the specified filters.
        """
        return self._list(unnamed=unnamed, limit=limit, offset=offset, desc=desc)

    def get_or_create(self, *, name: str | None = None) -> dict:
        """Retrieve a named request queue, or create a new one when it doesn't exist.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/create-request-queue

        Args:
            name: The name of the request queue to retrieve or create.

        Returns:
            The retrieved or newly-created request queue.
        """
        return self._get_or_create(name=name)


class RequestQueueCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for manipulating request queues."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'request-queues')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        unnamed: bool | None = None,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available request queues.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/get-list-of-request-queues

        Args:
            unnamed: Whether to include unnamed request queues in the list.
            limit: How many request queues to retrieve.
            offset: What request queue to include as first when retrieving the list.
            desc: Whether to sort therequest queues in descending order based on their modification date.

        Returns:
            The list of available request queues matching the specified filters.
        """
        return await self._list(unnamed=unnamed, limit=limit, offset=offset, desc=desc)

    async def get_or_create(self, *, name: str | None = None) -> dict:
        """Retrieve a named request queue, or create a new one when it doesn't exist.

        https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/create-request-queue

        Args:
            name: The name of the request queue to retrieve or create.

        Returns:
            The retrieved or newly-created request queue.
        """
        return await self._get_or_create(name=name)


================================================
File: /src/apify_client/clients/resource_clients/__init__.py
================================================
from .actor import ActorClient, ActorClientAsync
from .actor_collection import ActorCollectionClient, ActorCollectionClientAsync
from .actor_env_var import ActorEnvVarClient, ActorEnvVarClientAsync
from .actor_env_var_collection import ActorEnvVarCollectionClient, ActorEnvVarCollectionClientAsync
from .actor_version import ActorVersionClient, ActorVersionClientAsync
from .actor_version_collection import ActorVersionCollectionClient, ActorVersionCollectionClientAsync
from .build import BuildClient, BuildClientAsync
from .build_collection import BuildCollectionClient, BuildCollectionClientAsync
from .dataset import DatasetClient, DatasetClientAsync
from .dataset_collection import DatasetCollectionClient, DatasetCollectionClientAsync
from .key_value_store import KeyValueStoreClient, KeyValueStoreClientAsync
from .key_value_store_collection import KeyValueStoreCollectionClient, KeyValueStoreCollectionClientAsync
from .log import LogClient, LogClientAsync
from .request_queue import RequestQueueClient, RequestQueueClientAsync
from .request_queue_collection import RequestQueueCollectionClient, RequestQueueCollectionClientAsync
from .run import RunClient, RunClientAsync
from .run_collection import RunCollectionClient, RunCollectionClientAsync
from .schedule import ScheduleClient, ScheduleClientAsync
from .schedule_collection import ScheduleCollectionClient, ScheduleCollectionClientAsync
from .store_collection import StoreCollectionClient, StoreCollectionClientAsync
from .task import TaskClient, TaskClientAsync
from .task_collection import TaskCollectionClient, TaskCollectionClientAsync
from .user import UserClient, UserClientAsync
from .webhook import WebhookClient, WebhookClientAsync
from .webhook_collection import WebhookCollectionClient, WebhookCollectionClientAsync
from .webhook_dispatch import WebhookDispatchClient, WebhookDispatchClientAsync
from .webhook_dispatch_collection import WebhookDispatchCollectionClient, WebhookDispatchCollectionClientAsync

__all__ = [
    'ActorClient',
    'ActorClientAsync',
    'ActorCollectionClient',
    'ActorCollectionClientAsync',
    'ActorEnvVarClient',
    'ActorEnvVarClientAsync',
    'ActorEnvVarCollectionClient',
    'ActorEnvVarCollectionClientAsync',
    'ActorVersionClient',
    'ActorVersionClientAsync',
    'ActorVersionCollectionClient',
    'ActorVersionCollectionClientAsync',
    'BuildClient',
    'BuildClientAsync',
    'BuildCollectionClient',
    'BuildCollectionClientAsync',
    'DatasetClient',
    'DatasetClientAsync',
    'DatasetCollectionClient',
    'DatasetCollectionClientAsync',
    'KeyValueStoreClient',
    'KeyValueStoreClientAsync',
    'KeyValueStoreCollectionClient',
    'KeyValueStoreCollectionClientAsync',
    'LogClient',
    'LogClientAsync',
    'RequestQueueClient',
    'RequestQueueClientAsync',
    'RequestQueueCollectionClient',
    'RequestQueueCollectionClientAsync',
    'RunClient',
    'RunClientAsync',
    'RunCollectionClient',
    'RunCollectionClientAsync',
    'ScheduleClient',
    'ScheduleClientAsync',
    'ScheduleCollectionClient',
    'ScheduleCollectionClientAsync',
    'StoreCollectionClient',
    'StoreCollectionClientAsync',
    'TaskClient',
    'TaskClientAsync',
    'TaskCollectionClient',
    'TaskCollectionClientAsync',
    'UserClient',
    'UserClientAsync',
    'WebhookClient',
    'WebhookClientAsync',
    'WebhookCollectionClient',
    'WebhookCollectionClientAsync',
    'WebhookDispatchClient',
    'WebhookDispatchClientAsync',
    'WebhookDispatchCollectionClient',
    'WebhookDispatchCollectionClientAsync',
]


================================================
File: /src/apify_client/clients/resource_clients/task_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync
from apify_client.clients.resource_clients.task import get_task_representation

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class TaskCollectionClient(ResourceCollectionClient):
    """Sub-client for manipulating tasks."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-tasks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available tasks.

        https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/get-list-of-tasks

        Args:
            limit: How many tasks to list.
            offset: What task to include as first when retrieving the list.
            desc: Whether to sort the tasks in descending order based on their creation date.

        Returns:
            The list of available tasks matching the specified filters.
        """
        return self._list(limit=limit, offset=offset, desc=desc)

    def create(
        self,
        *,
        actor_id: str,
        name: str,
        build: str | None = None,
        timeout_secs: int | None = None,
        memory_mbytes: int | None = None,
        max_items: int | None = None,
        task_input: dict | None = None,
        title: str | None = None,
        actor_standby_desired_requests_per_actor_run: int | None = None,
        actor_standby_max_requests_per_actor_run: int | None = None,
        actor_standby_idle_timeout_secs: int | None = None,
        actor_standby_build: str | None = None,
        actor_standby_memory_mbytes: int | None = None,
    ) -> dict:
        """Create a new task.

        https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/create-task

        Args:
            actor_id: Id of the Actor that should be run.
            name: Name of the task.
            build: Actor build to run. It can be either a build tag or build number. By default, the run uses
                the build specified in the task settings (typically latest).
            memory_mbytes: Memory limit for the run, in megabytes. By default, the run uses a memory limit specified
                in the task settings.
            max_items: Maximum number of results that will be returned by runs of this task. If the Actor of this task
                is charged per result, you will not be charged for more results than the given limit.
            timeout_secs: Optional timeout for the run, in seconds. By default, the run uses timeout specified
                in the task settings.
            task_input: Task input object.
            title: A human-friendly equivalent of the name.
            actor_standby_desired_requests_per_actor_run: The desired number of concurrent HTTP requests for
                a single Actor Standby run.
            actor_standby_max_requests_per_actor_run: The maximum number of concurrent HTTP requests for
                a single Actor Standby run.
            actor_standby_idle_timeout_secs: If the Actor run does not receive any requests for this time,
                it will be shut down.
            actor_standby_build: The build tag or number to run when the Actor is in Standby mode.
            actor_standby_memory_mbytes: The memory in megabytes to use when the Actor is in Standby mode.

        Returns:
            The created task.
        """
        task_representation = get_task_representation(
            actor_id=actor_id,
            name=name,
            task_input=task_input,
            build=build,
            max_items=max_items,
            memory_mbytes=memory_mbytes,
            timeout_secs=timeout_secs,
            title=title,
            actor_standby_desired_requests_per_actor_run=actor_standby_desired_requests_per_actor_run,
            actor_standby_max_requests_per_actor_run=actor_standby_max_requests_per_actor_run,
            actor_standby_idle_timeout_secs=actor_standby_idle_timeout_secs,
            actor_standby_build=actor_standby_build,
            actor_standby_memory_mbytes=actor_standby_memory_mbytes,
        )

        return self._create(filter_out_none_values_recursively(task_representation))


class TaskCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for manipulating tasks."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-tasks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available tasks.

        https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/get-list-of-tasks

        Args:
            limit: How many tasks to list.
            offset: What task to include as first when retrieving the list.
            desc: Whether to sort the tasks in descending order based on their creation date.

        Returns:
            The list of available tasks matching the specified filters.
        """
        return await self._list(limit=limit, offset=offset, desc=desc)

    async def create(
        self,
        *,
        actor_id: str,
        name: str,
        build: str | None = None,
        timeout_secs: int | None = None,
        memory_mbytes: int | None = None,
        max_items: int | None = None,
        task_input: dict | None = None,
        title: str | None = None,
        actor_standby_desired_requests_per_actor_run: int | None = None,
        actor_standby_max_requests_per_actor_run: int | None = None,
        actor_standby_idle_timeout_secs: int | None = None,
        actor_standby_build: str | None = None,
        actor_standby_memory_mbytes: int | None = None,
    ) -> dict:
        """Create a new task.

        https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/create-task

        Args:
            actor_id: Id of the Actor that should be run.
            name: Name of the task.
            build: Actor build to run. It can be either a build tag or build number. By default, the run uses
                the build specified in the task settings (typically latest).
            memory_mbytes: Memory limit for the run, in megabytes. By default, the run uses a memory limit specified
                in the task settings.
            max_items: Maximum number of results that will be returned by runs of this task. If the Actor of this task
                is charged per result, you will not be charged for more results than the given limit.
            timeout_secs: Optional timeout for the run, in seconds. By default, the run uses timeout specified
                in the task settings.
            task_input: Task input object.
            title: A human-friendly equivalent of the name.
            actor_standby_desired_requests_per_actor_run: The desired number of concurrent HTTP requests for
                a single Actor Standby run.
            actor_standby_max_requests_per_actor_run: The maximum number of concurrent HTTP requests for
                a single Actor Standby run.
            actor_standby_idle_timeout_secs: If the Actor run does not receive any requests for this time,
                it will be shut down.
            actor_standby_build: The build tag or number to run when the Actor is in Standby mode.
            actor_standby_memory_mbytes: The memory in megabytes to use when the Actor is in Standby mode.

        Returns:
            The created task.
        """
        task_representation = get_task_representation(
            actor_id=actor_id,
            name=name,
            task_input=task_input,
            build=build,
            max_items=max_items,
            memory_mbytes=memory_mbytes,
            timeout_secs=timeout_secs,
            title=title,
            actor_standby_desired_requests_per_actor_run=actor_standby_desired_requests_per_actor_run,
            actor_standby_max_requests_per_actor_run=actor_standby_max_requests_per_actor_run,
            actor_standby_idle_timeout_secs=actor_standby_idle_timeout_secs,
            actor_standby_build=actor_standby_build,
            actor_standby_memory_mbytes=actor_standby_memory_mbytes,
        )

        return await self._create(filter_out_none_values_recursively(task_representation))


================================================
File: /src/apify_client/clients/resource_clients/run_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import ignore_docs, maybe_extract_enum_member_value

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync

if TYPE_CHECKING:
    from apify_shared.consts import ActorJobStatus
    from apify_shared.models import ListPage


class RunCollectionClient(ResourceCollectionClient):
    """Sub-client for listing Actor runs."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-runs')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
        status: ActorJobStatus | None = None,
    ) -> ListPage[dict]:
        """List all Actor runs.

        List all Actor runs, either of a single Actor, or all user's Actors, depending on where this client
        was initialized from.

        https://docs.apify.com/api/v2#/reference/actors/run-collection/get-list-of-runs
        https://docs.apify.com/api/v2#/reference/actor-runs/run-collection/get-user-runs-list

        Args:
            limit: How many runs to retrieve.
            offset: What run to include as first when retrieving the list.
            desc: Whether to sort the runs in descending order based on their start date.
            status: Retrieve only runs with the provided status.

        Returns:
            The retrieved Actor runs.
        """
        return self._list(
            limit=limit,
            offset=offset,
            desc=desc,
            status=maybe_extract_enum_member_value(status),
        )


class RunCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for listing Actor runs."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'actor-runs')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
        status: ActorJobStatus | None = None,
    ) -> ListPage[dict]:
        """List all Actor runs.

        List all Actor runs, either of a single Actor, or all user's Actors, depending on where this client
        was initialized from.

        https://docs.apify.com/api/v2#/reference/actors/run-collection/get-list-of-runs
        https://docs.apify.com/api/v2#/reference/actor-runs/run-collection/get-user-runs-list

        Args:
            limit: How many runs to retrieve.
            offset: What run to include as first when retrieving the list.
            desc: Whether to sort the runs in descending order based on their start date.
            status: Retrieve only runs with the provided status.

        Returns:
            The retrieved Actor runs.
        """
        return await self._list(
            limit=limit,
            offset=offset,
            desc=desc,
            status=maybe_extract_enum_member_value(status),
        )


================================================
File: /src/apify_client/clients/resource_clients/actor_env_var_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync
from apify_client.clients.resource_clients.actor_env_var import get_actor_env_var_representation

if TYPE_CHECKING:
    from apify_shared.models import ListPage


class ActorEnvVarCollectionClient(ResourceCollectionClient):
    """Sub-client for manipulating actor env vars."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'env-vars')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(self) -> ListPage[dict]:
        """List the available actor environment variables.

        https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/get-list-of-environment-variables

        Returns:
            The list of available actor environment variables.
        """
        return self._list()

    def create(
        self,
        *,
        is_secret: bool | None = None,
        name: str,
        value: str,
    ) -> dict:
        """Create a new actor environment variable.

        https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/create-environment-variable

        Args:
            is_secret: Whether the environment variable is secret or not.
            name: The name of the environment variable.
            value: The value of the environment variable.

        Returns:
            The created actor environment variable.
        """
        actor_env_var_representation = get_actor_env_var_representation(
            is_secret=is_secret,
            name=name,
            value=value,
        )

        return self._create(filter_out_none_values_recursively(actor_env_var_representation))


class ActorEnvVarCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for manipulating actor env vars."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'env-vars')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(self) -> ListPage[dict]:
        """List the available actor environment variables.

        https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/get-list-of-environment-variables

        Returns:
            The list of available actor environment variables.
        """
        return await self._list()

    async def create(
        self,
        *,
        is_secret: bool | None = None,
        name: str,
        value: str,
    ) -> dict:
        """Create a new actor environment variable.

        https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/create-environment-variable

        Args:
            is_secret: Whether the environment variable is secret or not.
            name: The name of the environment variable.
            value: The value of the environment variable.

        Returns:
            The created actor environment variable.
        """
        actor_env_var_representation = get_actor_env_var_representation(
            is_secret=is_secret,
            name=name,
            value=value,
        )

        return await self._create(filter_out_none_values_recursively(actor_env_var_representation))


================================================
File: /src/apify_client/clients/resource_clients/webhook_collection.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import filter_out_none_values_recursively, ignore_docs

from apify_client.clients.base import ResourceCollectionClient, ResourceCollectionClientAsync
from apify_client.clients.resource_clients.webhook import get_webhook_representation

if TYPE_CHECKING:
    from apify_shared.consts import WebhookEventType
    from apify_shared.models import ListPage


class WebhookCollectionClient(ResourceCollectionClient):
    """Sub-client for manipulating webhooks."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhooks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available webhooks.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/get-list-of-webhooks

        Args:
            limit: How many webhooks to retrieve.
            offset: What webhook to include as first when retrieving the list.
            desc: Whether to sort the webhooks in descending order based on their date of creation.

        Returns:
            The list of available webhooks matching the specified filters.
        """
        return self._list(limit=limit, offset=offset, desc=desc)

    def create(
        self,
        *,
        event_types: list[WebhookEventType],  # type: ignore[valid-type]
        request_url: str,
        payload_template: str | None = None,
        headers_template: str | None = None,
        actor_id: str | None = None,
        actor_task_id: str | None = None,
        actor_run_id: str | None = None,
        ignore_ssl_errors: bool | None = None,
        do_not_retry: bool | None = None,
        idempotency_key: str | None = None,
        is_ad_hoc: bool | None = None,
    ) -> dict:
        """Create a new webhook.

        You have to specify exactly one out of actor_id, actor_task_id or actor_run_id.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/create-webhook

        Args:
            event_types: List of event types that should trigger the webhook. At least one is required.
            request_url: URL that will be invoked once the webhook is triggered.
            payload_template: Specification of the payload that will be sent to request_url.
            headers_template: Headers that will be sent to the request_url.
            actor_id: Id of the Actor whose runs should trigger the webhook.
            actor_task_id: Id of the Actor task whose runs should trigger the webhook.
            actor_run_id: Id of the Actor run which should trigger the webhook.
            ignore_ssl_errors: Whether the webhook should ignore SSL errors returned by request_url.
            do_not_retry: Whether the webhook should retry sending the payload to request_url upon failure.
            idempotency_key: A unique identifier of a webhook. You can use it to ensure that you won't create
                the same webhook multiple times.
            is_ad_hoc: Set to True if you want the webhook to be triggered only the first time the condition
                is fulfilled. Only applicable when actor_run_id is filled.

        Returns:
           The created webhook.
        """
        webhook_representation = get_webhook_representation(
            event_types=event_types,
            request_url=request_url,
            payload_template=payload_template,
            headers_template=headers_template,
            actor_id=actor_id,
            actor_task_id=actor_task_id,
            actor_run_id=actor_run_id,
            ignore_ssl_errors=ignore_ssl_errors,
            do_not_retry=do_not_retry,
            idempotency_key=idempotency_key,
            is_ad_hoc=is_ad_hoc,
        )

        return self._create(filter_out_none_values_recursively(webhook_representation))


class WebhookCollectionClientAsync(ResourceCollectionClientAsync):
    """Async sub-client for manipulating webhooks."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'webhooks')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    async def list(
        self,
        *,
        limit: int | None = None,
        offset: int | None = None,
        desc: bool | None = None,
    ) -> ListPage[dict]:
        """List the available webhooks.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/get-list-of-webhooks

        Args:
            limit: How many webhooks to retrieve.
            offset: What webhook to include as first when retrieving the list.
            desc: Whether to sort the webhooks in descending order based on their date of creation.

        Returns:
            The list of available webhooks matching the specified filters.
        """
        return await self._list(limit=limit, offset=offset, desc=desc)

    async def create(
        self,
        *,
        event_types: list[WebhookEventType],  # type: ignore[valid-type]
        request_url: str,
        payload_template: str | None = None,
        headers_template: str | None = None,
        actor_id: str | None = None,
        actor_task_id: str | None = None,
        actor_run_id: str | None = None,
        ignore_ssl_errors: bool | None = None,
        do_not_retry: bool | None = None,
        idempotency_key: str | None = None,
        is_ad_hoc: bool | None = None,
    ) -> dict:
        """Create a new webhook.

        You have to specify exactly one out of actor_id, actor_task_id or actor_run_id.

        https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/create-webhook

        Args:
            event_types: List of event types that should trigger the webhook. At least one is required.
            request_url: URL that will be invoked once the webhook is triggered.
            payload_template: Specification of the payload that will be sent to request_url.
            headers_template: Headers that will be sent to the request_url.
            actor_id: Id of the Actor whose runs should trigger the webhook.
            actor_task_id: Id of the Actor task whose runs should trigger the webhook.
            actor_run_id: Id of the Actor run which should trigger the webhook.
            ignore_ssl_errors: Whether the webhook should ignore SSL errors returned by request_url.
            do_not_retry: Whether the webhook should retry sending the payload to request_url upon failure.
            idempotency_key: A unique identifier of a webhook. You can use it to ensure that you won't create
                the same webhook multiple times.
            is_ad_hoc: Set to True if you want the webhook to be triggered only the first time the condition
                is fulfilled. Only applicable when actor_run_id is filled.

        Returns:
           The created webhook.
        """
        webhook_representation = get_webhook_representation(
            event_types=event_types,
            request_url=request_url,
            payload_template=payload_template,
            headers_template=headers_template,
            actor_id=actor_id,
            actor_task_id=actor_task_id,
            actor_run_id=actor_run_id,
            ignore_ssl_errors=ignore_ssl_errors,
            do_not_retry=do_not_retry,
            idempotency_key=idempotency_key,
            is_ad_hoc=is_ad_hoc,
        )

        return await self._create(filter_out_none_values_recursively(webhook_representation))


================================================
File: /src/apify_client/clients/resource_clients/actor.py
================================================
from __future__ import annotations

from typing import TYPE_CHECKING, Any

from apify_shared.utils import (
    filter_out_none_values_recursively,
    ignore_docs,
    maybe_extract_enum_member_value,
    parse_date_fields,
)

from apify_client._utils import encode_key_value_store_record_value, encode_webhook_list_to_base64, pluck_data
from apify_client.clients.base import ResourceClient, ResourceClientAsync
from apify_client.clients.resource_clients.actor_version import ActorVersionClient, ActorVersionClientAsync
from apify_client.clients.resource_clients.actor_version_collection import (
    ActorVersionCollectionClient,
    ActorVersionCollectionClientAsync,
)
from apify_client.clients.resource_clients.build_collection import BuildCollectionClient, BuildCollectionClientAsync
from apify_client.clients.resource_clients.run import RunClient, RunClientAsync
from apify_client.clients.resource_clients.run_collection import RunCollectionClient, RunCollectionClientAsync
from apify_client.clients.resource_clients.webhook_collection import (
    WebhookCollectionClient,
    WebhookCollectionClientAsync,
)

if TYPE_CHECKING:
    from apify_shared.consts import ActorJobStatus, MetaOrigin


def get_actor_representation(
    *,
    name: str | None,
    title: str | None = None,
    description: str | None = None,
    seo_title: str | None = None,
    seo_description: str | None = None,
    versions: list[dict] | None = None,
    restart_on_error: bool | None = None,
    is_public: bool | None = None,
    is_deprecated: bool | None = None,
    is_anonymously_runnable: bool | None = None,
    categories: list[str] | None = None,
    default_run_build: str | None = None,
    default_run_max_items: int | None = None,
    default_run_memory_mbytes: int | None = None,
    default_run_timeout_secs: int | None = None,
    example_run_input_body: Any = None,
    example_run_input_content_type: str | None = None,
    actor_standby_is_enabled: bool | None = None,
    actor_standby_desired_requests_per_actor_run: int | None = None,
    actor_standby_max_requests_per_actor_run: int | None = None,
    actor_standby_idle_timeout_secs: int | None = None,
    actor_standby_build: str | None = None,
    actor_standby_memory_mbytes: int | None = None,
) -> dict:
    """Get dictionary representation of the Actor."""
    return {
        'name': name,
        'title': title,
        'description': description,
        'seoTitle': seo_title,
        'seoDescription': seo_description,
        'versions': versions,
        'restartOnError': restart_on_error,
        'isPublic': is_public,
        'isDeprecated': is_deprecated,
        'isAnonymouslyRunnable': is_anonymously_runnable,
        'categories': categories,
        'defaultRunOptions': {
            'build': default_run_build,
            'maxItems': default_run_max_items,
            'memoryMbytes': default_run_memory_mbytes,
            'timeoutSecs': default_run_timeout_secs,
        },
        'exampleRunInput': {
            'body': example_run_input_body,
            'contentType': example_run_input_content_type,
        },
        'actorStandby': {
            'isEnabled': actor_standby_is_enabled,
            'desiredRequestsPerActorRun': actor_standby_desired_requests_per_actor_run,
            'maxRequestsPerActorRun': actor_standby_max_requests_per_actor_run,
            'idleTimeoutSecs': actor_standby_idle_timeout_secs,
            'build': actor_standby_build,
            'memoryMbytes': actor_standby_memory_mbytes,
        },
    }


class ActorClient(ResourceClient):
    """Sub-client for manipulating a single Actor."""

    @ignore_docs
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        resource_path = kwargs.pop('resource_path', 'acts')
        super().__init__(*args, resource_path=resource_path, **kwargs)

    def get(self) -> dict | None:
        """Retrieve the Actor.

        https://docs.apify.com/api/v2#/reference/actors/actor-object/get-actor

        Returns:
            The retrieved Actor.
        """
        return self._get()

    def update(
        self,
        *,
        name: str | None = None,
        title: str | None = None,
        description: str | None = None,
        seo_title: str | None = None,
        seo_description: str | None = None,
        versions: list[dict] | None = None,
        restart_on_error: bool | None = None,
        is_public: bool | None = None,
        is_deprecated: bool | None = None,
        is_anonymously_runnable: bool | None = None,
        categories: list[str] | None = None,
        default_run_build: str | None = None,
        default_run_max_items: int | None = None,
        default_run_memory_mbytes: int | None = None,
        default_run_timeout_secs: int | None = None,
        example_run_input_body: Any = None,
        example_run_input_content_type: str | None = None,
        actor_standby_is_enabled: bool | None = None,
        actor_standby_desired_requests_per_actor_run: int | None = None,
        actor_standby_max_requests_per_actor_run: int | None = None,
        actor_standby_idle_timeout_secs: int | None = None,
        actor_standby_build: str | None = None,
        actor_standby_memory_mbytes: int | None = None,
    ) -> dict:
        """Update the Actor with the specified fields.

        https://docs.apify.com/api/v2#/reference/actors/actor-object/update-actor

        Args:
            name: The name of the Actor.
            title: The title of the Actor (human-readable).
            description: The description for the Actor.
            seo_title: The title of the Actor optimized for search engines.
            seo_description: The description of the Actor optimized for search engines.
            versions: The list of Actor versions.
            restart_on_error: If true, the main Actor run process will be restarted whenever it exits with
                a non-zero status code.
            is_public: Whether the Actor is public.
            is_deprecated: Whether the Actor is deprecated.
            is_anonymously_runnable: Whether the Actor is anonymously runnable.
            categories: The categories to which the Actor belongs to.
            default_run_build: Tag or number of the build that you want to run by default.
            default_run_max_items: Default limit of the number of results that will be returned
                by runs of this Actor, if the Actor is charged per result.
            default_run_memory_mbytes: Default amount of memory allocated for the runs of this Actor, in megabytes.
            default_run_timeout_secs: Default timeout for the runs of this Actor in seconds.
            example_run_input_body: Input to be prefilled as default input to new users 