"""
Base agent class for all specialized agents
"""

from abc import ABC, abstractmethod
from typing import Dict, Any


class BaseAgent(ABC):
    """Abstract base class for security agents"""
    
    def __init__(self, name: str, memory_manager):
        self.name = name
        self.memory = memory_manager
    
    @abstractmethod
    async def execute(self, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute agent task with given context"""
        pass
