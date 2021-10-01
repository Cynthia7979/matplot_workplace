from mpl_toolkits import mplot3d
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

# Square
label = ("A", "B", "C", "D", "A")
x = (1, 1, 3, 3, 1)
y = np.multiply((1, 1, 1, 1, 1), 1)
z = (1, 3, 3, 1, 1)


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


if __name__ == '__main__':
    perspective()
    # multi_view()
