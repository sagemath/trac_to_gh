# Issue 3829: wester.py disagrees with Wester!!!

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2008-08-13 00:51:01

Assignee: gfurnish


```
sage: f = log(tan(x/2 + pi/4)) - arcsin(tan(x))
sage: bool(f == 0)
False
```


This just plain disagrees with Wester's benchmarks. The function is identically zero. I'm going to go through `wester.py` and check to see if there are any more...


---

Comment by was created at 2008-08-13 03:56:28

But, we *still* have bool(...) False, so all the above comments apply.

```
sage: # (YES) Ln(Tan(x/2+Pi/4))-ArcSinh(Tan(x))=0
sage: # Yes, in that the thing is clearly not equal to 0!
sage: f = log(tan(x/2 + pi/4)) - arcsinh(tan(x))
sage: bool(f == 0)
False
```


And there should be a patch attached to this ticket that fixes the doctest to have an h, and also 
does not put (YES) in the comment.     

The reason the above is unfortunately not a Sage bug is that in Maxima bool(...) only returns True when its algorithm can definitely prove Truth, and not otherwise.  And that's documented.


---

Attachment


---

Comment by burcin created at 2009-02-08 15:02:53

attachment:trac_3829-wester.patch fixes the typo.

I am not sure how to handle the new results of evaluating the function f. I pasted the new values obtained on my laptop. If they vary on different platforms, we could replace that line with a test that they are < 1e-10.


---

Comment by rlm created at 2009-02-09 16:06:19

Having `(NO)` in the comment is worse, because the identity is true! What should be there is a short explanation of why `bool(f == 0)` returns False, even though we know it is true.


---

Attachment


---

Comment by burcin created at 2009-02-09 16:56:11

I thought the (NO) in the comments indicates that Sage does not give the answer Wester says it should.

I added a comment explaning the Sage/Maxima policy on equality of symbolic expressions.


---

Comment by fredrik.johansson created at 2009-02-10 15:36:33

Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.

Or is some nonstandard branch cut convention implied here?


---

Comment by rlm created at 2009-02-10 16:12:03

Replying to [comment:8 fredrik.johansson]:
> Why should this be considered true? The equality clearly doesn't hold for all x. Try for example evaluating numerically with x = 3.
> 
> Or is some nonstandard branch cut convention implied here?

Fredrik,

I spent quite some time convincing myself that that identity is true. The proof is attached as PDF. You must be able to take the logarithm of `tan(x/2 + pi/4)` in order for the identity to make sense, but for any branch you take where it makes sense it is true. The problem with evaluating numerically at `x = 3` is that symbolic log doesn't like negative numbers, and `tan(3/2 + pi/4) = -1.15265520898227` so it returns a `NaN`.


---

Comment by mabshoff created at 2009-04-13 02:30:12

Ooops, unfortunately this patch has bitrotted: 

```
sage-3.4.1.rc3/devel/sage$ patch -p1 --dry-run < trac_3829-wester.take2.patch 
patching file sage/calculus/wester.py
Hunk #1 FAILED at 253.
1 out of 1 hunk FAILED -- saving rejects to file sage/calculus/wester.py.rej
```

I was paranoid about merging this since it potentially introduces numerical noise and I thought that 3.4.1 was about done for the last couple weeks, so sorry about that.

Cheers,

Michael


---

Comment by AlexGhitza created at 2009-05-31 13:44:34

Apply only `trac_3829-rebased.patch`, which is rebased against 4.0.


---

Attachment

rebased against 4.0


---

Comment by ncalexan created at 2009-06-13 20:33:12

Resolution: fixed
