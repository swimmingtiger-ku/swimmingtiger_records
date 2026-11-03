"""수호회 기록실 빌드: 기록 데이터(JSON)를 동아리 비밀번호로 암호화해 index.html 생성.

사용법:
  python3 tools/build_site.py --data data.json --password <동아리 비밀번호>

data.json 형식 (저장소에 올리지 않음):
  {"snap": "11월 3일",
   "log":  [[년도, 성별, 이름, 종목, 기록, 대회, 순위, 규격, 비고], ...],   # '2018~ 기록모음' 탭, 머리글 제외
   "best": [[...], ...]}                                                  # '고려대 기록(2018~)' 탭 A:D 전체
"""
import argparse, base64, json, os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes

ITER = 600_000
here = os.path.dirname(os.path.abspath(__file__))
ap = argparse.ArgumentParser()
ap.add_argument("--data", required=True)
ap.add_argument("--password", required=True)
ap.add_argument("--out", default=os.path.join(here, "..", "index.html"))
a = ap.parse_args()

plain = json.dumps(json.load(open(a.data, encoding="utf-8")), ensure_ascii=False, separators=(",", ":")).encode()
salt, iv = os.urandom(16), os.urandom(12)
key = PBKDF2HMAC(algorithm=hashes.SHA256(), length=32, salt=salt, iterations=ITER).derive(a.password.encode())
ct = AESGCM(key).encrypt(iv, plain, None)
enc = {"salt": base64.b64encode(salt).decode(), "iv": base64.b64encode(iv).decode(), "iter": ITER, "data": base64.b64encode(ct).decode()}
tpl = open(os.path.join(here, "template.html"), encoding="utf-8").read()
open(a.out, "w", encoding="utf-8").write(tpl.replace("__ENC__", json.dumps(enc)))
print("written", a.out, len(ct), "bytes encrypted")
