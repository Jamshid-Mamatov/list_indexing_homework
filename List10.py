def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    max=list_num[0]
    if list_num[-1]>max:
        max=list_num[-1]
    return max
