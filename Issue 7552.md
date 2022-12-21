# Issue 7552: Update the Twisted package to 9.0

Issue created by migration from Trac.

Original creator: timdumol

Original creation time: 2009-11-29 08:12:32

Assignee: tbd

CC:  mhansen jsp

[Twisted http://twistedmatrix.com] has just recently released a new version, 9.0. This update includes several major changes, the most significant to Sage development being support for WSGI in the Twisted.web framework (rather than the Twisted.web2 framework).


---

Comment by timdumol created at 2009-11-29 08:13:56

Markup change.


---

Comment by timdumol created at 2009-11-29 08:16:15

New package up at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I've tried it on a few worksheets, and things seem to be working well. The notebook tests pass as well.


---

Comment by timdumol created at 2009-11-29 08:16:15

Changing status from new to needs_review.


---

Comment by timdumol created at 2009-11-29 08:16:50

Added package link to description.


---

Comment by timdumol created at 2009-11-29 08:21:06

Added release notes.


---

Comment by was created at 2009-12-21 22:16:29

Changing status from needs_review to needs_work.


---

Comment by was created at 2009-12-21 22:16:29

1. Typing "hg status" gives:

```
wstein`@`sage:~/build/referee/sage-4.3.rc0/twisted-9.0.p0$ hg status
! patches/keys.py
! patches/sob.py
```

This is because you just deleted those files instead of doing "hg rm".  To fix, put them back, then do "hg rm". 

2. You forgot to remove patches/filepath.py, but aren't using it anymore:

```
-cp patches/filepath.py src/twisted/python/
```



---

Comment by timdumol created at 2009-12-22 04:49:27

New version with the fixes at http://sage.math.washington.edu/home/timdumol/twisted-9.0.p0.spkg. I neglected changing the version number.


---

Comment by timdumol created at 2009-12-22 04:49:27

Changing status from needs_work to needs_review.


---

Comment by mpatel created at 2010-01-15 20:49:41

Should we add

```sh
rm -rf "$SAGE_LOCAL"/lib/python/site-packages/twisted
```

to

```sh
# Deleting the old version is *very* important with this package.
rm -rf "$SAGE_LOCAL"/lib/python/site-packages/Twisted*
```

in `spkg-install`?


---

Comment by mpatel created at 2010-01-15 20:54:37

Also, `hg ci`.


---

Comment by mpatel created at 2010-01-15 20:56:38

Replying to [comment:8 mpatel]:
> Also, `hg ci`.
Oops.  I mean that `hg stat` gives

```
! patches/filepath.py
! patches/filepath.py.patch
! patches/keys.py
! patches/keys.py.patch
! patches/sob.py
! patches/sob.py.patch
```



---

Comment by mpatel created at 2010-01-15 21:38:47

I've put these changes and added a description to `SPKG.txt` in

 * http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p1.spkg

I didn't upgrade `zope.interface` to 3.5.3, since `sagenb-*.spkg` includes it.

The Se and doc tests pass for me.  Positive review, but someone should review my changes.


---

Comment by drkirkby created at 2010-02-22 00:31:23

I've not checked it for functionality, but this does at least build on Solaris. 

Dave


---

Comment by mpatel created at 2010-02-22 21:08:56

Requesting an assist, whenever it's convenient.


---

Comment by drkirkby created at 2010-02-24 21:30:30

Also see #8352, which makes a very small change to twisted's spkg-install file, so the previous version of twisted builds on any platform as 64-bit, not just OS X. 

Basically changing 


```
if [ `uname` = "Darwin" -a "$SAGE64" = "yes" ]; then
   echo "64 bit MacIntel"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi

```


to


```
if ["x$SAGE64" = xyes ]; then
   echo "64 bit build"
   CFLAGS="-O2 -g -m64 "; export CFLAGS
   LDFLAGS="-m64 "; export LDFLAGS
fi
```


I'm happy to give the other ticket positive review, but are not going to just now, until I find the best way of handling this. 


Dave


---

Comment by drkirkby created at 2010-02-25 03:52:30

I got no feedback from sage-devel on the best way to handle this, so I've give #8352 positive review. 

I'm not marking it as 'needs work', as that might not be the right thing to do, it might be best if you incorporate the changes from that ticket too.


---

Comment by mpatel created at 2010-02-25 08:00:05

I've added #8352's patch to

  * http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg

Let me know if there are any problems.


---

Comment by drkirkby created at 2010-02-25 13:15:06

I think the first release of this in SPKG.txt should have been simply twisted-9.0 and not twisted-9.0.p0. The p's are only added after patches are applied at a later date. But it is pretty clear from the message that this was the first time version 9.0 was used, so I'm going to overlook that. 

I've added Jaap Spies as an author, as his changes are incorporated too. 

*Note to the release manager. When this ticket is merged, #8352 can be closed.*


---

Comment by drkirkby created at 2010-02-25 13:15:06

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-02 22:45:29

Resolution: fixed


---

Comment by mvngu created at 2010-03-02 22:45:29

Merged [twisted-9.0.p2.spkg](http://sage.math.washington.edu/home/mpatel/trac/7552/twisted-9.0.p2.spkg) in the standard spkg repository.
