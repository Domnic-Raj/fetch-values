import os

from base64 import b64encode
from nacl import encoding, public

key = os.getenv("key")
#print(key)
def encrypt(public_key: str, secret_value: str) -> str:
  """Encrypt a Unicode string using the public key."""
  public_key = public.PublicKey(public_key.encode("utf-8"), encoding.Base64Encoder())
  sealed_box = public.SealedBox(public_key)
  encrypted = sealed_box.encrypt(secret_value.encode("utf-8"))
  return b64encode(encrypted).decode("utf-8")

encrypted_secret = encrypt(key, "team_new1")
print(encrypted_secret)
with open("env_vars.sh", "w") as file:
    file.write(f"export encrypted_secret={encrypted_secret}\n")
