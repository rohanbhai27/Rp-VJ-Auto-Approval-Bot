# Don't Remove Credit @RnpUpdate
# Subscribe YouTube Channel For Amazing Bot @RnpDeveloper
# Ask Doubt on telegram @MrRnp


from os import path, getenv

class Config:
    API_ID = int(getenv("API_ID", "1573160"))
    API_HASH = getenv("API_HASH", "1d01fb2352b99803ef08638c1d671a2f")
    BOT_TOKEN = getenv("BOT_TOKEN", "6665785453:AAESaB-IvP2jekrakszG6mhYg3gk8Zor36s")
    FSUB = getenv("FSUB", "RnpUpdates")
    CHID = int(getenv("CHID", "-1002055258280"))
    SUDO = list(map(int, getenv("SUDO", "5970509661").split()))
    MONGO_URI = getenv("MONGO_URI", "mongodb+srv://TestBot:347027@cluster0.vhjfsa4.mongodb.net/?retryWrites=true&w=majority")
    
cfg = Config()

# Don't Remove Credit @RnpUpdate
# Subscribe YouTube Channel For Amazing Bot @RnpDeveloper
# Ask Doubt on telegram @MrRnp
