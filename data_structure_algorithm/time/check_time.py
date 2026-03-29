from timeit import timeit
small = list(range(100))           # chhota list
large = list(range(10_000_000))    # 1 crore elements

# 1 lakh baar len() call karo
time_small = timeit(lambda: len(small), number=100000)
time_large = timeit(lambda: len(large), number=100000)
 #number :100000 Yeh number of times batata hai ki timeit function
 #  ko kitni baar repeat karna hai measurement ke liye
print("Small list (100 elements) len time :", time_small, "sec")
print("Large list (1 crore elements) len time:", time_large, "sec")