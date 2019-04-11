
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   if int_list == None: #Accounts for the occurence if the list is None
       raise ValueError('List is None type')
   if int_list == []:
       return None
   largest_number = int_list[0] #Creates a starting point in which to execute comparisons
   for i in range(len(int_list)): #Loops through the length of the list
       if largest_number < int_list[i]: #Checks if the next value is greater than the previous value
           largest_number = int_list[i] #If it does find a larger value than sets that value equal to the temp variable largest_number
   return largest_number #After the search, returns the largest variable found

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   if int_list == None: #Raises an error if the list is None
      raise ValueError('List is None type')
   if len(int_list) == 1: #Tests if base case is met
       return int_list #returns the one item list that was the end value of the original list
   int_list[1:] = (reverse_rec(int_list[1:])) #Recursively replaces the int_list with the new reversed list
   int_list.append(int_list.pop(0)) #Pops the first value of the list, and places it into back of the list
   return int_list #returns the new reversed list

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """
   if int_list == None: #Checks for the occurence of the list being None
       raise ValueError(f'could not find {target} in {int_list}') #Raises error of None List
   if high > (len(int_list) - 1):
       return None
   if low < 0:
       low = None

   mid_range_index = (high+low)//2 #Finds the middle of the index of a list with a floor divide
   if mid_range_index == low:
       return None #Returns None if the target is not found
   elif int_list[mid_range_index] < target: #Checks the sorted list if the target is greater than the middle of the index
       return bin_search(target, mid_range_index, high, int_list) #Begins recursion if target is greater than mid_range_index
   elif int_list[mid_range_index] > target: #Checks the sorted list if the target is less than the middle of the index
       return bin_search(target, low, mid_range_index, int_list) #Begins recursion if target is less than mid_range_index
   elif int_list[mid_range_index] == target: #checks if the target is at mid_range_index
       return mid_range_index #Returns value if found at mid_range_index
