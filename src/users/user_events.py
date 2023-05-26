import sys
import json
import requests
from requests import HTTPError, TooManyRedirects


URL_GITHUB_API = "https://api.github.com/"
#JSON_PATH = ".//tokens//token.json"


#def read_json_authorization(json_path=JSON_PATH):
#    """
#    Read json file to get token.
#    """
#    try:
#        with open(json_path, "rt", encoding="utf-8") as f:
#            json_token = f.read()
#    except OSError as err:
#        print("OS error:", err)
#    finally:
#        f.close()
#
#    client_json_token = json.loads(json_token)
#    client_id, client_token = client_json_token["id"], client_json_token#["token"]
#
#    return (client_id, client_token)
#
## asignment id and token
#your_id, your_token = *read_json_authorization(),


def user_public_events(username="cireu"):
    if username is None:
        raise ValueError("username must be not none.")
    elif username is False:
        raise ValueError("username must be not False.")
    else:
        url_concate = URL_GITHUB_API + f'users/{username}/events/public'

    headers={
        "Accept": "application/vnd.github+json",   # `vnd.github`到底什么意思，不过可以换成 `application/json` 
        #"Authorization": f"token {your_token}", 
        'X-GitHub-Api-Version': '2022-11-28'
        }

    # r = requests.get(url=url_concate, headers=headers)
    with requests.request(method='get', url=url_concate, headers=headers) as r:
        if r.status_code == requests.codes.ok:
            return r.json()  # maybe change.
        elif r.status_code in [403, 404]:
            return f"""{r.status_code}, {r.json()['message']}, \nmaybe you try to use a REST API endpoint without a token, \nor with a token that has insufficient permissions."""
        else:
            return f"{r.status_code}, {r.json()['message']}"

def main():
    input_name = input("Input Github username: ")
    try:
        r = requests.get(URL_GITHUB_API + f'users/{input_name}')
        r.raise_for_status()
    except ConnectionError as CE:
        raise CE
    except HTTPError as HE:
        print("HTTPError, The username is not found in Github.")
        raise HE
    except TooManyRedirects as TMR:
        raise TMR
    else:
        print(user_public_events(input_name))
    finally:
        print("\r\nFinished.")
    return 0

# Execute when the module is not initialized from an import statement.
# if __name__ == '__main__':
#     sys.exit(main())
