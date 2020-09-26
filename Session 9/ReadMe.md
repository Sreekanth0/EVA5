### Session-9 Assignment

Here we are training Cifar10 dataset with Session 8 model along with augmentations from Albumentations library and get atleast 87% accuracy. 

The package used here is developed by part of our team [Athena](https://github.com/firekind/athena). 

Here while training i used augmentations like Horizantal Flip with 50% probability, Contrast changes & HueSaturation for variations in images. It didn't very good results. Need to explore more of this library.

### Training

1. I have trained around for 100 epochs.
2. Used Step Learning rate & SGD optimizer with momentum. 
3. Tried l1 loss, but didn't got good result. 
4. Highest accuracy achieved is 87.91 in epoch 68.



Epoch: 68 / 100 782/782 [==============================] - 29s 37ms/step - train loss: 0.0244 - train accuracy: 99.4260 Test set: Average loss: 0.4403, Accuracy: 8791/10000 (87.91%).
