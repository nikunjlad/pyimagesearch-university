"""_summary_

This is a utility script which is used to provide helper functions to be used in the main code.
"""

# import necessary libraries
import imutils

def sliding_window(image, step, ws):
    """_summary_

    This function is used to create patches of an image using a sliding window technique where given an image,
    we just need the step size (in pixels) to denote how much to step our windows of size (ws pixels) from left to right
    and from top to bottom.

    Args:
        image (np.ndarray): the input image on which to perform sliding window operations
        step (int): the amount of pixels to jump from left-to-right or from top-to-bottom when sliding a window
        ws (tuple(int, int)): a tuple consisting of 2 integers denoting size of window in terms of width and height pixels

    Yields:
        tuple(int, int, np.ndarray): returns the starting x,y co-ordinates of the window and the window patch size of
                                     the sliced image itself.

    """

    # loop over the height of the image for 0th pixel to (last pixel - window size height) in increments of the step value
    for y in range(0, image.shape[0] - ws, step):

        # loop over the width of the image for 0th pixel to (last pixel - window size width) in increments of the step value
        for x in range(0, image.shape[1] - ws, step):

            # get the tuple consisting of starting x,y co-ordinates of the window and the window sliced patch of the image
            yield (x, y, image[y:y + ws[1], x:x + ws[0]])


def image_pyramid(image, scale=1.5, minSize=(224,224)):
    """_summary_

    Args:
        image (_type_): _description_
        scale (float, optional): _description_. Defaults to 1.5.
        minSize (tuple, optional): _description_. Defaults to (224,224).

    Yields:
        _type_: _description_
    """
    yield image

    while True:

        w = int(image.shape[1] / scale)
        image = imutils.resize(image=image, width=w)

        if image.shape[0] < minSize[1] or image.shape[1] < minSize[0]:
            break

        yield image