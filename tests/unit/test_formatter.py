"""
Tests for the data formatting functions.
"""
import pytest

# Import the functions to be tested
from src.data_processing.formatter import create_training_pair, format_for_training

# --- Tests for create_training_pair ---

def test_create_training_pair_basic():
    """Test creating a single prompt-completion pair."""
    post = "Excited to share insights on leveraging AI for business growth at #TechConf2024!"
    topic = "AI in Business"
    expected_output = {
        "prompt": f"Topic: {topic}\n\nWrite a LinkedIn post about the specified topic.\n\nPost:",
        "completion": f" {post}"
    }
    
    # This test will likely fail until the function is implemented correctly
    actual_output = create_training_pair(post, topic)
    assert actual_output == expected_output

def test_create_training_pair_different_content():
    """Test with different post and topic content."""
    post = "Networking is key! Met some amazing people at the industry mixer last night."
    topic = "Professional Networking"
    expected_output = {
        "prompt": f"Topic: {topic}\n\nWrite a LinkedIn post about the specified topic.\n\nPost:",
        "completion": f" {post}"
    }
    actual_output = create_training_pair(post, topic)
    assert actual_output == expected_output

# --- Tests for format_for_training ---

def test_format_for_training_basic():
    """Test formatting multiple posts and topics."""
    posts = [
        "Post 1 about AI.",
        "Post 2 about Marketing."
    ]
    topics = [
        "Artificial Intelligence",
        "Digital Marketing"
    ]
    expected_output = [
        {
            "prompt": "Topic: Artificial Intelligence\n\nWrite a LinkedIn post about the specified topic.\n\nPost:",
            "completion": " Post 1 about AI."
        },
        {
            "prompt": "Topic: Digital Marketing\n\nWrite a LinkedIn post about the specified topic.\n\nPost:",
            "completion": " Post 2 about Marketing."
        }
    ]
    
    # This test will fail until the function is implemented correctly
    actual_output = format_for_training(posts, topics)
    assert actual_output == expected_output

def test_format_for_training_empty_lists():
    """Test formatting with empty input lists."""
    posts = []
    topics = []
    expected_output = []
    actual_output = format_for_training(posts, topics)
    assert actual_output == expected_output

def test_format_for_training_mismatched_lengths():
    """Test formatting with lists of different lengths (should raise error)."""
    posts = ["Post 1"]
    topics = ["Topic 1", "Topic 2"] # Mismatched length
    
    # This test expects a ValueError
    with pytest.raises(ValueError):
        format_for_training(posts, topics)
