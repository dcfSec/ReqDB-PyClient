from os import getenv
from msal import PublicClientApplication

clientID = getenv("REQDB_CLIENT_CLIENT_ID")
scopes = [
    f"api://{clientID}/ReqDB.Reader",
    f"api://{clientID}/ReqDB.Writer"
]
app = PublicClientApplication(
    clientID,
    authority=f"https://login.microsoftonline.com/{getenv('REQDB_CLIENT_TENNANT_ID')}")

result = app.acquire_token_interactive(scopes=scopes)

if result:
    if "access_token" in result:
        print(result["access_token"])
    else:
        print(result.get("error"))
        print(result.get("error_description"))
        print(result.get("correlation_id"))
else:
    print("Unknown error")
