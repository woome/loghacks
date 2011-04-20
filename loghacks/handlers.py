import logging
import sys

class StreamLoggingHandler(logging.StreamHandler):
    """A new stream logging handler that fixed problems with pythons default.

    On close the handler catches exceptions with clean up so as not to cause
    fatal messages about the underlying stream having gone away.
    """

    def __init__(self, *args):
        logging.StreamHandler.__init__(self, *args)
    
    def flush(self):
        try:
            logging.StreamHandler.flush(self)
        except Exception:
            print >>sys.stderr, "an error occured closing up the stream handler"

    def close(self):
        try:
            logging.StreamHandler.flush(self)
        except Exception:
            print >>sys.stderr, "an error occured closing up the stream handler"

# End

