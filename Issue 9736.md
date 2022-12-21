# Issue 9736: gfran totally broken on 32-bit OpenSolaris  on x86 CPU

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-12 17:27:24

Assignee: mvngu

CC:  jsp jhpalmieri

*== Hardware & Software ==
 * Sun Ultra 27 
 * 3.33 GHz Intel W3580 Xeon. Quad core. 8 threads. 
 * 12 GB RAM
 * OpenSolaris 2009.06 snv_134b X86
 * Sage 4.5.3.alpha0
 * gcc 4.5.0 configured to use the Sun linker and GNU assembler. 
 == The problem ==
It would appear 'gfan' is totally broken on this setup, and as a result several tests fail. Strangly, the same problem is *not* observed on a Dell Optiplex 755 running Solaris 10 on x86 - it's only seen on the OpenSolaris machine. 



```
sage -t  -long devel/sage/doc/en/tutorial/tour_advanced.rst
**********************************************************************
File "/export/home/drkirkby/32/sage-4.5.3.alpha0/devel/sage-main/doc/en/tutorial/tour_advanced.rst", line 66:
    sage: F.reduced_groebner_bases ()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1, in <module>
        F.reduced_groebner_bases ()###line 66:
    sage: F.reduced_groebner_bases ()
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/lib/python/site-packages/sage/rings/polynomial/groebner_fan.py", line 696, in reduced_groebner_bases
        G = self._gfan_reduced_groebner_bases()
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/lib/python/site-packages/sage/rings/polynomial/groebner_fan.py", line 647, in _gfan_reduced_groebner_bases
        B = self.gfan()
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/lib/python/site-packages/sage/rings/polynomial/groebner_fan.py", line 755, in gfan
        s = gfan(I, cmd, verbose=self.__verbose, format=format)
      File "/export/home/drkirkby/32/sage-4.5.3.alpha0/local/lib/python/site-packages/sage/interfaces/gfan.py", line 67, in __call__
        raise RuntimeError, err
    RuntimeError: ld.so.1: gfan: fatal: relocation error: file /export/home/drkirkby/32/sage-4.5.3.alpha0/local/bin/gfan: symbol _ZNSt15_List_node_base7_M_hookEPS_: referenced symbol not found
```





---

Comment by drkirkby created at 2010-08-14 09:00:15

This was an error on my part. `LD_LIBRARY_PATH` was not set, and neither were `LD_OPTIONS`, so gfan was picking up the older gcc header files included with OpenSolaris, and not the newer ones which were part of the gcc 4.5.0 on the system. 

As such, this ticket is invalid. 

The only issues affecting 32-bit build on OpenSolaris on x86 are the same as as those effecting 32-bit builds Solaris 10 x86. These are shown on the METATICKET #9734. The problems effecting the 32-bit builds on x86 hardward are:

 * Numerical noise issues, #9689,  #9693 and #9735.
 * Issues related to SYMPOW (#9703), which is a rather dubious package that is presenting problems on multiple systems (Cygwin and ArchLinux being two of them) - see #9166. 

Dave


---

Comment by drkirkby created at 2010-08-14 09:00:15

Resolution: invalid
