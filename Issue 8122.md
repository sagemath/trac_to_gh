# Issue 8122: Sage patches added directly to symmetica source

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-29 18:51:48

Assignee: GeorgSWeber

CC:  jsp mvngu

The symmerica package says in SPKG.txt


```
## Special Update/Build Instructions

Against common policy the patches in the patches directory have been applied to 
the src directory:

 * de.patch (Turn off banner)
 * macro.h.patch (Change some return types, this can be avoided)
 * makefile.patch (Fix compiler, inject CFLAGS)
 * sort_sum_rename.patch (rename sort tp sym_sort, sum to sym_sum) 
```


It would appear various patches have been made to the source code. 


http://boxen.math.washington.edu/home/kirkby/portability/symmetrica-2.0.p5/

has an updated version of symmetica, which will build with any compiler, and in 64-bit mode. However, it does not resolve the issue of patching the source directly. I modified the makefile, which had already been modified before. A patch was left, so I have tried to recreate the original makefile. But other files have been changed too. The packages is basically a bit of a mess


---

Comment by kini created at 2012-10-02 22:07:09

Has this been fixed already? Looks like the text you quoted no longer exists in SPKG.txt in symmetrica-2.0.p7.spkg, which currently ships with Sage.


---

Comment by kini created at 2012-10-02 22:07:22

Changing status from new to needs_info.


---

Comment by jdemeyer created at 2013-12-29 23:33:51

Changing status from needs_info to positive_review.


---

Comment by jdemeyer created at 2013-12-29 23:33:51

Duplicate of #10719.


---

Comment by vbraun created at 2014-01-04 04:18:20

Resolution: fixed
