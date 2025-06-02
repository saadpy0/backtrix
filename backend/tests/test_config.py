from app.core.config import settings

def test_settings():
    """Test that settings are loaded correctly."""
    assert settings.SUPABASE_URL is not None
    assert settings.SUPABASE_SERVICE_KEY is not None
    print("Settings loaded successfully!")
    print(f"SUPABASE_URL: {settings.SUPABASE_URL}")
    print(f"SUPABASE_SERVICE_KEY: {settings.SUPABASE_SERVICE_KEY[:10]}...")  # Only print first 10 chars for security

if __name__ == "__main__":
    test_settings() 