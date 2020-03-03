import os
import unittest
import numpy as np
from . import common
from osgeo import gdal
from osgeo import osr

from configuration import MultiplePaths
from core.gdal_python import coherence_masking


class CoherenceMaskingTest(unittest.TestCase):
    """ """
    def test_coherence_files_not_converted(self):
        """ """
        # define constants
        NO_DATA_VALUE = 0
        driver = gdal.GetDriverByName("GTiff")

        # create a sample gdal dataset

        # sample gdal dataset
        sample_gdal_filename = "sample_gdal_dataset_01122000.tif"
        options = ['PROFILE=GeoTIFF']
        sample_gdal_dataset = driver.Create(sample_gdal_filename, 5, 5, 1, gdal.GDT_Float32, options=options)
        srs = osr.SpatialReference()
        wkt_projection = srs.ExportToWkt()
        sample_gdal_dataset.SetProjection(wkt_projection)

        sample_gdal_band = sample_gdal_dataset.GetRasterBand(1)
        sample_gdal_band.SetNoDataValue(NO_DATA_VALUE)
        sample_gdal_band.WriteArray(np.arange(25).reshape(5, 5))
        sample_gdal_band.FlushCache()

        # create a coherence mask dataset
        outDir = "" # we won't be creating any output coherence mask files as there are already GeoTIFFs
        coherence_mask_filename = MultiplePaths(outDir, "coherence_mask_dataset_01122000.tif")
        coherence_mask_dataset = driver.Create(coherence_mask_filename.converted_path, 5, 5, 1, gdal.GDT_Float32)
        srs = osr.SpatialReference()
        wkt_projection = srs.ExportToWkt()
        coherence_mask_dataset.SetProjection(wkt_projection)
        coherence_mask_band = coherence_mask_dataset.GetRasterBand(1)
        coherence_mask_band.SetNoDataValue(NO_DATA_VALUE)
        coherence_mask_band.WriteArray(np.arange(0, 75, 3).reshape(5, 5) / 100.0)
        # del the tmp handler datasets created
        del coherence_mask_dataset
        # create an artificial masked dataset
        expected_result_array = np.nan_to_num(
            np.array(
                [
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [np.nan, np.nan, np.nan, np.nan, np.nan],
                    [10.0, 11.0, 12.0, 13.0, 14.0],
                    [15.0, 16.0, 17.0, 18.0, 19.0],
                    [20.0, 21.0, 22.0, 23.0, 24.0],
                ]
            )
        )

        # use the gdal_python.coherence_masking to find the actual mask dataset
        coherence_thresh = 0.3
        coherence_masking(sample_gdal_dataset, sample_gdal_filename, [coherence_mask_filename], coherence_thresh)
        sample_gdal_array = np.nan_to_num(sample_gdal_dataset.GetRasterBand(1).ReadAsArray())

        # compare the artificial masked and actual masked datasets
        self.assertTrue(np.array_equiv(sample_gdal_array, expected_result_array))

        # del the tmp datasets created
        os.remove(coherence_mask_filename.converted_path)

        del sample_gdal_dataset
        os.remove(sample_gdal_filename)


if __name__ == "__main__":
    unittest.main()
