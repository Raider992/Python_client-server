from functools import wraps
import inspect
import logging
import utils.log.log_decorator_config


class Trace:

    def __call__(self, func):
        @wraps(func)
        def decorated(*args, **kwargs):
            logger = logging.getLogger('func_tracing_class')
            stack = inspect.stack()
            parent_func = stack[1].function
            arg = f'{args} {kwargs}'
            logger.debug('Функция вызвана',
                         extra={'func_name': func.__name__, 'func_args': arg, 'parent_func': parent_func})
            return func(*args, **kwargs)

        return decorated
