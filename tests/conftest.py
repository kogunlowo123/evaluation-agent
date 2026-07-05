"""Test configuration for Evaluation Agent."""

import pytest


@pytest.fixture
def agent_config():
    return {"name": "evaluation-agent", "category": "AI Engineering"}
