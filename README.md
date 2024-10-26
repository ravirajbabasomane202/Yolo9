#make Writable dataset
icacls "C:\Users\SidMane\Documents\ML_Tutorials\ML_Programs\Projects\Doctor_AI_FractureXpert\dataset" /grant "laptop-5pukkhtu\sid mane:F" /T

#train dataset 
python train.py --batch 8 --epochs 25 --device cuda:0 --close-mosaic 15 --weights weights\gelan-c.pt  --cfg weights\gelan-c.pt --cfg models\detect\gelan-c.yaml  --hyp hyp.scratch-high.yaml