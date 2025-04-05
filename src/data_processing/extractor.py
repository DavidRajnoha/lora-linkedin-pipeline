"""
Handles topic extraction from LinkedIn posts.
"""
import os
import openai
from typing import List, Optional
from dotenv import load_dotenv

# Load environment variables (especially OPENAI_API_KEY)
load_dotenv()

# Initialize the OpenAI client (ensure API key is set in .env or environment)
# It's better to initialize it once here if possible, or handle it within functions
# For simplicity and testability with mocking, we might initialize it inside extract_topic
# client = openai.OpenAI()

def extract_topic(post: str, model: str = "gpt-3.5-turbo", temperature: float = 0.2) -> str:
    """
    Extracts the main topic from a single LinkedIn post using an LLM.

    Args:
        post: The text content of the LinkedIn post.
        model: The OpenAI model to use for extraction.
        temperature: The sampling temperature for the LLM.

    Returns:
        The extracted topic as a string.
        Returns "General" if the post is empty or whitespace.
        Raises openai.APIError if the API call fails.
    """
    if not post or post.isspace():
        return "General"
        
    try:
        # Initialize client here to ensure API key is loaded and allow easy mocking
        client = openai.OpenAI()
        
        # Define the system message to guide the LLM
        system_prompt = (
            "You are an expert assistant skilled in analyzing text and extracting the core topic. "
            "Identify the main subject or theme of the following LinkedIn post. "
            "Respond with only the topic name (e.g., 'Artificial Intelligence', 'Marketing Strategy', 'Software Development'). "
            "Keep the topic concise, ideally 2-4 words."
        )
        
        # Call the OpenAI API
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": post}
            ],
            temperature=temperature,
            max_tokens=20 # Limit the response length for topic extraction
        )
        
        # Extract the topic from the response
        topic = response.choices[0].message.content.strip()
        return topic
        
    except openai.APIError as e:
        # Log the error or handle it as needed, here we re-raise for the test
        print(f"OpenAI API error during topic extraction: {e}")
        raise e
    except Exception as e:
        # Catch other potential exceptions
        print(f"An unexpected error occurred during topic extraction: {e}")
        # Decide how to handle unexpected errors, maybe return a default or raise
        return "Error: Extraction Failed" # Or re-raise e


def batch_extract_topics(posts: List[str], model: str = "gpt-3.5-turbo", temperature: float = 0.2) -> List[str]:
    """
    Extracts topics from a list of LinkedIn posts.

    Args:
        posts: A list of post content strings.
        model: The OpenAI model to use.
        temperature: The sampling temperature for the LLM.

    Returns:
        A list of extracted topics corresponding to the input posts.
    """
    # Simple sequential implementation for now
    topics = [extract_topic(post, model=model, temperature=temperature) for post in posts]
    return topics