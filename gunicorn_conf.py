import multiprocessing

bind = '0.0.0.0:18000'
workers = multiprocessing.cpu_count() * 2 + 1