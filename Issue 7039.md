# Issue 7039: zn_poly-0.9 uses gcc, irrespective of setting of CC

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-09-27 16:01:04

Assignee: tbd

CC:  david.kirkby@onetel.net

Keywords: GNUism

Some time ago I sorted out the fact that znpoly failed to build if the linker used was the Sun linker, as znpoly used GNU specific flags. 

Well it seems there was another defect too, as the setting of CC is ignored too. 


```
zn_poly-0.9.p1/src/src/ks_support.c
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
make[2]: Entering directory `/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/spkg/build/zn_poly-0.9.p1/src'
gcc -fPIC -O3 -L. -I/export/home/drkirkby/sage/gcc32/sage-4.1.2.alpha2/local/include -I./include -DNDEBUG -o src/array.o -c src/array.c

```



---

Comment by Snark created at 2012-06-16 20:12:58

At ticket #12433, I ask about writing an autotools build system for zn_poly and push it upstream. Wouldn't that fix that report too?


---

Comment by jdemeyer created at 2015-09-08 12:48:16

Changing component from build to packages: standard.


---

Comment by jdemeyer created at 2015-09-08 13:02:09

Duplicate of #12433.


---

Comment by jdemeyer created at 2015-09-08 13:02:09

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-08 13:02:13

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:58:01

Resolution: fixed


---

Comment by drkirkby created at 2015-09-12 15:26:01

Should this not be "wont fix"? 

This almost automatic setting 

new -> needs_review
need_review to positive review
positive_review to closed. 

is in my opinion a bad thing.


---

Comment by jhpalmieri created at 2015-09-12 15:39:26

It looks like it is "won't fix": look at the ticket's "milestone".
