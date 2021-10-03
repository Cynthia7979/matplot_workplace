"""
3d_proj_test.py
---------------

Code for the International Baccalaureate (IB) Mathematics AA Extended Essay:
What are the Advantages and Disadvantages of Different Projection Methods?

Written by Yirou (Cynthia) Wang.

Query about the topic or the code are welcomed, but do *not* plagiarize in any means.
Usages of this code, in sections or in its entirety, need to include a note specifying the original author.
"""

import numpy as np
import matplotlib.pyplot as plt

# # Pyramid
# label = ('C', 'B', 'D', 'C', 'A', 'B', 'A', 'D')
# x = (3, 1, 5, 3, 3, 1, 3, 5)
# y = (2, 5, 5, 2, 4, 5, 4, 5)
# z = (0, 0, 0, 0, 4, 0, 4, 0)

# # Cube
# label = ('A', 'B', 'C', 'D', 'A', 'E', 'F', 'B', 'F', 'G', 'C', 'G', 'H', 'D', 'H', 'E')
# x = (1, 1, 3, 3, 1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1)
# y = (1, 3, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 1, 1, 1)
# z = (1, 1, 1, 1, 1, 3, 3, 1, 3, 3, 1, 3, 3, 1, 3, 3)

# # Square
# label = ("A", "B", "C", "D", "A")
# x = (1, 1, 3, 3, 1)
# y = np.multiply((1, 1, 1, 1, 1), 1)
# z = (1, 3, 3, 1, 1)

# Test
label = []
x = np.linspace(-1, 1)
y = x
z = np.ones_like(y)


def draw_3d(fig, ax, x_=x, y_=y, z_=z, label_=label, show_coord=True, annotate=True, linestyle=''):
    fig.suptitle('3D Figure')
    ax.plot3D(x_, y_, z_, linestyle)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    if annotate:
        ax = annotate_pts(
            ax, [(x_[i], y_[i], z_[i]) for i in range(len(label_))],
            show_coord=show_coord,
            label_=label_
        )
    return fig, ax


def annotate_pts(ax, coord_list, prec=3, size=10, show_coord=True, label_=label):
    annotated = []
    for i, text in enumerate(label_):
        annotation = f'{text} {("("+",".join([str(round(coord, prec)) for coord in coord_list[i]])+")")*show_coord}'
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
    # Display 3D Figure
    draw_3d(fig3d, ax3d)

    # Display projection plane
    xx, zz = np.meshgrid(range(1, 6), range(6))
    yy = zz * 0
    ax3d.plot_surface(xx, yy, zz, alpha=.25, color='b')

    # Plot projected figure in 2D
    fig2d, ax2d = plt.subplots()
    fig2d.suptitle('Projected Figure')
    ax2d.set_xlabel("X")
    ax2d.set_ylabel("Z")
    ax2d.plot(x, z)
    annotate_pts(ax2d, [(x[i], z[i]) for i in range(len(label))])

    # Display the projected figure in 3D
    ax3d.plot3D(x, np.multiply(x, 0), z, 'r', alpha=.5)

    plt.show()


def perspective():
    vanishing_pt = (1.5, -5, 1.5)
    proj_plane_y = 0

    fig3d, ax3d = plt.subplots(subplot_kw=dict(projection='3d'))
    fig3d, ax3d = draw_3d(fig3d, ax3d, show_coord=False)  # Show 3d figure

    # Plot vanishing point
    ax3d.plot(*vanishing_pt, 'ro')
    ax3d.text(*vanishing_pt, 'V')

    # Plot projection plane
    # Source: https://stackoverflow.com/questions/29394305/how-does-one-draw-the-x-0-plane-using-matplotlib-mpl3d
    xx, zz = np.meshgrid(range(min(x+(vanishing_pt[0],))-1, max(x+(vanishing_pt[0],))+2),
                         range(min(z+(vanishing_pt[2],))-1, max(z+(vanishing_pt[2],))+2))
    yy = zz * 0
    ax3d.plot_surface(xx, yy, zz, alpha=.25, color='b')

    # Calculate projected figure
    fig2d, ax2d = plt.subplots()
    fig2d.suptitle('Projected Figure')
    x2d, z2d = [], []
    for i in range(len(x)):
        dir_vector = (x[i]-vanishing_pt[0], y[i]-vanishing_pt[1], z[i]-vanishing_pt[2])
        init_point = (x[i], y[i], z[i])
        # Line eq: init_point + a*dir_vector
        k = (proj_plane_y-init_point[1]) / dir_vector[1]  # Calculate multiple of dir vector at which y=0
        x2d.append(init_point[0] + k * dir_vector[0])
        z2d.append(init_point[2] + k * dir_vector[2])

        # Display the projection rays
        ax3d.plot(
            (x[i], vanishing_pt[0]), (y[i], vanishing_pt[1]), (z[i], vanishing_pt[2]),
            'k--',
            # linewidth=0.5,
            # alpha=.3
        )

    # Display the projected figure in 3D
    ax3d.plot3D(
        x2d, np.multiply(x2d, 0), z2d,
        'r',
        # alpha=.5
    )
    annotate_pts(
        ax3d, [(x2d[i], 0, z2d[i]) for i in range(len(label))],
        label_=[l+"'" for l in label],
        show_coord=False,
        size=12
    )

    # Plot projected figure
    ax2d.set_xlabel("X")
    ax2d.set_ylabel("Z")
    ax2d.plot(x2d, z2d)
    ax2d = annotate_pts(
        ax2d, [(x2d[i], z2d[i]) for i in range(len(label))],
        show_coord=False)
    plt.show()


def curvilinear():
    center = (0, 0, 0)  # Do not change this
    radius = 5
    proj_plane_x = radius+1
    fig3d, ax3d = plt.subplots(subplot_kw=dict(projection='3d'))



    # Display the projection sphere
    # Source: https://stackoverflow.com/questions/11140163/plotting-a-3d-cube-a-sphere-and-a-vector-in-matplotlib
    u, v = np.mgrid[0:2 * np.pi:20j, 0:np.pi:10j]
    x_ = (np.cos(u) * np.sin(v) * radius) + center[0]
    y_ = (np.sin(u) * np.sin(v) * radius) + center[1]
    z_ = (np.cos(v) * radius) + center[2]
    ax3d.plot_wireframe(x_, y_, z_, alpha=.3)

    # Display the projection plane
    # Source: https://stackoverflow.com/questions/29394305/how-does-one-draw-the-x-0-plane-using-matplotlib-mpl3d
    yy, zz = np.meshgrid(range(-radius-1, radius+2),
                         range(-radius-1, radius+2))
    xx = np.ones_like(zz) * proj_plane_x
    ax3d.plot_surface(xx, yy, zz, alpha=.25, color='b')

    x_sphere, y_sphere, z_sphere = [], [], []
    for i in range(len(x)):
        current_point = (x[i], y[i], z[i])
        projected_point = np.multiply(current_point,
                                      (radius / np.sqrt(sum(a**2 for a in current_point))))
        # Attained through similar triangles

        # Calculate primary projected point (on sphere)
        pri_pro_x, pri_pro_y, pri_pro_z = projected_point
        x_sphere.append(pri_pro_x)
        y_sphere.append(pri_pro_y)
        z_sphere.append(pri_pro_z)

        # Display the projection rays
        ax3d.plot(
            (x[i], pri_pro_x), (y[i], pri_pro_y), (z[i], pri_pro_z),
            'k--',
            # linewidth=0.5,
            # alpha=.3
        )
    ax3d.plot3D(x_sphere, y_sphere, z_sphere)

    # Project the sphere to y=-radius orthographically
    fig2d, ax2d = plt.subplots()
    ax2d.plot(y_sphere, z_sphere)
    plt.show()


if __name__ == '__main__':
    # perspective()
    # multi_view()
    curvilinear()
