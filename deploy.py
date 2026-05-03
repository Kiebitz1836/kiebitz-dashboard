import base64, json, urllib.request

TOKEN = "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"
OWNER = "Kiebitz1836"
REPO  = "kiebitz-dashboard"
FILE  = "index.html"
SHA   = "fbc06df26a7af3badcdeb5c5e3ae8527dd68c32c"

with open("index.html", "rb") as f:
    content = base64.b64encode(f.read()).decode()

data = json.dumps({
    "message": "Update dashboard design",
    "content": content,
    "sha": SHA
}).encode()

req = urllib.request.Request(
    f"https://api.github.com/repos/{OWNER}/{REPO}/contents/{FILE}",
    data=data, method="PUT",
    headers={
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github.v3+json",
        "Content-Type": "application/json",
        "User-Agent": "deploy-script"
    }
)
resp = urllib.request.urlopen(req)
print("✓ Deployed!", resp.status)
