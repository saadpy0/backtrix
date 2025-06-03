from fastapi import HTTPException, Header, Depends, Request
from typing import Optional
import logging

from app.db.supabase_client import get_supabase_client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

async def get_current_user(request: Request):
    """
    Dependency to get current user from JWT token.
    This can be used in any endpoint that requires authentication.
    
    Usage:
        @router.get("/protected-endpoint")
        async def protected_endpoint(current_user = Depends(get_current_user)):
            return {"message": f"Hello {current_user.user.email}"}
    """
    auth_header = request.headers.get("authorization", "")
    if not auth_header.startswith("Bearer "):
        raise HTTPException(
            status_code=401,
            detail="Invalid authorization header"
        )
    
    token = auth_header.split(" ")[1]
    supabase = get_supabase_client()
    
    try:
        # Verify the JWT token and get user
        user = supabase.auth.get_user(token)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )
            
        return user
    except Exception as e:
        logger.error(f"Error verifying token: {str(e)}")
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        ) 