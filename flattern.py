def flattern_list(seq):
    """
    The function to flattern a complex list 
    
    """
    for _element in seq:
        print(f"processing {_element}")
        if hasattr(_element, '__iter__'):
            print(f"element {_element} has __iter__")
            yield from flattern_list(_element)
        else:
            print(f"element has no  __iter__")
            yield _element
            

print(list(flattern_list([1, [2, [3,4, [5,[6]]]]])))
