# Issue 4702: improve magma interface coverage

Issue created by migration from Trac.

Original creator: ncalexan

Original creation time: 2008-12-05 00:39:40

Assignee: was

CC:  was

Keywords: magma interface

A drop in the bucket, but a useful drop.  Vectors and modules, inexact fields, conversions from sage.


---

Attachment


---

Attachment


---

Comment by was created at 2008-12-05 02:13:54

REFEREE REPORT:

All the code looks good.  I doctested the whole tree and there are several doctests failures in free_module.py, but no other doctest failures.  

Nick, could you "explain" this behavior

```
sage: a = RR(pi)
sage: a
3.14159265358979
sage: magma(a)
3.14159265358979
sage: a = RR(pi)
sage: b = magma(a)
sage: b
3.14159265358979
sage: b.Parent()
Real field of precision 15
sage: b._sage_()
3.1415926535898
sage: b._sage_().parent()
Real Field with 49 bits of precision
```

I.e., why precision is lost in going back and forth.  Technically, it's not a priori necessary to loose bits, is it? 

Another remark -- the MagmaElement objects all have a sage method, so you can do

```
sage: b.sage()
```

instead of `b._sage_()` in doctests, which likely sets a better example.

This is a superb patch.  I read carefully through the rest and I'm happy with
everything.  I just want a short discussion about precision issues (going back and forth) and strategies, and fixing of the free_module.py doctests.

By the way, Sage numbers I think don't print all their decimal digits by default.  This a feature that Carl Witty added about a year ago, and may be responsible for the precision loss going back and forth.

William


---

Attachment

i made this since for doctesting purposes I wanted to (1) leave nick's code in place and (2) have a clean doctesting slate.  It's his patch rebased to apply after my #4701 and with all his doctests "fixed" to give the output they give.  Obviously after reading my referee report it's possible nick will change his mind about his implementation, and not want that output.


---

Attachment

I wasn't testing free_module.py correctly, so that's fixed.

I have made sure we lose no precision in the rings.  I talked to Carl Witty about truncating; we shouldn't do it, but Magma seems to do it anyway:


```
sage: a = 61/3.0; a
20.3333333333333
sage: a.str(truncate=False)
'20.333333333333332'
sage: magma(a).sage()
20.3333333333333
sage: magma(a).sage().str(truncate=False)
'20.333333333333300'
sage: magma('RealField(53 : Bits := true)!20.333333333333332')
20.3333333333333
sage: magma('RealField(53 : Bits := true)!20.333333333333332').sage().str(truncate=False)
'20.333333333333300'
sage: magma('RealField(53 : Bits := true)!20.333333333333332').Sage()
RealField(53)(20.3333333333333)
```


It's coming back from Magma truncated, and I have no idea how to make Magma print it without truncation.  I say we leave it as is -- losing a bit or three at the end is not a huge concern for me.


---

Attachment

Both 4702-ncalexan-magma-updates-2.patch and 4702-extcode-magma.2.patch apply fresh.


---

Attachment

Positive review!

Mabshoff, apply exactly these two patches:

```
4702-ncalexan-magma-updates-2.patch
4702-extcode-ncalexan-magma.patch
```



---

Comment by mabshoff created at 2008-12-05 09:37:21

Resolution: fixed


---

Comment by mabshoff created at 2008-12-05 09:37:21

Merged 4702-ncalexan-magma-updates-2.patch and 4702-extcode-magma.2.patch in Sage 3.2.2.alpha0.

Nick: your patches were both diffs and I caught this only once I have merged 4702-ncalexan-magma-updates-2.patch. Please make sure to post hg patches.

Cheers,

Michael


---

Comment by mabshoff created at 2008-12-07 08:56:20

I just noticed that I merged the wrong patch, so I am reverting 4702-extcode-magma.2.patch and merging 4702-extcode-ncalexan-magma.patch instead.
