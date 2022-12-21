# Issue 8416: long doctest elliptic_curves/ell_modular_symbols.py fails on Solaris 10 (SPARC)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-03-02 10:58:15

Assignee: cremona

Applying all the patches at #8409, Sage 4.3.3 builds and passes all the normal doctests on Solaris 10 (SPARC) using the following hardware:

 * Sun Blade 1000
 * 2 x 900 MHz UltraSPARC III+ CPUs
 * 2 GB RAM
 * Solaris 10 03/2005 (first release of Solaris 10)
 * gcc 4.4.3 (uses Sun linker and assembler)

Running the long doctests there was one failure:


```
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
A mysterious error (perhaps a memory error?) occurred, which may have crashed doctest.
         [3.0 s]
```


This needs to be investigated. I've no idea if this is troublesome on any other platform.


PS, Using the hardware above, the time taken for the longest test was 1764.9 s.


```
sage -t  -long "devel/sage/sage/modular/ssmod/ssmod.py"
         [1764.9 s]
```


Dave 


---

Comment by drkirkby created at 2010-03-02 14:43:46

For reasons unknown, after I rebuilt the Sage library fully 

$ ./sage -ba

so the problem went away. I wont request the ticket is closed yet, until it has been tested again, as I can't understand why this should have happened. 


```
drkirkby`@`redstart:~/fresh/sage-4.3.3$ ./sage -t  -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
sage -t -long "devel/sage/sage/schemes/elliptic_curves/ell_modular_symbols.py"
	 [190.8 s]

```


Dave


---

Comment by drkirkby created at 2010-03-02 14:43:46

Changing status from new to needs_info.


---

Comment by drkirkby created at 2010-06-05 19:23:20

This can now be closed - it was solved ages ago now.


---

Comment by mvngu created at 2010-06-05 19:30:26

Resolution: fixed
