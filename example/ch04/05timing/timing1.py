from timeit import timeit

setup = 'from datetime import datetime'
statement = 'datetime.now()'
result = timeit(setup=setup, stmt=statement, number=1000)
print(f'実行時間の平均：{result / 1000}s == {result}ms')
