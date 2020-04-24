from pathlib import Path
import datetime
import logging
import os


REPORT_PATH = f'{Path(__file__).parents[1]}/reports'


class LogReport:
    def init_report_config(self):
        logging.basicConfig(format="%(asctime)s - [%(name)s] - "
                            "%(levelname)s - %(message)s",
                            filename='dash_api.log',
                            filemode='w',
                            level=logging.DEBUG)
        if not os.path.exists(REPORT_PATH):
            os.makedirs(REPORT_PATH)
        dt = datetime.datetime.now().strftime("%Y-%m-%dT%H:%MZ")
        filename = f'{dt}_report.csv'
        handler = logging.FileHandler(f'{REPORT_PATH}/{filename}')
        log_formatter = logging.Formatter(
            '%(asctime)s.%(msecs)03d,%(size)s,%(message)s', '%H:%M:%S')
        handler.setFormatter(log_formatter)
        logging.getLogger('dash_api').addHandler(handler)

    def end_report(self):
        # restart global logging
        for handler in logging.root.handlers[:]:
            for handler in logging.getLogger('dash_api').handlers[:]:
                logging.getLogger('dash_api').removeHandler(handler)
