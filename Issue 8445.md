# Issue 8445: sh: kpsewhich: not found -  Sage 4.3.4.alpha0 on Solaris

Issue created by migration from https://trac.sagemath.org/ticket/8445

Original creator: drkirkby

Original creation time: 2010-03-05 13:42:44

Assignee: drkirkby

CC:  mvngu jsp jhpalmieri mpatel sage-combinat

## Background
After downloading the 4.3.4.alpha0.tar I applied some patches necessary to get this to build on Solaris 10 (SPARC). Namely: 

 === Patches installed to allow Sage to build properly === 
 * #7867 A patch for Python which allows Python modules to be built properly. 
 * #8440 A patch for Python to allow the _multiprocessing module to build. 

 === Patches installed to allow most all doctests to pass in 4.3.3 (a few fail in 4.3.4.alpha0 ===

 * #8374 Numerical noise in sage/symbolic/constants_c.pyx
 * #8375 Numerical noise in sage/symbolic/pynac.pyx
 * #8391 Change 'top' to 'prstat' on Solaris, othewise lots of doctests time out.
 * #8408 Update sqlite to the latest version (otherwise #8397, #8398, #8399, #8400 and #8401 all fail). 

 == The problems == 

Running the long doctests I see:


```
sage -t  -long "devel/sage/sage/categories/finite_semigroups.py"
sh: kpsewhich: not found
sh: kpsewhich: not found
**********************************************************************
File "/export/home/drkirkby/32/sage-4.3.4.alpha0/devel/sage/sage/categories/finite_semigroups.py", line 232:
    sage: sorted(S.j_transversal_of_idempotents())
Expected:
    ['a', 'ab', 'ac', 'acb', 'b', 'bc', 'c']
Got:
    ['a', 'ab', 'ac', 'acb', 'b', 'c', 'cb']
```


So there are two problems. 
 * kpsewhich: not found 
 * doctest failure

But #8180 was supposed to fix this kpsewhich issue, so I believe the fix is not working fully.  

I'll create a ticket for the test failure if needed. But I believe I see this mentioned on sage-devel, so it looks like I'm not the only one with this issue. So a ticket for it probably exists already.


---

Comment by mvngu created at 2010-03-05 13:55:12

The sage-combinat team might be interested in this ticket.


---

Comment by jhpalmieri created at 2010-03-05 20:45:35

Changing status from new to needs_review.


---

Comment by jhpalmieri created at 2010-03-05 20:45:35

Here's a patch.  It's hard for me to doctest it on Solaris: I think the only machine I have access to is t2.math, but there isn't enough room in /scratch for me to install Sage.  So please test it out.  It works for me on several other machines, and on t2, if I `load` a file containing the relevant code, that works as well.

The patch also reformats the warning messages that get printed if tkz-berge.sty (etc.) are not present.


---

Attachment

Thank's John,

I will test this, but it might take me a few days, as I have a very busy schedule this week. 

Fortunately this is not a critical patch. 

Dave


---

Comment by drkirkby created at 2010-03-06 21:48:19

Changing assignee from drkirkby to jhpalmieri.


---

Comment by drkirkby created at 2010-03-06 21:48:19

John, 

I've tested this on Solaris, and find no more "kpsewhich" problems. So from my point of view it is working. 

However, I don't feel comfortable giving this a positive review, as I don't understand much of the code. 

Perhaps one of the others cc'ed on the ticket can look over this, keeping in mind that it does solve the problem I reported. 

Dave


---

Comment by mhansen created at 2010-03-06 23:37:01

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-03-06 23:37:01

This change looks good to me.


---

Comment by mhansen created at 2010-03-07 00:01:40

Resolution: fixed
