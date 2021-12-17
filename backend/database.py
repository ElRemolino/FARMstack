from model import UserSchema

import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017');
db = client.pkmnTrainers
collection = db.pkmn



# add pokemon to team

# remove pokemon  from team



