# Issue 8432: make iconv a prerequisite for building gd

Issue created by migration from https://trac.sagemath.org/ticket/8432

Original creator: mvngu

Original creation time: 2010-03-04 03:55:31

Assignee: tbd

From [sage-release](http://groups.google.com/group/sage-release/msg/2c501eca0da2a056):

```
As expected based on my experience with 4.3.3, I got a build error
building 4.3.4.alpha0, though this time it was a linking error with gd
rather than cddlib. Again, this is Fedora 10 on a 64-bit system, but
on a 32-bit network, so there exist 32-bit libraries findable via NFS
(under /usr/local). But this time I don't see any obvious evidence
that this is the source of the trouble.
-----
/bin/sh ./libtool --tag=CC --mode=link gcc  -fPIC -g -I"/scratch/
sage-4.3.4.alph
a0/local/include" -I/scratch/sage-4.3.4.alpha0/local/include/
freetype2/  -L/scra
tch/sage-4.3.4.alpha0/local/lib -Wl,--rpath -Wl,/scratch/
sage-4.3.4.alpha0/local
/lib  -L/scratch/sage-4.3.4.alpha0/local/lib  -o annotate
annotate.o ./libgd.la
 -lfontconfig -lfreetype -lpng12 -lz -lm
gcc -fPIC -g -I/scratch/sage-4.3.4.alpha0/local/include -I/scratch/
sage-4.3.4.al
pha0/local/include/freetype2/ -Wl,--rpath -Wl,/scratch/
sage-4.3.4.alpha0/local/l
ib -o .libs/annotate annotate.o  -L/scratch/sage-4.3.4.alpha0/local/
lib ./.libs/
libgd.so -lfontconfig /scratch/sage-4.3.4.alpha0/local/lib/
libfreetype.so /scrat
ch/sage-4.3.4.alpha0/local/lib/libpng12.so -lz -lm -Wl,--rpath -Wl,/
scratch/sage
-4.3.4.alpha0/local/lib
./.libs/libgd.so: undefined reference to `libiconv'
./.libs/libgd.so: undefined reference to `libiconv_close'
./.libs/libgd.so: undefined reference to `libiconv_open'
collect2: ld returned 1 exit status
```

This is due to gd being built before iconv. mpatel suggested at [#8191](http://trac.sagemath.org/sage_trac/ticket/8191#comment:10) to make iconv a dependency for building gd. See also #8306 which implements this dependency rule.


---

Comment by mvngu created at 2010-03-04 04:02:24

differences between deps in Sage 4.3.4.alpha0 and updated deps


---

Attachment

updated deps


---

Attachment


---

Comment by mvngu created at 2010-03-04 04:03:13

Changing status from new to needs_review.


---

Comment by mvngu created at 2010-03-04 04:07:06

You should replace the current file `SAGE_ROOT/spkg/standard/deps` in Sage 4.3.4.alpha0 with the updated one on this ticket, i.e. [deps](http://trac.sagemath.org/sage_trac/attachment/ticket/8432/deps).


---

Comment by drkirkby created at 2010-03-04 05:30:43

I'll make a patch for that. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how it ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too. 

There is, as yet an untested file on 't2' 

/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar

which has

* sage-4.3.4.alpha0 source
* All the patches list at http://trac.sagemath.org/sage_trac/ticket/8409 applied
* This item addressed. 

That may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.

Dave


---

Comment by drkirkby created at 2010-03-04 05:30:43

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2010-03-04 05:34:13

Sorry, I forgot to preview my previous post. I'll make it again. 

I'll make a patch for this bug. Sorry, I overlooked the importance of this. I'm still somewhat puzzled how gd ever built on Fedora if it needs an iconv - unless gd has been recently updated to need iconv too.

There is, as yet an untested file on 't2'

/rootpool2/local/kirkby/sage-4.3.4.alpha0.Solaris-untested.tar

which has

 * sage-4.3.4.alpha0 source 
 * All the patches list at  http://trac.sagemath.org/sage_trac/ticket/8409 applied 
 * This item addressed.

That may or may not build on 't2', but if it does, it should have all known bug fixes that allow all doctests (including the long ones) to pass.

Dave


---

Comment by drkirkby created at 2010-03-04 06:08:57

I realise I can't make a patch for this, as this is not under revision control. But I can give it a positive review. Minh will have to integrate this manually.


---

Comment by drkirkby created at 2010-03-04 06:08:57

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 08:29:23

Resolution: fixed
