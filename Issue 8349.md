# Issue 8349: bug in isogenies

Issue created by migration from Trac.

Original creator: wuthrich

Original creation time: 2010-02-24 17:38:51

Assignee: cremona

Keywords: isogeny, elliptic curves

Something is wrong with the post_isomorphism of isogenies of elliptic curves :


```
sage: E = EllipticCurve(GF(17), [0,-1,0,-3,-1])
sage: P = E([16,0])
sage: phi = E.isogeny(P,codomain=E)
sage: phi(P)
(9 : 11 : 1)
sage: phi(P) in E
False
```




---

Attachment


---

Comment by craigcitro created at 2010-02-24 18:36:22

Changing status from new to needs_review.


---

Comment by craigcitro created at 2010-02-24 18:36:22

Attached a quick fix -- I'm happy to let it be ignored if there's something classier to be done.


---

Comment by wuthrich created at 2010-02-24 18:56:29

Wow. That was *very* quick. But maybe a bit too quick.


```
sage: E = EllipticCurve('11a1')
sage: phi = E.isogeny(None,codomain=EllipticCurve('11a2'),degree=5)
sage: [phi(P) for P in E.torsion_points()]
[(0 : 1 : 0), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1), (1/3 : 1/2 : 1)]
```


again the images are not even on the `codomain()`. I.e. there is probably a second spot that needs a small change.


---

Comment by wuthrich created at 2010-02-24 18:56:29

Changing status from needs_review to needs_work.


---

Attachment


---

Comment by wuthrich created at 2010-02-24 19:04:07

I think that should do it also for the kohel part.


---

Comment by wuthrich created at 2010-02-24 19:04:07

Changing status from needs_work to needs_review.


---

Comment by cremona created at 2010-02-24 20:16:40

What about lines 981, 1002, in the patched file?  They both say 
 {{{
           return self.__E2(0)
}}}
so shouldn't they also be changed to return 0 on the correct codomain?


---

Comment by wuthrich created at 2010-02-24 22:35:46

No, these two lines must stay as they are. They do the right thing.


---

Comment by cremona created at 2010-02-24 22:43:46

Replying to [comment:5 wuthrich]:
> No, these two lines must stay as they are. They do the right thing.

OK, I trust you -- I tried to find an example where they did not do the right thing, and could not.

I'm happy -- patch (just the 2nd one) applies to 4.3.3 and test pass.


---

Comment by cremona created at 2010-02-24 22:43:46

Changing status from needs_review to positive_review.


---

Comment by mvngu created at 2010-03-03 14:06:17

Resolution: fixed


---

Comment by mvngu created at 2010-03-03 14:06:17

Merged [trac_8349.2.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8349/trac_8349.2.patch).
