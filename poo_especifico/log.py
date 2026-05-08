# Abstração
from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt'

class Log:
    def _log(self, msg):
        raise NotImplementedError("Implement the log method.")
    
    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_sucess(self, msg):
        return self._log(f'Sucess: {msg}')



class LogFileMixin(Log):
    def _log(self, msg):
        formated_msg = f'{msg} ({self.__class__.__name__})'
        # Saving on Log
        print('Saving on log:', formated_msg)
        with open(LOG_FILE, 'a') as file:
            file.write(formated_msg)
            file.write('\n')



class LogPrintMixin(Log):
    def _log(self, msg):
        print(f'{msg} ({self.__class__.__name__})')



if __name__ == "__main__":
    lp = LogPrintMixin()
    lp.log_error("Anything")
    lp.log_sucess("Cool")

    lf = LogFileMixin()
    lf.log_sucess("Very Cool")
    lf.log_error("Bad")