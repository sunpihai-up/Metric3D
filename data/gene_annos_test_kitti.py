if __name__=='__main__':
    import os
    import json

    f = open("./data/kitti_eigen_test.txt", "r")
    data_root = './data/eigen/test'
    rgb_root = os.path.join(data_root, 'rgb')
    gt_root = os.path.join(data_root, 'gt')

    lines = f.readlines()
    num = 0

    cam_in = [707.0493, 707.0493, 604.0814, 180.5066]
    depth_scale = 256.

    files = []
    for line in lines:
        splitLine = line.split()
        r_path, d_path = splitLine[0], splitLine[1]
        if d_path == "None":
            continue
        rgb_path = os.path.join(rgb_root, r_path)
        gt_path = os.path.join(gt_path, d_path)

        meta_data = {}
        meta_data['cam_in'] = cam_in
        meta_data['rgb'] = rgb_path
        meta_data['depth'] = gt_path
        meta_data['depth_scale'] = depth_scale
        files.append(meta_data)
    files_dict = dict(files=files)

    with open(os.join(data_root, 'test_annotations.json'), 'w') as f:
        json.dump(files_dict, f)
        