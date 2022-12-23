# Issue 2513: Weird printing issues with cython, caused by LANG environment variable

Issue created by migration from https://trac.sagemath.org/ticket/2513

Original creator: craigcitro

Original creation time: 2008-03-13 23:22:50

Assignee: craigcitro

CC:  robertwb cwitty

So I've noticed for a little while now that I have the following strange problem: 


```
sage/rings/number_field/totallyreal_data.c: In function â:
sage/rings/number_field/totallyreal_data.c:1920: error: â undeclared (first use in this function)
```


But then, if you comment out the fix for trac ticket #276 (which sets the environment variable `LANG`), that same error becomes:


```
sage/rings/number_field/totallyreal_data.c: In function '__pyx_f_4sage_5rings_12number_field_16totallyreal_data_lagrange_degree_3_c':
sage/rings/number_field/totallyreal_data.c:1920: error: 'intp' undeclared (first use in this function)
```


Obviously we'd prefer the second. What I think we should do is move setting the `LANG` environment variable somewhere closer in the build & run process to where Maxima gets initialized. I haven't had time to sit down and look at this at all -- I'm assigning it to myself, but if someone else wants to jump in and fix it before me, I definitely won't mind.

I'm also adding robertwb to the cc, because I think I recall him saying he ran into this, too, and he's (1) probably happy to have a workaround, and (2) likely to come up with a fix himself, saving me work. :)


---

Comment by craigcitro created at 2008-03-13 23:24:10

Typo in the title.


---

Comment by craigcitro created at 2009-06-14 09:02:43

So I just happened to glance back at this ticket tonight because I hit this same bug; looking at #276, that was a fix for `clisp` -- which is now *gone*! So I'm attaching a patch that just un-does the work of the patch at #276, which will fix this weird printing issue.


---

Attachment


---

Comment by ncalexan created at 2009-06-14 22:12:56

Resolution: fixed
