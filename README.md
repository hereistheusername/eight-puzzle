# eight-puzzle

## Introduce

**dependencies**

1. Numpy: use ndarray to represent state of eight puzzle
2. PyInquirer: use this module to constructe command line interface

**preparation**

> pip install -r ./requirements.txt

**execution**

>python eight_puzzle.py

## Performance

Instead of computing distances while sorting, I put distances in nodes to reduce computation.

Here is the current performance.(recording time drags the speed slightly)

<img src="img/README/QQ20210210-150445@2x.png" alt="QQ20210210-150445@2x" style="zoom:50%;" />

Below is the performance before improvment.

<img src="img/README/QQ20210210-150625@2x.png" alt="QQ20210210-150625@2x" style="zoom:50%;" />

## Examples

<img src="img/README/image-20210223115316236.png" alt="image-20210223115316236" style="zoom:50%;" />

According to the performance of your computer, Uniform Cost Search will time out between depth 10 and 15.