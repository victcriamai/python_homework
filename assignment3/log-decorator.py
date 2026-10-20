# one time setup
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
...
# To write a log record:
logger.log(logging.INFO, "this string would be logged")


def logger_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        logger.log(logging.INFO, f"function: {func.__name__}")
        logger.log(logging.INFO, f"positional parameters: {list(args) if args else 'none'}")
        logger.log(logging.INFO, f"keyword parameters: {kwargs if kwargs else 'none'}")
        logger.log(logging.INFO, f"return:{result}\n")

        return result
    return wrapper


@logger_decorator
def func1():
    print("Hello, World!")

@logger_decorator
def func2(*args):
    return True

@logger_decorator
def func3(**kwargs):
    return logger_decorator


func1()
func2(1, 2, 3)
func3(name = "Victoria", message = "Hi")



    


