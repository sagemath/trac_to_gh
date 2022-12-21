# Issue 9330: Documentation for sha_tate.py not quite looking right

Issue created by migration from Trac.

Original creator: kcrisman

Original creation time: 2010-06-24 15:55:55

Assignee: cremona

CC:  jhpalmieri

When you look at [this](http://www.sagemath.org/doc/reference/sage/schemes/elliptic_curves/sha_tate.html), there are a number of things wrong or confusing in the documentation.

Most importantly, several instances of Sha should have ticks, probably.  But are they referring to the mathematical object 

```
`Sha`
```

or the computer structure of the class

```
``Sha``
```

?  If I knew what was intended (given that the distinction is quite small), I would do this patch myself.  But it looks like sometimes the group is intended, other times the class object.

In line 198, 

```
 You can increase the `descent_second_limit` (in the above example
```

should have double ticks.

We also get the following warning:

```
sage-4.4.4/local/lib/python2.6/site-packages/sage/schemes/elliptic_curves/sha_tate.py:docstring of sage.schemes.elliptic_curves.sha_tate.Sha.bound_kato:12: (WARNING/2) Definition list ends without a blank line; unexpected unindent.
```

this probably refers to 

```
       THEOREM (Kato): Suppose `L(E,1) \neq 0` and `p \neq 2, 3` is a prime such that
            - `E` does not have additive reduction at `p`,
            - the mod-`p` representation is surjective.
       Then `{ord}_p(\#Sha(E))` divides `{ord}_p(L(E,1)\cdot\#E(\QQ)_{tor}^2/(\Omega_E \cdot \prod c_q))`.
```

but I'm not sure.

In line 756 we have 

```
We get no information the curve has rank 2.::
```



---

Comment by cremona created at 2010-06-24 16:01:07

Is there any reason we cannot use the proper cyrillic font for Sha?

\newcommand{\Sha}{{\mbox{\textcyr{Sh}}}}


---

Comment by kcrisman created at 2010-06-24 16:04:35

Does jsmath support this?  Otherwise one would have to do the right encoding.  Anyway, it looks like my job here is done - interest has been piqued ;)


---

Comment by jhpalmieri created at 2010-07-06 22:43:52

See #9442 for the warning when building the reference manual.


---

Attachment

exported against 4.5.2.alpha1


---

Comment by wuthrich created at 2010-07-28 15:41:13

Changing status from new to needs_review.


---

Comment by wuthrich created at 2010-07-28 15:41:13

I changed Sha to `Sha` thoughout the document as it should be. There should be a better solution for this. Alas the unicode letter Ш does not work in the pdf version (it works fine in the html). The \textcyr does not seem to work with LaTeX either. Probably it needs addtional fonts or so and I would object to include them just because of this one letter.

So I think this is as far as I can do the changes.

I also renamed constistantly the group as Tate-Shafarevich and not Shafarevich-Tate. (There is a debate about this, which I do not want to see repeated here. google tells me that T-S is more frequent.)


---

Comment by kcrisman created at 2010-07-28 15:53:55

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2010-07-28 15:53:55

There are a few other things in the Description which need to be taken care of; in the first case, it's to add double ticks, and in the second it's (probably) to add the word 'when'.   

I removed the issue from #9442 from the Description since that is already merged in rc0 - one will probably have to rebase (very slightly) against 4.5.2.rc0 or 4.5.2, since that has been merged.  Once that's done (and once I build one of those) I'll also check whether it looks right, but from a cursory glance this looks like a great improvement (and in consistency!).  Or jhpalmieri can do it :)


---

Comment by wuthrich created at 2010-07-28 16:15:34

Changing status from needs_work to needs_review.


---

Comment by wuthrich created at 2010-07-28 16:15:34

I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.

It should always be `Sha` never ``Sha``.

I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.


---

Comment by wuthrich created at 2010-07-28 16:16:55

Oops the ` went away. I meant

It should always be ``Sha`` never ```Sha```


---

Comment by kcrisman created at 2010-07-28 17:34:38

Replying to [comment:6 wuthrich]:
> I don't understand this. My file sha_tate.py looks well different from the documentation link that you give. For instance I have changed the ``descent... thingy in trac 9287 merged as 14603 in 4.5.2.alpha1.

Yes, sorry I didn't see that - I've changed the description.  What is up with the "We get no information the " bit?  Maybe this is grammatically correct in the context of Tate-Shaf groups?  

Incidentally, though you changed the references to T-S, the file is S-T :)  Oh well; maybe that's as it should be if there isn't agreement.

> It should always be `Sha` never ``Sha``.
> 
> I believe this ticket solves the remaining problems. Though I have not checked it is needs to be rebased.

Unfortunately I can't check this right now either, but if someone else doesn't, I'll do so soon.


---

Comment by wuthrich created at 2010-07-29 09:56:07

exported against 4.5.2.alpha1, to be apply after trac_9330.patch


---

Attachment

Yop, sorry, I did not see that the 'when' was still missing. Here is an additional patch.

Luckily the filename is not visible to the user, so I don't have to bother changing it. ... and it gives some voice to the other order.

There is no problem with the rebase, because the patches here are exported against 4.5.2.alpha1 and #9442 was merged in 4.5.alpha4 if I am not mistaken. At least the addition lines are clearly in the file before I edited it.


---

Comment by kcrisman created at 2010-07-29 19:24:25

Unfortunately, I can't get this to work right when doing `sage-docbuild reference html` on my computer (probably due to latex not being in my PATH).  Someone else will have to review it, though it seems good!


---

Comment by kcrisman created at 2010-08-11 19:57:08

I figured out how to get my latex in my PATH finally.  There are a few things which *could* be put in ticks or double ticks still, but not ones I feel are necessary at this point, more ambiguous - and none related to Sha.  Positive review


---

Comment by kcrisman created at 2010-08-11 19:57:08

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-09-15 11:38:11

Resolution: fixed


---

Comment by leif created at 2010-09-16 08:45:53

These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (_Shafarevich-Tate_ -> _Tate-Shafarevich_).

I don't know if there's a separate ticket for this.


---

Comment by leif created at 2010-09-16 09:50:10

Replying to [comment:14 leif]:
> These changes also require modifying doctests in `sage/schemes/elliptic_curves/BSD.py` (_Shafarevich-Tate_ -> _Tate-Shafarevich_).
> 
> I don't know if there's a separate ticket for this.

I've opened #9916 for that. Patch needs review.
