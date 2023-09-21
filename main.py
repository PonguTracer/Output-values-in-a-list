# Define a function to get user input and return the list of integers and threshold value
def get_user_values():
    num_values = int(input())
    values = []
    
    for _ in range(num_values):
        value = int(input())
        values.append(value)
    
    threshold = int(input())
    
    return values, threshold

# Define a function to filter integers less than or equal to the threshold
def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    filtered_values = [value for value in user_values if value <= upper_threshold]
    return filtered_values

# Main program
if __name__ == "__main__":
    user_values, threshold = get_user_values()
    filtered_values = ints_less_than_or_equal_to_threshold(user_values, threshold)
    
    for value in filtered_values:
        print(value)
