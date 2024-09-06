# 安装 mmdet

## Clone
```shell
git clone https://github.com/open-mmlab/mmdetection.git mmdetection3.3
cd mmdetection3.3
```

## 安装依赖
```shell
conda create --name lcs_mmdetection3.3 python=3.8
conda activate lcs_mmdetection3.3
pip install torch==2.1.2 torchvision==0.16.2 torchaudio==2.1.2 --index-url https://download.pytorch.org/whl/cu121
pip install -U openmim
mim install mmcv
pip install -v -e .
```

## 验证
```shell
python -c 'import torch;print(torch.__version__);print(torch.version.cuda)'
python -c 'from mmdet.apis import init_detector, inference_detector'

mim download mmdet --config rtmdet_tiny_8xb32-300e_coco --dest .
python demo/image_demo.py demo/demo.jpg rtmdet_tiny_8xb32-300e_coco.py \
--weights rtmdet_tiny_8xb32-300e_coco_20220902_112414-78e30dcc.pth --device cuda:0
```