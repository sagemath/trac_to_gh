# Issue 9009: Mercurial is not building 64-bit with OpenSolaris with SAGE64=yes.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-05-21 16:17:10

Assignee: drkirkby

The title says it all. This should be a pretty easy one to solve:


```
creating build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
copying hgext/zeroconf/__init__.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
copying hgext/zeroconf/Zeroconf.py -> build/lib.solaris-2.11-i86pc-2.6/hgext/zeroconf
running build_ext
building 'mercurial.base85' extension
creating build/temp.solaris-2.11-i86pc-2.6
creating build/temp.solaris-2.11-i86pc-2.6/mercurial
gcc -fno-strict-aliasing -DNDEBUG -g -O3 -Wall -Wstrict-prototypes -fPIC -I/export/home/drkirkby/sage-4.4.2/local/include/python2.6 -c mercurial/base85.c -o build/temp.solaris-2.11-i86pc-2.6/mercurial/base85.o
In file included from /export/home/drkirkby/sage-4.4.2/local/include/python2.6/Python.h:58,
                 from mercurial/base85.c:12:
/export/home/drkirkby/sage-4.4.2/local/include/python2.6/pyport.h:685:2: error: #error "LONG_BIT definition appears wrong for platform (bad gcc/glibc config?)."
error: command 'gcc' failed with exit status 1
Error building mercurial

real	0m0.142s
user	0m0.083s
sys	0m0.055s
sage: An error occurred while installing mercurial-1.3.1.p1
```


The option -m64 is only being added if SAGE64 is set to yes *and* the platform is OS X, so it does not work on OpenSolaris. I've seen this problem many times, and the fix is pretty simple. 


---

Attachment

Mercurial patch to allow to build 64-bit on any operating system, not just OS X


---

Comment by drkirkby created at 2010-05-23 11:45:30

The revised spkg at http://boxen.math.washington.edu/home/kirkby/patches/mercurial-1.3.1.p2/mercurial-1.3.1.p2.spkg

resolves this issue, by removing the restriction that the operating system needs to be OS X in order that a 64-bit compilation can be performed.  


```
creating /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES
copying locale/el/LC_MESSAGES/hg.mo -> /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial/locale/el/LC_MESSAGES
running install_egg_info
Writing /export/home/drkirkby/sage-4.4.2/local/lib/python/mercurial-1.3.1-py2.6.egg-info
Deleting dead links

real    0m1.380s
user    0m1.068s
sys     0m0.269s
Successfully installed mercurial-1.3.1.p2
```



---

Comment by drkirkby created at 2010-05-23 11:45:38

Changing status from new to needs_review.


---

Comment by leif created at 2010-05-23 15:49:00

The patch looks ok (though I don't like _overwriting_ CFLAGS, but this has been in before).

Should perhaps be tested/reviewed by some MacOS and/or Solaris users.


---

Comment by mvngu created at 2010-05-23 21:31:22

I have tested the updated spkg on the machines t2.math (Solaris), sage.math (Ubuntu), and bsd.math (Mac OS X). The effect of the change is more prominent on t2.math because without the updated spkg, Mercurial won't build at all on that machine during the the Sage compilation process. Positive review from me.


---

Comment by mvngu created at 2010-05-23 21:31:22

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-05-24 18:25:25

For other OpenSolaris issues, see #9026


---

Comment by mhansen created at 2010-06-07 04:53:11

Resolution: fixed
