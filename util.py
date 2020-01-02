import math
import pandas as pd


def get_first_digit(number):
    if number == 0:
        return number
    number = math.fabs(number)
    zeros = math.log(number, 10)
    result = math.floor(number / 10 ** math.floor(zeros))
    return result if result < 10 else get_first_digit(result)   #occasionally rounding error causes this to be 10, not 10; for example number = 1000.0


def examine_first_digits(histogram: pd.Series):
    import matplotlib.pyplot as plt

    fd = pd.Series(histogram.values).apply(get_first_digit)
    fd_counts = fd.value_counts()
    print(fd_counts)
    for i in range(1, len(fd_counts)):
        print(fd_counts.iloc[i - 1] / fd_counts.iloc[i])
    plt.bar(fd_counts.index, fd_counts.values)
    plt.show()


def do_stocks_first_digit():
    """
    This isn't a utility function, just something that uses the first digit thing.
    :return:
    """
    # TODO: move this function somewhere else.
    import stocks_lump
    import matplotlib.pyplot as plt
    sp = stocks_lump.get_sp_500()
    sp['diff_amt_fd'] = sp.diff_amt.apply(get_first_digit)
    print(sp.head())
    fd = sp.diff_amt_fd.value_counts()
    plt.bar(fd.index, fd.values)
    print(fd)
    plt.show()


do_stocks_first_digit()
