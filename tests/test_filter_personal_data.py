# tests/test_filter_personal_data.py

import pytest
from brainboost_data_tools_pipe_pii_package.BBFilterPersonalData import BBFilterPersonalData

@pytest.fixture
def filter_pii():
    return BBFilterPersonalData()

def test_filter_no_pii(filter_pii):
    text = "This is a sample text without any personal information."
    expected = text
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_person_email(filter_pii):
    text = "Contact me at jane.doe@example.com."
    expected = "Contact me at [FILTERED]."
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_person_phone(filter_pii):
    text = "Call me at 555-123-4567."
    expected = "Call me at [FILTERED]."
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_api_key(filter_pii):
    text = "My API key is ABCDEFGHIJKLMNOPQRSTUVWXYZ123456."
    expected = "My API key is [FILTERED]."
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_id_number(filter_pii):
    text = "My ID number is 123-45-6789."
    expected = "My ID number is [FILTERED]."
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_multiple_pii(filter_pii):
    text = (
        "Hello John Doe,\n"
        "Please send the report to john.doe@example.com.\n"
        "You can reach me at 123-456-7890 or my API key is ABCDEFGHIJKLMNOPQRSTUVWXYZ123456.\n"
        "Best,\n"
        "Jane Smith"
    )
    expected = (
        "Hello [FILTERED],\n"
        "Please send the report to [FILTERED].\n"
        "You can reach me at [FILTERED] or my API key is [FILTERED].\n"
        "Best,\n"
        "[FILTERED]"
    )
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_partial_pii(filter_pii):
    text = "Hello John, your email is john@example.com and phone is 555-1234."
    expected = "Hello [FILTERED], your email is [FILTERED] and phone is [FILTERED]."
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_empty_string(filter_pii):
    text = ""
    expected = ""
    result = filter_pii.filter(text)
    assert result == expected

def test_filter_special_characters(filter_pii):
    text = "Contact: jane_doe+test@example.co.uk, Phone: (555) 123-4567!"
    expected = "Contact: [FILTERED], Phone: [FILTERED]!"
    result = filter_pii.filter(text)
    assert result == expected
