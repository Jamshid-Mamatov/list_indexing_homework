def main(list1):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(list1)):
        if list1[i]==1:
    
            list1[i]=True
        else:
            list1[i]=False
    return list1
