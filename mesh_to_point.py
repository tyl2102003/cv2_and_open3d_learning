import open3d as o3d
import numpy as np

# print('input')
# bunny = o3d.data.BunnyMesh()
# mesh = o3d.io.read_triangle_mesh(bunny.path)

# # fit to unit cube
# mesh.scale(1 / np.max(mesh.get_max_bound() - mesh.get_min_bound()),
#            center=mesh.get_center())
# # o3d.visualization.draw_geometries([mesh])
# o3d.visualization.draw(mesh)
#
# print('voxelization')
# voxel_grid = o3d.geometry.VoxelGrid.create_from_triangle_mesh(mesh,
#                                                               voxel_size=0.05)
# # o3d.visualization.draw_geometries([voxel_grid])
# o3d.visualization.draw(voxel_grid)

# 读取mesh文件
mesh = o3d.io.read_triangle_mesh('埋件装配体.STL')

print(mesh, type(mesh))
# 均匀采样8000个点,参考链接http://www.open3d.org/docs/release/python_api/open3d.geometry.TriangleMesh.html
pt = mesh.sample_points_uniformly(8000)
# 用np.asarray()方法将pointcould类型数据打印出来，注意points是pt的一个属性
p = np.asarray(pt.points)
print(p)
# o3d.visualization.draw(pt)

# o3d.io.write_point_cloud(filename='rabbit.pcd',pointcloud=pt, write_ascii=True)
# 将 pointcloud 类型数据pt 保存成.pcd文件，也可以保存成其他的
o3d.io.write_point_cloud(filename='埋件装配体.pts', pointcloud=pt, write_ascii=True)

