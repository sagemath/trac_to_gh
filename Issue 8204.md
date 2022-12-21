# Issue 8204: when upgrading sage, cddlib spkg goes interactive due to some errors in it

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-02-07 05:15:06

Assignee: tbd

There is something very broken about the new cddlib-094f.p2 standard spkg.  When I upgrade from sage-4.3.1 on any machine, it always asks me questions about some messed up patch.  This is very, very bad. 


```
...
cddlib-094f.p2/.hg/branch                                         
cddlib-094f.p2/.hg/branch.cache                                   
cddlib-094f.p2/.hg/requires                                       
cddlib-094f.p2/SPKG.txt                                           
Finished extraction                                               
****************************************************              
Host system                                                       
uname -a:                                                         
Linux boxen 2.6.24-24-server #1 SMP Fri Sep 18 16:47:05 UTC 2009 x86_64 GNU/Linux
****************************************************                             
****************************************************                             
CC Version                                                                       
gcc -v                                                                           
Using built-in specs.                                                            
Target: x86_64-linux-gnu                                                         
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.2 --program-suffix=-4.2 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu                           
Thread model: posix                                                                                                         
gcc version 4.2.4 (Ubuntu 4.2.4-1ubuntu4)                                                                                   
****************************************************                                                                        
patching file src/src-gmp/Makefile.am                                                                                       
Reversed (or previously applied) patch detected!  Assume -R? [n]                                                            
Apply anyway? [n]                                                                                                           
Skipping patch.                                                                                                             
2 out of 2 hunks ignored -- saving rejects to file src/src-gmp/Makefile.am.rej                                              
patching file src/src/Makefile.am                                                                                           
Reversed (or previously applied) patch detected!  
Assume -R? [n]     *** INTERACTIVE QUESTION!!! **** 
Apply anyway? [n]                                                                                                           
Skipping patch.                            
```



---

Comment by mvngu created at 2010-02-07 05:18:28

The problem is due to #7109. See #8115 for the same problem.


---

Comment by drkirkby created at 2010-02-07 08:43:20

On a similar, but not identical issue, #8122 has edits to the source directly, not via creating new versions of files, or by calling patch. It's bad practice, but not as serious as this one.


---

Comment by vbraun created at 2010-02-20 17:38:09

Changing status from new to needs_review.


---

Comment by vbraun created at 2010-02-20 17:38:09

Fixed by cddlib-094f.p4.spkg, see #8115.


---

Comment by mvngu created at 2010-02-20 17:43:19

Close as a duplicate of #8115.


---

Comment by mvngu created at 2010-02-20 17:43:19

Resolution: duplicate
