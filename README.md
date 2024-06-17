# How to use ChatGPT API for completion

## Open API pre requisits

What you need to do to integrate and use the ChatGPT api is the following:
- create the account https://openai.com/chatgpt/
- add a payment method and setup your budget(I sugest to keep it low as possible) at https://platform.openai.com/settings/organization/billing/overview
- create the APIKEY that you will use at your profile or direct to https://platform.openai.com/api-keys
- Aftercreate store the APIKEY at a safe location, you do not want it to be leaked to the internet.

## configure the environment

create your environment:

```$python -m virtualenv venv```

activate it:

```$source activate venv/bin/activate```

Install some the 2 libraries `requests` and `dotenv`:

```
pip install python-dotenv
pip install requests
```

or copy the requirements.txt and run:

```
$pip install -r requirements.txt
```

create the file ".env" with the APIKEY:
```
OPENAI_API_KEY=replace-openapikey-generated-at-the-openapi
```

## lets do the trick

create the file `example_chatgpt.py`
```
#example_chatgpt.py
import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

# Ensure you have the OpenAI API key set as an environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

message = "Hello!"

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": message
        }
    ]
}

response = requests.post(url, headers=headers, json=data)

if response.status_code == 200:
    pprint(response.json())
else:
    pprint(f"Request failed with status code {response.status_code}: {response.text}")
```

## what this code does?

import the libraries
```
#example_chatgpt.py
import os
import requests
from pprint import pprint
from dotenv import load_dotenv
```

load the apikey from .env:
```
# Ensure you have the OpenAI API key set as an environment variable
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable not set.")

```

write the message and create the payload to call the chat gpt:
```

url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {OPENAI_API_KEY}"
}
data = {
    "model": "gpt-3.5-turbo",
    "messages": [
        {
            "role": "user",
            "content": message
        }
    ]
}

```
calling the api:

```
response = requests.post(url, headers=headers, json=data)
```
print the response:

```
if response.status_code == 200:
    pprint(response.json())
else:
    pprint(f"Request failed with status code {response.status_code}: {response.text}")
```


## run the code:

```
python example_chatgpt.py
```

The output in the console should be someting like this:

```
{'id': 'chatcmpl-9b9xJVZ6flOjxhawgtgQC75SUnmvR', 'object': 'chat.completion', 'created': 1718643433, 'model': 'gpt-3.5-turbo-0125', 'choices': [
        {'index': 0, 'message': {'role': 'assistant', 'content': 'Hello! How can I assist you today?'
            }, 'logprobs': None, 'finish_reason': 'stop'
        }
    ], 'usage': {'prompt_tokens': 9, 'completion_tokens': 9, 'total_tokens': 18
    }, 'system_fingerprint': None
}
```
the message content is the response that you should be familiar with the chat that you are used to, in my example I had this:
```
'message': {'role': 'assistant', 'content': 'Hello! How can I assist you today?'
            }
```
## Further considerations

now that you know how to use look at the API documentation, in order to customize the requests that you want:

https://platform.openai.com/docs/api-reference/chat/create
