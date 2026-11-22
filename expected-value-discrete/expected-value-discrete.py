import numpy as np

def expected_value_discrete(x: list, p: list) -> float:
    """
    Returns the expected value as a Python float.
    """
    x_array=np.asarray(x,dtype=float)
    y_array=np.asarray(p,dtype=float)
    return np.sum(np.dot(x_array,y_array))
    # Write code here
    pass