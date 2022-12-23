# Issue 4058: [with patch, needs review] move integer ring to the new coercion model

Issue created by migration from https://trac.sagemath.org/ticket/4058

Original creator: robertwb

Original creation time: 2008-09-04 04:27:58

Assignee: robertwb

CC:  alexghitza malb

A couple of bugfixes are included as well. 


---

Attachment


---

Comment by AlexGhitza created at 2008-09-20 04:46:22

I'm getting an error trying to apply this patch to a fresh 3.1.2:


```
patching file sage/interfaces/expect.py
Hunk #1 FAILED at 1385
1 out of 1 hunk FAILED -- saving rejects to file sage/interfaces/expect.py.rej
patch failed, unable to continue (try -v)
patch failed, rejects left in working dir
```



---

Comment by robertwb created at 2008-09-20 06:30:46

I'll rebase this as soon as I get 3.1.2.


---

Attachment


---

Comment by robertwb created at 2008-09-23 19:00:42

Refreshed the patch so it applies cleanly to 3.1.2.


---

Comment by mhansen created at 2008-09-24 02:47:38

Looks good to me.


---

Comment by mabshoff created at 2008-09-24 04:20:59

One thing I notice with this patch is that sr.py now takes around 650 seconds instead of 450 or so:

```
sage -t -long devel/sage/sage/crypto/mq/sr.py
         [655.1 s]
```

I am still merging the patch, but can we get this issue fixed next?

Cheers,

Michael


---

Comment by mabshoff created at 2008-09-24 04:22:24

Merged 4058-integer-coerce.2.patch in Sage 3.1.3.alpha1


---

Comment by mabshoff created at 2008-09-24 04:22:24

Resolution: fixed


---

Comment by robertwb created at 2008-09-24 05:13:08

I will certainly look into that.


---

Comment by robertwb created at 2008-09-24 05:43:14

Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown.


---

Comment by robertwb created at 2008-09-24 08:42:49

See #4186 for a fix.


---

Comment by mabshoff created at 2008-09-24 08:51:35

Replying to [comment:9 robertwb]:
> Interestingly enough, on my machine `sage -t sage/crypto/mq/sr.py`, so it is just the (single) long doctest that provides the slowdown. 

Yeah, in that doctest we do some wacky coercion into some mv polynomial ring with a couple thousand variables, so this is really an interesting test case. This was first discussed at SD6 in Bristol, so it just shows how much the coercion re-re-write has been an interesting road :)

Cheers,

Michael
