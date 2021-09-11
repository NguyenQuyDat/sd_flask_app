import config


def get_log():
    """Get a specific number of the last lines of the log file."""
    log_path = config.Config.LOG_FILE_PATH
    nr_lines = config.Config.NR_DISPLAY_LOG_LINES
    log_text = None
    try:
        with open(log_path, "r") as file:
            log_text = list(file)[-nr_lines:]
    except FileExistsError:
        pass

    return log_text
