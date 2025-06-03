from fastapi import APIRouter, HTTPException, Depends, Header
from pydantic import BaseModel, EmailStr
from typing import Optional
import logging

from app.db.supabase_client import get_supabase_client
from app.schemas.user import UserCreate, UserLogin, UserResponse
from app.security.utils import get_current_user

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/signup", response_model=UserResponse)
async def signup(user_data: UserCreate):
    """
    Register a new user with email and password.
    """
    logger.info(f"Received signup request for email: {user_data.email}")
    supabase = get_supabase_client()
    logger.info("About to call supabase.auth.sign_up")
    try:
        response = supabase.auth.sign_up({
            "email": user_data.email,
            "password": user_data.password
        })
        logger.info(f"Supabase sign_up call response: {response}")
        if response.user:
            logger.info("Supabase sign_up call succeeded, user created.")
            return UserResponse(
                id=response.user.id,
                email=response.user.email,
                created_at=response.user.created_at,
                access_token=response.session.access_token if response.session else None,
                refresh_token=response.session.refresh_token if response.session else None
            )
        else:
            logger.error(f"Supabase sign_up call failed, response: {response}")
            raise HTTPException(
                status_code=400,
                detail="Failed to create user"
            )
    except Exception as e:
        logger.error(f"Error during signup: {str(e)}")
        error_msg = str(e)
        if "User already registered" in error_msg:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
        elif "Password should be at least 6 characters" in error_msg:
            raise HTTPException(
                status_code=400,
                detail="Password must be at least 6 characters long"
            )
        else:
            raise HTTPException(
                status_code=400,
                detail=str(e)
            )

@router.post("/login", response_model=UserResponse)
async def login(user_data: UserLogin):
    """
    Login a user with email and password.
    Returns user info and session tokens.
    """
    logger.info(f"Received login request for email: {user_data.email}")
    supabase = get_supabase_client()
    logger.info("About to call supabase.auth.sign_in_with_password")
    try:
        response = supabase.auth.sign_in_with_password({
            "email": user_data.email,
            "password": user_data.password
        })
        logger.info(f"Supabase sign_in_with_password response: {response}")
        
        if not response:
            logger.error("Login failed: Empty response from Supabase")
            raise HTTPException(
                status_code=401,
                detail="Authentication failed"
            )
            
        if not response.user:
            logger.error("Login failed: No user in response")
            raise HTTPException(
                status_code=401,
                detail="User not found"
            )
            
        if not response.session:
            logger.error("Login failed: No session in response")
            raise HTTPException(
                status_code=401,
                detail="Session creation failed"
            )
            
        logger.info("Login successful")
        return UserResponse(
            id=response.user.id,
            email=response.user.email,
            created_at=response.user.created_at,
            access_token=response.session.access_token,
            refresh_token=response.session.refresh_token
        )
            
    except Exception as e:
        logger.error(f"Error during login: {str(e)}")
        error_msg = str(e)
        if "Invalid login credentials" in error_msg:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        elif "Email not confirmed" in error_msg:
            raise HTTPException(
                status_code=401,
                detail="Please confirm your email before logging in"
            )
        elif "Invalid email" in error_msg:
            raise HTTPException(
                status_code=400,
                detail="Invalid email format"
            )
        elif "Password should be at least 6 characters" in error_msg:
            raise HTTPException(
                status_code=400,
                detail="Password must be at least 6 characters long"
            )
        else:
            raise HTTPException(
                status_code=401,
                detail=f"Authentication failed: {error_msg}"
            ) 

@router.get("/me", response_model=UserResponse)
async def get_me(current_user = Depends(get_current_user)):
    """
    Get current user information
    """
    logger.info(f"Getting user info for: {current_user.user.email}")
    
    return UserResponse(
        id=current_user.user.id,
        email=current_user.user.email,
        created_at=current_user.user.created_at,
        access_token=None,  # We don't have access to the token here
        refresh_token=None  # We don't have access to the refresh token here
    ) 