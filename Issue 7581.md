# Issue 7581: use prCopyR to coerce multivariate polynomials in the simple case

Issue created by migration from https://trac.sagemath.org/ticket/7581

Original creator: malb

Original creation time: 2009-12-02 11:47:01

Assignee: malb

CC:  simonking

Mike Hansen wrote on [sage-devel]:

The following messages are probably relevant for the fast conversion
between singular polynomial rings:

On Sat, Oct 18, 2008 at 2:55 AM, Michael Brickenstein
<brickenstein`@`mfo.de> wrote:
> In Singular the same thing is essentially done from the > interpreter
> level by the more general command fetch.
> I had a look, what it does internally and came to the conclusion,
> that it just calls
> poly prCopyR(poly p, ring src_r, ring dest_r)
> in your simple case (same coefficient domains).
> So first, you should setup a new ring and
> then map the polynomial via
> prCopyR
>
> Michael

On Mon, Oct 20, 2008 at 8:43 PM,  <hannes`@`mathematik.uni-kl.de> wrote:
> if the monomial ordering is really the same,
> you may also use
> poly prCopyR_NoSort(poly p, ring src_r, ring dest_r)
> which avoids the sorting the polynomial after mapping each monomial.
> There are also corresponding routines for ideals
> (ideal idrCopyR(ideal id, ring src_r, ring dest_r),
> ideal idrCopyR_NoSort(ideal id, ring src_r, ring dest_r)
> )
>


---

Attachment


---

Comment by malb created at 2009-12-02 11:56:13

The attached patch makes things slightly faster.

*Before*

```
sage: R1 = PolynomialRing(QQ,'x',10001,order='lex')
sage: R2 = PolynomialRing(QQ,'x',10002,order='deglex')
sage: x10000 = R1('x10000')
sage: %time a = R2(x10000)
CPU times: user 5.77 s, sys: 0.18 s, total: 5.95 s
Wall time: 7.54 s
sage: %time a = R2(x10000)
CPU times: user 5.43 s, sys: 0.00 s, total: 5.43 s
Wall time: 5.59 s

sage: x10001 = R2('x10001')
sage: %time x10000 + x10001
CPU times: user 16.87 s, sys: 0.00 s, total: 16.87 s
Wall time: 17.05 s
x10000 + x10001
sage: %time x10000 + x10001
CPU times: user 5.43 s, sys: 0.00 s, total: 5.43 s
Wall time: 5.49 s
x10000 + x10001
```


*After*

```
sage: R1 = PolynomialRing(QQ,'x',10001,order='lex')
sage: R2 = PolynomialRing(QQ,'x',10002,order='deglex')
sage: x10000 = R1('x10000')
sage: %time a = R2(x10000)
CPU times: user 1.18 s, sys: 0.16 s, total: 1.34 s
Wall time: 1.36 s
sage: %time a = R2(x10000)
CPU times: user 0.87 s, sys: 0.00 s, total: 0.87 s
Wall time: 0.92 s

sage: x10001 = R2('x10001')
sage: %time x10000 + x10001
CPU times: user 7.67 s, sys: 0.00 s, total: 7.67 s
Wall time: 7.77 s
x10000 + x10001
sage: %time x10000 + x10001
CPU times: user 0.86 s, sys: 0.00 s, total: 0.87 s
Wall time: 0.91 s
x10000 + x10001
```


I haven't run doctests yet.


---

Comment by malb created at 2009-12-02 11:56:13

Changing status from new to needs_work.


---

Comment by malb created at 2009-12-02 11:58:52

The patch depends on #7577 (I'll provide an alternative patch soon)


---

Comment by SimonKing created at 2009-12-02 12:00:10

Replying to [comment:1 malb]:
> The attached patch makes things slightly faster.

"Slightly"?? It's amazing! Hopefully I'll find the time for a proper review soon.


---

Comment by malb created at 2009-12-02 12:08:36

Replying to [comment:3 SimonKing]:
> "Slightly"?? It's amazing! Hopefully I'll find the time for a proper review soon.

:) It still sucks that adding two variables takes close to second. But Singular uses a dense representation for monomials and thus there isn't that much we can do. For your review, try to find corner cases where things go wrong (I'll do the same of course).


---

Comment by malb created at 2009-12-02 12:19:33

Doctests in 4.3.alpha0 pass on sage.math


---

Comment by SimonKing created at 2009-12-03 09:40:27

Sorry, but neither of the patches applies to a fresh build of sage-4.3.alpha0.

But it could actually be that my sage-4.3.alpha0 has a problem. After building it, I did
  ./sage -clone infinitepoly
waited 8 hours, but it wasn't finished. It seems that it hanged while trying to do the documentation. Eventually, I pressed Ctrl-C (was needed several times). 

The clone seemed to work, though. But:

```
sage: hg_sage.import_patch('patches/singular_prcopyr_no7577.patch')
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg status
/home/SimonKing/sandbox/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg status
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg import   "/home/SimonKing/sandbox/patches/singular_prcopyr_no7577.patch"
applying /home/SimonKing/sandbox/patches/singular_prcopyr_no7577.patch
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #1 FAILED at 959
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
abort: patch failed to apply
```


OK, back, ./sage -br main.


```
sage: hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7581/singular_prcopyr.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7581/singular_prcopyr.patch
Loading: [.]
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg status
/home/SimonKing/sandbox/sage-4.3.alpha0/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg status
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg import   "/home/SimonKing/.sage/temp/sage.math.washington.edu/13821/tmp_1.patch"
abort: outstanding uncommitted changes
```


OK, what are the changes?

```
sage: hg_sage.diff()
cd "/home/SimonKing/sandbox/sage-4.3.alpha0/devel/sage" && hg diff  | less
(END)
```


No changes, then, but there are uncommitted changes. Frustrating.

Conclusion: I can not give a positive review, of course, but the problem seems to be deeper, so, it isn't "needs work" either. I'll mark it "needs review".


---

Comment by SimonKing created at 2009-12-03 09:40:27

Changing status from needs_work to needs_review.


---

Comment by malb created at 2009-12-03 10:09:09

The repository in 4.3.alpha0 is borked, try `hg status`, it will point out two files which are missing. Then create those files (i.e. `touch /path/to/filename`) afterwards, importing should work.


---

Comment by SimonKing created at 2009-12-03 13:59:44

Hi Martin!

Replying to [comment:7 malb]:
> The repository in 4.3.alpha0 is borked, try `hg status`, it will point out two files which are missing. Then create those files (i.e. `touch /path/to/filename`) afterwards, importing should work.

I followed the advices that [Minh](http://groups.google.com/group/sage-devel/browse_thread/thread/11f432ca0302189e) gave. However, there were problems applying the "no7577" patch. 

It simply does not work.


```
sage: hg_sage.log()
changeset:   13375:44f70d431d43
tag:         tip
user:        Mike Hansen <mhansen@gmail.com>
date:        Sat Nov 21 03:45:06 2009 -0800
summary:     4.3.alpha0
...
```


So, it is a fresh 4.3.alpha0


```
sage: hg_sage.status()
Getting status of modified or unknown files:
cd "/home/SimonKing/sandbox/sage-4.3.alpha0FOOBAR/devel/sage" && hg status

---

Branch: exp
```


So, there are no uncommitted changes.


```
sage: hg_sage.import_patch('http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7581/singular_prcopyr_no7577.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7581/singular_prcopyr_no7577.patch
Loading: [.]
cd "/home/SimonKing/sandbox/sage-4.3.alpha0FOOBAR/devel/sage" && hg status
/home/SimonKing/sandbox/sage-4.3.alpha0FOOBAR/local/lib/python2.6/site-packages/sage/misc/hg.py:240: DeprecationWarning: os.popen3 is deprecated.  Use the subprocess module.
  x = os.popen3(s)
cd "/home/SimonKing/sandbox/sage-4.3.alpha0FOOBAR/devel/sage" && hg status
cd "/home/SimonKing/sandbox/sage-4.3.alpha0FOOBAR/devel/sage" && hg import   "/home/SimonKing/.sage/temp/sage.math.washington.edu/22357/tmp_1.patch"
applying /home/SimonKing/.sage/temp/sage.math.washington.edu/22357/tmp_1.patch
patching file sage/libs/singular/singular-cdefs.pxi
Hunk #1 FAILED at 959
1 out of 1 hunks FAILED -- saving rejects to file sage/libs/singular/singular-cdefs.pxi.rej
abort: patch failed to apply
```


:-/

I don't see what I did wrong here. So, I guess it is "needs work".

Best regards,

Simon


---

Comment by SimonKing created at 2009-12-03 13:59:44

Changing status from needs_review to needs_work.


---

Comment by SimonKing created at 2009-12-03 14:05:31

I tried to modify the files manually, and I think I found the problem.

Apparently your version of sage/libs/singular/singular-cdefs.pxi that you based your patch on is _not_ the version in sage-4.3.alpha0.

Namely, sage/libs/singular/singular-cdefs.pxi only has 930 lines, while your patches start at line 963 and 973, respectively.

So, can you please provide a new patch?

Cheers,

Simon


---

Attachment

next attempt


---

Comment by malb created at 2009-12-03 14:41:31

I've updated the patch. Hopefully, this one works.


---

Comment by SimonKing created at 2009-12-03 15:34:29

Replying to [comment:10 malb]:
> I've updated the patch. Hopefully, this one works.

It applies!

And I can confirm the improvement. I am now doing `sage -testall`.


---

Comment by SimonKing created at 2009-12-03 16:34:25

Changing status from needs_work to needs_review.


---

Comment by SimonKing created at 2009-12-03 16:34:25

`sage -testall` passes. 

Your patch provides a strong improvement. However, genuine Singular is match faster:

```
> system("--ticks-per-sec",1000);
> ring r1 = 0, (x(1..10000)),dp;
> poly p = x(10000);
> ring r2 = 0, (x(1..10001)), dp;
> int t = timer;
> poly q1 = imap(r1,p);
> timer-t;
410
> poly q2 = fetch(r1,p);
> timer-t;
430
```


So, 0.41s for imap and only 0.02s for fetch, in a situation where (even with your patch) Sage needs 5.43s! And I think imap does exactly what one needs in element conversion -- I mean, take a variable from one ring and return the variable with the same name in another ring.

Is it possible to wrap imap in libsingular? This would probably yield a drastic improvement (factor 10?).

But I guess this should be a different ticket, and since your patch does provide a good improvement, I give it a positive review.

There is no button for "positive review"? Well, I guess I first have to change it into "needs review", and then push the button...

Cheers,
Simon


---

Comment by SimonKing created at 2009-12-03 16:34:39

Changing status from needs_review to positive_review.


---

Comment by SimonKing created at 2009-12-03 16:45:29

Replying to [comment:12 SimonKing]:
...
> So, 0.41s for imap and only 0.02s for fetch, in a situation where (even with your patch) Sage needs 5.43s! 

Oops, I was copying the wrong number. With your patch, it is 1.18 s. However, it'd be great if this could be improved to, say, 0.5s.


---

Comment by SimonKing created at 2009-12-03 16:54:01

Replying to [comment:15 SimonKing]:
> Replying to [comment:12 SimonKing]:
> ...
> > So, 0.41s for imap and only 0.02s for fetch, in a situation where (even with your patch) Sage needs 5.43s! 
> 
> Oops, I was copying the wrong number. With your patch, it is 1.18 s. However, it'd be great if this could be improved to, say, 0.5s.
> 

Double oops. I have my children in the office and am a bit distracted.

OK.

We have 

```
> system("--ticks-per-sec",1000);
> ring r1 = 0, (x(1..10000)),dp;
> poly p = x(10000);
> ring r2 = 0, (x(1..10001)), dp;
> int t = timer;
> imap(r1,p)+x(10001);
x(10000)+x(10001)
> timer-t;
410
```


while we have (with your patch)

```
sage: R1 = PolynomialRing(QQ,'x',10001,order='deglex')
sage: R2 = PolynomialRing(QQ,'x',10002,order='deglex')
sage: x10000 = R1('x10000')
sage: x10001 = R2('x10001')
sage: %time R2(x10000) + x10001
CPU times: user 0.74 s, sys: 0.00 s, total: 0.74 s
Wall time: 0.73 s
x10000 + x10001
```


I think this is equivalent to what I did in Singular. In other words, your patch is not far from native Singular.

This confirms my positive review.

Cheers,

Simon


---

Comment by mhansen created at 2009-12-04 05:48:54

Resolution: fixed
