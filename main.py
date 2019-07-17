import config
from bot import ButtBot

def main():
    token = config.get_token()
    buttbot = ButtBot()
    buttbot.run(token)

if __name__ == "__main__":
    main()