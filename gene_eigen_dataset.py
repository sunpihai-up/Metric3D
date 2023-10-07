if __name__=='__main__':
    import os
    from shutil import copy

    dstD = "E:/eigen/train"
    f = open("./data/kitti_eigen_train.txt", "r")
    lines = f.readlines()
    num = 0
    num2 = 0
    for line in lines:
        if (num2 > 10):
            break
        splitLine = line.split()
        r_path, d_path = splitLine[0], splitLine[1]
        if d_path == "None":
            continue
        
        rgb_path = "E:/kitt-raw/raw/" + r_path
        depth_path = "E:/kitti-depthp/data_depth_annotated/train/" + d_path
        
        if os.path.exists(depth_path) == False:
            depth_path = depth_path.replace('train', 'val')
        if os.path.exists(dstD + "/rgb/" + r_path) or os.path.exists(dstD + "/gt/" + d_path):
            continue
        if os.path.exists(rgb_path) and os.path.exists(depth_path):
            num = num + 1
            os.makedirs(os.path.dirname(dstD + "/rgb/" + r_path), exist_ok=True)
            copy(rgb_path, dstD + "/rgb/" + r_path)
            os.makedirs(os.path.dirname(dstD + "/gt/" + d_path), exist_ok=True)
            copy(depth_path, dstD + "/gt/" + d_path)
            print(f"NO: {num}, " + rgb_path + " is OK!")
        elif not(os.path.exists(rgb_path) and os.path.exists(depth_path)):
            print(rgb_path)
            num2 = num2 + 1