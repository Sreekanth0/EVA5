#### Total Parameters: 17,090

**Highest Accuracy achieved:** 99.42 in 16th Epoch



Things i tried:

First i added Batch Normalization to every layer & later player with number of filters & layers so that i can get under 20K Parameters.

Later tried out different architecture types,  Like pyramid or maintaining similar size filters in a block. 

I used only one maxpooling layer that to in the middle of the network, not near the input or output.

Didn't used Activation or batchnorm at the final layers.

I used Average Pooling with kernel equal to size of image at that layer which is equal to Global Average Pooling.

I did used dropout with small value, so that model can learn better.

I got the test accuracy of 99.42 in 16th epoch. 



