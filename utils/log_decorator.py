from functools import wraps
import logging
import inspect


def config_logger():
    logger = logging.getLogger('func_tracing_class')
    file_handler = logging.FileHandler('utils/log/func_call.log', encoding='utf-8')
    _format = logging.Formatter('%(message)s : %(asctime)s - %(func_name)s - %(func_args)s из %(parent_func)s')
    file_handler.setFormatter(_format)
    logger.addHandler(file_handler)
    logger.setLevel(logging.DEBUG)


class Trace():
    def __init__(self):
        config_logger()

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            res = func(*args, **kwargs)
            logger = logging.getLogger('func_tracing_class')
            stack = inspect.stack()
            parent_func = stack[1].function
            arg = f'{args} {kwargs}'
            logger.debug('Функция вызвана', extra={'func_name': func.__name__, 'func_args': arg, 'parent_func': parent_func})
            return res

        return decorated
