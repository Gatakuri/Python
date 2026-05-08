from log import LogPrintMixin, LogFileMixin

lp = LogPrintMixin()
lp.log_error("Anything")
lp.log_sucess("Cool")

lf = LogFileMixin()
lf.log_sucess("Very Cool")
lf.log_error("Bad")