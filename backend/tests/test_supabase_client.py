from app.db.supabase_client import supabase

def test_supabase_client():
    """Test that Supabase client is initialized correctly."""
    try:
        # Just verify the client object exists and has the expected attributes
        assert hasattr(supabase, 'auth')
        assert hasattr(supabase, 'table')
        print("Supabase client initialized successfully!")
    except Exception as e:
        print(f"Error testing Supabase client: {str(e)}")
        raise

if __name__ == "__main__":
    test_supabase_client() 