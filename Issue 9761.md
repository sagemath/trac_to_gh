# Issue 9761: Update zn_poly's SPKG.txt to indicate it depends on Python.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-18 11:49:26

Assignee: mvngu

As noted at #9761, although the spkg-install script for zn_poly is a bash script, it actually calls a Python script `zn_poly-*/src/makemakefile.py`. Therefore the SPKG.txt file should indicate this dependency, as it is far from obvious. 

Clearly this is a minor issue, but one worth fixing. 


---

Comment by leif created at 2010-08-18 12:52:15

Replying to [ticket:9762 drkirkby]:
> Clearly this is a minor issue, but one worth fixing. 

It's "only" documentation... ;-)


---

Comment by drkirkby created at 2010-08-18 13:35:05

Replying to [comment:1 leif]:
> Replying to [ticket:9762 drkirkby]:
> > Clearly this is a minor issue, but one worth fixing. 
> 
> It's "only" documentation... ;-)
> 
True, but #9603 is more important, as it actually stops something building!

Dave


---

Comment by mmezzarobba created at 2015-04-14 11:30:27

The `SPKG.txt` now says:

```
## Dependencies

 * GMP/MPIR
 * (some) Python (to create the Makefile)
 * GNU patch
 * NTL apparently only if we configured zn_poly differently (same for FLINT)
```



---

Comment by mmezzarobba created at 2015-04-14 11:30:27

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-14 12:14:07

Changing status from needs_review to positive_review.


---

Comment by leif created at 2015-04-14 13:41:18

Oh yes, fixed years ago...


---

Comment by vbraun created at 2015-04-14 23:03:28

Resolution: fixed
