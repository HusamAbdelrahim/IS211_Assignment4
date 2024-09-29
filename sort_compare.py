import random
import time

# insertion sort algorithm
def insertion_sort(arr):
    start_time = time.time()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1] that are greater than key
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return time.time() - start_time  # Return time taken

# shell sort algorithm
def shell_sort(arr):
    start_time = time.time()
    n = len(arr)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
    return time.time() - start_time  # Return time taken

# python's built-in sort function (Timsort)
def python_sort(arr):
    start_time = time.time()
    arr.sort()  # Use Python's built-in sort
    return time.time() - start_time  # Return time taken

# helper function to generate a random list of positive integers
def generate_random_list(size):
    return [random.randint(1, 10000) for _ in range(size)]

def main():
    sizes = [500, 1000, 5000]  # List sizes
    num_trials = 100  # num of trials per size

    for size in sizes:
        insertion_total_time = 0
        shell_total_time = 0
        python_total_time = 0

        for _ in range(num_trials):
            random_list = generate_random_list(size)

            # insertion sort
            insertion_time = insertion_sort(random_list.copy())
            insertion_total_time += insertion_time

            # shell sort
            shell_time = shell_sort(random_list.copy())
            shell_total_time += shell_time

            # python built-in sort
            python_time = python_sort(random_list.copy())
            python_total_time += python_time

        print(f"For list size {size}:")
        print(f"Insertion Sort took {insertion_total_time / num_trials:.7f} seconds on average")
        print(f"Shell Sort took {shell_total_time / num_trials:.7f} seconds on average")
        print(f"Python Sort took {python_total_time / num_trials:.7f} seconds on average")
        print("-" * 50)

if __name__ == "__main__":
    main()

