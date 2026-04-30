"""Configuration constants for the flight cache system."""
import os
from pathlib import Path

# Airport config — change this per repo
AIRPORT = os.environ.get("AIRPORT", "SNN")

# Paths
CACHE_DIR = Path.home() / ".flightcache"
DB_PATH = CACHE_DIR / "flights.db"
LOG_PATH = CACHE_DIR / "refresh.log"
LOCK_PATH = CACHE_DIR / "refresh.lock"

# Rate limiting — adaptive (see rate_limiter.py LEVELS)
MIN_DELAY = 0.5
MAX_DELAY = 1.0

# Backoff on errors
BACKOFF_INITIAL = 60
BACKOFF_MULTIPLIER = 2
BACKOFF_MAX = 600
MAX_CONSECUTIVE_ERRORS = 5

CHROME_VERSIONS = ["chrome_100", "chrome_104", "chrome_116", "chrome_120"]

CONSENT_COOKIES = [
    "CONSENT=YES+cb.20210328-17-p0.en+FX+987; SOCS=CAISHAgDEhJnd3NfMjAyNjAzMjEtMF9SQzIaAmVuIAEaBgiVg_rNBg",
    "CONSENT=YES+cb.20210420-09-p0.en+FX+112; SOCS=CAISHAgDEhJnd3NfMjAyNjAzMjAtMF9SQzIaAmVuIAEaBgiVg_rNBg",
    "CONSENT=YES+cb.20210515-14-p0.en+FX+555; SOCS=CAISHAgDEhJnd3NfMjAyNjAzMTktMF9SQzIaAmVuIAEaBgiVg_rNBg",
]
