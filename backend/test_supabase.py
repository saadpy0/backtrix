from app.db.supabase_client import get_supabase_client
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def test_supabase_connection():
    try:
        # Get Supabase client
        supabase = get_supabase_client()
        
        # Try a simple query to test connection
        # This will attempt to get the current user (should be None if not authenticated)
        response = supabase.auth.get_user()
        
        logger.info("Successfully connected to Supabase!")
        logger.info(f"Response: {response}")
        return True
    except Exception as e:
        logger.error(f"Failed to connect to Supabase: {str(e)}")
        return False

if __name__ == "__main__":
    test_supabase_connection() 