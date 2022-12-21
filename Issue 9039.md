# Issue 9039: major error in E.sha().bound_kato() for E an elliptic curve

Issue created by migration from Trac.

Original creator: rlm

Original creation time: 2010-05-25 00:37:50

Assignee: cremona

CC:  wuthrich

Does not check for primes of bad reduction at all!!


---

Comment by rlm created at 2010-05-25 01:15:47

I haven't yet fixed the documentation results, since the returned lists are different, mainly to highlight the differences... Also I'm not entirely sure I have the code exactly right, maybe you can verify this. I also think that the references need updating/completing.

Input is welcome! Here are the doc differences:


```
sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
Saturation index bound = 265
WARNING: saturation at primes p > 100 will not be done;  
points may be unsaturated at primes between 100 and index bound
Failed to saturate MW basis at primes [ ]
*** saturation possibly incomplete at primes [ ]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 876:
    sage: E.sha().bound_kato()
Expected:
    [2, 3, 5]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 879:
    sage: E.sha().bound_kato()
Expected:
    [2, 3, 5]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 882:
    sage: E.sha().bound_kato()
Expected:
    [2, 3]
Got:
    [2]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 888:
    sage: E.sha().bound_kato()                 # long time (about 1 second)
Expected:
    [2, 3, 5]
Got:
    [2, 5, 23]
**********************************************************************
File "/Users/rlmill/sage-4.4.1/devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py", line 896:
    sage: E.sha().bound_kato()                 # long time (< 10 seconds)
Expected:
    [2, 3, 7]
Got:
    [2, 7, 29]
**********************************************************************
1 items had failures:
   5 of  15 in __main__.example_8
***Test Failed*** 5 failures.
For whitespace errors, see the file /Users/rlmill/.sage//tmp/.doctest_sha_tate.py
	 [154.4 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/schemes/elliptic_curves/sha_tate.py"
Total time for all tests: 154.4 seconds
```



---

Comment by wuthrich created at 2010-05-25 14:03:15

In principle, I agree with the changes. Certainly the additive primes must go in that list.

When it comes to the the condition on the mod-p representation, I would propose to wait. I have submitted a correction for the article proving this. But before I get the confirmation that everything is fine now, I would not want to change this back in sage. Also there will be other places as in p_primary_bound where a change will be needed in that case.

Do you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?

Chris.


---

Comment by rlm created at 2010-05-25 16:54:31

Chris,

Replying to [comment:2 wuthrich]:
> Do you want to wait ? Or do you want to fix the issue with the additive first and open another ticket when/if the corrections are accepted ?

I am not in favor of waiting. Let's get the patch up to speed with what is currently known and verified, and update the function once we're ready to.

In order to get an acceptable patch for now, are you saying that the only change should be to add in the additive primes? If so I can modify my patch to do only that.


---

Comment by wuthrich created at 2010-05-25 21:46:23

Yes, the list should contain 2, all primes of additive reduction and all for which the mod-p representation is not surjective.


---

Comment by rlm created at 2010-05-25 22:34:38

Changing status from new to needs_review.


---

Comment by rlm created at 2010-05-25 22:34:38

The new patch gives doctest changes as well. Are you sure that this is correct (mod-p vs. p-adic rep'n surjective, etc.) for p=3? If it is, then it's all ready for review.


---

Comment by wuthrich created at 2010-05-26 09:54:56

Ooops, you are right. Elkies describes these curves (they are rare) and shows that they do not contain SL_2(Z_p) in the p-adic Galois image. And that is needed for Kato's theorem 12.5. I have the vague feeling that one could lower it to the case of mod-p-surjectivity with some work, but I am sure it is not yet known if that is true.

That makes the check at 3 quite painful. Maybe we should just include 3 by default. I will look at the galois representations in sage soon again. Maybe I find an easy way to check it for p=3.

Chris.


---

Attachment

Chris,

Take a look at the newest patch. This should provide a correct version of `bound_kato`.


---

Comment by wuthrich created at 2010-05-28 13:14:59

All tests passed. This small but important change must go in !
Thanks, Robert.


---

Comment by wuthrich created at 2010-05-28 13:14:59

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-06-04 15:28:21

I'm merging this in, since Robert begged me to, and it's a 1-line fix I understand well, that has very, very low chance of causing any trouble elsewhere.


---

Comment by was created at 2010-06-04 15:28:21

Resolution: fixed
