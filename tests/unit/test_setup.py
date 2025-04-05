"""
Test module to verify the project environment is set up correctly.
"""
import pytest
import sys
from pathlib import Path
from src.main import app


def test_main():
    """Test that the main function can be imported."""
    assert app()


def test_python_version():
    """Test that Python version is at least 3.11."""
    assert sys.version_info.major == 3
    assert sys.version_info.minor >= 11


def test_project_structure():
    """Test that the basic project structure exists."""
    # Get the project root directory (2 levels up from this test file)
    project_root = Path(__file__).parent.parent.parent
    
    # Check that essential directories exist
    # assert (project_root / "src").is_dir()
    # assert (project_root / "tests").is_dir()
    # assert (project_root / "src" / "cli").is_dir()
    # assert (project_root / "src" / "data_processing").is_dir()
    # assert (project_root / "src" / "training").is_dir()
    # assert (project_root / "src" / "generation").is_dir()
    
    # Check that essential files exist
    assert (project_root / "pyproject.toml").is_file()
    assert (project_root / "README.md").is_file()

