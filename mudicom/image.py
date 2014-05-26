from __future__ import division
import os.path
import numpy
import gdcm
from .base import BaseDicom
from .reader import Reader


class Image(BaseDicom):

    def __init__(self, fname):
        super(Image, self).__init__(fname)

    def get_image(self):
        """ Extract image from DICOM file """
        file_reader = Reader(self.fname)
        dataset = file_reader.get_dataset()

        image_reader = self.gdcm.ImageReader()
        pixel_array = gdcm_to_numpy(image_reader.GetImage())
        # save full image
        pil_image = Image.fromarray(pixel_format)
        pil_image.save(os.path.join(self.file_name, ".png"))
        # save thumbnail of image
        pil_image.thumbnail((150,150,), Image.ANTIALIAS)
        pil_image.save(os.path.join(self.file_name, "_thumb.png"), "PNG")

def gdcm_to_numpy(image):
    """ Converts a GDCM image to a numpy array. """
    gdcm_typemap = {
        gdcm.PixelFormat.UINT8:     numpy.int8,
        gdcm.PixelFormat.INT8:      numpy.uint8,
        gdcm.PixelFormat.UINT16:    numpy.uint16,
        gdcm.PixelFormat.INT16:     numpy.int16,
        gdcm.PixelFormat.UINT32:    numpy.uint32,
        gdcm.PixelFormat.INT32:     numpy.int32,
        gdcm.PixelFormat.FLOAT32:   numpy.float32,
        gdcm.PixelFormat.FLOAT64:   numpy.float64 
    }
    pixel_format = image.GetPixelFormat().GetScalarType()
    if pixel_format in gdcm_typemap:
        data_type = gdcm_typemap[pixel_format]
        print(data_type)
    else:
        raise KeyError(''.join(pixel_format, " is not a supported pixel format"))

    # dimension = image.GetDimension(0), image.GetDimension(1)
    dimension = image.GetDimension(1), image.GetDimension(0)
    gdcm_array = image.GetBuffer()
    ## use float for accurate scaling
    result = numpy.frombuffer(gdcm_array, dtype=data_type).astype(float)
    ## optional gamma scaling
    maxV = float(result[result.argmax()])
    result = result + 0.5 * (maxV - result)
    result = numpy.log(result + 50) ## apprx background level

    result.shape = dimension

    return result