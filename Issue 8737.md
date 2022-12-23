# Issue 8737: compile plot3d/base.pyx and index_face_set with "-std=c99"

Issue created by migration from https://trac.sagemath.org/ticket/8737

Original creator: jhpalmieri

Original creation time: 2010-04-21 15:25:00

Assignee: jason, was

CC:  robertwb robert.marik drkirkby mvngu

This is a followup to [http://trac.sagemath.org/sage_trac/ticket/8424#comment:5](http://trac.sagemath.org/sage_trac/ticket/8424#comment:5).  Without this patch, the Sage library (as of 4.4.alpha0) doesn't build on t2.



---

Comment by jhpalmieri created at 2010-04-21 18:00:34

Changing status from new to needs_review.


---

Comment by robertwb created at 2010-04-21 18:11:18

Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it.


---

Comment by jhpalmieri created at 2010-04-21 18:21:19

Replying to [comment:2 robertwb]:
> Nearly every instance of `-std=c99` is also paired with `-D_XPG6`. I'm honestly unsure as to why, but if we don't we should justify it. 

It looks like about half of them have `-D_XPG6`.  I can't really tell what this flag means (except something about "issue 6 of the X/Open Portability Guide"), so I have no idea if it's a good idea.  Without it for these two pyx files, the Sage library builds on t2, for what that's worth.


---

Comment by drkirkby created at 2010-04-21 23:40:17

I would rephrase the question and ask why are people adding -D_XPG6? Can they justify it? 

We can justify adding -std=c99, as we want to make use of a feature that was not defined until the C99 standard.  I don't know of any justification for adding -D_XPG6. (That is not to say there is not any, but I think the onus should be on someone who adds -D_XPG6 to justify why they add it.) 

There are quite a few bits of code in Sage which appear to be added just because someone else did so before, without anyone understanding why they did it. One sees things like 


```
path="$SAGE_LOCAL"/bin
```


when it should be:

```
path="$SAGE_LOCAL/bin"
```

I suspect people are just cutting/pasting without any understanding. 

I think it is better to just leave it as -std=c99, until such time as someone can justify why -D_XPG6 is best added. 

Please note, I'm not saying -D_XPG6 might not be right, but only that I'd rather not add things we don't understand. 

Dave


---

Comment by drkirkby created at 2010-04-21 23:40:17

Changing assignee from jason, was to drkirkby.


---

Comment by robertwb created at 2010-04-21 23:48:23

The first time it popped up was for FLINT: 

http://hg.sagemath.org/sage-main/diff/89003ef36bd6/setup.py


---

Comment by jhpalmieri created at 2010-04-22 02:18:36

I'm having the same problem with the file chmm.pyx, with the same solution.  So I'm adding it to this patch.


---

Attachment


---

Comment by jhpalmieri created at 2010-04-22 02:21:56

I should say, it's not exactly the same problem with chmm.pyx: the Sage library seems to build successfully, and indeed the Sage build completes without complaint, but Sage won't start up: it gives errors about `isfinite` and the file `chmm.so`.


---

Comment by was created at 2010-04-22 02:52:57

Regarding chmm: That makes sense, because I use isfinite in chmm.pyx:

```
cdef extern from "math.h":
    double log(double)
    double sqrt(double)
    double exp(double)
    int isnormal(double)
    int isfinite(double)
```


So I'm fine with building it with c99.

William


---

Comment by was created at 2010-04-22 22:40:31

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-23 17:08:13

Resolution: fixed


---

Comment by jhpalmieri created at 2010-04-23 17:08:13

Merged into 4.4.alpha2.
