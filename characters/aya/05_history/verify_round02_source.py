#!/usr/bin/env python3
"""Download and verify Aya ROUND 02 source from GitHub (or validate local copy)."""
import argparse
import hashlib
from pathlib import Path
from urllib.request import Request, urlopen

URL = ("https://raw.githubusercontent.com/kanotoAI/character-design-project/"
       "main/characters/aya/03_trials/AYA_ROUND_02_source_candidate.jpeg")
SIZE = 436348
SHA256 = "b345525922e339443b35ec949a65f3dd1022d490983b7585d462ed861f281924"
GIT_BLOB = "e6bd1e827f098df923d59fc219517cb80a780d30"

def verify(data):
    digest = hashlib.sha256(data).hexdigest()
    blob = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    print(f"bytes={len(data)}\nsha256={digest}\ngit_blob_sha={blob}")
    if (len(data), digest, blob) != (SIZE, SHA256, GIT_BLOB):
        raise ValueError("Mismatch: bytes differ from registered ROUND 02 original")
    print("PASS: byte-identical to registered ROUND 02 source")

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--source", type=Path, help="Verify a local file; skip download")
    p.add_argument("--output", type=Path, default=Path("AYA_ROUND_02_verified.jpeg"))
    args = p.parse_args()
    if args.source:
        data = args.source.read_bytes()
    else:
        with urlopen(Request(URL, headers={"User-Agent": "Aya-image-verifier/1.0"}), timeout=30) as r:
            data = r.read()
    verify(data)
    if not args.source:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_bytes(data)
        print(f"saved={args.output}")

if __name__ == "__main__":
    main()
