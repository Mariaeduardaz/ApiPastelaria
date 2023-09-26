from fastapi import Header, HTTPException
from settings import X_TOKEN, X_KEY
async def verify_token(x_token: str = Header()):
  if x_token != X_TOKEN:
    raise HTTPException(status_code=400, detail="X-Token header invalid")

async def verify_key(x_key: str = Header()):
  if x_key != X_KEY:
    raise HTTPException(status_code=400, detail="X-Key header invalid")
  return x_key