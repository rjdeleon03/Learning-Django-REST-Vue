import requests


def main():
    response = requests.get("http://www.google.com")
    print("Status Code: ", response.status_code)
    # print("Headers: ", response.headers)
    print("Body: ", response.text)


if __name__ == "__main__":
    main()
