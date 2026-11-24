"""Write the entry text for make.fun bounty u-gudril-cool-two-lines-of-morning-light-ade94fc5."""

import os
import sys
from pathlib import Path

TEXT = "The cat has not moved since six.\nThe square of light has, and takes her with it."

assert 1 <= len(TEXT) <= 280

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.environ.get("OUTPUT_DIR", "/output")
output_path = Path(output_dir) / "entry.txt"
output_path.parent.mkdir(parents=True, exist_ok=True)
output_path.write_bytes(TEXT.encode("utf-8"))
print(len(TEXT), file=sys.stderr)
