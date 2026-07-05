"""Evaluation Agent - Unit Tests."""

import pytest
from src.agent.tools import AgentTools


@pytest.mark.asyncio
async def test_create_eval_suite():
    """Test Create an evaluation suite with test cases and scoring rubrics."""
    tools = AgentTools()
    result = await tools.create_eval_suite(name="test", task_type="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_evaluation():
    """Test Run an evaluation suite against a model or pipeline."""
    tools = AgentTools()
    result = await tools.run_evaluation(eval_suite="test", target="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_compare_models():
    """Test Compare multiple models on the same evaluation suite."""
    tools = AgentTools()
    result = await tools.compare_models(eval_suite="test", models="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_run_safety_eval():
    """Test Run safety and bias evaluation with adversarial test cases."""
    tools = AgentTools()
    result = await tools.run_safety_eval(target="test", safety_categories="test")
    assert result is not None
    assert "status" in result or "tool" in result


@pytest.mark.asyncio
async def test_agent_initialization():
    """Test that the agent initializes correctly."""
    from src.agent.evaluation_agent_agent import EvaluationAgentAgent
    agent = EvaluationAgentAgent()
    assert agent.agent_id is not None
    assert agent._system_prompt is not None
    assert len(agent._tool_dispatch) > 0
