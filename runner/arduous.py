import logging
class Arduous:

    def configure_logger(
        filename='ARDUOUS.log',
        filemode='a',
        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
        datefmt='%H:%M:%S',
        level=logging.INFO
    ):
        logging.basicConfig(
            filename='ARDUOUS.log',
            filemode='a',
            format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
            datefmt='%H:%M:%S',
            level=logging.INFO
        )
        logger = logging.getLogger('Arduous')
        return logger

    def configure_server(real_time_graphs=True, real_time_logs=True, port_number=8080):
        pass

