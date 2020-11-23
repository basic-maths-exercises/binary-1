# An interesting sequence

We are now going to work out how to generate all the distinguishable permutations of the symbols in the list `[1,1,0,0,1]`.  Notice that as there are indistinguishable symbols in this list there are not 5! distinguishable permutations.  Some of 5! ways we could jumble up the 5 objects in the list are indistinguishable.  If we swap the first two symbols in `[1,1,0,0,1]` in this list for instance we get the same sequence.

We could generate the indistinguishable permutations by using the algorithm that we just developed and by removing any duplicate permutations.  As we will see over the next few exercises, however, there is a better way to complete this task.  To understand this better way of generating these sequences what I want you to consider in this exercise is the following function:

![](https://render.githubusercontent.com/render/math?math=b(\mathbf{s})=\sum_{n=0}^{m-1}s_n2^n)

In this expression, ![](https://render.githubusercontent.com/render/math?math=\mathbf{s}), is a vector with ![](https://render.githubusercontent.com/render/math?math=m) elements and each of the elements, ![](https://render.githubusercontent.com/render/math?math=s_i), is either 0 or 1.

Modify the code in `main.py` so that the function called `compute_b` calculates the quantity, b, that is defined in the formula above.  Notice that this function takes a list called `digits`, which a vector of 0 and 1s .  I have called this function with each of the 8 distinguishable vectors that I can construct by selecting 3 0s and 1s in total in the code at the bottom of the slide.
