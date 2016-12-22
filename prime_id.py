import sys
import math

'''
This program is my implementation from Level 1 of Google's foo.bar.

Thoughts:
- I am still unsure if calling answer() at the bottom of this script is the best approach.
- Obviously, not every edge case is considered, but it seems to work well.
- Specifications informed me that this should work for 0 < n < 10000 but it should work for any integer input.

Where can I optimize? 
- I can implement a skip-list type approach... If I know that we can skip to the xth prime for all n > some value... saves me the time of calculating the 0th -> (x-1)th primes.
- Caching past-generated primes
- Exploring better prime-generating algorithms
'''

def answer(n):
    n = int(n)
    prime_array = [] # Holding array of prime numbers
    prime_char_len = 0 # Tracking effective length of prime string
    prime_str = "" # Concatenates all primes into single string
    used_ids = {} # Keeping record of used IDs
    last_prime = 2

    # Build array of primes
    while prime_char_len < (n + 5):
        prime_array.append(str(last_prime))
        prime_char_len += len(str(last_prime))
        last_prime = next_prime(last_prime)
    prime_str = "".join(map(str,prime_array)) # Cast to strings, concatenate
    new_id = prime_str[n:n+5] # Extracting substring
    # Edge Case: duplicate ID
    if used_ids.get(new_id):
        print "Duplicate ID found. Plan not Completely Fool Proof."
        return False
    else:
        used_ids[new_id] = new_id
        print new_id
        return new_id
        
def next_prime(last_prime):
    if last_prime % 2 == 0:
        last_prime += 1
    else:
        last_prime += 2
    #print(type(last_prime)) 
    for i in range(2,int(math.sqrt(last_prime))+1):
        if last_prime % i == 0: 
            return next_prime(last_prime)
    else: 
        return last_prime

answer(sys.argv[1]) 
    
