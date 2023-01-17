from bot import start_bot

if __name__ == "__main__":
    try:
        start_bot()
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')