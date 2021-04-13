from random import randint

import pandas

from RBTree import RBTree

if __name__ == '__main__':
    def get_stat_arithmetic_progression(n, step):
        count = 0
        counts = []
        iterations = []
        for i in range(n):
            rb = RBTree()
            count = count + step
            for i in range(0, count):
                rb.insert(randint(0, 1000))
            counts.append(count)
            iterations.append(rb.iterations_insert)
        data = dict(length=counts, iterations=iterations)
        df = pandas.DataFrame(data)
        df.to_csv(r'iterations_arith.csv', sep=';', index=False)
        print("Complete!")

    def get_stat_geometric_progression(n, step):
        count = 1
        counts = []
        iterations = []
        for i in range(n):
            rb = RBTree()
            count = count * step
            for i in range(0, count):
                rb.insert(randint(0, 1000))
            counts.append(count)
            iterations.append(rb.iterations_insert)
        data = dict(length=counts, iterations=iterations)
        df = pandas.DataFrame(data)
        df.to_csv(r'iterations_geometric.csv', sep=';', index=False)
        print("Complete!")

    # первое число - количество массивов, второе - шаг прогрессии
    get_stat_arithmetic_progression(100, 3)
    get_stat_geometric_progression(15, 2)

