# chat_api/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated  # Optional: Add authentication
from openai import OpenAI, APIError, RateLimitError, APIConnectionError
from django.conf import settings
import logging

# Set up logging
logger = logging.getLogger(__name__)

# Initialize the OpenAI client once
try:
    client = OpenAI(api_key=settings.OPENAI_API_KEY)
except (AttributeError, ValueError) as e:
    logger.error(f"Failed to initialize OpenAI client: {e}")
    client = None

class AIChatView(APIView):
    """
    Handles POST requests to get a response from the AI model.
    This view does NOT store any conversation history.
    """
    
    # Optional: Add authentication if needed
    # permission_classes = [IsAuthenticated]
    
    def post(self, request):
        # 1. Configuration Check
        if not client:
            return Response(
                {"error": "OpenAI client is not configured. Check your OPENAI_API_KEY in .env."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )

        # 2. Get and validate user message
        user_message = self._validate_message(request)
        if isinstance(user_message, Response):
            return user_message

        # 3. Get optional parameters
        system_prompt = request.data.get('system_prompt', "You are a helpful and friendly assistant.")
        model = request.data.get('model', 'gpt-3.5-turbo')
        max_tokens = request.data.get('max_tokens', 500)

        # 4. Structure the conversation
        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_message},
        ]

        # 5. Call the OpenAI API
        return self._call_openai_api(messages, model, max_tokens)

    def _validate_message(self, request):
        """Validate the incoming message"""
        try:
            user_message = request.data.get('message', '').strip()
            if not user_message:
                return Response(
                    {"error": "No 'message' provided in the request body."},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            # Optional: Check message length
            if len(user_message) > 4000:
                return Response(
                    {"error": "Message too long. Maximum 4000 characters allowed."},
                    status=status.HTTP_400_BAD_REQUEST
                )
                
            return user_message
            
        except Exception as e:
            logger.error(f"Error validating message: {e}")
            return Response(
                {"error": "Invalid request data format."},
                status=status.HTTP_400_BAD_REQUEST
            )

    def _call_openai_api(self, messages, model, max_tokens):
        """Make the API call to OpenAI with enhanced error handling"""
        try:
            chat_completion = client.chat.completions.create(
                model=model,
                messages=messages,
                max_tokens=max_tokens,
                temperature=0.7,  # Add creativity control
            )
            
            # Extract response
            ai_response = chat_completion.choices[0].message.content
            
            # Optional: Log usage for monitoring
            logger.info(f"OpenAI API call completed. Model: {model}, Tokens used: {chat_completion.usage.total_tokens}")
            
            return Response(
                {
                    "message": ai_response,
                    "model": model,
                    "usage": {
                        "total_tokens": chat_completion.usage.total_tokens,
                        "prompt_tokens": chat_completion.usage.prompt_tokens,
                        "completion_tokens": chat_completion.usage.completion_tokens,
                    }
                },
                status=status.HTTP_200_OK
            )

        except RateLimitError as e:
            logger.error(f"OpenAI rate limit exceeded: {e}")
            return Response(
                {"error": "Rate limit exceeded. Please try again later."},
                status=status.HTTP_429_TOO_MANY_REQUESTS
            )
        except APIConnectionError as e:
            logger.error(f"OpenAI connection error: {e}")
            return Response(
                {"error": "Connection error. Please try again."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except APIError as e:
            logger.error(f"OpenAI API error: {e}")
            return Response(
                {"error": "AI service temporarily unavailable."},
                status=status.HTTP_503_SERVICE_UNAVAILABLE
            )
        except Exception as e:
            logger.error(f"Unexpected error in OpenAI API call: {e}")
            return Response(
                {"error": "An unexpected error occurred. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )