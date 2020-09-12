### Session-7 Assignment

Here we are training our model on Cifar10 dataset to get 80+ accuracy under 1M parameters. 

Part of our team worked on a application [Athena](https://github.com/firekind/athena), and we created models separately for training, you can find **my Model Architecture** [here](https://github.com/firekind/athena/blob/master/athena/models/cifar10_v2.py)

I followed similar to **Resnet18 Architecture**, where i maintained channel sizes same in the block and doubled it as move to next blocks, till i reach 8*8 size features.  I used **Depthwise Separable Convolutions** a lot as we have a constraint on parameters. Instead of maxpooling i used convolutions with stride 2 to decrease the size of features. 

To avoid overfitting i used dropout of 0.1 per layer and Batch Normalization along with L1 Regularization. Model performed good as we can see from the **gap between train & test accuracy.**

Total number of **parameters are: 677,738** and reached **Test accuracy around 82.8%.**

### Training:

The model was trained for 50 epochs, with an SGD optimizer with learning rate 0.001 and momentum 0.9. I used L1 Regularization as well. The highest accuracy was achieved around 83%. A snippet of the training output is shown below:

**Final Epochs **

![](images/epochs.png)



I did calculated **Receptive filed per layer and output size** as well. You can find below.



![](images/RF_calc.png)





