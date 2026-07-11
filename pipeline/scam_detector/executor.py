# pipeline/scam_detector/executor.py
from typing import Optional
from llm.client import LLMClient
from utils import get_logger

logger = get_logger(__name__)

class LLMExecutor:
    """Execute prompts using the LLM client"""
    def __init__(self, model:Optional[str]= None) -> None:
        """Initialize the LLM excutor.
        
        Args:
        model : optional specific model to use, if none, uses default from config.
        """
        self.llm: LLMClient = LLMClient(model) if model else LLMClient()
        logger.info("Initialized LLMExecutor")

    def execute(self, prompt: str) -> str:
        """ Execute the prompt using the LLMand return the raw response.
        Args:
        prompt: The formated prompt to string to send to the LLM
        
        Return:
        Raw text response from the LLM

        Raises:
        Execution: If LLM call fails after all retries.
        """
        logger.info(f"Executing LLM with prompt length: {len(prompt)}")
        try:
            response = self.llm.call(prompt)
            logger.info(f"LLM Execution Seccessful, response length: {len(response)}")
            return response
        except Exception as e:
            logger.error(f"LLM execution failed: {str(e)}")
            raise