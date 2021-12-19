from basic import Basic

basic = Basic()


def getAccessToken():
    return basic.get_access_token()


if __name__ == "__main__":
    basic.run()