"""
Tests for the data processing pipeline, starting with data loading.
"""
import pytest
from pathlib import Path
import pandas as pd
import tempfile
import os

# Correct import path for functions within the 'src' directory
from src.data_processing.pipeline import load_posts

@pytest.fixture
def temp_csv_file():
    """Fixture to create a temporary CSV file for testing."""
    posts = ["This is the first post.", "Here's another one.", "", "A third valid post."]
    df = pd.DataFrame({"post_content": posts})
    
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".csv") as temp_file:
        df.to_csv(temp_file.name, index=False)
        file_path = temp_file.name
    
    yield Path(file_path)
    
    # Cleanup: remove the temporary file
    os.remove(file_path)


def test_load_posts_from_csv(temp_csv_file):
    """Test loading posts from a CSV file, expecting empty posts to be removed."""
    loaded_posts = load_posts(temp_csv_file)
    assert isinstance(loaded_posts, list)
    assert len(loaded_posts) == 3 # Expecting the empty post to be removed
    assert loaded_posts == ["This is the first post.", "Here's another one.", "A third valid post."]


def test_load_posts_file_not_found():
    """Test that loading posts raises FileNotFoundError for non-existent files."""
    non_existent_path = Path("non_existent_file.csv")
    with pytest.raises(FileNotFoundError):
        load_posts(non_existent_path)


def test_load_posts_invalid_format():
    """Test loading posts from a file with incorrect format (e.g., wrong column name)."""
    with tempfile.NamedTemporaryFile(mode='w+', delete=False, suffix=".csv") as temp_file:
        df = pd.DataFrame({"wrong_column": ["post 1", "post 2"]})
        df.to_csv(temp_file.name, index=False)
        file_path = temp_file.name
        
    with pytest.raises(ValueError): # Expecting a ValueError for incorrect format
         load_posts(Path(file_path))
        
    os.remove(file_path)
