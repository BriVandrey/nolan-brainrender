from brainrender import settings
from brainrender import Scene
from bg_atlasapi import show_atlases


def save_csv_with_list_of_abbreviations(scene):
    # run this to make a csv file with all tha names of the brain areas available in the atlas
    regions = scene.atlas.lookup_df
    regions.to_csv('regions.csv')
    print(regions.head())
    print(scene.atlas.hierarchy)


def plot_brain_with_ec_and_hpc_highlighted(scene, hemisphere=None, color_ec='skyblue', color_hpc='yellow', color_dec='navy', color_brain='grey'):
    # these lines add the the structures to the image
    root = scene.add_brain_region("root", alpha=0.1, color=color_brain)  # this is the brian outline
    ec = scene.add_brain_region("ENT", alpha=0.6, color=color_ec, hemisphere=hemisphere)
    hpc = scene.add_brain_region("HIP", alpha=0.6, color=color_hpc, hemisphere=hemisphere)
    deep_EC = scene.add_brain_region("ENTm5", "ENTm6", "ENTl5", "ENTl6a", alpha=0.6, color=color_dec, hemisphere=hemisphere)

    ec_slice = scene.add_brain_region("ENT", alpha=1, color=color_dec, hemisphere=hemisphere, force=True)
    hpc_slice = scene.add_brain_region("HIP", alpha=1, color=color_dec, hemisphere=hemisphere, force=True)
    m5, m6, l5, l6 = scene.add_brain_region("ENTm5", "ENTm6", "ENTl5", "ENTl6a", alpha=1, color=color_dec, hemisphere=hemisphere, force=True)

    # the code below adds a slice (horizontal) to the image
    # root_to_slice = scene.add_brain_region("root", alpha=0.3, color=color_brain, force=True)
    root_to_slice2 = scene.add_brain_region("root", alpha=1, color=color_dec, force=True)

    plane_pos1 = [ec.centerOfMass()[0], ec.centerOfMass()[1] - 1200, ec.centerOfMass()[2]]
    plane_pos2 = [ec.centerOfMass()[0], ec.centerOfMass()[1] - 1100, ec.centerOfMass()[2]]
    plane1 = scene.atlas.get_plane(pos=plane_pos1, norm=(0, 1, 0))
    plane2 = scene.atlas.get_plane(pos=plane_pos2, norm=(0, -1, 0))
    #scene.slice(plane1, actors=[root_to_slice], close_actors=True)  # this looks like a plane
    #scene.slice(plane2, actors=[root_to_slice], close_actors=True)

    scene.slice(plane1, actors=[root_to_slice2, ec_slice, hpc_slice, m5, m6, l5, l6], close_actors=False)  # this looks like a line
    scene.slice(plane2, actors=[root_to_slice2, ec_slice, hpc_slice, m5, m6, l5, l6], close_actors=False)
    return scene


def plot_horizontal_slice(scene, hemisphere=None, color_ec='skyblue', color_hpc='yellow', color_dec='navy'):
    # these lines add the the structures to the image
    root = scene.add_brain_region("root", alpha=0.1, color='grey', hemisphere=hemisphere)  # this is the brian outline
    ec = scene.add_brain_region("ENT", alpha=0.6, color=color_ec, hemisphere=hemisphere)
    hpc = scene.add_brain_region("HIP", alpha=0.6, color=color_hpc, hemisphere=hemisphere)
    m5, m6, l5, l6 = scene.add_brain_region("ENTm5", "ENTm6", "ENTl5", "ENTl6a", alpha=0.6, color=color_dec, hemisphere=hemisphere)
    plane_pos1 = [ec.centerOfMass()[0], ec.centerOfMass()[1] - 1200, ec.centerOfMass()[2]]
    plane_pos2 = [ec.centerOfMass()[0], ec.centerOfMass()[1] - 1100, ec.centerOfMass()[2]]
    plane1 = scene.atlas.get_plane(pos=plane_pos1, norm=(0, 1, 0))
    plane2 = scene.atlas.get_plane(pos=plane_pos2, norm=(0, -1, 0))
    scene.slice(plane1, actors=[root, ec, hpc, m5, m6, l5, l6], close_actors=True)
    scene.slice(plane2, actors=[root, ec, hpc, m5, m6, l5, l6], close_actors=True)
    return scene


def plot_horizontal_slice_lec_mec(scene, hemisphere=None, color_mec='skyblue', color_hpc='yellow', color_lec='navy'):
    # these lines add the the structures to the image
    root = scene.add_brain_region("root", alpha=0.1, color='grey', hemisphere=hemisphere)  # this is the brian outline
    mec = scene.add_brain_region("ENTm", alpha=0.6, color=color_mec, hemisphere=hemisphere)
    # lec = scene.add_brain_region("ENTl", alpha=0.6, color=color_lec, hemisphere=hemisphere)
    hpc = scene.add_brain_region("HIP", alpha=0.6, color=color_hpc, hemisphere=hemisphere)
    # bs = scene.add_brain_region("BS", alpha=0.1, color='grey', hemisphere=hemisphere)
    plane_pos1 = [mec.centerOfMass()[0], mec.centerOfMass()[1] - 1200, mec.centerOfMass()[2]]
    plane_pos2 = [mec.centerOfMass()[0], mec.centerOfMass()[1] - 1100, mec.centerOfMass()[2]]
    plane1 = scene.atlas.get_plane(pos=plane_pos1, norm=(0, 1, 0))
    plane2 = scene.atlas.get_plane(pos=plane_pos2, norm=(0, -1, 0))
    scene.slice(plane1, actors=[root, mec, hpc], close_actors=True)
    scene.slice(plane2, actors=[root, mec, hpc], close_actors=True)
    return scene


def plot_lec_vs_mec(scene, hemisphere=None, color_mec='skyblue', color_hpc='yellow', color_lec='navy', color_brain='grey'):
    # these lines add the the structures to the image
    root = scene.add_brain_region("root", alpha=0.1, color=color_brain)  # this is the brian outline
    mec = scene.add_brain_region("ENTm", alpha=0.6, color=color_mec, hemisphere=hemisphere)
    lec = scene.add_brain_region("ENTl", alpha=0.6, color=color_lec, hemisphere=hemisphere)
    hpc = scene.add_brain_region("HIP", alpha=0.6, color=color_hpc, hemisphere=hemisphere)
    # bs = scene.add_brain_region("BS", alpha=0.1, color='grey')

    mec_slice = scene.add_brain_region("ENTm", alpha=1, color=color_mec, hemisphere=hemisphere, force=True)
    lec_slice = scene.add_brain_region("ENTl", alpha=1, color=color_lec, hemisphere=hemisphere, force=True)
    hpc_slice = scene.add_brain_region("HIP", alpha=1, color=color_hpc, hemisphere=hemisphere, force=True)
    # bs_slice = scene.add_brain_region("BS", alpha=0.1, color='grey', force=True)

    # the code below adds a slice (horizontal) to the image
    # root_to_slice = scene.add_brain_region("root", alpha=0.3, color=color_brain, force=True)
    root_to_slice2 = scene.add_brain_region("root", alpha=1, color='navy', force=True)

    plane_pos1 = [mec.centerOfMass()[0], mec.centerOfMass()[1] - 1200, mec.centerOfMass()[2]]
    plane_pos2 = [mec.centerOfMass()[0], mec.centerOfMass()[1] - 1100, mec.centerOfMass()[2]]
    plane1 = scene.atlas.get_plane(pos=plane_pos1, norm=(0, 1, 0))
    plane2 = scene.atlas.get_plane(pos=plane_pos2, norm=(0, -1, 0))
    #scene.slice(plane1, actors=[root_to_slice], close_actors=True)  # this looks like a plane
    #scene.slice(plane2, actors=[root_to_slice], close_actors=True)

    scene.slice(plane1, actors=[root_to_slice2, mec_slice, hpc_slice, lec_slice], close_actors=False)  # this looks like a line
    scene.slice(plane2, actors=[root_to_slice2, mec_slice, hpc_slice, lec_slice], close_actors=False)

    return scene


def draw_brain(save_path=None):
    settings.SHADER_STYLE = "default"
    settings.ROOT_ALPHA = .1   # this sets how transparent the brain outline is
    settings.SHOW_AXES = False  # hides the axes from the image
    color_lec = [68, 119, 170]
    color_mec = [102, 204, 238]
    color_hpc = [204, 187, 68]
    # atlas = 'osten_mouse_25um'
    atlas = None
    scene = Scene(root=False, inset=False, screenshots_folder=save_path, atlas_name=atlas)  # makes a scene instance
    # show_atlases()
    scene = plot_lec_vs_mec(scene, hemisphere=None, color_mec=color_mec, color_hpc=color_hpc, color_lec=color_lec, color_brain='grey')
    # scene = plot_brain_with_ec_and_hpc_highlighted(scene, color_ec='skyblue', color_hpc='yellow', color_dec='navy', color_brain='grey')  # code to add structures to the scene
    scene.render(zoom=1.5)  # this line will display the image
    # these lines will make a new scene with a horizontal section
    scene = Scene(root=False, inset=False, screenshots_folder=save_path, atlas_name=atlas)  # makes a scene instance
    # scene = plot_horizontal_slice(scene, hemisphere=None, color_ec='skyblue', color_hpc='yellow', color_dec='navy')
    scene = plot_horizontal_slice_lec_mec(scene, hemisphere=None, color_mec=color_mec, color_hpc=color_hpc, color_lec=color_lec)
    # scene.screenshot(name='deep_mec_review.png', scale=2)  # this line will save a screenshot
    scene.render(zoom=1.5)  # this line will display the image (not compatible with the screenshot...)


def main():
    # output figures will be saved here
    draw_brain()


if __name__ == '__main__':
    main()
