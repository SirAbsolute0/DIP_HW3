from unittest import result
import numpy as np
import math
from cmath import pi

class Filtering:

    def __init__(self, image):
        self.image = image

    def get_gaussian_filter(self):
        """Initialzes/Computes and returns a 5X5 Gaussian filter"""
        local_img = self.image
        filter = np.zeros((5, 5))
        sigma = 6
        sum = 0
        
        for x in range(0, filter.shape[0]):
            for y in range(0, filter.shape[1]):
                filter[x, y] = 1/( 2*pi*(sigma**2) ) * math.exp( -1*( ((x-2)**2 + (y-2)**2) / (2* (sigma**2)) ))
                sum += filter[x, y]
        
        for num_1 in filter:
            for num_2 in filter:
                num_2 *= (1/sum)
        return filter

    def get_laplacian_filter(self):
        """Initialzes and returns a 3X3 Laplacian filter"""
        filter = np.matrix([[0, -1, 0],
                            [-1, 4, -1],
                            [0, -1, 0]])
        return filter

    def filter(self, filter_name):
        """Perform filtering on the image using the specified filter, and returns a filtered image
            takes as input:
            filter_name: a string, specifying the type of filter to use ["gaussian", laplacian"]
            return type: a 2d numpy array
                """
        if(filter_name == "gaussian"):
            original_filter = Filtering.get_gaussian_filter(self)
            filter = original_filter.copy()


            #Rotate filter 180 degrees
            x = original_filter.shape[0] - 1
            y = original_filter.shape[1] - 1

            i = 0
            while (x >= 0):
                j = 0
                while (y >= 0):
                    filter[i, j] = original_filter[x, y]
                    j += 1
                    y -= 1
                i += 1
                x -= 1

            local_img = self.image.copy()
            padded_img = np.zeros([local_img.shape[0] + 4, local_img.shape[1] + 4])

            #padded 0s
            for x in range(0, local_img.shape[0]):
                for y in range(0, local_img.shape[1]):
                    padded_img[x + 2, y + 2] = local_img[x, y]
            
            result_img = padded_img.copy()
            #convolution
            for x in range(0, padded_img.shape[0] - 4):
                for y in range(0, padded_img.shape[1] - 4):
                    result_img[x + 2, y + 2] = ( padded_img[x, y]*filter[0, 0] + padded_img[x, y+1]*filter[0,1]
                                            +  padded_img[x, y+2]*filter[0,2] + padded_img[x, y+3]*filter[0,3]
                                            +  padded_img[x, y+4]*filter[0,4] + padded_img[x+1,y]*filter[1,0]
                                            +  padded_img[x+1, y+1]*filter[1,1] + padded_img[x+1, y+2]*filter[1,2]
                                            +  padded_img[x+1, y+3]*filter[1,3] + padded_img[x+1, y+4]*filter[1,4]
                                            +  padded_img[x+2, y]*filter[2,0] + padded_img[x+2, y+1]*filter[2,1]
                                            +  padded_img[x+2, y+2]*filter[2,2] + padded_img[x+2, y+3]*filter[2,3]
                                            +  padded_img[x+2, y+4]*filter[2,4] + padded_img[x+3, y]*filter[3,0]
                                            +  padded_img[x+3, y+1]*filter[3,1] + padded_img[x+3, y+2]*filter[3,2]
                                            +  padded_img[x+3, y+3]*filter[3,3] + padded_img[x+3, y+4]*filter[3,4]
                                            +  padded_img[x+4, y]*filter[4,0] + padded_img[x+4, y+1]*filter[4,1]
                                            +  padded_img[x+4, y+2]*filter[4,2] + padded_img[x+4, y+3]*filter[4,3]
                                            +  padded_img[x+4, y+4]*filter[4,4] ) *(1/np.sum(filter))

            #Deleting padded zeros from final picture
            result_img = np.delete(result_img, result_img.shape[0] - 1, 0)
            result_img = np.delete(result_img, result_img.shape[1] - 1, 1)
            result_img = np.delete(result_img, result_img.shape[0] - 1, 0)
            result_img = np.delete(result_img, result_img.shape[1] - 1, 1)
            result_img = np.delete(result_img, 0, 0)
            result_img = np.delete(result_img, 0, 1)   
            result_img = np.delete(result_img, 0, 0)
            result_img = np.delete(result_img, 0, 1)   

            return(result_img)

            
        elif(filter_name == "laplacian"):
            original_filter = Filtering.get_laplacian_filter(self)
            filter = original_filter.copy()

            #Rotate filter 180 degrees
            x = original_filter.shape[0] - 1
            y = original_filter.shape[1] - 1

            i = 0
            while (x >= 0):
                j = 0
                while (y >= 0):
                    filter[i, j] = original_filter[x, y]
                    j += 1
                    y -= 1
                i += 1
                x -= 1

            local_img = self.image.copy()
            padded_img = np.zeros([local_img.shape[0] + 2, local_img.shape[1] + 2])

            #padded 0s
            for x in range(0, local_img.shape[0]):
                for y in range(0, local_img.shape[1]):
                    padded_img[x + 1, y + 1] = local_img[x, y]
            
            result_img = padded_img.copy()
            #convolution
            for x in range(0, padded_img.shape[0] - 2):
                for y in range(0, padded_img.shape[1] - 2):
                    temp = ( padded_img[x, y]*filter[0, 0] + padded_img[x, y+1]*filter[0,1]
                                +  padded_img[x, y+2]*filter[0,2] + padded_img[x+1,y]*filter[1,0]
                                +  padded_img[x+1, y+1]*filter[1,1] + padded_img[x+1, y+2]*filter[1,2]
                                +  padded_img[x+2, y]*filter[2,0] + padded_img[x+2, y+1]*filter[2,1]
                                +  padded_img[x+2, y+2]*filter[2,2] )
                    
                    if(temp <= 0):
                        result_img[x + 1, y + 1] = 0
                    else:
                        result_img[x + 1, y + 1] = temp
            
            #Deleting padded zeros from final picture
            result_img = np.delete(result_img, result_img.shape[0] - 1, 0)
            result_img = np.delete(result_img, result_img.shape[1] - 1, 1)
            result_img = np.delete(result_img, 0, 0)
            result_img = np.delete(result_img, 0, 1)

            return(result_img)
        return self.image

