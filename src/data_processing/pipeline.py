"""
Main orchestration pipeline for data processing.
"""
from pathlib import Path
from typing import List, Dict
import pandas as pd

def load_posts(input_path: Path, content_column: str = "post_content") -> List[str]:
    """
    Load posts from a CSV file, validate, and return a list of non-empty post strings.

    Args:
        input_path: Path to the input CSV file.
        content_column: Name of the column containing the post text.

    Returns:
        A list of non-empty post strings.
        
    Raises:
        FileNotFoundError: If the input_path does not exist.
        ValueError: If the content_column is not found in the CSV or if the file is not a valid CSV.
    """
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
        
    try:
        df = pd.read_csv(input_path)
    except pd.errors.EmptyDataError:
        return [] # Return empty list for empty file
    except Exception as e:
        raise ValueError(f"Failed to read CSV file: {e}")

    if content_column not in df.columns:
        raise ValueError(f"Content column '{content_column}' not found in CSV file.")
        
    # Get posts, convert to string, fill NA with empty string
    posts = df[content_column].astype(str).fillna('').tolist()
    
    # Filter out empty strings and strings that become empty after stripping whitespace
    # Also filter out the literal string "nan" which can result from empty values in CSV
    non_empty_posts = [
        post for post in posts 
        if post.strip() and post != 'nan'
    ]
    
    return non_empty_posts

def process_posts(input_path: Path, output_path: Path) -> None:
    """
    Process posts from input file to training data at output path.
    This involves loading, extracting topics (if applicable), formatting, and saving.

    Args:
        input_path: Path to the input CSV file containing posts.
        output_path: Path to save the formatted training data (e.g., JSON file).
    """
    raise NotImplementedError