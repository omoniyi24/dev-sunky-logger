from error.deverror import DevError
from info.devinfo import DevInfo
from warning.warning import DevWarning


class SunkyLog:

    def dev_error(self, msg):
        log_err = DevError()
        return log_err.dev_error(msg)

    def dev_info(self, msg):
        log_info = DevInfo()
        return log_info.dev_info(msg)

    def dev_warn(self, msg):
        log_warn = DevWarning()
        return log_warn.dev_warn(msg)

