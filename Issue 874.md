# Issue 874: Implement Jordan and Rational Canonical Form

Issue created by migration from https://trac.sagemath.org/ticket/874

Original creator: robertwb

Original creation time: 2007-10-13 05:57:48

Assignee: was




---

Comment by craigcitro created at 2008-01-29 12:29:27

Changing assignee from was to craigcitro.


---

Comment by craigcitro created at 2008-01-29 12:29:27

Changing status from new to assigned.


---

Comment by craigcitro created at 2008-01-29 12:29:27

I have naive code (= compute Smith Normal Form) written to do both of these now. I need to get it cleaned up and included (which means figuring out where it goes in sage/matrix/), but I wanted to put a note up to avoid duplication of work. 

That said, if someone has an interesting/clever algorithm, it's probably better than what I've written, so that should be submitted.

William points out that for JCF over exact fields, using A.decomposition() will probably be much better.


---

Comment by was created at 2008-01-29 12:38:58

I mean RCF not JCF over exact fields...


---

Comment by jason created at 2008-01-29 16:10:42

Compute Jordan Canonical form extremely naively.


---

Attachment

That's funny, I just wrote some code last night to compute jordan canonical form using the powers of A-xI, the by-hand method you learn in linear algebra.  I've attached it above.  Your code probably blows this out of the water, but it would be interesting to see the speed comparison anyway.  The patch is a bit faster after you apply the patch in #1973.


---

Comment by jason created at 2008-01-29 16:26:04

The article:

http://www.sciencedirect.com/science?_ob=ArticleURL&_udi=B6WM7-45M2XHC-M&_user=716796&_rdoc=1&_fmt=&_orig=search&_sort=d&view=c&_acct=C000040078&_version=1&_urlVersion=0&_userid=716796&md5=10649e53c80185bed8cf7ff212858f11

might be useful to implement a fast algorithm (and may be what William is talking about above mentioning decompositions).


---

Comment by craigcitro created at 2008-01-30 09:09:37

It's interesting that Jason had so much faith in my code -- apparently William's skepticism was warranted. :) It turns out that it's terrible right now -- on small examples, it's roughly 5X slower than Jason's, and it's still running on a large example (where your code took 7.5 sec). 

The problem is easy to understand when you look at the code: to compute the Smith Normal Form of T-x*I, I work over a polynomial ring, and there's neither (1) specialized polynomial arithmetic (i.e. as in the ZZ[X] case) nor (2) a specific type for matrices of polynomials (at least that I know about!). As a result, lots of things that should be C calls are instead Python calls. 

I glanced at the Allan Steel paper above -- we should probably go ahead and implement something like this in the long-term. In the short term, though, Jason's code is definitely superior. I think we should add one thing, though -- passing in a base_ring argument, and just changing 

  evals = self.charpoly().roots()

to 

  evals = self.charpoly().roots(base_ring)

we'd have something that would work over an arbitrary base ring (indeed, the error checking is already there!). I'm making one implicit assumption, namely that the coercion model could handle coercing matrices around for us, but that doesn't seem unlikely at all -- if nothing else, we'd find coercion bugs to fix.


---

Comment by mabshoff created at 2008-02-15 22:22:55

Jason's code might be naive, but at least it seems to work. Implementing an efficient/fast version of the algorithm should be another ticket once we merged this version.

Cheers,

Michael


---

Attachment

Apply (and review) instead of original jordan-form.patch.


---

Comment by jason created at 2008-02-16 05:50:47

The jordan-form.2.patch replaces jordan-form.patch and:

1. rebases against 2.10.1

2. implements the base_ring argument mentioned above

3. uses the Partition object instead of the deprecated partitions_associated function.


---

Comment by craigcitro created at 2008-02-16 06:00:18

I agree with Michael's sentiment above that this should get merged -- maybe merge it, and: 

- make another ticket saying we still need a rational canonical form algorithm
- note in the docstring for Jordan canonical form that the algorithm is the naive one

Does that seem reasonable?


---

Comment by was created at 2008-02-16 06:09:00

Yes, I agree with craig.  It's very good to have a step 1 that implements something naive, then a step 2 that greatly optimizes it in special cases.  It is also a very good idea to be bluntly clear that an implementation is naive if it is.


---

Attachment

Adds a note saying that the computation is naive.


---

Comment by jason created at 2008-02-22 20:38:22

The jordan-form.3.patch adds a note to the docs saying that the computation is naive.


---

Comment by jason created at 2008-02-22 20:39:07

jordan-form.3.patch should be applied instead of any of the previous ones.


---

Comment by craigcitro created at 2008-02-23 01:05:18

So I agree with Jason's earlier comments on IRC that this ticket should be put to bed already. I have only two minor nitpicks:

 * it's going to need to be re-based against 2.10.2 when it's out
 * I think `jordan_form()` should take an optional argument `subdivide=True`, 
 which it passes off to `block_diagonal_matrix`. (This is just so that the user can 
 control whether or not the matrix gets printed with blocks shown, which I know 
 most people probably like, but I personally find annoying.)

Jason, if you want to do that real quick when 2.10.2 is out, I'll give it a positive review.

-cc


---

Comment by mhansen created at 2008-02-27 18:53:18

I get the following on 2.10.3.alpha0

```
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg status
cd "/home/mhansen/sage-2.10.3.alpha0/devel/sage" && hg import   "/home/mhansen/.sage/temp/sage/15288/tmp_2.patch"
applying /home/mhansen/.sage/temp/sage/15288/tmp_2.patch
patching file sage/matrix/matrix2.pyx
Hunk #1 FAILED at 3035
1 out of 1 hunk FAILED -- saving rejects to file sage/matrix/matrix2.pyx.rej
abort: patch failed to apply
```



---

Attachment

New patch posted which applies cleanly against 2.10.3.alpha0 + #1186. Just apply 874.patch.


Positive review from me.


---

Comment by mabshoff created at 2008-02-28 00:41:03

Resolution: fixed


---

Comment by mabshoff created at 2008-02-28 00:41:03

Merged 874.patch in Sage 2.10.3.rc0


---

Comment by jvoight created at 2008-03-12 19:28:52

So did the algorithm for rational canonical form not get implemented?  (This would follow from a Smith normal form for a matrix over F[x], if it is computed...)

JV


---

Comment by craigcitro created at 2008-03-12 19:59:03

I implemented rational canonical form in precisely that way. It's horrendously slow. William has already written code that can be used to make a usable rational canonical form algorithm (which is mentioned above) -- someone should open another ticket about this, probably.
