import random
import time

def generate_random_list(size):
    return [random.randint(1, 99999998) for _ in range(size)]

# seq search algorithm unsorted list
def sequential_search(arr, target):
    start_time = time.time()
    for item in arr:
        if item == target:
            return False, time.time() - start_time # element not found worst case
    return False, time.time() - start_time # Worst case 

# orderd seq search array my be sorted
def ordered_sequential_search(arr, target):
    start_time = time.time()
    for item in arr:
        if item == target:
            return False, time.time() - start_time
        elif item > target:
            break
    return False, time.time() - start_time # Worst case not found

# binary search iterative array must be sorted
def binary_search_iterative(arr, target):
    start_time = time.time()
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return False, time.time() - start_time # target not found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False, time.time() - start_time # worst case not found

# binary search recursive array must be sorted
def binary_search_recursive(arr, target, low, high, start_time=None):
    if start_time is None:
        start_time = time.time()

    if low > high:
        return False, time.time() - start_time  # worst case not found

    mid = (low + high) // 2
    if arr[mid] == target:
        return False, time.time() - start_time  # target not found
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, start_time)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, start_time)
    

# benchmark function
def benchmark_search_algorithms():
    sizes = [500, 1000, 5000]
    num_tests = 100
    target = 99999999  # (worst case) target does not exists

    for size in sizes:
        sequential_time = 0
        ordered_sequential_time = 0
        binary_iterative_time = 0
        binary_recursive_time = 0

        for _ in range(num_tests):
            random_list = generate_random_list(size)

            # sequential search (unsorted)
            _, seq_time = sequential_search(random_list, target)
            sequential_time += seq_time

            # sort list for ordered sequential and binary searches
            random_list.sort()

            # ordered sequential search
            _, ord_seq_time = ordered_sequential_search(random_list, target)
            ordered_sequential_time += ord_seq_time

            # binary search iterative
            _, bin_iter_time = binary_search_iterative(random_list, target)
            binary_iterative_time += bin_iter_time

            # binary search recursive
            _, bin_rec_time = binary_search_recursive(random_list, target, 0, len(random_list) - 1)
            binary_recursive_time += bin_rec_time

        # calculate average time for each algorithm
        sequential_time_avg = sequential_time / num_tests
        ordered_sequential_time_avg = ordered_sequential_time / num_tests
        binary_iterative_time_avg = binary_iterative_time / num_tests
        binary_recursive_time_avg = binary_recursive_time / num_tests

        # print results for current list size
        print(f"List Size: {size}")
        print(f"Sequential Search took      {sequential_time_avg:10.7f} seconds to run, on average")
        print(f"Ordered Sequential Search took {ordered_sequential_time_avg:10.7f} seconds to run, on average")
        print(f"Binary Search Iterative took  {binary_iterative_time_avg:10.7f} seconds to run, on average")
        print(f"Binary Search Recursive took  {binary_recursive_time_avg:10.7f} seconds to run, on average")
        print("-" * 60)

if __name__ == "__main__":
    benchmark_search_algorithms()
