from __future__ import division
import os.path
import numpy
import gdcm

from .base import BaseDicom
from .reader import Reader


class Image(BaseDicom):

    def __init__(self, fname):
        super(Image, self).__init__(fname)

    def get_numpy(self):
        """ Extract image from DICOM file """
        # load GDCM's image reading functionality
        image_reader = self.gdcm.ImageReader()
        image_reader.SetFileName(self.fname)
        if not image_reader.Read():
            raise Exception("Could not read DICOM image")
        pixel_array = gdcm_to_numpy(image_reader.GetImage())
        return pixel_array

    def save_image_plt(self, fname, pixel_array, vmin=None, vmax=None, 
        cmap=None, format=None, origin=None):
        """ Requires matplotlib """
        from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
        from matplotlib.figure import Figure
        from pylab import cm
        if cmap is None:
            cmap = cm.bone

        fig = Figure(figsize=pixel_array.shape[::-1], dpi=1, frameon=False)
        #fig.set_size_inches(5.12, 5.12)
        canvas = FigureCanvas(fig)
        fig.figimage(pixel_array, cmap=cmap, vmin=vmin, vmax=vmax, origin=origin)
        fig.savefig(fname, dpi=1, format=format)
        return True

    def save_image_pil(self, fname, pixel_array):
        """ Requires PIL """
        from PIL import Image as pillow

        pil_image = pillow.fromarray(pixel_array.astype('uint8'))
        pil_image.save(fname)
        # save thumbnail of image
        #pil_image.thumbnail((150,150,), pillow.ANTIALIAS)
        #pil_image.save(''.join([file_name, "_thumb.png"]), "PNG")
        return True

def gdcm_to_numpy(image):
    """ Converts a GDCM image to a numpy array. """
    gdcm_typemap = {
        gdcm.PixelFormat.INT8:     numpy.int8,
        gdcm.PixelFormat.UINT8:    numpy.uint8,
        gdcm.PixelFormat.UINT16:   numpy.uint16,
        gdcm.PixelFormat.INT16:    numpy.int16,
        gdcm.PixelFormat.UINT32:   numpy.uint32,
        gdcm.PixelFormat.INT32:    numpy.int32,
        gdcm.PixelFormat.FLOAT32:  numpy.float32,
        gdcm.PixelFormat.FLOAT64:  numpy.float64 
    }
    pixel_format = image.GetPixelFormat().GetScalarType()
    if pixel_format in gdcm_typemap:
        data_type = gdcm_typemap[pixel_format]
    else:
        raise KeyError(''.join(pixel_format, " is not a supported pixel format"))

    #dimension = image.GetDimension(0), image.GetDimension(1)
    dimensions = image.GetDimension(1), image.GetDimension(0)
    gdcm_array = image.GetBuffer()
    ## use float for accurate scaling
    result = numpy.frombuffer(gdcm_array, dtype=data_type).astype(float)
    result.shape = dimensions
    return result
