import os
import shutil
import random

# 源目录
src_img_dir = r'D:\dataOK\images'
src_label_dir = r'D:\dataOK\labels'

# 创建dataset目录在与原图片文件夹同级目录
dataset_dir = os.path.join(os.path.dirname(src_img_dir), 'dataset')
train_dir = os.path.join(dataset_dir, 'train')
val_dir = os.path.join(dataset_dir, 'val')
os.makedirs(os.path.join(train_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(train_dir, 'labels'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'images'), exist_ok=True)
os.makedirs(os.path.join(val_dir, 'labels'), exist_ok=True)

# 获取源目录下所有文件名
img_filenames = os.listdir(src_img_dir)
label_filenames = os.listdir(src_label_dir)

# 乱序文件列表
random.shuffle(img_filenames)

# 计算训练集和验证集数量
num_images = len(img_filenames)
num_train = int(0.8 * num_images)
num_val = num_images - num_train

# 分割数据
train_images = img_filenames[:num_train]
val_images = img_filenames[num_train:]

for filename in train_images:
    # 检查文件是否为.jpg或.png图片
    if filename.lower().endswith(('.jpg', '.png','.tif','jpeg','.webp')):
        src_img_path = os.path.join(src_img_dir, filename)
        dst_img_path = os.path.join(train_dir, 'images', filename)

        base_name, ext = os.path.splitext(filename)
        label_filename = base_name + '.txt'
        src_label_path = os.path.join(src_label_dir, label_filename)
        dst_label_path = os.path.join(train_dir, 'labels', label_filename)

        # 检查源文件是否存在
        if os.path.exists(src_img_path) and os.path.exists(src_label_path):
            shutil.move(src_img_path, dst_img_path)
            shutil.move(src_label_path, dst_label_path)

for filename in val_images:
    # 检查文件是否为.jpg或.png图片
    if filename.lower().endswith(('.jpg', '.png','.tif','jpeg','.webp')):
        src_img_path = os.path.join(src_img_dir, filename)
        dst_img_path = os.path.join(val_dir, 'images', filename)

        base_name, ext = os.path.splitext(filename)
        label_filename = base_name + '.txt'
        src_label_path = os.path.join(src_label_dir, label_filename)
        dst_label_path = os.path.join(val_dir, 'labels', label_filename)

        # 检查源文件是否存在
        if os.path.exists(src_img_path) and os.path.exists(src_label_path):
            shutil.move(src_img_path, dst_img_path)
            shutil.move(src_label_path, dst_label_path)
print("提取完毕")