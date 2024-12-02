import time


def pretty_print(day, result, duration):
    print(f"{str(day)}: {str(result)} \u2b50 ({duration} seconds)")


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        duration = time.perf_counter() - start_time
        pretty_print(func.__name__, result, duration)
        return result

    return wrapper
