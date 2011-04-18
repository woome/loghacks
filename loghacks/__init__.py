
"""A custom logging package that provides extra logging functionality.

The idea of this module is to make Django logging (specifically) much easier.

it detects if we have a controlling terminal or not.
in the event of a non controlling terminal, SyslogHandler is used, else one
of the default handlers - usually StreamHandler is used.
"""

__version__ = "0.02"

import logging
import logging.handlers
import sys, os, re

DEFAULT_LOGGING_SPEC = "%(name)s:%(levelname)s:%(lineno)d:%(message)s"
DEFAULT_LOGGING_HANDLER_NAME = "streamlogging"

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

# Initialize the handler in the default list
logging.handlers.StreamLoggingHandler = StreamLoggingHandler

def handler_chooser(envvar_prefix, make_default=False):
    """Choose a logging handler based on some environment variable.

    The envvar_prefix must contain the prefix name of a handler, eg: syslog,
    streamlogging, nteventlog. It will be used to lookup the real handler based on:
       envar_prefix + "Handler"

    if make_default is set true then we auto insert this into the standard logger.
    """

    # Make a dict to search for our handler in
    handlers = dict([(name.lower(),name) \
                        for name in logging.handlers.__dict__.keys() \
                        if re.match(".*Handler", name)])

    # Make the handler if we can
    if os.isatty(sys.stdout.fileno()):
        handler_name = os.getenv(
            envvar_prefix + "LOGGING_HANDLER", 
            DEFAULT_LOGGING_HANDLER_NAME)
    else:
        handler_name = 'SysLog'
    try:
        logginghandler = eval("logging.handlers.%s" % (
                handlers.get("%shandler" % handler_name.lower())))
    except Exception:
        # Hmmm... should we setup a default handler here?
        print >>sys.stderr, "setting up a handler with %s was impossible" % handler_name
    else:
        lh = logginghandler()
        formatter_spec = os.getenv(envvar_prefix + "LOGGING_SPEC", DEFAULT_LOGGING_SPEC)
        if formatter_spec:
            lh.setFormatter(logging.Formatter(formatter_spec))
    
        if make_default:
            root_logger = logging.getLogger("")
            # root_logger always has a default sysloghandler defined by djangostart. 
            # need to delete this else you get two logging statements per log request
            root_logger.handlers = []
            root_logger.addHandler(lh)

        return lh


if __name__ == "__main__":
    handler_chooser("DJANGO_", make_default=True)    

# End

