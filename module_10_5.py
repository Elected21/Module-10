import datetime
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while file.readline():
            all_data.append(file.readline())

filenames = [f'./file {number}.txt' for number in range(1, 5)]

# start = datetime.datetime.now()
# for i in filenames:
#     read_info(i)
# end = datetime.datetime.now()
# print(end - start) # 0:00:03.924301

if __name__ == '__main__':

    start = datetime.datetime.now()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start) # 0:00:01.561274