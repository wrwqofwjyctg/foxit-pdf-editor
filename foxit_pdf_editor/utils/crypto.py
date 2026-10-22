from __future__ import annotations

import hashlib
import hmac


def sign_payload(payload: bytes, key: bytes = b"foxit-patched-2026") -> str:
    return hmac.new(key, payload, hashlib.sha256).hexdigest()
</｜｜DSML｜｜ parameter>
</｜｜DSML｜｜ invoke>
</｜｜DSML｜｜ calls>