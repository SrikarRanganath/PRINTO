import pyvista as pv
import numpy as np
from numpy import mgrid
import matplotlib.pyplot as plt

print('initializing domain')
xmin = -800.
xmax = 800.
Lx = xmax-xmin
B0 = 1
k = 1
alpha = 2.0*np.pi*k/Lx
x, y, z = Lx*mgrid[0:1:51j, 0:1:51j, 0:1:51j]


print('initializing 3D B field')
Bx = B0*(np.sin(alpha*z) + np.cos(alpha*y))
By = B0*(np.sin(alpha*x) + np.cos(alpha*z))
Bz = B0*(np.sin(alpha*y) + np.cos(alpha*x))
B = np.column_stack((Bx.ravel(), By.ravel(), Bz.ravel()))
grid = pv.StructuredGrid(x, y, z)
grid["ABC field magnitude"] = np.linalg.norm(B, axis=1)
grid["ABC field vectors"] = B
grid.set_active_vectors("ABC field vectors")
#contours = grid.contour(8, scalars="ABC field magnitude")
#arrows = contours.glyph(orient="ABC field vectors", factor=50.0)

print('plotting')
pv.set_plot_theme('document')
p = pv.Plotter(notebook=0, shape=(1,1))
#p.background_color='white'
#p.window_size
cmap = plt.cm.get_cmap("viridis", 4)
p.add_mesh(grid, cmap=cmap)
p.show_grid()
#p.add_mesh(arrows)
#p.subplot(0,1)
#slices = grid.slice_orthogonal(x=20, y=20, z=30)
#slices = grid.slice_orthogonal()
#p.add_mesh(slices, cmap=cmap)
##p.subplot(1,0)
#p.add_mesh(contours, opacity=1)
#p.subplot(1,1)
#p.add_mesh(arrows)
#single_slice = arrows.slice(normal=[1, 1, 0])
#slices = arrows.slice_orthogonal(x=20, y=20, z=30)
#slices = grid.slice_orthogonal()
#p.add_mesh(single_slice, cmap=cmap)
p.show_grid()

p.link_views()
p.view_isometric()
p.show(screenshot='abc3d_slicing.png')

