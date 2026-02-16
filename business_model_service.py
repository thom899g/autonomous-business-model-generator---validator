from typing import Dict, Optional
import logging
from .generator.business_model_generator import BusinessModelGenerator
from .validator.business_model_validator import BusinessModelValidator

class BusinessModelService:
    """
    Service class to generate and validate business models.
    
    Attributes:
        generator (BusinessModelGenerator): Instance of the business model generator.
        validator (BusinessModelValidator): Instance of the business model validator.
    """

    def __init__(self, knowledge_base):
        self.generator = BusinessModelGenerator(knowledge_base)
        self.validator = BusinessModelValidator()

    def generate_and_validate_model(self, market_trend_data: Dict) -> Dict:
        """
        Generates a new business model and validates it.
        
        Args:
            market_trend_data (Dict): Market trend data to base the model on.
            
        Returns:
            Dict: Validated business model if successful.
            
        Raises:
            Exception: If generation or validation fails.
        """
        try:
            # Generate new model
            new_model =