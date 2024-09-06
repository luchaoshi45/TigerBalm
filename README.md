
# TigerBalm 🚀🚀🚀

Python implementation of common cv data script

## 目录

```markdown
labelme2coco: labelme 格式目标检测数据集转化为 coco 格式
images
    |---  1.jpg
    |---  1.json
    |---  2.jpg
    |---  2.json
    ...

script: 脚本

visualization 数据可视化
```

## 命令

```shell
# 启动 labelme
labelme

# labelme2coco
python labelme2coco/labelme2coco.py --input_dir batch_data/test --output_dir output/labelme2coco --labels labels.txt

# jpeg2jpg
python script/jpeg2jpg.py

# visualization
python visualization/voc.py --input C:/Users/Administrator/Desktop/a --output ./output/visualization_voc --num 20
```

