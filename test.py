from arduous.arduous import Arduous
from arduous.logger import ArduousLogger
from arduous.events import LoggerEvents
from arduous.decorators import audit_action

arduous = Arduous()

logger = arduous.configure_logger()

arduous_logger = ArduousLogger(logger)

logger_events = LoggerEvents(arduous_logger)

logger_subs_activate = logger_events.logger_subs_activate

# lol why microsft I can not read process ?? 
@audit_action(logger_subs_activate, fans=False, power=False, process=False, temp=False)
def some_func():
    for _ in range(10):
        print("hello")





some_func()