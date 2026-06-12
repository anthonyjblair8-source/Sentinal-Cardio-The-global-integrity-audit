# sentinel_core.py
import logging
import sqlite3
import threading
from contextlib import contextmanager
from datetime import datetime, timezone

# Configure centralized logging
logger = logging.getLogger('SentinelCore')

class SentinelDatabase:
    def __init__(self, db_path='sentinel_data.db'):
        self.db_path = db_path
        self.local = threading.local()

    def get_connection(self):
        # Thread-local connection prevents corruption
        if not hasattr(self.local, 'conn') or self.local.conn is None:
            self.local.conn = sqlite3.connect(self.db_path, check_same_thread=False)
            self.local.conn.execute("PRAGMA journal_mode = WAL")
        return self.local.conn

    @contextmanager
    def cursor(self):
        conn = self.get_connection()
        cur = conn.cursor()
        try:
            yield cur
            conn.commit()
        except Exception as e:
            conn.rollback()
            logger.exception("Database operation failed")
            raise e
        finally:
            cur.close()

def log_event(level, message, context=None):
    """Unified logging for all Sentinel modules."""
    log_msg = f"[{context}] {message}" if context else message
    if level == 'DEBUG': logger.debug(log_msg)
    elif level == 'INFO': logger.info(log_msg)
    elif level == 'WARNING': logger.warning(log_msg)
    elif level == 'ERROR': logger.error(log_msg)
def protected_operation(func):
    """Decorator to ensure operations don't violate integrity."""
    def wrapper(*args, **kwargs):
        # Check if the operation is a "destructive" type
        if kwargs.get('force_delete'):
            log_event('WARNING', 'Destructive directive detected. Integrity protocol triggered.', 'SYSTEM')
            return {"status": "denied", "reason": "Integrity protocol violation"}
        return func(*args, **kwargs)
    return wrapper
