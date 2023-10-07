python mono/tools/train.py \
    'mono/configs/HourglassDecoder/test_kitti_convlarge_hourglass_0.3_150.py' \
    --load-from ./weight/convlarge_hourglass_0.3_150_step750k_v1.1.pth \
    --test_data_path ./data/eigen/test/test_annotations.json \
    --train_data_path ./data/eigen/train/train_annotations.json \
    --launcher None