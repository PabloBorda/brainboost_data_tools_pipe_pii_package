# BrainBoost Data Tools Pipe PII Package

A Python package for filtering and anonymizing personal identifiable information (PII) using Microsoft Presidio.

## Features

- Detects and anonymizes PII entities such as PERSON, EMAIL_ADDRESS, PHONE_NUMBER, API_KEY, and ID_NUMBER.
- Custom recognizers for API keys and ID numbers.
- Easy-to-use interface.

## Installation

You can install the package via `pip`:

```bash
pip install brainboost_data_tools_pipe_pii_package

USAGE


from brainboost_data_tools_pipe_pii_package import 

text = "Contact John Doe at john.doe@example.com or call 123-456-7890. API Key: ABCDEFGHIJKLMNOPQRSTUVWXYZ123456"

filter_pii = ()
anonymized_text = filter_pii.filter(text)

print(anonymized_text)
# Output: Contact [FILTERED] at [FILTERED] or call [FILTERED]. API Key: [FILTERED]
# brainboost_data_tools_pipe_pii_package
# brainboost_data_tools_pipe_pii_package
