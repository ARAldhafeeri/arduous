from runner.arduous import Arduous
from runner.logger import ArduousLogger
from runner.events import LoggerEvents
from runner.helpers import trace

arduous = Arduous()

logger = arduous.configure_logger()

arduous_logger = ArduousLogger(logger)

logger_events = LoggerEvents(arduous_logger)

logger_subs_activate = logger_events.logger_subs_activate


trace(logger_subs_activate,all=True)
