# def process_data(data, operation):            junior level code, you cant assume that all the data the user passes will be correct
#     result = []                               assume the user is dumb, Make sure to tell which one of the values input is wrong, if a incorrect value has been input 
#     for item in data:
#         if operation == "square":
#             result.append(item * item)
#         elif operation == "double":
#             result.append(item * 2)
#         elif operation == "halve":
#             result.append(item / 2)
        
#     return result

# data = [2, 4, 6, 8]
# operation = "square"
# result = process_data(data, operation)
# print(result)

#Senior developer code //////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def validate_data(data):
    if not isinstance(data, list):
        raise ValueError("Data must be a list of numbers")
    
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError("All items in the data list nmust be numbers")
        
def validate_operation(operation):
    valid_operations = ["square", "double", "halve"]
    if operation not in valid_operations:
        raise ValueError(f"Invalid operation, must be one of {valid_operations}")
    
def process_data(data,operation):
    validate_data(data)
    validate_operation(operation)

    result = []
    for item in data:
        if operation == "square":
            result.append(item * item)
        elif operation == "double":
            result.append(item * 2)
        elif operation =="halve":
            result.append(item / 2)

    return result

try:
    data = [2, 4, 6, 8]
    operation = "square"
    result = process_data(data, operation)
    print(result)
except ValueError as e:
    print(e)
