import logging
import os

os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/risk_engine.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger("risk_engine")