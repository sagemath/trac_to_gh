# Issue 7040: Code actually in Sage (not other project) ignores CC and uses gcc.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 16:15:31

Assignee: tbd

Keywords: GNUism

Using

     * Solaris 10 update 7 on SPARC
     * sage-4.1.2.alpha2
     * Sun Studio 12.1
     * An updated configure script to allow the Sun compiler to be used http://sagetrac.org/sage_trac/ticket/7021

CC was set to the Sun C compiler. The code in the Sage (probalby 

./spkg/standard/sage-4.1.2.alpha2.spkg ) is using gcc  and ignoring CC. 


```
make[1]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg'
sage-spkg sage-4.1.2.alpha2
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or
SAGE_ROOT/local/bin/ directory.
sage-4.1.2.alpha2
Machine:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
Deleting directories from past builds of previous/current versions of sage-4.1.2.alpha2
Extracting package /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg ...
-rw-r--r--   1 drkirkby other    39522776 Sep 21 23:28 /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/standard/sage-4.1.2.alpha2.spkg
sage-4.1.2.alpha2/
sage-4.1.2.alpha2/doc/
<SNIP>
sage-4.1.2.alpha2/sage/symbolic/callable.py
sage-4.1.2.alpha2/spkg-install
sage-4.1.2.alpha2/README.txt
Finished extraction
****************************************************
Host system
uname -a:
SunOS swan 5.10 Generic_139555-08 sun4u sparc SUNW,Sun-Blade-1000
****************************************************
****************************************************
CC Version
/opt/xxxsunstudio12.1/bin/cc -v


usage: cc [ options] files.  Use 'cc -flags' for details
****************************************************
mv: cannot access /export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/devel/sage-main
gcc -o src/convert.pic.o -c -fPIC -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/python2.6 -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include/NTL -Iinclude src/convert.c
```



---

Comment by jdemeyer created at 2017-04-19 13:14:10

Sage just runs `distutils`, so it uses whatever compiler Python was configured with.


---

Comment by jdemeyer created at 2017-04-19 13:14:10

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2017-04-19 13:14:14

Changing status from needs_review to positive_review.


---

Comment by embray created at 2017-07-13 07:54:31

Closing tickets in the sage-duplicate/invalid/wontfix module with positive_review (i.e. someone has confirmed they should be closed).


---

Comment by embray created at 2017-07-13 07:54:31

Resolution: wontfix
