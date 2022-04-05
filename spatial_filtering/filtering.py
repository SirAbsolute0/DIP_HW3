import numpy as np


class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""

        return np.zeros((5, 5))

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""

        return np.zeros((3, 3))

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """

        return self.image

