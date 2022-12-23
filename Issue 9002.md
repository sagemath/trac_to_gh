# Issue 9002: Noise on PPC Mac in parametric_surface.pyx

Issue created by migration from https://trac.sagemath.org/ticket/9002

Original creator: kcrisman

Original creation time: 2010-05-21 00:01:14

Assignee: tbd

CC:  georgsweber

With 4.4.2 on 10.4 on PPC G4:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
```



---

Comment by kcrisman created at 2010-05-26 02:13:27

Changing status from new to needs_review.


---

Comment by kcrisman created at 2010-05-26 02:13:27

This should be tested both on a PPC Mac and some Intel or AMD architecture.  Works for me :)


---

Comment by drkirkby created at 2010-06-23 00:55:19

How is the "expected" value arrived at? It is just what someone happened to get on their computer, or was it evaluated to high precision in a different way?


---

Comment by kcrisman created at 2010-06-23 13:19:45

The expected value doesn't matter in that sense.  It is just creating a box which contains a certain graphic, and the last few digits are completely irrelevant (try the pictures).  E.g., 

```
sage: from sage.plot.plot3d.parametric_surface import MobiusStrip
sage: M = MobiusStrip(.0000000000007,.00000000000003,2)
sage: M.bounding_box()
((-7.3000000000000002e-13, -7.0049870840325469e-13, -2.9940801852848143e-14), (7.3000000000000002e-13, 7.0049870840325469e-13, 2.9940801852848143e-14))
```

and you can also check by looking at the graphic that the box is correct (though the formatting of the numbers could be better, which is a separate issue).

Now, that doesn't mean that somewhere there isn't some evil bug lurking.  But tracking down where the discrepancy comes from in this code would mean following a *lot* of branches, for no real purpose.  Most likely it is the fact that `MobiusStrip` has an `eval()` method that uses `math.sin` and `math.cos` a lot, which presumably will be very slightly different on different architectures.

David, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.

Georg, when you review this, you might as well try the example in this comment, to make sure that it looks right, but if it does then just do a normal review.  Unless you want to compare what you get from `eval()` with this one, which is surely where the actual difference lies.  I essentially only have access to one box at a time, so it's very difficult for me to compare them.


---

Comment by drkirkby created at 2010-06-23 13:48:16

Replying to [comment:3 kcrisman]:
> David, I realize this is a decision regarding how far back to look for numerical consistency, and I agree than for things like `gamma(2.3)` it would be very good to ensure maximum consistency.  But here the whole point is a heuristic to get a box that encloses the figure, and differences at that level of accuracy are irrelevant and take resources away from other badly needed improvements to Sage.  So it is unfortunate that we won't track it down, but it is reasonable, I think.

Fair enough. Your point is taken. I just tend to "see red" when I see numerical noise fixes, where it appears the original "expected" value just seems to be based on what someone happened to get on their computer on that particular day, with no further reasoning. Then when it fails, someone adds a few dots and it magically passes. IMHO, too many people seem happy to do this. 

But in this case, I can see where you are coming from. Tracing the exact value would be a pointless waste of time. 

<moan> Personally, where is is possible, I'd like to see high precision numerical values put as a comment in a doc test. So your gamma(2.3) would record a value like 1.16671190519816034504188144120291793853399434971946889397020666387 and say what method was used to get it. Then if code is updated and tests fail, we could question the changes more objecitively than just fixing them by adding a few dots. Ideally such a number should shows results from a independent methods. </moan>

Dave


---

Comment by drkirkby created at 2010-06-23 13:50:22

England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. 

Dave


---

Comment by kcrisman created at 2010-06-23 14:10:26

Replying to [comment:5 drkirkby]:
> England vs Slovenia kicks off in 10 minutes. After the game I'll review this. It looks simple enough, and you have convinced me there is no point worrying unduly about the exact number. 

Ah, see, I get to wait for a few more hours until Germany-Ghana.  I suppose I should watch US-Algeria too, but work calls.

Do you have a PPC Mac box to test this on?  I think we still need Georg or someone else for that.


---

Comment by drkirkby created at 2010-06-23 17:17:07

I'm happy to give this a positive. We know what result it was producing, and your fix should allow that to pass. I can't possibly see how this can make the situation any worst, even in the *very* unlikely even it does not cure the problem. 

I've tested on SPARC (Solaris 10) and x86 (Linux) processors. 

## Linux (sage.math) with Intel Xeon processor

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
	 [11.3 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 11.3 seconds
kirkby@sage:~/sage-4.4.3$ uname -a
Linux sage.math.washington.edu 2.6.24-26-server #1 SMP Tue Dec 1 18:26:43 UTC 2009 x86_64 GNU/Linux
```


## 'redstart' Solaris 10 with Sun UltraSPARC III+ processors

```
drkirkby@redstart:~/sage-4.4.4.alpha1$ ./sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
	 [33.6 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 33.6 seconds
```



---

Comment by drkirkby created at 2010-06-23 17:17:07

Changing status from needs_review to positive_review.


---

Comment by GeorgSWeber created at 2010-06-28 21:49:28

On my Mac PPC (PowerPC_G4) with vanilla Sage-4.4.3, before applying the patch:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
**********************************************************************
File "/Volumes/SageVolume/sage/sage-4.4.3/devel/sage/sage/plot/plot3d/parametric_surface.pyx", line 311:
    sage: M.bounding_box()
Expected:
    ((-10.0, -7.5390734925047846, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
Got:
    ((-10.0, -7.5390734925047855, -2.9940801852848145), (10.0, 7.5390734925047846, 2.9940801852848145))
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_11
***Test Failed*** 1 failures.
For whitespace errors, see the file /Users/georgweber/.sage//tmp/.doctest_parametric_surface.py
         [106.1 s]
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
Total time for all tests: 106.1 seconds
```

and after applying the patch:

```
sage -t  "devel/sage/sage/plot/plot3d/parametric_surface.pyx"
         [86.9 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 87.0 seconds
```

Good work, positive review well deserved!


---

Comment by ddrake created at 2010-07-22 02:52:29

This ticket seems the same as #9516...


---

Comment by ddrake created at 2010-07-22 02:55:46

Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.


---

Comment by drkirkby created at 2010-07-22 06:53:38

Replying to [comment:11 ddrake]:
> Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.

Have you made that comment on the wrong ticket? I see

`# User crisman`@`Crismans-Computer.local`

in the patch. 

Dave


---

Comment by drkirkby created at 2010-07-22 07:09:38

Replying to [comment:12 drkirkby]:
> Replying to [comment:11 ddrake]:
> > Karl-Dieter (or release manager): can you fix the User field in your patch? It looks like you didn't set a username in your hgrc.
> 
> Have you made that comment on the wrong ticket? I see
> 
> `# User crisman`@`Crismans-Computer.local`
> 
> in the patch. 
> 
> Dave 

Thinking about that more, that more, your point is valid, as that is not a full name. I can understand someone not wanting their full email address. Just in case the person does not know the format, a .hgrc which adds a name and email address would be:

```
drkirkby@hawk:~$ cat .hgrc
[ui]
username = Forename Surname <your.address@yoursite.com>

[extensions]
# Enable the Mercurial queue extension.
hgext.mq =
```



---

Comment by kcrisman created at 2010-07-22 12:33:07

Sorry, I didn't think of that.  I created this patch on a PPC Mac, and it's one I don't ordinarily use for Sage developing and hence didn't have an hgrc file.  I'll try to fix that momentarily.  Otherwise all my patches have my usual email address on them.


---

Attachment

Based on 4.5.1


---

Comment by kcrisman created at 2010-07-22 12:36:43

Hopefully this will address the issue!


---

Comment by ddrake created at 2010-07-22 23:34:01

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 23:34:01

Replying to [comment:15 kcrisman]:
> Hopefully this will address the issue!

Excellent. Thanks! Merged in 4.5.2.alpha1.
