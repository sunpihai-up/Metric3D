if __name__=='__main__':
    import os
    import json

    f = open("./data/kitti_eigen_test.txt", "r")
    lines = f.readlines()
    files = []
    for line in lines:
        r_path, d_path,  = line.split(' ')
        if depth_path == "None":
            continue
        rgb_path = "./eigen/test/rgb/" + r_path
        depth_path = "./eigen/test/gt/" + d_path
        cam_in = [707.0493, 707.0493, 604.0814, 180.5066]
        depth_scale = 256.
        if os.path.exists(rgb_path) == False:
            raise RuntimeError(f'File does not exist: {rgb_path}')
        if os.path.exists(depth_path) == False:
            raise RuntimeError(f'File does not exist: {depth_path}')
        
        meta_data = {}
        meta_data['cam_in'] = cam_in
        meta_data['rgb'] = rgb_path
        meta_data['depth'] = depth_path
        meta_data['depth_scale'] = depth_scale
        files.append(meta_data)
    files_dict = dict(files=files)
    with open(osp.join('./data/eigen/test_annotations.json'), 'w') as f:
        json.dump(files_dict, f)
        