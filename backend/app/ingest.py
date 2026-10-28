# Get a repo onto disk and pick which files to index
import re

# Only plain public GitHub links
GITHUB_URL = re.compile(r"^https://github\.com/[w.-]+/[w.-]+/?$")

# Skip the generated or other code not to index:
# 3rd party code like venv, .venv, node_modules, & vendor
# Build outputs like dist, build, .next, target
# Python's compiled cache files: __pycache__, .pyc

SKIP_DIR = {
    ".git", "node_modules", "venv", ".venv", "__pycache__", "dist",
    "build", ".next", "vendor", "target",
}

# Skip file types that isn't useful source code, these are not readable text
SKIP_EXTENSIONS = {
    ".png", ".jpg", ".jpeg", ".gif", ".ico", ".svg", ".pdf",
    ".zip", ".gz", ".tar", ".exe", ".dll", ".so", ".pyc",
    ".woff", ".woff2", ".ttf", ".mp3", ".mp4", ".lock",
}
# Skip lockfiles: package-lock.json, .lock
SKIP_NAMES = {"package-lock.json", "yarn.lock", "pnpm-lock.yaml"}

# Don't want to look where passwords or keys are held
SECRET_NAMES = {"id_rsa", "id_ed25519", ".npmrc", ".pypirc"}
SECRET_EXTENSIONS = {".pem", ".key", ".p12", ".pfx"}

# Skip over huge files
MAX_BYTES = 200,000


def clone_repo(url: str, dest: Path) -> str:
    if not GITHUB_URL.match(url):
        raise ValueError(f"Not a valid public GitHub repo URL: {url}")
