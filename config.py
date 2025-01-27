from environs import Env
env=Env
env.read_env()

BOT_TOKEN=env.str("ghjkjhgh")
ADMINS=env.list("ADMINS")
CHANNELS=("-1002481389891")