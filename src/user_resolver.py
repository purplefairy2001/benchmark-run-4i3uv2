"""User resolver with LRU-cached permission lookups."""

import functools
from typing import Optional


def _fetch_user_permissions(user_id: int) -> list[str]:
    """Simulate an expensive DB call."""
    return ["read", "write"] if user_id % 2 == 0 else ["read"]


@functools.lru_cache(maxsize=512)
def get_user_permissions(user_id: int) -> list[str]:
    return _fetch_user_permissions(user_id)


def resolve_user(user_id: int, action: str) -> Optional[dict]:
    permissions = get_user_permissions(user_id)
    if action not in permissions:
        return None
    return {"user_id": user_id, "action": action, "allowed": True}
