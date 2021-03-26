import logging

logger = logging.getLogger('func_tracing_class')
file_handler = logging.FileHandler('utils/log/func_call.log', encoding='utf-8')
_format = logging.Formatter('%(message)s : %(asctime)s - %(func_name)s - %(func_args)s из %(parent_func)s')
file_handler.setFormatter(_format)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)
