import numpy as np
import open3d as o3d
import rasterio as rio
from rasterio import mask
from shapely.geometry import Point
import scipy.interpolate as sci
import matplotlib.pyplot as plt
import lidario

# target = 199414.11489207728, 223588.55983083232
# path_to_tif = "../data/DSM_vlaanderen/DHMVIIDSMRAS1m_k09/GeoTIFF/DHMVIIDSMRAS1m_k09.tif"
crop_directory = "api/src/data/output/"
crop_name = "result"
translator = lidario.Translator("geotiff", "np")

# Translate the tif file and get the pandas.Dataframe


class TiffTo3D:

    def __init__(self, xtarget, ytarget, path_to_tif):
        self.xtarget = xtarget
        self.ytarget = ytarget
        self.path_to_tif = path_to_tif

    def target_to_buffer(self):
        """
        Creating a squared buffer of 40 pixels around target point
        """
        return Point(self.xtarget, self.ytarget).buffer(20, cap_style=3)

    def tif_crop(self):
        """
        Crop tif file with rio.mask
        Increase its resolution with linear interpolation, RectBivariateSpline
        Increase house height (*3) as height reduced due to higher resolution
        Reshape crop to correspond to original tif, (1,outinter.shape[0],outinter.shape[1])
        Update metadata with crop characteristics
        Save crop as tif in /data/output directory
        """
        with rio.open(self.path_to_tif) as srcA:
            out_image, out_transform = rio.mask.mask(srcA, [self.target_to_buffer()], crop=True, filled=False)
            out_meta = srcA.meta
        x_in, y_in, x_out, y_out = np.arange(0, out_image.shape[1], 1), np.arange(0, out_image.shape[2], 1), \
                                   np.arange(0, out_image.shape[1], 0.25), np.arange(0, out_image.shape[2], 0.25)
        f = sci.RectBivariateSpline(x_in, y_in, out_image.squeeze())
        outinter = f(x_out, y_out)
        outinter = outinter * 3
        outinter = np.where(outinter > np.percentile(outinter, 99.8), np.percentile(outinter, 99.8), outinter)
        outinter = outinter.reshape(1, outinter.shape[0], outinter.shape[1])
        outinter = outinter.astype('float32')
        out_meta.update({"driver": "GTiff", "height": outinter.shape[1], "width": outinter.shape[2], "transform": out_transform})
        with rio.open(f"{crop_directory}{crop_name}.tif", "w", **out_meta) as dest:
            dest.write(outinter)

    def crop_to_3D (self):
        point_cloud = translator.translate(f"{crop_directory}{crop_name}.tif")
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
            poisson_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9, linear_fit =True)
        densities = np.asarray(densities)
        density_colors = plt.get_cmap('gist_gray')((densities - densities.min()) / (densities.max() - densities.min()))
        density_colors = density_colors[:, :3]
        density_mesh = o3d.geometry.TriangleMesh()
        density_mesh.vertices = poisson_mesh.vertices
        density_mesh.triangles = poisson_mesh.triangles
        density_mesh.triangle_normals = poisson_mesh.triangle_normals
        density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
        vertices_to_remove = densities < np.quantile(densities, 0.01)
        density_mesh.remove_vertices_by_mask(vertices_to_remove)
        return o3d.visualization.draw_geometries([density_mesh])

    def crop_to_3Dobj (self):
        point_cloud = translator.translate(f"{crop_directory}{crop_name}.tif")
        pcd = o3d.geometry.PointCloud()
        pcd.points = o3d.utility.Vector3dVector(point_cloud[:,:3])
        pcd.estimate_normals(search_param=o3d.geometry.KDTreeSearchParamHybrid(radius=0.1, max_nn=30))
        with o3d.utility.VerbosityContextManager(o3d.utility.VerbosityLevel.Debug) as cm:
            poisson_mesh, densities = o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=9, linear_fit =True)
        densities = np.asarray(densities)
        density_colors = plt.get_cmap('Greys')((densities - densities.min()) / (densities.max() - densities.min()))
        density_colors = density_colors[:, :3]
        density_mesh = o3d.geometry.TriangleMesh()
        density_mesh.vertices = poisson_mesh.vertices
        density_mesh.triangles = poisson_mesh.triangles
        density_mesh.triangle_normals = poisson_mesh.triangle_normals
        density_mesh.vertex_colors = o3d.utility.Vector3dVector(density_colors)
        vertices_to_remove = densities < np.quantile(densities, 0.01)
        density_mesh.remove_vertices_by_mask(vertices_to_remove)
        return o3d.io.write_triangle_mesh("./static/threejs/house_sample.obj", density_mesh)

# TiffTo3D(target[0], target[1], path_to_tif).tif_crop()
#
#
# TiffTo3D(target[0], target[1], path_to_tif).crop_to_3D()
