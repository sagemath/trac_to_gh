# Issue 8532: Optional package mpi4py-1.1.0 fails to install on Solaris 10 SPARC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-13 23:24:05

Assignee: tbd

CC:  jhpalmieri chapoton dimpase

## Hardware & associated software

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

 == Sage version ==
 * 4.3.4.alpha1
 * Patch #8509 removing the -o option to grep to allow packages to install. 

 == The problem with the optional package mpi4py-1.1.0  ==

This might be because MPI fails to install - see #8522. 


```
src/mpi4py.MPI.c:79127: error: 'MPI_VERSION' undeclared (first use in this function)
src/mpi4py.MPI.c:79139: error: 'MPI_SUBVERSION' undeclared (first use in this function)
src/mpi4py.MPI.c:79151: error: 'MPI_MAX_PROCESSOR_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79163: error: 'MPI_MAX_ERROR_STRING' undeclared (first use in this function)
src/mpi4py.MPI.c:79175: error: 'MPI_MAX_PORT_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79187: error: 'MPI_MAX_INFO_KEY' undeclared (first use in this function)
src/mpi4py.MPI.c:79199: error: 'MPI_MAX_INFO_VAL' undeclared (first use in this function)
src/mpi4py.MPI.c:79211: error: 'MPI_MAX_OBJECT_NAME' undeclared (first use in this function)
src/mpi4py.MPI.c:79223: error: 'MPI_MAX_DATAREP_STRING' undeclared (first use in this function)
error: command 'gcc' failed with exit status 1

real    0m5.609s
user    0m5.111s
sys     0m0.434s
sage: An error occurred while installing mpi4py-1.1.0
```




---

Comment by mkoeppe created at 2020-06-19 18:07:10

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-06-19 18:07:10

solaris tickets should be closed as outdated


---

Comment by chapoton created at 2020-06-19 18:48:24

Resolution: invalid
