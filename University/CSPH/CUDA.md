# CUDA Theory

## Why CUDA sucks!

* Proprietary spawn of the devil (NVIDIA)
 
## CUDA Architecture

CUDA Architecture can be split into three mastryoska-levels:

* **Kernel Grid** \Rightarrow The full compiled code to run on the GPU. It is split into Blocks

* **Blocks** $\Rightarrow$ A organization of threads. One block is executed by a streaming multiprocessing unit. Blocks are **Independent**

* **Threads** $\Rightarrow$ Basically a vector (think SIMD). Each thread runs on one of the GPU cores

A Kernel grid can only be launched with **only one** configuration(1-D, 2-D, 3-D), we can however launch multiple kernel grids with different configurations.

## Basic CUDA Syntax

Very similiar to-C, in fact made to integrate with C and C++



### Bulk Lauching
 ```cpp
 function<<<NumBlocks, ThreadsPerBlock>>>(function parameters);
 ```
