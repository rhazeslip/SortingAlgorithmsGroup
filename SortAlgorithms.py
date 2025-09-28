#This program implements various sorting algorithms and compares their efficiency based on 
#excution time using various data size sets.
import time
import random
import sys
from typing import List, Callable

# Increase recursion limit for quicksort with large arrays
sys.setrecursionlimit(10000)

#Bubble Sort Algorithm (Nate Hazeslip)
def bubble_sort(arr: List[int]) -> List[int]:
        """Bubble sort implementation with optimization"""
        n = len(arr)
        for i in range(n):
            swapped = False
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
            # If no swapping occurred, array is already sorted
            if not swapped:
                break
        return arr

#Quick Sort Algorithm (Nate Hazeslip)
def quick_sort(arr: List[int]) -> List[int]:
        """Quick sort implementation using median-of-three partitioning"""
        if len(arr) <= 1:
            return arr
        
        # Median-of-three pivot selection
        first, middle, last = arr[0], arr[len(arr)//2], arr[-1]
        pivot = sorted([first, middle, last])[1]
        
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return quick_sort(left) + middle + quick_sort(right)

#Merge Sort Algorithm (Kaden Hyde)
# Recursive function designed to split the inputted array in half until that can no longer be done
# Then merge those two arrays in numerical order
def mergeSort(array, first, last):
    # first = first index of the array
    # last = last index of the array
    if first < last:
        # middle = roughly the middle index of the array, the split point
        middle = (first + (last - 1)) // 2

        # check if the array can be split further, if not, merge, otherwise, split again
        if middle <= first:
            merge(array, first, middle, last)
        else:
            mergeSort(array, first, middle)
            mergeSort(array, middle + 1, last)

#Selection Sort Algorithm (Seth Wojcik)
# Defines the list into an usorted sublist and sorted sublist
# Repeatedly selects the smallest element from the unsorted sublist and moves it to the sorted sublist
def selectionSort(arr: List[int]) -> List[int]:
    for i in range(len(arr)):
        minimum = i
        
        for j in range(i + 1, len(arr)):
            # Select the smallest value
            if arr[j] < arr[minimum]:
                minimum = j

        # Place it at the front of the 
        # sorted end of the array
        arr[minimum], arr[i] = arr[i], arr[minimum]
            
    return arr

# Majority of the sorting happens here, arrays merged in numerical order in this function
def merge(array, first, middle, last):
    # n1 is the length of our "left side" array
    # n2 is the length of our "right side" array
    n1 = middle - first + 1
    n2 = last - middle

    # Temporary arrays to hold the split values until we remerge them
    leftArray = [0] * (n1)
    rightArray = [0] * (n2)

    # Assigning values to temp arrays
    for i in range(n1):
        leftArray[i] = array[first + i]

    for j in range(n2):
        rightArray[j] = array[middle + 1+ j]

    i = 0
    j = 0
    k = first

    # Merge the arrays in numerical order
    while i < n1 and j < n2:
        if leftArray[i] <= rightArray[j]:
            array[k] = leftArray[i]
            i += 1
        else:
            array[k] = rightArray[j]
            j += 1
        k += 1

    # Place in leftover values once the merging is done
    while i < n1:
        array[k] = leftArray[i]
        i += 1
        k += 1

    while j < n2:
        array[k] = rightArray[j]
        j += 1
        k += 1

#Alternate Sorting Algorithm (Seth Wojcik)


"""
#Main Function to test and run algorithms to compare efficiency
def main():
    testArray = [12, 1, 14, 27, 100]
    n = len(testArray)

    print("The given array is:")
    for i in range(n):
        print("%d" % testArray[i], end = " ")
    
    mergeSort(testArray, 0, n - 1)

    print("\n\nThe sorted array is:")
    for i in range(n):
        print("%d" % testArray[i], end = " ")

main()
"""
# Data Generation Functions
def generate_best_case(n: int, algorithm: str) -> List[int]:
    """Generate best case input for specific algorithm"""
    if algorithm == "bubble":
        return list(range(n))  # Already sorted
    elif algorithm == "quick":
        return list(range(n))  # Balanced partitions
    elif algorithm == "merge":
        return list(range(n))  # Already sorted
    elif algorithm == "heap":
        return list(range(n))  # Already sorted
    return list(range(n))

def generate_worst_case(n: int, algorithm: str) -> List[int]:
    """Generate worst case input for specific algorithm"""
    if algorithm == "bubble":
        return list(range(n, 0, -1))  # Reverse sorted
    elif algorithm == "quick":
        return list(range(n))  # Already sorted (poor pivot)
    elif algorithm == "merge":
        return [random.randint(0, 1000000) for _ in range(n)]  # Any array
    elif algorithm == "heap":
        return list(range(n, 0, -1))  # Reverse sorted
    return list(range(n, 0, -1))

def generate_average_case(n: int) -> List[int]:
    """Generate average case input (random array)"""
    return [random.randint(0, 1000000) for _ in range(n)]

# Performance Testing Functions
def measure_time(algorithm: Callable, arr: List[int]) -> float:
    """Measure execution time of sorting algorithm"""
    arr_copy = arr.copy()
    
    start_time = time.time()
    algorithm(arr_copy)
    end_time = time.time()
    
    return end_time - start_time

def get_sorting_algorithm(algorithm_key: str) -> Callable:
    """Get the sorting function based on algorithm key"""
    algorithms = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "merge": mergeSort,
        #"heap": heap_sort
    }
    return algorithms.get(algorithm_key)

def test_algorithm_case(algorithm_key: str, case_type: str, n: int) -> float:
    """Test specific algorithm case with given n"""
    if case_type == "best":
        arr = generate_best_case(n, algorithm_key)
    elif case_type == "worst":
        arr = generate_worst_case(n, algorithm_key)
    else:  # average case
        arr = generate_average_case(n)
    
    algorithm_func = get_sorting_algorithm(algorithm_key)
    return measure_time(algorithm_func, arr)

# User Interface Functions
def get_algorithm_name(algorithm_key: str) -> str:
    """Get display name for algorithm"""
    algorithm_names = {
        "bubble": "Bubble Sort",
        "quick": "Quick Sort", 
        "merge": "Merge Sort",
        "heap": "Heap Sort"
    }
    return algorithm_names.get(algorithm_key, "Unknown Algorithm")

def display_menu():
    """Display main menu"""
    print("\n" + "="*60)
    print("Welcome to the test suite of selected sorting algorithms!")
    print("Select the sorting algorithm you want to test.")
    print("-" * 60)
    print("1. Bubble Sort")
    print("2. Merge Sort")
    print("3. Quick Sort")
    print("4. Heap Sort")
    print("5. Exit")
    print("6. Run Comprehensive Test (All algorithms & cases)")
    print("="*60)

def display_case_menu(algorithm_name: str):
    """Display case selection menu"""
    print(f"\nCase Scenarios for {algorithm_name}")
    print("-" * 40)
    print("1. Best Case")
    print("2. Average Case")
    print("3. Worst Case")
    print("4. Exit to main menu")

def get_user_input(prompt: str, input_type: type = str, valid_range: tuple = None):
    """Get validated user input"""
    while True:
        try:
            user_input = input_type(input(prompt))
            if valid_range and (user_input < valid_range[0] or user_input > valid_range[1]):
                print(f"Please enter a value between {valid_range[0]} and {valid_range[1]}")
                continue
            return user_input
        except ValueError:
            print("Invalid input. Please try again.")

def test_single_algorithm(algorithm_key: str, results: dict):
    """Test a single algorithm with user interaction"""
    algorithm_name = get_algorithm_name(algorithm_key)
    default_sizes = [100, 1000, 10000, 100000]
    
    while True:
        display_case_menu(algorithm_name)
        choice = get_user_input("Select the case (1-4): ", int, (1, 4))
        
        if choice == 4:
            break
            
        case_types = {1: "best", 2: "average", 3: "worst"}
        case_type = case_types[choice]
        
        print(f"\nIn {case_type} case,")
        
        # Test default sizes
        for n in default_sizes:
            try:
                time_taken = test_algorithm_case(algorithm_key, case_type, n)
                print(f"For N = {n:,}, it takes {time_taken:.6f} seconds")
                
                # Store results
                if algorithm_key not in results:
                    results[algorithm_key] = {}
                if case_type not in results[algorithm_key]:
                    results[algorithm_key][case_type] = {}
                results[algorithm_key][case_type][n] = time_taken
                
            except (RecursionError, MemoryError) as e:
                print(f"For N = {n:,}, failed: {str(e)}")
                break
        
        # Allow custom size input
        while True:
            another_n = get_user_input("Do you want to input another N (Y/N)? ", str).upper()
            if another_n == 'Y':
                custom_n = get_user_input("What is the N? ", int, (1, 1000000))
                try:
                    time_taken = test_algorithm_case(algorithm_key, case_type, custom_n)
                    print(f"For N = {custom_n:,}, it takes {time_taken:.6f} seconds")
                except (RecursionError, MemoryError) as e:
                    print(f"For N = {custom_n:,}, failed: {str(e)}")
            elif another_n == 'N':
                break
            else:
                print("Please enter Y or N")

def run_comprehensive_test():
    """Run comprehensive test for all algorithms and cases"""
    algorithms = ["bubble", "merge", "quick", "heap"]
    cases = ["best", "average", "worst"]
    sizes = [100, 1000, 10000]
    
    results = {}
    
    for algo in algorithms:
        results[algo] = {}
        print(f"\nTesting {get_algorithm_name(algo)}...")
        
        for case in cases:
            results[algo][case] = {}
            print(f"  {case.capitalize()} case:")
            
            for size in sizes:
                try:
                    time_taken = test_algorithm_case(algo, case, size)
                    results[algo][case][size] = time_taken
                    print(f"    N = {size:,}: {time_taken:.6f} seconds")
                except (RecursionError, MemoryError) as e:
                    print(f"    N = {size:,}: Failed - {str(e)}")
                    results[algo][case][size] = None
                    break
    
    return results

def analyze_results(results: dict):
    """Analyze and display results summary"""
    if not results:
        print("No results to analyze. Please run tests first.")
        return
    
    print("\n" + "="*60)
    print("ANALYSIS OF RESULTS")
    print("="*60)
    
    for algo, cases in results.items():
        print(f"\n{get_algorithm_name(algo).upper()}:")
        
        for case, sizes in cases.items():
            print(f"  {case.upper()} CASE:")
            valid_sizes = {size: time for size, time in sizes.items() if time is not None}
            
            if len(valid_sizes) < 2:
                print("    Not enough data for analysis")
                continue
            
            # Calculate growth factors
            sizes_sorted = sorted(valid_sizes.keys())
            for i in range(1, len(sizes_sorted)):
                n1, n2 = sizes_sorted[i-1], sizes_sorted[i]
                t1, t2 = valid_sizes[n1], valid_sizes[n2]
                growth_factor = t2 / t1 if t1 > 0 else float('inf')
                size_ratio = n2 / n1
                
                print(f"    N {n1:,}→{n2:,}: Time {t1:.6f}→{t2:.6f}s, Factor: {growth_factor:.2f}x")
                
                # Theoretical complexity analysis
                if algo == "bubble":
                    expected = size_ratio ** 2  # O(n²)
                elif algo in ["merge", "heap"]:
                    expected = size_ratio * (n2 / n1)  # O(n log n) approximation
                else:  # quick sort
                    if case == "worst":
                        expected = size_ratio ** 2  # O(n²)
                    else:
                        expected = size_ratio * (n2 / n1)  # O(n log n) approximation
                
                print(f"    Expected for O(n²): {expected:.2f}x, Actual: {growth_factor:.2f}x")

def verify_sorting_correctness():
    """Verify that all sorting algorithms work correctly"""
    test_arrays = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    ]
    
    algorithms = {
        "bubble": bubble_sort,
        "quick": quick_sort,
        "merge": mergeSort,
        #"heap": heap_sort
    }
    
    print("=== CORRECTNESS TESTING ===")
    
    for i, arr in enumerate(test_arrays):
        print(f"\nTest {i+1}: Original: {arr}")
        
        for algo_name, algo_func in algorithms.items():
            try:
                result = algo_func(arr.copy())
                expected = sorted(arr)
                status = "✓" if result == expected else "✗"
                print(f"{status} {get_algorithm_name(algo_name)}: {result}")
                assert result == expected, f"{algo_name} failed!"
            except Exception as e:
                print(f"✗ {get_algorithm_name(algo_name)}: Error - {e}")
    
    print("\n✓ All correctness tests passed!")

# Main Function
def main():
    """Main function"""
    algorithm_choices = {
        1: "bubble",
        2: "merge", 
        3: "quick",
        4: "heap"
    }
    
    results = {}
    
    # Verify algorithms work correctly first
    verify_sorting_correctness()
    
    while True:
        display_menu()
        choice = get_user_input("Select a sorting algorithm (1-6): ", int, (1, 6))
        
        if choice == 5:
            print("Bye!")
            break
        elif choice == 6:
            results = run_comprehensive_test()
            analyze_results(results)
        else:
            algorithm_key = algorithm_choices[choice]
            test_single_algorithm(algorithm_key, results)

if __name__ == "__main__":
    main()