"""
Tests for the topic extraction functionality.
"""
import pytest
from unittest.mock import patch, MagicMock
import openai # Ensure openai is imported if needed for mocking structure

# Import the functions to be tested
from src.data_processing.extractor import extract_topic, batch_extract_topics

# --- Tests for extract_topic --- 

# Mock the specific client path used by the openai library >= v1.0.0
@patch('openai.OpenAI') 
def test_extract_topic_success(MockOpenAI):
    """Test successful topic extraction using a mocked LLM response."""
    # Setup the mock client and its response
    mock_client = MockOpenAI.return_value
    mock_chat_completion = MagicMock()
    mock_chat_completion.choices = [MagicMock()]
    mock_chat_completion.choices[0].message = MagicMock()
    mock_chat_completion.choices[0].message.content = "Technology and AI"
    mock_client.chat.completions.create.return_value = mock_chat_completion

    post = "Discussing the future of artificial intelligence and its impact on tech jobs."
    expected_topic = "Technology and AI"
    
    actual_topic = extract_topic(post)
    assert actual_topic == expected_topic
    mock_client.chat.completions.create.assert_called_once() # Verify the mock was called


@patch('openai.OpenAI') 
def test_extract_topic_api_error(MockOpenAI):
    """Test handling of an error from the OpenAI API."""
    # Setup the mock client to raise an API error
    mock_client = MockOpenAI.return_value
    mock_client.chat.completions.create.side_effect = openai.APIError("API connection failed", request=None, body=None)

    post = "A simple post about daily life."
    
    # Expect the function to raise the APIError
    with pytest.raises(openai.APIError): 
        extract_topic(post)


def test_extract_topic_empty_post():
    """Test topic extraction with an empty or whitespace-only post."""
    assert extract_topic("") == "General" # Assuming default for empty
    assert extract_topic("   ") == "General"

# --- Tests for batch_extract_topics --- 

# We'll keep these tests focused on batching, mocking the implemented extract_topic
@patch('src.data_processing.extractor.extract_topic') 
def test_batch_extract_topics_success(mock_extract_topic):
    """Test batch extraction, assuming individual extraction works."""
    posts = [
        "Post about AI.", 
        "Post about Marketing.", 
        "Post about Startups."
    ]
    expected_topics = ["AI", "Marketing", "Startups"]
    
    # Configure the mock to return different topics for each call
    mock_extract_topic.side_effect = expected_topics
    
    # The current batch_extract_topics just calls extract_topic in a loop
    actual_topics = batch_extract_topics(posts)
    
    assert actual_topics == expected_topics
    assert mock_extract_topic.call_count == len(posts)


def test_batch_extract_topics_empty_list():
    """Test batch extraction with an empty list of posts."""
    assert batch_extract_topics([]) == []
