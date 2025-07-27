import logging


class LoggerManager:
    def __init__(self, filename, file_log_level=logging.DEBUG, console_log_level=logging.INFO, name=__name__):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(logging.DEBUG)  # Set the logger's level to the lowest one needed (DEBUG)

        # Create handlers
        self.file_handler = logging.FileHandler(filename, mode='w', encoding='utf-8')
        self.console_handler = logging.StreamHandler()

        # Set levels for handlers
        self.file_handler.setLevel(file_log_level)  # By default, log everything to the file
        self.console_handler.setLevel(console_log_level)  # By default, log only INFO or higher to the console

        # Create formatters and add them to the handlers
        log_format = '%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(message)s'
        formatter = logging.Formatter(log_format)

        self.file_handler.setFormatter(formatter)
        self.console_handler.setFormatter(formatter)

        # Add the handlers to the logger
        # (old) if not self.logger.hasHandlers():  # Avoid duplicate handlers
        if not self.logger.handlers:  # Avoid duplicate handlers
            self.logger.addHandler(self.file_handler)
            self.logger.addHandler(self.console_handler)
        self.logger.propagate = True  # Ensure that the logs propagate properly. If duplicated change it to False

    def set_console_level(self, level):
        """Set the logging level for the console handler."""
        self.console_handler.setLevel(level)

    def set_file_level(self, level):
        """Set the logging level for the file handler."""
        self.file_handler.setLevel(level)

    def get_logger(self):
        """Return the logger instance."""
        return self.logger


if __name__ == '__main__':
    logger = LoggerManager(filename='run_cli.log').get_logger()
    logger.info(f"Start logging....")
