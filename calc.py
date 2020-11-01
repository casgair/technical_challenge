import operator

# Dictionary of available operators
operators = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def prefix_calculator(line):
    """
    Calculate result for a prefix string. The input is traversed in reverse order.
    If a number is encountered it is added to the number stack,
    if an operator is enountered it is used with the two next two elements from the number queue.
    :param line: Input string in prefix format
    :return: Result in float format
    """
    # Split input string into list
    split_prefix_line = line.split(" ")
    # Stack of numbers, add to this when encountering any number or when a number result has been calculated
    number_stack = []
    # Loop through split prefix string in reverse order
    for element in reversed(split_prefix_line):
        if element in operators:
            # Get operator python function from operator string
            op = operators[element]
            # Get first input to op, first number in the number stack
            n1 = number_stack.pop()
            # Get second input to op, second number in the number stack
            n2 = number_stack.pop()
            # Calculate op result for n1 and n2
            result = op(n1, n2)
            # Add result to number stack
            number_stack.append(result)
        else:
            number_stack.append(float(element))
    # Return last number in number stack, which holds current result
    return number_stack[0]


def infix_to_prefix(line):
    """
    Produces a string in prefix notation given an infix string.
    Based losely on the Shunting-yard algorithm: https://en.wikipedia.org/wiki/Shunting-yard_algorithm
    :param line: Input string in infix format with paranthesis
    :return: String in prefix format
    """
    # Split string into list
    split_line = line.split(" ")
    # List containing final output after traversing the string
    output = []
    # Stack of ops
    op_stack = []
    # Traverse infix string once in reverse order
    for element in reversed(split_line):
        # If ) is encountered it is added to the op stack
        if element is ")":
            op_stack.append(element)
        # If ( is encountered we have hit the end of one full op statement, (A + B) for example
        # The op is added to beginning of output, and ) is removed from ops if in top of stack
        if element is "(":
            output.insert(0, op_stack.pop())
            if op_stack:
                if op_stack[-1] is ")":
                    op_stack.pop()
        # If an op is encountered it's simply added to the op stack
        if element in operators:
            op_stack.append(element)
        # If a digit is encountered it is directly added to the output
        if element.isdigit():
            output.insert(0, element)
    # Add final op from stack if still one in there
    if op_stack:
        output.insert(0, op_stack.pop())

    # Output list is converted from list to space delimated string
    return " ".join(output)


def infix_calculator(line):
    """
    Calculate result of infix string, converts string to prefix and calculates result using prefix function.
    :param line: Input string in infix format with paranthesis
    :return: Result in float format
    """
    # Convert input line from infix to prefix
    prefix_line = infix_to_prefix(line)
    # Use prefix calculator on converted infix line
    result = prefix_calculator(prefix_line)
    return result


if "__main__" in __name__:

    # All prefix test cases supplied
    prefix_test_cases = {
        "+ 1 2": 3.0,
        "+ 1 * 2 3": 7.0,
        "+ * 1 2 3": 5.0,
        "- / 10 + 1 1 * 1 2": 3.0,
        "- 0 3": -3.0,
        "/ 3 2": 1.5
    }

    # All infix test cases supplied
    infix_test_cases = {
        "( 1 + 2 )": 3.0,
        "( 1 + ( 2 * 3 ) )": 7.0,
        "( ( 1 * 2 ) + 3 )": 5.0,
        "( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )": -1.8
    }

    # Test and display all test cases for both prefix and infix

    print("\n#### Test prefix calculator ####\n")
    for test_case, test_answer in prefix_test_cases.items():
        result = prefix_calculator(test_case)
        print("Test case: {}".format(test_case))
        print("Calculation: {}".format(result))
        print("Answer: {}\n".format(test_answer))
        assert result == test_answer
    print("All prefix tests passed.\n")

    print("#### Test infix calculator ####\n")
    for test_case, test_answer in infix_test_cases.items():
        result = infix_calculator(test_case)
        print("Test case: {}".format(test_case))
        print("Calculation: {}".format(result))
        print("Answer: {}\n".format(test_answer))
        assert result == test_answer
    print("All infix tests passed.")
