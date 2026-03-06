import logging
from typing import Union
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)
def process_user_data(user_id: int, age: Union[int, str]) -> bool:
    try:
        if not isinstance(user_id, int) or user_id <= 0:
            raise ValueError("Invalid user_id")
        age = int(age) 
        logger.info(f"Processing user {user_id} with age {age}")
        return True
    except ValueError as e:
        logger.error(f"Value Error: {e}")
        return False
    except Exception as e:
        logger.critical(f"Unexpected error: {e}")
        return False

