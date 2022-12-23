# Issue 8400: doctest devel/sage/sage/databases/database.py fails on Solaris 10 (SPARC)

Issue created by migration from https://trac.sagemath.org/ticket/8400

Original creator: drkirkby

Original creation time: 2010-02-28 16:25:56

Assignee: tbd

## Details of the computer
 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3

 == Sage version 4.3.3 (with several patches) ==
I'm using a patched version of Sage sage-4.3.3. The patches include:

 * #7867 Python patch, to allow Sage library to build. 
 * #8191 Addition of iconv, which is needed for R
 * #8285 Update R's spkg-install to work on Solaris
 * #8363 Remove a useless check for mpir in cddlib 
 * #8375 Numerical noise in devel/sage/sage/symbolic/pynac.pyx
 * #8374 Numerical noise in devel/sage/sage/symbolic/constants_c.pyx
 * #8371 Patch to allow pyprocessing to build - it failed after python was patched as #7867. (Note #6503 aims to remove pyprocessing completely). 

 == The problem ==
There are 8 test failures on this rather old SPARC. Increasing SAGE_TIMEOUT allowed 3 to pass. The longest is "devel/sage/sage/rings/polynomial/symmetric_ideal.py" which takes 459.4 s. 

However, 5 failures remain outstanding. 


```
    sage -t  "devel/sage/sage/graphs/graph_list.py" # Segfault
    sage -t  "devel/sage/sage/graphs/generic_graph.py" # Segfault
    sage -t  "devel/sage/sage/graphs/graph.py" # Segfault
    sage -t  "devel/sage/sage/graphs/graph_database.py" # Segfault
    sage -t  "devel/sage/sage/databases/database.py" # Segfault
```

This ticket is documenting graph_database.py, or to be more precise

"devel/sage/sage/graphs/graph_database.py"


---

Comment by drkirkby created at 2010-03-01 13:35:39

This problem goes away if sqlite is updated to version 3.6.22, which is the latest version.

I created a trac ticket for that - #8408

Dave


---

Comment by mhansen created at 2010-03-06 23:11:27

Resolution: fixed


---

Comment by mhansen created at 2010-03-06 23:11:27

Fixed by #8408
