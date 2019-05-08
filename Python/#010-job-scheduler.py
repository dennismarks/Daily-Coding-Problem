from time import sleep


def f():
    print("Hello, world!")


def job_scheduler(f, n):
    """
    Asked by Apple.

    Implement a job scheduler which takes in a function f and an integer n,
    and calls f after n milliseconds.
    """
    delay_in_seconds = n / 1000
    sleep(delay_in_seconds)
    f()


if __name__ == '__main__':
    job_scheduler(f, 3000)

