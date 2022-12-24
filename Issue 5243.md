# Issue 5243: [with patch, needs review] non decreasing parking functions

archive/issues_005243.json:
```json
{
    "body": "Assignee: @mwhansen\n\nCC:  sage-combinat @dandrake\n\nKeywords: parking functions / Dyck words\n\nThis patch implement the combinatorial classes of non decreassing parking function with the usual methods (counting/listing/!__contains!__/iterating)... It also implements bijections from and to Dyck words.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5243\n\n",
    "created_at": "2009-02-12T13:45:37Z",
    "labels": [
        "combinatorics",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "[with patch, needs review] non decreasing parking functions",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5243",
    "user": "@hivert"
}
```
Assignee: @mwhansen

CC:  sage-combinat @dandrake

Keywords: parking functions / Dyck words

This patch implement the combinatorial classes of non decreassing parking function with the usual methods (counting/listing/!__contains!__/iterating)... It also implements bijections from and to Dyck words.

Issue created by migration from https://trac.sagemath.org/ticket/5243





---

archive/issue_comments_040186.json:
```json
{
    "body": "Changing assignee from @mwhansen to @nthiery.",
    "created_at": "2009-02-12T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40186",
    "user": "@hivert"
}
```

Changing assignee from @mwhansen to @nthiery.



---

archive/issue_comments_040187.json:
```json
{
    "body": "Nicolas is rewiewing it rigth there. I currently taking case of its remark.",
    "created_at": "2009-02-12T18:39:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40187",
    "user": "@hivert"
}
```

Nicolas is rewiewing it rigth there. I currently taking case of its remark.



---

archive/issue_comments_040188.json:
```json
{
    "body": "I modified my patch according to Nicolas remarks. I took the occasion to adapt this patch to the design change of patch #5255.",
    "created_at": "2009-02-13T16:25:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40188",
    "user": "@hivert"
}
```

I modified my patch according to Nicolas remarks. I took the occasion to adapt this patch to the design change of patch #5255.



---

archive/issue_comments_040189.json:
```json
{
    "body": "Changing assignee from @nthiery to @hivert.",
    "created_at": "2009-03-01T18:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40189",
    "user": "@hivert"
}
```

Changing assignee from @nthiery to @hivert.



---

archive/issue_comments_040190.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-01T18:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40190",
    "user": "@hivert"
}
```

Changing status from new to assigned.



---

archive/issue_comments_040191.json:
```json
{
    "body": "The patch is now rebased an finalized. Ready for review. \n\nFlorent",
    "created_at": "2009-04-05T16:51:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40191",
    "user": "@hivert"
}
```

The patch is now rebased an finalized. Ready for review. 

Florent



---

archive/issue_comments_040192.json:
```json
{
    "body": "Rebased patch",
    "created_at": "2009-04-05T16:52:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40192",
    "user": "@hivert"
}
```

Rebased patch



---

archive/issue_comments_040193.json:
```json
{
    "body": "Attachment [non_decreasing_parking_function-5243-submitted.patch](tarball://root/attachments/some-uuid/ticket5243/non_decreasing_parking_function-5243-submitted.patch) by @nthiery created at 2009-04-14 02:14:33",
    "created_at": "2009-04-14T02:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40193",
    "user": "@nthiery"
}
```

Attachment [non_decreasing_parking_function-5243-submitted.patch](tarball://root/attachments/some-uuid/ticket5243/non_decreasing_parking_function-5243-submitted.patch) by @nthiery created at 2009-04-14 02:14:33



---

archive/issue_comments_040194.json:
```json
{
    "body": "Florent, I'm working on reviewing this, and I already see a bunch of things in the docstrings that I'd like changed -- these range from grammar and usage changes to different formatting suggestions. Would you like me to list all the changes, and have you edit the patch, or should I upload a \"referee patch\" that changes the bits I'd like changed?\n\nBTW, I can already say that you've got some lovely ASCII art in your docstrings!",
    "created_at": "2009-04-16T08:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40194",
    "user": "@dandrake"
}
```

Florent, I'm working on reviewing this, and I already see a bunch of things in the docstrings that I'd like changed -- these range from grammar and usage changes to different formatting suggestions. Would you like me to list all the changes, and have you edit the patch, or should I upload a "referee patch" that changes the bits I'd like changed?

BTW, I can already say that you've got some lovely ASCII art in your docstrings!



---

archive/issue_comments_040195.json:
```json
{
    "body": "Hi Dan, \n\nThank you for reviewing this one. It is not a very important one for the sage community, but it was my first submitted ticket and I'll be glad seeing it merged.\nIt will be a test-case for a future (vaporware ? :-) bijection infrastructure. \n\nIf it's not too much work for you I'd rather you upload a referee patch, unless you have big changes. If they are a bunch on typos and presentation change, my experience is that it's not that much more work creating a new patch than explaining by trac or e-mail what you want to do. Is it ok with you ? When you say \"usage changes\" is this English usage and or sage usage ?\n\n> BTW, I can already say that you've got some lovely ASCII art in your docstrings!\n\nA picture is always clearer than a long explanation :)\n\nCheers,\n\nFlorent",
    "created_at": "2009-04-17T13:09:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40195",
    "user": "@hivert"
}
```

Hi Dan, 

Thank you for reviewing this one. It is not a very important one for the sage community, but it was my first submitted ticket and I'll be glad seeing it merged.
It will be a test-case for a future (vaporware ? :-) bijection infrastructure. 

If it's not too much work for you I'd rather you upload a referee patch, unless you have big changes. If they are a bunch on typos and presentation change, my experience is that it's not that much more work creating a new patch than explaining by trac or e-mail what you want to do. Is it ok with you ? When you say "usage changes" is this English usage and or sage usage ?

> BTW, I can already say that you've got some lovely ASCII art in your docstrings!

A picture is always clearer than a long explanation :)

Cheers,

Florent



---

archive/issue_comments_040196.json:
```json
{
    "body": "I am working on reviewing this, and I have a couple questions and one larger concern. First, some questions. I'm just curious about these things:\n\n* what does the ``@`classmethod` decorator do?\n* why does the `keys` method return the domain of the function? It seems strange to have a `keys` method for something list-based, and not dictionary-based.\n\nHere are my concerns:\n* Your code does not check to see if it gets a list of positive integers, so you can do `NonDecreasingParkingFunction[[0, .1, pi/3, sqrt(2)])`, yikes! Do we want to require lists of positive integers?\n* In `is_a()`, you have:\n\n```\n   for i in range(len(x)-1):\n        if x[i] > x[i+1] or x[i] > i+1:\n            return False\n```\n\n    Instead of iterating over indices and doing a list lookup every time, would it be faster to use Python's `enumerate` in something like this?\n\n```\n   prev = 1\n   for i, elt in enumerate(x):\n       if prev > elt or elt > i+1:\n           return False\n       prev = elt\n```\n\n    That would also let you finish the function with `return True`, since the `enumerate` loop would check the final element.\n\n* Right now when you give the `NonDecreasingParkingFunction` constructor a bad list, I see a strange error message:\n\n```\nsage: NonDecreasingParkingFunction([1,1,4])\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (5, 0))\n\n---------------------------------------------------------------------------\nAssertionError                            Traceback (most recent call last)\n\n/home/drake/.sage/temp/klee/10186/_home_drake__sage_init_sage_0.py in <module>()\n\n/var/tmp/sage-3.4.2/local/lib/python2.5/site-packages/sage/combinat/non_decreasing_parking_function.pyc in __init__(self, lst)\n    383             [1, 1, 2, 2, 5, 6]\n    384         \"\"\"\n--> 385         assert(is_a(lst))\n    386         CombinatorialObject.__init__(self, lst)\n    387         \n\nAssertionError: \n```\n\n* Also, related to `is_a`: the `assert` statement should give the user some idea of what has gone wrong. I suggest changing the assert line (line 409) to `assert is_a(lst), 'list is not a non-decreasing parking function.'`. Also note that `assert` is a statement, not a function -- just like `print` before Python 3.0.\n* My biggest concern is with the getitem stuff. You are effectively shifting the list indices by 1, which really bothers me. Perhaps other people don't feel this way, and perhaps this is the best decision, but whenever I am thinking of something as a list, I *really* want the indices to be zero-based, since that's what the rest of Sage/Python does. Right now, we have:\n\n```\nsage: f = NonDecreasingParkingFunction([1,1,2,3])\nsage: f[2]\n1\nsage: f[3]\n2\n```\n\n    When I use square brackets, I'm thinking \"list index\", and I really want it zero-based. Perhaps we should make these objects callable, so we can treat them like functions? I would not mind having `f(2)` be 1 and `f(3)` be 2, since the round parentheses indicate a function call, and indeed the above object f is a function that sends 3 to 2.\n\nI'm marking this \"needs work\" because of the list index issue. I have a patch which fixes a bunch of tiny docstring bits which I'll upload once we have the rest of this sorted out.",
    "created_at": "2009-05-06T04:08:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40196",
    "user": "@dandrake"
}
```

I am working on reviewing this, and I have a couple questions and one larger concern. First, some questions. I'm just curious about these things:

* what does the ``@`classmethod` decorator do?
* why does the `keys` method return the domain of the function? It seems strange to have a `keys` method for something list-based, and not dictionary-based.

Here are my concerns:
* Your code does not check to see if it gets a list of positive integers, so you can do `NonDecreasingParkingFunction[[0, .1, pi/3, sqrt(2)])`, yikes! Do we want to require lists of positive integers?
* In `is_a()`, you have:

```
   for i in range(len(x)-1):
        if x[i] > x[i+1] or x[i] > i+1:
            return False
```

    Instead of iterating over indices and doing a list lookup every time, would it be faster to use Python's `enumerate` in something like this?

```
   prev = 1
   for i, elt in enumerate(x):
       if prev > elt or elt > i+1:
           return False
       prev = elt
```

    That would also let you finish the function with `return True`, since the `enumerate` loop would check the final element.

* Right now when you give the `NonDecreasingParkingFunction` constructor a bad list, I see a strange error message:

```
sage: NonDecreasingParkingFunction([1,1,4])
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (5, 0))

---------------------------------------------------------------------------
AssertionError                            Traceback (most recent call last)

/home/drake/.sage/temp/klee/10186/_home_drake__sage_init_sage_0.py in <module>()

/var/tmp/sage-3.4.2/local/lib/python2.5/site-packages/sage/combinat/non_decreasing_parking_function.pyc in __init__(self, lst)
    383             [1, 1, 2, 2, 5, 6]
    384         """
--> 385         assert(is_a(lst))
    386         CombinatorialObject.__init__(self, lst)
    387         

AssertionError: 
```

* Also, related to `is_a`: the `assert` statement should give the user some idea of what has gone wrong. I suggest changing the assert line (line 409) to `assert is_a(lst), 'list is not a non-decreasing parking function.'`. Also note that `assert` is a statement, not a function -- just like `print` before Python 3.0.
* My biggest concern is with the getitem stuff. You are effectively shifting the list indices by 1, which really bothers me. Perhaps other people don't feel this way, and perhaps this is the best decision, but whenever I am thinking of something as a list, I *really* want the indices to be zero-based, since that's what the rest of Sage/Python does. Right now, we have:

```
sage: f = NonDecreasingParkingFunction([1,1,2,3])
sage: f[2]
1
sage: f[3]
2
```

    When I use square brackets, I'm thinking "list index", and I really want it zero-based. Perhaps we should make these objects callable, so we can treat them like functions? I would not mind having `f(2)` be 1 and `f(3)` be 2, since the round parentheses indicate a function call, and indeed the above object f is a function that sends 3 to 2.

I'm marking this "needs work" because of the list index issue. I have a patch which fixes a bunch of tiny docstring bits which I'll upload once we have the rest of this sorted out.



---

archive/issue_comments_040197.json:
```json
{
    "body": "I uploaded my documentation fixes patch, since there's no reason to keep it secret; it only fixes docstring bits (mostly it changes \"non decreasing\" to \"non-decreasing\" :) except in three places:\n\n* changes two \"`assert(foo)`\" statements to \"`assert foo, 'what went wrong'`\"\n* changes the `is_a()` function as I described above. If the consensus is that we should keep it the way it was, I have no problem removing this change from my patch.",
    "created_at": "2009-05-06T04:26:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40197",
    "user": "@dandrake"
}
```

I uploaded my documentation fixes patch, since there's no reason to keep it secret; it only fixes docstring bits (mostly it changes "non decreasing" to "non-decreasing" :) except in three places:

* changes two "`assert(foo)`" statements to "`assert foo, 'what went wrong'`"
* changes the `is_a()` function as I described above. If the consensus is that we should keep it the way it was, I have no problem removing this change from my patch.



---

archive/issue_comments_040198.json:
```json
{
    "body": "Attachment [trac_5243-fixes.patch](tarball://root/attachments/some-uuid/ticket5243/trac_5243-fixes.patch) by @dandrake created at 2009-05-06 04:28:52",
    "created_at": "2009-05-06T04:28:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40198",
    "user": "@dandrake"
}
```

Attachment [trac_5243-fixes.patch](tarball://root/attachments/some-uuid/ticket5243/trac_5243-fixes.patch) by @dandrake created at 2009-05-06 04:28:52



---

archive/issue_comments_040199.json:
```json
{
    "body": "Attachment [trac_5243-getitem_vs_call.patch](tarball://root/attachments/some-uuid/ticket5243/trac_5243-getitem_vs_call.patch) by @mwhansen created at 2009-09-26 04:16:51",
    "created_at": "2009-09-26T04:16:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40199",
    "user": "@mwhansen"
}
```

Attachment [trac_5243-getitem_vs_call.patch](tarball://root/attachments/some-uuid/ticket5243/trac_5243-getitem_vs_call.patch) by @mwhansen created at 2009-09-26 04:16:51



---

archive/issue_comments_040200.json:
```json
{
    "body": "Dan's changes look good to me, and I've added a patch which switches the behavior of __getitem__.  I think with these, it can go in.  Dan, do you want to sign off on the rest?",
    "created_at": "2009-09-26T04:19:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40200",
    "user": "@mwhansen"
}
```

Dan's changes look good to me, and I've added a patch which switches the behavior of __getitem__.  I think with these, it can go in.  Dan, do you want to sign off on the rest?



---

archive/issue_comments_040201.json:
```json
{
    "body": "Looks good to me. Positive review. I think this will have to wait for 4.1.3, since 4.1.2 is now in feature freeze.",
    "created_at": "2009-09-28T02:46:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40201",
    "user": "@dandrake"
}
```

Looks good to me. Positive review. I think this will have to wait for 4.1.3, since 4.1.2 is now in feature freeze.



---

archive/issue_comments_040202.json:
```json
{
    "body": "Merged all 3 patches.",
    "created_at": "2009-10-15T07:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40202",
    "user": "@mwhansen"
}
```

Merged all 3 patches.



---

archive/issue_comments_040203.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T07:26:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5243",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5243#issuecomment-40203",
    "user": "@mwhansen"
}
```

Resolution: fixed
