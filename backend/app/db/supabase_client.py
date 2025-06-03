from supabase import create_client, Client
from app.core.config import settings
from functools import lru_cache

@lru_cache()
def get_supabase_client() -> Client:
    """
    Get a cached Supabase client instance.
    Returns:
        Client: Initialized Supabase client
    """
    return create_client(
        supabase_url=settings.SUPABASE_URL,
        supabase_key=settings.SUPABASE_ANON_KEY  # Use anon key for auth operations
    )

# Create a global client instance
supabase: Client = get_supabase_client() 