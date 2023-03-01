# Problem Set 4A
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return sequence
    all_permutations = []
    for char in sequence:
        remaining_string = "".join(sequence.split(char))
        temp_permutations = get_permutations(remaining_string)
        for perm in temp_permutations:
            all_permutations.append(char + perm)

    return all_permutations


if __name__ == '__main__':
    #    #EXAMPLE
    example_input = 'abc'
    print('Input:', example_input)
    print('Expected Output:', ['abc', 'acb', 'bac', 'bca', 'cab', 'cba'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'xyz'
    print('Input:', example_input)
    print('Expected Output:', ['xyz', 'xzy', 'yxz', 'yzx', 'zxy', 'zyx'])
    print('Actual Output:', get_permutations(example_input))

    example_input = 'efg'
    print('Input:', example_input)
    print('Expected Output:', ['efg', 'egf', 'feg', 'fge', 'gef', 'gfe'])
    print('Actual Output:', get_permutations(example_input))
#    # Put three example test cases here (for your sanity, limit your inputs
#    to be three characters or fewer as you will have n! permutations for a
#    sequence of length n)
