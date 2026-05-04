import logging
import json
from typing import Any, Dict, List, Optional, Union
from uuid import UUID

from langchain_core.callbacks import BaseCallbackHandler
from langchain_core.messages import BaseMessage
from langchain_core.outputs import LLMResult

logger = logging.getLogger(__name__)

class LoggingCallbackHandler(BaseCallbackHandler):
    """Callback handler that logs LLM inputs/outputs and tool invocations at INFO level."""

    def on_chat_model_start(
        self,
        serialized: Dict[str, Any],
        messages: List[List[BaseMessage]],
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Run when LLM starts."""
        for i, message_list in enumerate(messages):
            logger.info(f"--- [LLM PROMPT {i+1}] ---")
            for msg in message_list:
                logger.info(f"Role: {msg.type.upper()}\nContent:\n{msg.content}\n")
            logger.info("-" * 30)

    def on_llm_end(
        self,
        response: LLMResult,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run when LLM ends running."""
        for i, generation_list in enumerate(response.generations):
            logger.info(f"--- [LLM OUTPUT {i+1}] ---")
            for gen in generation_list:
                logger.info(f"{gen.text}\n")
            logger.info("-" * 30)

    def on_tool_start(
        self,
        serialized: Dict[str, Any],
        input_str: str,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        tags: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None,
        inputs: Optional[Dict[str, Any]] = None,
        **kwargs: Any,
    ) -> Any:
        """Run when tool starts running."""
        tool_name = serialized.get("name", "unknown_tool")
        logger.info(f"--- [TOOL CALL: {tool_name}] ---")
        if inputs:
            logger.info(f"Arguments: {json.dumps(inputs, indent=2)}")
        else:
            logger.info(f"Input: {input_str}")
        logger.info("-" * 30)

    def on_tool_end(
        self,
        output: Any,
        *,
        run_id: UUID,
        parent_run_id: Optional[UUID] = None,
        **kwargs: Any,
    ) -> Any:
        """Run when tool ends running."""
        logger.info(f"--- [TOOL OUTPUT] ---")
        logger.info(f"{output}")
        logger.info("-" * 30)
