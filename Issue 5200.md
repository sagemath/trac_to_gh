# Issue 5200: [with patch, needs review] subsets and subwords bug fix + improvements.

Issue created by migration from https://trac.sagemath.org/ticket/5200

Original creator: hivert

Original creation time: 2009-02-07 14:02:38

Assignee: mhansen

CC:  sage-combinat

Keywords: subsets, subwords

This patches deals with several issues concerning subwords and subsets:
  1. It implements subsets for finite multisets (sets with repetitions).
     Before the patch:

```
sage: Subsets([2,2,3]).list()
[{}, {2}, {3}, {2, 3}]
```

     After:

```
sage: Subsets([2,2,3]).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```

  1. It implement `__contains__` which was missing for subsets and subwords:
     Before:

```
sage: st = Subsets([1,2,2,3]); Set([1,2]) in st
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)
```

     After:

```
sage: st = Subsets([1,2,2,3]); Set([1,2]) in st
True
```

  1. It fixes a bug in smallest_positions:
     Before:

```
sage: sage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])
[4, 4, 4]
```

     After:

```
sage.combinat.subword.smallest_positions([2,4,3,3,1,2],[1,3,3])
False
```

     which means that 113 is not a subword of 243312. 
  4. It finally improves the doc and the tests.

Since this is my first trac submission, any comment about this text or the patch is strongly welcome...


---

Comment by hivert created at 2009-03-01 15:15:05

It has been decided (direct talk with Nicolas + irssi with Mike) that the user has to explicitely set that he want multisets. Therefore, on the contrary that is anounced, the following is not working:

```
sage: Subsets([2,2,3]).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```

Instead one should write

```
sage: Subsets([2,2,3], multiset=True).list()
[[], [2], [3], [2, 2], [2, 3], [2, 2, 3]]
```



---

Comment by hivert created at 2009-03-01 15:20:02

Changing assignee from mhansen to hivert.


---

Comment by hivert created at 2009-03-01 15:20:14

Changing status from new to assigned.


---

Comment by hivert created at 2009-03-01 15:28:42

Sorry for the mess with the description... I just realize because of my mistake that it is possible to change the description. :-)  

I've uploaded a new patch according to remark of Nicolas and Mike. It should be ready for review and hopefully integration. 

Cheers,

Florent


---

Comment by hivert created at 2009-03-17 17:53:12

New patch after Nicolas review.


---

Attachment

Nicolas sent me a review on sage-combinat-devel. The new subsets_subwords-5200-submitted.2.patch patch fixes the various problems pointed out by the review (typos + code improvements). 

Florent


---

Comment by nthiery created at 2009-03-19 18:18:40

Florent: feel free to switch the title to with review after the following micro updates:
 - iterate -> iterates
 - of all -> ""


---

Attachment

Last review patch.


---

Comment by hivert created at 2009-03-19 21:06:00

The review patch I just submitted address Nicolas last comment.
Sorry for the mess with several version of the patch. The correct patch are:

 * attachment:subsets_subwords-5200-submitted.2.patch
 * attachment:subsets_subwords-5200-review.patch

According to Nicolas la remarks I allow myself to change the review title. Please tell me if it's not allowed by the review rules. 

Florent


---

Comment by mabshoff created at 2009-03-25 06:41:46

"with review" is meaningless :)

Nicolas: Can you give this a formal positive review?

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 06:50:19

After re-reading Nicola's comment I am giving this patch a positive review in his name. The two patches also pass doctests.

Cheers,

Michael


---

Comment by mabshoff created at 2009-03-25 06:51:21

Resolution: fixed


---

Comment by mabshoff created at 2009-03-25 06:51:21

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
