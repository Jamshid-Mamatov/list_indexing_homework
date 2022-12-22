def main(list1):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    count=0
    for i in range(len(list1)):
        if list1[0]!=list1[i]:
            return False
        else:
            count+=1
    return count==len(list1)
