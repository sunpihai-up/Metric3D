if __name__=='__main__':
    import os
    from shutil import copy

    dstD = "E:/eigen/train"
    f = open("./data/kitti_eigen_train.txt", "r")
    lines = f.readlines()
    for line in lines:
        r_path, d_path,  = line.split(' ')
        if depth_path == "None":
            continue
        rgb_path = "E:/kitt-raw/raw/" + r_path
        depth_path = "E:/kitti-depthp/data_depth_annotated/train/" + d_path
        if os.path.exists(depth_path) == False:
            depth_path = depth_path.replace('train', 'val')
        if os.path.exists(rgb_path) and os.path.exists(depth_path):
            copy(rgb_path, dstD + "/rgb/" + r_path)
            copy(depth_path, dstD + "/gt/" + d_path)
    
    # dstD = "E:/eigen/test"
    # f = open("./data/kitti_eigen_test.txt", "r")
    # lines = f.readlines()
    # for line in lines:
    #     r_path, d_path,  = line.split(' ')
    #     if depth_path == "None":
    #         continue
    #     rgb_path = "E:/kitt-raw/raw" + r_path
    #     depth_path = "E:/kitti-depthp/data_depth_annotated/train" + d_path
    #     if os.path.exists(depth_path) == False:
    #         depth_path = depth_path.replace('train', 'val')
    #     if os.path.exists(rgb_path) and os.path.exists(depth_path):
    #         copy(rgb_path, dstD + "/rgb/" + r_path)
    #         copy(depth_path, dstD + "/gt/" + d_path)