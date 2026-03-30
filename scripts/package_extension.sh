#!/bin/zsh

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
EXTENSION_DIR="$PROJECT_DIR"
DIST_DIR="$PROJECT_DIR/dist"
PACKAGE_DIR="$DIST_DIR/package"
VERSION="$(PROJECT_DIR="$PROJECT_DIR" python3 - <<'PY'
import json
import os
from pathlib import Path
manifest = json.loads((Path(os.environ["PROJECT_DIR"]) / "manifest.json").read_text())
print(manifest["version"])
PY
)"
ZIP_NAME="RightCount-$VERSION.zip"
ZIP_PATH="$DIST_DIR/$ZIP_NAME"

rm -rf "$PACKAGE_DIR" "$ZIP_PATH"
mkdir -p "$PACKAGE_DIR/icons" "$DIST_DIR"

cp "$EXTENSION_DIR/manifest.json" "$PACKAGE_DIR/"
cp "$EXTENSION_DIR/content.js" "$PACKAGE_DIR/"
cp "$EXTENSION_DIR/placement-core.js" "$PACKAGE_DIR/"
cp "$EXTENSION_DIR/icons/"*.png "$PACKAGE_DIR/icons/"

(
  cd "$PACKAGE_DIR"
  zip -qr "$ZIP_PATH" .
)

echo "Created package: $ZIP_PATH"
