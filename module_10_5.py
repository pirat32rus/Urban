import multiprocessing
import time

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

if __name__ == '__main__':
    filenames = [f'./file {number}.txt' for number in range(1, 5)]

    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    linear_time = time.time() - start_time
    print(f'Линейный вызов: {linear_time:.6f} секунд')

    start_time = time.time()
    with multiprocessing.Pool() as pool:
        pool.map(read_info, filenames)
    parallel_time = time.time() - start_time
    print(f'Многопроцессный вызов: {parallel_time:.6f} секунд')
