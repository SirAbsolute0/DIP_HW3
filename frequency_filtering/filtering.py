# For this part of the assignment, You can use inbuilt functions to compute the fourier transform
# You are welcome to use fft that are available in numpy and opencv

import numpy as np
import cv2

class Filtering:

    def __init__(self, image):
        """initializes the variables for frequency filtering on an input image
        takes as input:
        image: the input image
        """
        self.image = image
        self.mask = self.get_mask

    def get_mask(self, shape):
        """Computes a user-defined mask
        takes as input:
        shape: the shape of the mask to be generated
        rtype: a 2d numpy array with size of shape
        """
        #Initiate my own mask based on the given picture DFT on a frequency domain
        filter = np.ones(shape)
        filter[220:240, 285:305] = 0
        filter[265:275, 275:285] = 0
        filter[275:295, 205:225] = 0
        filter[235:255, 225:245] = 0
        return filter

    def post_process_image(self, image):
        """Post processing to display DFTs and IDFTs
        takes as input:
        image: the image obtained from the inverse fourier transform
        return an image with full contrast stretch
        -----------------------------------------------------
        You can perform post processing as needed. For example,
        1. You can perfrom log compression
        2. You can perfrom a full contrast stretch (fsimage)
        3. You can take negative (255 - fsimage)
        4. etc.
        """
        #Thie post_process_image function is only for viewing fft image
        #Calculate magnitude, take log and then do full contrast stretch
        magnitude = np.abs(image)
        result_img = np.log(magnitude)
        stretch_img = result_img.copy()

        min = np.amin(result_img)
        max = np.amax(result_img)
        
        for x in range(0, result_img.shape[0]):
            for y in range(0, result_img.shape[1]):
                result_img[x, y] = int((254/(max - min)) * (result_img[x, y] - min) + 0.5)

        return result_img

    def filter(self):
        """Performs frequency filtering on an input image
        returns a filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering
        ----------------------------------------------------------
        You are allowed to use inbuilt functions to compute fft
        There are packages available in numpy as well as in opencv
        Steps:
        1. Compute the fft of the image
        2. shift the fft to center the low frequencies
        3. get the mask (write your code in functions provided above) the functions can be called by self.filter(shape)
        4. filter the image frequency based on the mask (Convolution theorem)
        5. compute the inverse shift
        6. compute the inverse fourier transform
        7. compute the magnitude
        8. You will need to do post processing on the magnitude and depending on the algorithm (use post_process_image to write this code)
        Note: You do not have to do zero padding as discussed in class, the inbuilt functions takes care of that
        filtered image, magnitude of frequency_filtering, magnitude of filtered frequency_filtering: Make sure all images being returned have grey scale full contrast stretch and dtype=uint8
        """
        #Get local copy of image
        local_img = self.image.copy()
        
        #performed fft and shift from original image
        fft_img = np.fft.ifftshift(np.fft.fft2(local_img))

        #copy out a version of the fft_image for display
        result_filtered_display = self.post_process_image(fft_img)

        #Initiate the filter/mask
        filter = self.get_mask(local_img.shape)

        #Apply the filter to the fft_image
        result_filtered = fft_img.copy()
        for x in range(0, result_filtered.shape[0]):
            for y in range(0, result_filtered.shape[1]):
                result_filtered[x, y] = fft_img[x, y] * filter[x, y]
                result_filtered_display[x, y] = result_filtered_display[x, y] * filter[x, y]
        
        #shift and do ifft on the image with filter applied
        final_img = np.fft.ifft2(np.fft.ifftshift(result_filtered))

        #calculate magnitude and do full contrast stretch to display the result image
        result = np.abs(final_img)    

        min = np.amin(result)
        max = np.amax(result)
        
        for x in range(0, result.shape[0]):
            for y in range(0, result.shape[1]):
                result[x, y] = int((254/(max - min)) * (result[x, y] - min) + 0.5)
        
        return [self.post_process_image(fft_img), result_filtered_display, result ]
