def answer(array):
    # Split major/minor/revision into indeces
    l = list(array)
    if l:
        # Convert version strings to version arrays
        for index,string in enumerate(l):
            l[index] = [int(x) for x in string.split(".")]
            # Ensures that shorter versions sort higher
            while len(l[index]) < 3:
                l[index].append(None) # None < 0
        # Call sorting algorithm on new version array
        output = version_sort(l)
        print output
        return output
    else:
        print "Invalid input. Exiting."
        quit()
    
def version_sort(array):
    # Merge sort customized for this 2D list
    array_len = len(array)
    # Cannot divide further
    if array_len <= 1: 
        return array
    middle = array_len // 2
    left = version_sort(array[:middle])
    right = version_sort(array[middle:])
    merged = []
    # Data needed to iterate through sorted lists
    # Potentially wasteful
    len_left = len(left)
    len_right = len(right)
    i,j = 0,0
    ver_a = None
    ver_b = None
    ver_small = None
    # Potentially shakey logic
    while True: 
        # If left value was not appended to merge
        if (not ver_a) and i < len_left:
            ver_a = left[i]
            i += 1
        # If right value was not appended to merge
        if (not ver_b) and j < len_right: 
            ver_b = right[j]
            j += 1
        # Choose smallest of two versions
        ver_small = smallest(ver_a,ver_b)
        if ver_small:
            merged.append(ver_small)
            # Open up left or right placeholders
            # Ordering matters! Considers edge case in smallest()
            if ver_small == ver_a:
                ver_a = None
            elif ver_small == ver_b:
                ver_b = None
        # When left and right values have been exhausted
        else:
            return merged

def smallest(ver_a = [], ver_b = []):
    if ver_a and ver_b:
        # Using zip to make iterative tuples?
        for a,b in zip(ver_a,ver_b):
            if a < b:
                return ver_a
            elif a > b:
                return ver_b
        else:
            # Edge case: When both are equal, return left
            return ver_a
    # In case of shitty method parameters
    elif ver_a:
        return ver_a
    elif ver_b:
        return ver_b
    else:
        return None

answer({"1.1", "0.2", "3", "3.0", "1.2.3", "0.1.9"})
