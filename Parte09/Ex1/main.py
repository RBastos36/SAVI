#!/usr/bin/env python3
# Sistemas Avançados de Visão Industrial (SAVI 22-23)
# Miguel Riem Oliveira, DEM, UA


import open3d as o3d


view = {
	"class_name" : "ViewTrajectory",
	"interval" : 29,
	"is_loop" : False,
	"trajectory" : 
	[
		{
			"boundingbox_max" : [ 2.7116048336029053, 1.2182252407073975, 3.8905272483825684 ],
			"boundingbox_min" : [ -2.4257750511169434, -1.6397310495376587, -1.3339539766311646 ],
			"field_of_view" : 60.0,
			"front" : [ 0.0625507639510193, -0.15946487909230223, -0.98521995222651748 ],
			"lookat" : [ 0.14291489124298096, -0.21075290441513062, 1.2782866358757019 ],
			"up" : [ 0.14768928117943522, -0.97480600986548682, 0.16715597313536362 ],
			"zoom" : 0.69999999999999996
		}
	],
	"version_major" : 1,
	"version_minor" : 0
}


def main():

    # --------------------------------------
    # Initialization
    # --------------------------------------
    filename = '/home/rantonio/Desktop/rgbd-scenes-v2_pc/rgbd-scenes-v2/pc/02.ply'
    print('Loading file ' + filename)
    point_cloud = o3d.io.read_point_cloud(filename)
    print(point_cloud)

    # --------------------------------------
    # Execution
    # --------------------------------------

    # entities = [point_cloud]
    # o3d.visualization.draw_geometries(entities,
    #                                   zoom=0.3412,
    #                                   front=view['trajectory'][0]['front'],
    #                                   lookat=view['trajectory'][0]['lookat'],
    #                                   up=view['trajectory'][0]['up'])
    

    vis = o3d.visualization.Visualizer()
    vis.create_window(visible=True) #works for me with False, on some systems needs to be true
    vis.add_geometry(point_cloud)
    vis.update_geometry(point_cloud)
    vis.poll_events()
    vis.update_renderer()
    vis.capture_screen_image("/home/rantonio/Desktop/test.png")
    vis.destroy_window()


    # --------------------------------------
    # Termination
    # --------------------------------------


if __name__ == "__main__":
    main()
