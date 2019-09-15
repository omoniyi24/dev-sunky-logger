from error.deverror import DevError
from info.devinfo import DevInfo
from sunkylog import SunkyLog
from warning.warning import DevWarning


class test:
    # log_err = SunkyLog()
    # log_err.dev_error("good")

    # log_info = SunkyLog()
    # log_info.dev_info("good")

    log_warn = SunkyLog()
    log_warn.dev_warn("bad")