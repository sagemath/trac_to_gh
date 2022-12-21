# Issue 2785: The glitelib ticket

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-04-03 01:15:56

Assignee: gfurnish

This is the ticket for the glitelib spkg.  It requires an extcode patch.  Obtain at http://sage.math.washington.edu/home/gfurnish/spkg/glitelib-2.15.6.spkg


---

Comment by gfurnish created at 2008-04-03 01:16:04

Changing status from new to assigned.


---

Comment by gfurnish created at 2008-04-03 01:19:04

extcode patch


---

Attachment

This was voted in positively on sage-devel a while ago. Can somebody dig out the link?

Cheers,

Michael


---

Comment by gfurnish created at 2008-04-03 14:13:49

Voted for inclusion at http://groups.google.com/group/sage-devel/browse_thread/thread/e8ecbba8cd3deef2/59d047aaed4e6c66?lnk=gst&q=glib#59d047aaed4e6c66


---

Comment by mabshoff created at 2008-04-04 19:25:25

trac_2785_1.patch looks good to me. Merged in Sage 3.0.alpha1. The spkg still needs formal review.

Cheers,

Michael


---

Comment by gfurnish created at 2008-04-10 06:23:58

New spkg at http://sage.math.washington.edu/home/gfurnish/spkg/glitelib-2.15.6-p1.spkg


---

Comment by jkantor created at 2008-04-10 06:56:19

I don't think it worked. (Note I manually applied the patches in 1261 to an alpha1 build so its possible that is contributing).


```
Extracting package /Users/kantor/sage-3.0.alpha1/glitelib-2.15.6-p1.spkg ...
-rw-r--r--   1 kantor  kantor  135196 Apr  9 23:18 /Users/kantor/sage-3.0.alpha1/glitelib-2.15.6-p1.spkg
glitelib-2.15.6-p1/
glitelib-2.15.6-p1/.hgignore
glitelib-2.15.6-p1/.hg/
glitelib-2.15.6-p1/.hg/00changelog.i
glitelib-2.15.6-p1/.hg/requires
glitelib-2.15.6-p1/.hg/undo.dirstate
glitelib-2.15.6-p1/.hg/branch.cache
glitelib-2.15.6-p1/.hg/branch
glitelib-2.15.6-p1/.hg/store/
glitelib-2.15.6-p1/.hg/store/00manifest.i
glitelib-2.15.6-p1/.hg/store/undo
glitelib-2.15.6-p1/.hg/store/00changelog.i
glitelib-2.15.6-p1/.hg/store/data/
glitelib-2.15.6-p1/.hg/store/data/_s_p_k_g.txt.i
glitelib-2.15.6-p1/.hg/store/data/spkg-install.i
glitelib-2.15.6-p1/.hg/store/data/get-hg.i
glitelib-2.15.6-p1/.hg/store/data/.hgignore.i
glitelib-2.15.6-p1/.hg/store/data/get-orig-sources.i
glitelib-2.15.6-p1/.hg/dirstate
glitelib-2.15.6-p1/.hg/hgrc
glitelib-2.15.6-p1/src/
glitelib-2.15.6-p1/src/src/
glitelib-2.15.6-p1/src/src/garray.c
glitelib-2.15.6-p1/src/src/gslist.c
glitelib-2.15.6-p1/src/src/gqsort.c
glitelib-2.15.6-p1/src/src/gcache.c
glitelib-2.15.6-p1/src/src/gthread-none.c
glitelib-2.15.6-p1/src/src/gslice.c
glitelib-2.15.6-p1/src/src/gthread-win32.c
glitelib-2.15.6-p1/src/src/gthreadpool.c
glitelib-2.15.6-p1/src/src/gstrfuncs.c
glitelib-2.15.6-p1/src/src/gdataset.c
glitelib-2.15.6-p1/src/src/gnode.c
glitelib-2.15.6-p1/src/src/gsequence.c
glitelib-2.15.6-p1/src/src/gtimer.c
glitelib-2.15.6-p1/src/src/glist.c
glitelib-2.15.6-p1/src/src/gqueue.c
glitelib-2.15.6-p1/src/src/grel.c
glitelib-2.15.6-p1/src/src/gerror.c
glitelib-2.15.6-p1/src/src/ghash.c
glitelib-2.15.6-p1/src/src/gthread-impl.c
glitelib-2.15.6-p1/src/src/gthread-posix.c
glitelib-2.15.6-p1/src/src/grand.c
glitelib-2.15.6-p1/src/src/gtree.c
glitelib-2.15.6-p1/src/src/gthread.c
glitelib-2.15.6-p1/src/src/gasyncqueue.c
glitelib-2.15.6-p1/src/src/gatomic.c
glitelib-2.15.6-p1/src/src/gmem.c
glitelib-2.15.6-p1/src/src/gmp_globals.c
glitelib-2.15.6-p1/src/src/gprimes.c
glitelib-2.15.6-p1/src/include/
glitelib-2.15.6-p1/src/include/gquark.h
glitelib-2.15.6-p1/src/include/gprimes.h
glitelib-2.15.6-p1/src/include/gthread.h
glitelib-2.15.6-p1/src/include/gdataset.h
glitelib-2.15.6-p1/src/include/galiasdef.c
glitelib-2.15.6-p1/src/include/garray.h
glitelib-2.15.6-p1/src/include/gmacros.h
glitelib-2.15.6-p1/src/include/gerror.h
glitelib-2.15.6-p1/src/include/gcache.h
glitelib-2.15.6-p1/src/include/gthreadprivate.h
glitelib-2.15.6-p1/src/include/glist.h
glitelib-2.15.6-p1/src/include/gtimer.h
glitelib-2.15.6-p1/src/include/glib.h
glitelib-2.15.6-p1/src/include/gdatasetprivate.h
glitelib-2.15.6-p1/src/include/gutils.h
glitelib-2.15.6-p1/src/include/gmem.h
glitelib-2.15.6-p1/src/include/gthreadpool.h
glitelib-2.15.6-p1/src/include/gstrfuncs.h
glitelib-2.15.6-p1/src/include/grand.h
glitelib-2.15.6-p1/src/include/gslist.h
glitelib-2.15.6-p1/src/include/gtree.h
glitelib-2.15.6-p1/src/include/gsequence.h
glitelib-2.15.6-p1/src/include/gnode.h
glitelib-2.15.6-p1/src/include/galloca.h
glitelib-2.15.6-p1/src/include/gmp_globals.h
glitelib-2.15.6-p1/src/include/gslice.h
glitelib-2.15.6-p1/src/include/gasyncqueue.h
glitelib-2.15.6-p1/src/include/gatomic.h
glitelib-2.15.6-p1/src/include/grel.h
glitelib-2.15.6-p1/src/include/gtypes.h
glitelib-2.15.6-p1/src/include/ghash.h
glitelib-2.15.6-p1/src/include/galias.h
glitelib-2.15.6-p1/src/include/gqueue.h
glitelib-2.15.6-p1/src/include/gqsort.h
glitelib-2.15.6-p1/src/glitelib.py
glitelib-2.15.6-p1/SPKG.txt
glitelib-2.15.6-p1/spkg-install
Finished extraction
****************************************************
Host system
uname -a:
Darwin 389 8.11.1 Darwin Kernel Version 8.11.1: Wed Oct 10 18:23:28 PDT 2007; root:xnu-792.25.20~1/RELEASE_I386 i386 i386
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5367.obj~1/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=powerpc-apple-darwin8 --with-arch=nocona --with-tune=generic --program-prefix= --host=i686-apple-darwin8 --target=i686-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5367)
****************************************************
Configuring GLiteLib
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src
Building GLiteLib
In file included from /Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/galloca.h:30,
                 from /Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/glib.h:29,
                 from src/gasyncqueue.c:29:
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gtypes.h:457:21: error: missing binary operator before token "("
In file included from /Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/glib.h:46,
                 from src/gasyncqueue.c:29:
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:111: error: parse error before ‘gssize’
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:116: error: parse error before ‘gssize’
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:161: error: parse error before ‘gssize’
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:163: error: parse error before ‘gssize’


gcc -O2 -g -c -fPIC -fno-strict-aliasing src/gasyncqueue.c -DNDEBUG  -I/Users/kantor/sage-3.0.alpha1/local/include  -I/Users/kantor/sage-3.0.alpha1/local/include/csage  -I/Users/kantor/sage-3.0.alpha1/devel/sage/sage/ext  -I/Users/kantor/sage-3.0.alpha1/local/include/python2.5  -I/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include  -o src/gasyncqueue.o
In file included from /Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/garray.h:30,
                 from src/garray.c:36:
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gtypes.h:457:21: error: missing binary operator before token "("


gcc -O2 -g -c -fPIC -fno-strict-aliasing src/garray.c -DNDEBUG  -I/Users/kantor/sage-3.0.alpha1/local/include  -I/Users/kantor/sage-3.0.alpha1/local/include/csage  -I/Users/kantor/sage-3.0.alpha1/devel/sage/sage/ext  -I/Users/kantor/sage-3.0.alpha1/local/include/python2.5  -I/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include  -o src/garray.o

real    0m6.485s
user    0m2.428s
sys     0m3.671s
Successfully installed glitelib-2.15.6-p1
Now cleaning up tmp files.
Making SAGE/Python scripts relocatable...
Making script relocatable
Finished installing glitelib-2.15.6-p1.spkg
389:~/sage-3.0.alpha1 kantor$ gcc -v
Using built-in specs.
Target: i686-apple-darwin8
Configured with: /private/var/tmp/gcc/gcc-5367.obj~1/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=powerpc-apple-darwin8 --with-arch=nocona --with-tune=generic --program-prefix= --host=i686-apple-darwin8 --target=i686-apple-darwin8
Thread model: posix
gcc version 4.0.1 (Apple Computer, Inc. build 5367)
389:~/sage-3.0.alpha1 kantor$ ls
COPYING.txt             doc                     install.log             polybori-0.3.1.p0.spkg  tmp
HISTORY.txt             example.sage            ipython                 sage
README.txt              examples                local                   sage-README-osx.txt
data                    glitelib-2.15.6-p1.spkg makefile                sage-python
devel                   glitelib-2.15.6.spkg    matplotlibrc            spkg
389:~/sage-3.0.alpha1 kantor$ emacs install.log 

File Edit Options Buffers Tools Help                                                                                                     

/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:161: error: parse error before \342\200\230gssize\34\
2\200\231
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gstrfuncs.h:163: error: parse error before \342\200\230gssize\34\
2\200\231


gcc -O2 -g -c -fPIC -fno-strict-aliasing src/gasyncqueue.c -DNDEBUG  -I/Users/kantor/sage-3.0.alpha1/local/include  -I/Users/kantor/sage\
-3.0.alpha1/local/include/csage  -I/Users/kantor/sage-3.0.alpha1/devel/sage/sage/ext  -I/Users/kantor/sage-3.0.alpha1/local/include/pyth\
on2.5  -I/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include  -o src/gasyncqueue.o
In file included from /Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/garray.h:30,
                 from src/garray.c:36:
/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include/gtypes.h:457:21: error: missing binary operator before token "("


gcc -O2 -g -c -fPIC -fno-strict-aliasing src/garray.c -DNDEBUG  -I/Users/kantor/sage-3.0.alpha1/local/include  -I/Users/kantor/sage-3.0.\
alpha1/local/include/csage  -I/Users/kantor/sage-3.0.alpha1/devel/sage/sage/ext  -I/Users/kantor/sage-3.0.alpha1/local/include/python2.5\
  -I/Users/kantor/sage-3.0.alpha1/spkg/build/glitelib-2.15.6-p1/src/include  -o src/garray.o

real    0m6.485s
user    0m2.428s
sys     0m3.671s
Successfully installed glitelib-2.15.6-p1


```



---

Comment by boothby created at 2008-05-20 23:59:24

Build passes, and I've tested binary trees.  They work as advertized.  However, I had to modify misc/cython.py to get up and running.

We should test on more platforms than xeon/debian.


---

Comment by boothby created at 2008-06-11 21:18:41

Failure!


```
...
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: i686-apple-darwin9
Configured with: /var/tmp/gcc/gcc-5465~16/src/configure --disable-checking -enable-werror --prefix=/usr --mandir=/share/man --enable-languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic --host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
****************************************************
Configuring GLiteLib
Traceback (most recent call last):
  File "glitelib.py", line 337, in <module>
    buildglite(env,gccc)
  File "glitelib.py", line 29, in buildglite
    c_list.remove(os.path.abspath('src/gthread-win32.c'))
ValueError: list.remove(x): x not in list

real	0m2.957s
user	0m0.900s
sys	0m0.997s
Successfully installed glitelib-2.15.6
Now cleaning up tmp files.
Making SAGE/Python scripts relocatable...
Making script relocatable
Finished installing glitelib-2.15.6.spkg
```



---

Comment by craigcitro created at 2008-06-20 04:21:20

Changing keywords from "" to "editor_wstein".


---

Comment by malb created at 2009-01-22 23:05:33

It looks like this will never happen.


---

Comment by malb created at 2009-01-22 23:05:33

Resolution: wontfix
