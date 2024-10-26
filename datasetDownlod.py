#================== Step 1 ==========================
# import os
# import urllib.request

# # Define the download folder
# home = os.path.expanduser("~")
# weights_path = os.path.join(home, "weights")

# # Create the directory if it doesn't exist
# os.makedirs(weights_path, exist_ok=True)

# # URLs for downloading
# urls = [
#     "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt",
#     "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt",
#     "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt",
#     "https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt"
# ]

# # Download files
# for url in urls:
#     file_name = os.path.join(weights_path, url.split("/")[-1])
#     urllib.request.urlretrieve(url, file_name)
#     print(f"Downloaded {file_name}")

#================== Step 2 ==========================

# from roboflow import Roboflow
# rf = Roboflow(api_key="8u9qSFfQ9uTvqZKRqYV7")
# project = rf.workspace("handbruch").project("handbruche-2")
# version = project.version(3)
# dataset = version.download("yolov9")


#python train.py --batch 16 --epochs 25 --img 640 --device 0 --min-items 0 --close-mosaic 15 --data C:\Users\SidMane\Documents\ML_Tutorials\ML_Programs\Projects\Doctor_AI_FractureXpert\docmain\yolov9\Handbrüche-2-3\data.yaml --weights C:\Users\SidMane\Documents\ML_Tutorials\ML_Programs\Projects\Doctor_AI_FractureXpert\docmain\yolov9\weights\gelan-c.pt --cfg models\detect\gelan-c.yaml --hyp hyp.scratch-high.yaml
import torch
print(torch.cuda.is_available())  # Should return True
print(torch.cuda.device_count())  # Should return the number of GPUs
print(torch.cuda.get_device_name(0))  # Should return 'NVIDIA GeForce GTX 1650'

