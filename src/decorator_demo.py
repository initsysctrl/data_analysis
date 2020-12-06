import time
import functools


def timer_super(max_time=1):  # 在原装饰器上继续套娃，增加装饰器参数
    def timer(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            print(f"函数{func.__name__} 消耗时间 {end_time-start_time}")
            if (end_time-start_time) > max_time:
                print(f"超过最大耗时 {max_time}s")
            return result
        return wrapper
    return timer


@timer_super(0.5)
def func(x, y):
    print('执行fun 函数...')
    time.sleep(1)
    return x+y  # 核心函数有输出


result = func(1024, 996)
print(f"核心函数输出:{result}")
print(f"调用函数名称为：{func.__name__}")
