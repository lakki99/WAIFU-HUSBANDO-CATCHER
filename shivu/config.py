class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "1398386014"
    sudo_users = "6845325416", "6765826972"
    GROUP_ID = -1003916718652
    TOKEN = "6707490163:AAHZzqjm3rbEZsObRiNaT7DMtw_i5WPo_0o"
    mongo_url = "mongodb+srv://emledhu:emledhu44002@cluster0.op8secv.mongodb.net/?appName=Cluster0"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "Collect_em_support"
    UPDATE_CHAT = "Collect_em_support"
    BOT_USERNAME = "Collect_Em_AllBot"
    CHARA_CHANNEL_ID = "-1003592743292"
    api_id = 34686174
    api_hash = "a3b87284000993c5959da76ce0d48caf"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
