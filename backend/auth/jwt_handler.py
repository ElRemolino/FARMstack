# This file is responsible for signing, enconding, decoding and returning JWTs.
import time
import jwt
from decouple import config


JWT_SECRET = config("secret")
JWT_AlGORITHM = config("algorithm")

# returns the generated Token
def token_response(token: str):
    return {
        "access token" : token
    }

# signs the JWT string
def signJWT(userID: str):
    payload = {
        "userID": userID,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_AlGORITHM)
    return token_response(token)

def decodeJWT(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_AlGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}