# Issue 5569: [with patch, needs review] weil restriction of scalars

Issue created by migration from https://trac.sagemath.org/ticket/5569

Original creator: malb

Original creation time: 2009-03-19 22:28:05

Assignee: malb

CC:  cremona

While cleaning up `mq.MPolynomialSystem` I moved its misnamed `change_ring()` function to a more proper place, i.e. `weil_restriction()` on ideals. Note, that these are defined on varieties but we don't have any variety objects and the function indeed works with ideal generators.


---

Comment by was created at 2009-03-19 22:46:02


```
15:43 < wstein> The patch looks good, except why not define the Weil restriction of scalars
15:43 < wstein> functor.
15:43 < wstein> You don't define it, but giving a complete valid mathematical definition only
15:43 < wstein> takes about 2-3 sentences.
15:43 < wstein> I can't see why not to do that.
15:43 < malb> okay
15:44 < wstein> Serge Lang first taught me about that construction using equations
15:44 < wstein> when I was having lunch with him once in grad school.
15:44 < wstein> Then I personally realized it is a functor and used that to prove that
15:44 < malb> I knew about this for a while but learned the proper name just now
15:44 < wstein> it is unique up to whatever...
15:44 < wstein> It was just an exercise for me, of course, since it is all well known.
15:45 < wstein> Also, could you add an example that involves an elliptic curve (affine patch 
                of one, at least)
15:45 < wstein> over a quadratic field?
15:45 < wstein> That would be cool.
```



---

Attachment


---

Comment by was created at 2009-03-22 00:04:32

I give this a positive review.  Great work on the docstring!  

One comment.  It is sad that we have to write code like this to do a coercion:

```
 l = [helper(str(f))  for f in self.gens()] 
```


As a challenge to Martin -- can you improve Sage so this decimal string conversion (which could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one can use a homomorphism?


---

Comment by malb created at 2009-03-23 12:16:02

Replying to [comment:4 was]:
> As a challenge to Martin -- can you improve Sage so this decimal string conversion (which 
> could be a killer show stopper if the ideal had huge elements) isn't needed, and instead one 
> can use a homomorphism?

This is now #5590


---

Comment by mabshoff created at 2009-03-23 20:47:11

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 20:47:11

Merged in Sage 3.4.1.alpha0.

Cheers,

Michael
