"""
Functions for formatting extracted data into training pairs.
"""
from typing import List, Dict

def create_training_pair(post: str, topic: str) -> Dict[str, str]:
    """
    Creates a single prompt-completion pair for fine-tuning.

    Args:
        post: The original LinkedIn post content.
        topic: The extracted topic for the post.

    Returns:
        A dictionary containing the formatted 'prompt' and 'completion'.
    """
    # Define the prompt structure
    prompt = (
        f"Topic: {topic}\n\n"
        f"Write a LinkedIn post about the specified topic.\n\n"
        f"Post:"
    )
    
    # Ensure completion starts with a space, as often expected by models
    completion = f" {post}"
    
    return {"prompt": prompt, "completion": completion}

def format_for_training(posts: List[str], topics: List[str]) -> List[Dict[str, str]]:
    """
    Formats lists of posts and topics into a list of training pairs.

    Args:
        posts: A list of LinkedIn post strings.
        topics: A list of corresponding topic strings.

    Returns:
        A list of dictionaries, where each dictionary is a training pair.
        
    Raises:
        ValueError: If the lengths of the posts and topics lists do not match.
    """
    if len(posts) != len(topics):
        raise ValueError("The number of posts and topics must be the same.")

    training_data = []
    for post, topic in zip(posts, topics):
        training_pair = create_training_pair(post, topic)
        training_data.append(training_pair)
        
    return training_data