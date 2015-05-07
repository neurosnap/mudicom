# -*- coding: utf-8 -*-
"""
    mudicom.image
    ~~~~~~~~~~~~~

    Primary image module that converts DICOM pixel data into a numpy array
    as well as saving the image using Matplotlib or Pillow.
"""
import os.path
import sys
import numpy
import gdcm

class Image(object):
    """ This class attempts to extract an image out of the DICOM file.

    :param fname: Location and filename of DICOM file.
    """
    def __init__(self, fname):
        self.fname = fname

    def __repr__(self):
        return "<MudicomImage {0}>".format(self.fname)

    def __str__(self):
        return str(self.fname)

    @property
    def numpy(self):
        """ Grabs image data and converts it to a numpy array """
        # load GDCM's image reading functionality
        image_reader = gdcm.ImageReader()
        image_reader.SetFileName(self.fname)
        if not image_reader.Read():
            raise IOError("Could not read DICOM image")
        pixel_array = self._gdcm_to_numpy(image_reader.GetImage())
        return pixel_array

    def _gdcm_to_numpy(self, image):
        """ Converts a GDCM image to a numpy array.

        :param image: GDCM.ImageReader.GetImage()
        """
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
            self.data_type = gdcm_typemap[pixel_format]
        else:
            raise KeyError(''.join(pixel_format, \
                " is not a supported pixel format"))

        #dimension = image.GetDimension(0), image.GetDimension(1)
        self.dimensions = image.GetDimension(1), image.GetDimension(0)
        gdcm_array = image.GetBuffer()

        # GDCM returns char* as type str. This converts it to type bytes
        if sys.version_info >= (3, 0):
            gdcm_array = gdcm_array.encode(sys.getfilesystemencoding(), "surrogateescape")

        # use float for accurate scaling
        dimensions = image.GetDimensions()
        result = numpy.frombuffer(gdcm_array, dtype=self.data_type).astype(float)
        if len(dimensions) == 3:
            # for cine (animations) there are 3 dims: x, y, number of frames
            result.shape = dimensions[2], dimensions[0], dimensions[1]
        else:
            result.shape = dimensions
        return result

    def save_as_plt(self, fname, pixel_array=None, vmin=None, vmax=None,
        cmap=None, format=None, origin=None):
        """ This method saves the image from a numpy array using matplotlib

        :param fname: Location and name of the image file to be saved.
        :param pixel_array: Numpy pixel array, i.e. ``numpy()`` return value
        :param vmin: matplotlib vmin
        :param vmax: matplotlib vmax
        :param cmap: matplotlib color map
        :param format: matplotlib format
        :param origin: matplotlib origin

        This method will return True if successful
        """
        from matplotlib.backends.backend_agg \
        import FigureCanvasAgg as FigureCanvas
        from matplotlib.figure import Figure
        from pylab import cm

        if pixel_array is None:
            pixel_array = self.numpy()

        if cmap is None:
            cmap = cm.bone
        fig = Figure(figsize=pixel_array.shape[::-1], dpi=1, frameon=False)
        canvas = FigureCanvas(fig)
        fig.figimage(pixel_array, cmap=cmap, vmin=vmin,
            vmax=vmax, origin=origin)
        fig.savefig(fname, dpi=1, format=format)
        return True

    def save_as_pil(self, fname, pixel_array=None):
        """  This method saves the image from a numpy array using Pillow
        (PIL fork)

        :param fname: Location and name of the image file to be saved.
        :param pixel_array: Numpy pixel array, i.e. ``numpy()`` return value

        This method will return True if successful
        """
        if pixel_array is None:
            pixel_array = self.numpy()

        from PIL import Image as pillow
        pil_image = pillow.fromarray(pixel_array.astype('uint8'))
        pil_image.save(fname)
        return True
