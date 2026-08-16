import numpy as np

def rgb_to_grayscale(image):
    """
    Convert an RGB image to grayscale using luminosity method.
    
    Args:
        image: RGB image as list or numpy array of shape (H, W, 3)
               with values in range [0, 255]
    
    Returns:
        Grayscale image as 2D list with integer values,
        or -1 if input is invalid
    """
    # Write your code here
    try:
        arr = np.array(image)
    except Exception:
        return -1
    
    if arr.ndim != 3 or arr.shape[2] !=3:
        return -1
    if arr.shape[0] == 0 or arr.shape[1] == 0 :
        return -1

    if not np.issubdtype(arr.dtype,np.number):
        return -1
    
    if np.any(arr<0) or np.any(arr>255):
        return -1

    weights = np.array([0.299,0.587,0.114])
    gray = np.dot(arr,weights)
    gray = np.round(gray).astype(int)
    return gray.tolist()
    