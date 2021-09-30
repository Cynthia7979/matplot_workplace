from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Pyramid
# label = ('C', 'B', 'D', 'C', 'A', 'B', 'A', 'D')
# x = (3, 1, 5, 3, 3, 1, 3, 5)
# y = (2, 5, 5, 2, 4, 5, 4, 5)
# z = (0, 0, 0, 0, 4, 0, 4, 0)

# Cube
label = ('A', 'B', 'C', 'D', 'A', 'E', 'F', 'B', 'F', 'G', 'C', 'G', 'H', 'D', 'H', 'E')
x = (1, 1, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1)
y = (1, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1)
z = (1, 1, 1, 1, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3)


def draw_3d(fig, ax):
    fig.suptitle('3D Figure (Cube)')
    ax.plot3D(x, y, z)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax = annotate_pts(ax, [(x[i], y[i], z[i]) for i in range(len(label))])
    return fig, ax


def annotate_pts(ax, coord_list, prec=3, size=10):
    annotated = []
    for i, text in enumerate(label):
        annotation = f'{text} ({",".join([str(round(coord, prec)) for coord in coord_list[i]])})'
        if annotation in annotated:
            continue
        else:
            ax.text(
                *(coord_list[i]),
                annotation,
                size=size,
                color='blue'
            )
            annotated.append(annotation)
    return ax


def multi_view():
    fig3d, ax3d = plt.subplots(subplot_kw=dict(projection='3d'))
    draw_3d(fig3d, ax3d)
    # Display projection plane
    xx, zz = np.meshgrid(range(1, 6), range(6))
    yy = zz * 0
    ax3d.plot_surface(xx, yy, zz, alpha=.25, color='b')

    fig2d, ax2d = plt.subplots()
    fig2d.suptitle('Projected Figure')
    ax2d.set_xlabel("X")
    ax2d.set_ylabel("Z")
    ax2d.plot(x, z)
    annotate_pts(ax2d, [(x[i], z[i]) for i in range(len(label))])
    plt.show()


def perspective():
    # Project onto y=0 with vanishing point at (3, -10, 1.5)
    vanishing_pt = (1.5, -5, 1.5)
    proj_plane_y = 0

    fig3d, ax3d = plt.subplots(subplot_kw=dict(projection='3d'))
    fig3d, ax3d = draw_3d(fig3d, ax3d)  # Show 3d figure

    # Plot vanishing point
    ax3d.plot(*vanishing_pt, 'ro')
    ax3d.text(*vanishing_pt, 'Vanishing\nPoint')

    # Plot projection plane
    xx, zz = np.meshgrid(range(1, 4), range(4))
    yy = zz * 0
    ax3d.plot_surface(xx, yy, zz, alpha=.25, color='b')

    # Plot projected figure
    fig2d, ax2d = plt.subplots()
    fig2d.suptitle('Projected Figure')
    x2d, z2d = [], []
    for i in range(len(x)):
        dir_vector = (x[i]-vanishing_pt[0], y[i]-vanishing_pt[1], z[i]-vanishing_pt[2])
        init_point = (x[i], y[i], z[i])
        # Line eq: init_point + a*dir_vector
        k = -((proj_plane_y-init_point[1]) / dir_vector[1])  # Calculate multiple of dir vector at which y=0
        x2d.append(init_point[0] + k * dir_vector[0])
        z2d.append(init_point[2] + k * dir_vector[2])

    ax2d.set_xlabel("X")
    ax2d.set_ylabel("Z")
    ax2d.plot(x2d, z2d)
    # ax2d = annotate_pts(ax2d, [(x2d[i], z2d[i]) for i in range(len(label))])
    plt.show()


if __name__ == '__main__':
    perspective()
    # multi_view()
