.. _about:
.. highlight:: rst

====================================
About Spydur
====================================

*Spydur* is the name of University of Richmond's High Performance
Computing environment, and environment that is available to all
faculty and their students who do research.

UR purchased *Spydur* in 2021. It is a custom built cluster computer
to support the research done at UR. These nodes are available
as of |today|:

- 12 compute nodes with 52 Xeon cores and 384GB of memory each.
- 19 compute nodes with 52 Xeon cores and 768GB of memory each.
- 5 compute nodes with 52 Xeon cores and 1536GB of memory each.
- 2 compute nodes that support scientific computing with A40 GPUs.
- 1 compute node configured for AI and ML computing with A100 GPUs.

A total of 2028 Xeon cores and 28TB of memory. 

Storage is provided by 336TB disc in a RAID 6 configuration, supporting a minimum
of 2TB of fast SSD storage on each node.

*Spydur* runs the `SLURM <https://slurm.schedmd.com>`_ resource 
management software to schedule the work and allocate the 
available nodes fairly. More information about SLURM is available
on the SLURM website.

Partitions
--------------

The above nodes are grouped into named partitions.

- ``basic`` The default partition, and representing the nodes with 384GB and no GPU.
- ``medium`` Compute nodes with 768GB.
- ``large`` Compute nodes with 1536GB (1.5TB).
- ``ML`` The node with the A100 GPU.
- ``sci`` The two nodes with A40 GPUs. 

Additionally, we have "condo" nodes associated with UR faculty
who have purchased nodes for their particular research.  
