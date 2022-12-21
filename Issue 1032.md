# Issue 1032: [with patch] Latex'ing variable names is more robust and consistent.

Issue created by migration from Trac.

Original creator: jbmohler

Original creation time: 2007-10-29 20:47:42

Assignee: was

I've refined the latex_variable_name function and called it a few more places to make latex'ing much much better.

Patch attached.


---

Attachment

the patch


---

Comment by was created at 2007-10-29 21:17:31

Please not my worry on sage-devel about maybe this causing problems with singular...


---

Comment by mabshoff created at 2007-10-29 22:07:53

See http://groups.google.com/group/sage-devel/t/89472eb36248053a to be exact.

Cheers,

Michael


---

Comment by jbmohler created at 2007-10-31 15:23:42

Towards the bottom of the thread linked by mabshoff, I believe we have William's approval for this patch.

I've personally tested that singular, gp, maxima, and gap all appear to support '_'s in identifiers in their own interpreted languages.  I wanted to do some more extensive tests, but it wasn't quite as easy as I first thought it might be and now that I've tested each of their interpreted languages, I think such further testing does not hold much value.

Hence, I think this patch is good to be included (of course, I expect you to be suspicious of that statement -- since I'm the author of the patch!)


---

Comment by was created at 2007-11-01 19:49:12

I think this is fine to go in.


---

Comment by mabshoff created at 2007-11-01 23:26:31

Resolution: fixed


---

Comment by mabshoff created at 2007-11-01 23:26:31

applied to 2.8.11.rc1 - I might have misunderstood some of the discussion, sorry.

Cheers,

Michael


---

Comment by was created at 2007-11-02 00:50:31

Resolution changed from fixed to 


---

Comment by was created at 2007-11-02 00:50:31

This breaks a treasured old behavior:


```
17:48 < mabshoff> Stuff like
17:48 < mabshoff> File "polynomial_ring.py", line 383:
17:48 < mabshoff>     sage: latex(S)
17:48 < mabshoff> Expected:
17:48 < mabshoff>     \mathbf{Z}[\alpha_{12}]
17:48 < mabshoff> Got:
17:48 < mabshoff>     \mathbf{Z}[\text{alpha12}]
17:48 < mabshoff> Should I just fix those?
17:48 < wstein> Hey, \mathbf{Z}[\text{alpha12}] is pretty damned LAME imho.
17:48 < mabshoff> Nope, they actually look wrong.
17:48 < wstein> So joel got rid of the nice behavior that used to be there?
17:49 < wstein> That's stupid.
17:49 < wstein> Reject it.
17:49 < mabshoff> back it out?
17:49 < wstein> I'm ok with allowing alpha_12, but I don't agree with *forcing* the use 
                of underscores for subscripts.
17:49 < wstein> The latex form of alpha12 can't have any meaning except $\alpha_{12}$.
17:49 < wstein> Yes, I would back it out.
17:49 < wstein> That's annoying.

```



---

Comment by was created at 2007-11-02 00:50:31

Changing status from closed to reopened.


---

Comment by jbmohler created at 2007-11-02 11:47:31

I disagree with the doc-tests above

Exhibit A (vanilla 2.8.10):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.8.10, Release Date: 2007-10-28                      |
| Type notebook() for the GUI, and license() for information.        |
sage: P.<alpha12>=ZZ[]
sage: latex(P)
\mathbf{Z}[\text{alpha12}]
```


Exhibit B (my patched version):

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: latex
sage: P.<alpha12>=ZZ[]
sage: latex(P)
\mathbf{Z}[\alpha_{12}]
```



---

Attachment

the second patch (needed since hg already says the first patch is in)


---

Comment by jbmohler created at 2007-11-02 18:40:29

The second patch is just the first patch rehashed because the first patch is already in the tree and hg won't reimport.  There are no other differences.

It unbundles and passes all doc-tests against 2.8.11.rc1


---

Comment by mabshoff created at 2007-11-02 19:37:14

applied to 2.8.11.rc2.


---

Comment by mabshoff created at 2007-11-02 19:37:14

Resolution: fixed
