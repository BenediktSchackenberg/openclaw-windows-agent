from fastapi import Request, HTTPException

class AuthMiddleware:
    def __init__(self, app):
        self.app = app

    async def __call__(self, scope, receive, send):
        if scope["type"] == "http":
            request = Request(scope, receive)
            api_key = request.headers.get("x-api-key")

            if api_key != "expected-api-key":  # Replace with actual API key logic
                raise HTTPException(status_code=401, detail="Unauthorized")

        await self.app(scope, receive, send)