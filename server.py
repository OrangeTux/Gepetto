#!/usr/bin/env python
import os
from app import app


if __name__ == '__main__':
    host = None

    if 'GEPETTO_ENV' in os.environ and 'GEPETTO_ENV' == 'prod':
        # When host is set to 0.0.0.0 server is available externally.
        host = '0.0.0.0'

    app.run(host=host)
