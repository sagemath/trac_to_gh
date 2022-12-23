# Issue 7200: Fixing longest increasing subsequence (permutation method)

Issue created by migration from https://trac.sagemath.org/ticket/7200

Original creator: vferay

Original creation time: 2009-10-13 14:04:38

Assignee: mhansen

CC:  sage-combinat

Keywords: permutation

The method "longest_increasing_subsequence" was computing the longest increasing factors of the permutation!

This patch fixes the problem.


---

Comment by vferay created at 2009-10-13 14:16:19

Changing status from new to needs_review.


---

Attachment


---

Comment by vferay created at 2009-10-14 08:40:24

Changing assignee from mhansen to vferay.


---

Comment by hivert created at 2009-10-17 20:55:52

Changing status from needs_review to needs_info.


---

Comment by hivert created at 2009-10-17 20:55:52

I dislike the name `length_of_lis` ! I whould never had gessed the meaning of `lis`. Is it so painful to type `length_of_longest_increasing_subsequence` or `longest_incressing_subsequence_length` ? 

The latter is my favourite... 

I cc this to sage-combinat to have a vote. Add set the status to "needs info". 

Cheers,

Florent


---

Comment by vferay created at 2009-10-18 09:05:40

Hi Florent,

I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

Best,
Valentin


---

Comment by hivert created at 2009-10-23 16:44:27

Hi !

> I agree... I think "longest_increasing_subsequence_length" is also better because it will be near "longest_increasing_subsequences" in the method list...

In case you are just waiting for more vote, I think you can go for it ...

Florent


---

Attachment


---

Comment by vferay created at 2009-11-04 17:28:24

ok I changed the name. What shall I do now?


---

Comment by hivert created at 2009-11-04 21:30:54

Changing status from needs_info to needs_review.


---

Comment by hivert created at 2009-11-04 21:30:54

Replying to [comment:6 vferay]:
> ok I changed the name. What shall I do now?

First you should say something like:
"I just submitted a new version of the patch which is ready for review."

Then after that you should change the status which is currently "needs info" to "needs review" (see the frame at the bottom of the page) and then wait if someone react by putting a positive review or another request...

And finally for the release manager you should tell that only `permutations_fix_longest_increasing_subsequence_7200_vf.patch`
should be applied.

As you can see, I've done this for you :-). So everything is ok... 

I'm reviewing the patch...

Florent


---

Comment by hivert created at 2009-11-04 21:46:20

Changing status from needs_review to positive_review.


---

Comment by hivert created at 2009-11-04 21:46:20

Patch looks good, all tests ok. Positive review.

Cheers,

Florent


---

Attachment


---

Comment by mhansen created at 2009-11-05 01:47:57

I uploaded a patch which makes a small change to the documentation markup.  I've also updated the patch on the patch server.


---

Comment by mhansen created at 2009-11-05 01:47:57

Resolution: fixed
