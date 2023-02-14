"""
Script for plotting probe trajectories in superficial MEC
Dimensions used are relevant to Cambridge Neurotech 4-shank probes (P-Series, 64 channel)
"""

import math
import numpy as np
from brainrender import Scene
from brainrender import settings
from brainrender.actors import Cylinder


# developed by Harry Clark
def add_probes(scene, Cylinder2, cranial_site_xyz=np.array([0, 0, 0]), depth=1000,
               attack_angle_x=-15, color="red", distance_between_probes=250, radius=20):
    # presumes the only angle that varies is the y axis of the stereotax (What we call Y but is called X here)

    attack_angle_x = attack_angle_x*-1
    attack_angle_x = np.deg2rad(attack_angle_x)
    z = 0
    y = depth*np.cos(attack_angle_x)
    x = depth*np.sin(attack_angle_x)

    target_site = cranial_site_xyz + np.array([x, y, z])

    for i in range(4):
        probe_offset = np.array([0, 0, -i*distance_between_probes])
        actor = Cylinder2(StereoToCCF(cranial_site_xyz+probe_offset), StereoToCCF(target_site+probe_offset), scene.root, color=color, radius=radius)
        scene.add(actor)
    return


# developed by Matt Nolan
def StereoToCCF(SC=np.array([1, 1, 1]), angle=-0.0873):
    """
    :param SC: array with stereotaxic coordinates to be transformed
    :return: array containing corresponding CCF coordinates in μm
    """
    stretch = SC/np.array([1, 0.9434, 1])
    rotate = np.array([(stretch[0] * math.cos(angle) - stretch[1] * math.sin(angle)),
                       (stretch[0] * math.sin(angle) + stretch[1] * math.cos(angle)), stretch[2]])
    trans = rotate + np.array([5400, 440, 5700])

    return trans


def plot_probes_in_mec(Cylinder2):
    settings.SHADER_STYLE = 'plastic'  # other options: metallic, plastic, shiny, glossy, cartoon, default
    settings.ROOT_ALPHA = .1   # this sets how transparent the brain outline is
    settings.SHOW_AXES = True  # shows/hides the ABA CCF axes from the image
    scene = Scene(root=False, inset=False, atlas_name="allen_mouse_10um")  # makes a scene instance
    root = scene.add_brain_region("root", alpha=0.1, color="grey")  # this is the brain outline
    mec = scene.add_brain_region("ENTm", alpha=0.2, color="lightskyblue", hemisphere=None)  # whole mec
    mec_l2 = scene.add_brain_region("ENTm2", alpha=0.2, color="royalblue", hemisphere=None)  # mec l2
    mec_coords = np.array([3800, 0, -3100])  # AP: -3.8, ML: first probe at -3.1
  #  add_probes(scene, Cylinder2, cranial_site_xyz=mec_coords, attack_angle_x=-15, color="forestgreen", depth=2800, radius=11)  # probe at usual angle for implants (tetrodes)
    add_probes(scene, Cylinder2, cranial_site_xyz=mec_coords, attack_angle_x=-13, color="red", depth=3000, radius=10)  # probe angled 13 deg
    add_probes(scene, Cylinder2, cranial_site_xyz=mec_coords, attack_angle_x=-13, color="grey", depth=2800, radius=11)
    scene.render(zoom=2)


def main():
    # developed by Ian Hawes
    class Cylinder2(Cylinder):

        def __init__(self, pos_from, pos_to, root, color='black', alpha=1, radius=50):
            from vedo import shapes
            from brainrender.actor import Actor

            mesh = shapes.Cylinder(pos=[pos_from, pos_to], c=color, r=radius, alpha=alpha)
            Actor.__init__(self, mesh, name="Cylinder", br_class="Cylinder")

    plot_probes_in_mec(Cylinder2)


if __name__ == '__main__':
    main()