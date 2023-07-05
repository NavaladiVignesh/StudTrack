from django.db import connections
from django.db.utils import OperationalError


def test_connection():
    db_conn = connections['default']
    try:
        c = db_conn.cursor()
    except OperationalError:
        return False
    else:
        return True