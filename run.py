from app import main, client


if __name__ == '__main__':
        client.loop.set_debug(True)
        client.loop.run_until_complete(main())



