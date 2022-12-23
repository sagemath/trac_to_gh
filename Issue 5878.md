# Issue 5878: Add support for constructing irreducible matrix representations of the symmetric group

Issue created by migration from https://trac.sagemath.org/ticket/5878

Original creator: saliola

Original creation time: 2009-04-23 16:57:53

Assignee: saliola

CC:  sage-combinat

Keywords: sage-combinat

It would be great to be able to construct the matrices for the irreducible representations of the symmetric group.


---

Attachment

The patch adds functionality to construct Young's seminormal and orthogonal representations as well as the Specht representation. This is done via Yang-Baxter graphs, so the patch implements that as well.


---

Comment by saliola created at 2009-04-23 17:10:12

Warning: The patch depends on #5877.

But it doesn't have to though: #5877 fixes an issue that is required for the `to_character` method, and this method is not necessary for the rest of the code.


---

Comment by mvngu created at 2009-05-19 05:57:15

Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:

```
[mvngu@sage sage-4.0.alpha0]$ ./sage -t -long devel/sage-5878/sage/combinat/symmetric_group_representations.py
<LOTS_OF_BOOM!>
```

[Here's](http://sage.math.washington.edu/home/mvngu/patch/5878/log.txt) the full (but very long) error log from the doctests.


---

Comment by saliola created at 2009-05-19 08:03:47

Replying to [comment:3 mvngu]:
> Using sage-4.0.alpha0 with patch from #6048, doctesting with options `-t -long` gave me BOOM!:

I can't reproduce this. When I run the tests, with or without #6048, I get no failures:


```
karkwa: sage-4.0 -version
| Sage Version 4.0.alpha0, Release Date: 2009-05-15                  |
karkwa: hg qapplied 
non-ascii.patch
trac_5878.patch

karkwa: sage-4.0 -b && sage-4.0 -t -long symmetric_group_representations.py yang_baxter_graph.py 
...
real    0m1.263s
user    0m1.004s
sys     0m0.244s
sage -t -long "devel/sage-main/sage/combinat/symmetric_group_representations.py"
         [5.8 s]
sage -t -long "devel/sage-main/sage/combinat/yang_baxter_graph.py"
         [3.4 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 9.2 seconds
```


Can you re-check this?

Thanks,
Franco


---

Comment by mhansen created at 2009-06-04 18:48:09

Changing status from new to assigned.


---

Comment by mhansen created at 2009-06-04 18:48:09

Changing assignee from saliola to mhansen.


---

Attachment

Things look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.

Franco, can you just check over these?


---

Comment by saliola created at 2009-06-04 22:26:02

Replying to [comment:5 mhansen]:
> Things look good to me after I've applied my reviewer patch which takes care of the issues with the upgrade to 4.0.
> 
> Franco, can you just check over these?

Checked. They are correct.

Positive review for the reviewer patch.


---

Comment by mvngu created at 2009-06-08 03:58:39

So all patches have proper review? If so, then the summary should be changed.


---

Comment by ncalexan created at 2009-06-15 20:51:25

Patch looks good, tests pass on sage.math and my OS X 10.5 laptop.  I'm not expert enough to say the code is correct.  Is this positive review?


---

Comment by boothby created at 2009-06-19 18:34:22

This is ridiculous.  Mhansen gave it a positive review pending saliola's opinion.  Saliola confirmed mhansen's review and +1'd mhansen's patch.  I'm merging this one.


---

Comment by rlm created at 2009-06-24 09:58:04

Resolution: fixed
