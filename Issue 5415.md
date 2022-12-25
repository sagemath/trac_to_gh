# Issue 5415: wrong definition of multifactorial?

archive/issues_005415.json:
```json
{
    "body": "Assignee: @robertwb\n\nThe multifactorial method on integers is different than the one at http://mathworld.wolfram.com/Multifactorial.html and http://www.research.att.com/~njas/sequences/A007661; unless there are multiple competing definitions of multifactorial, this is a bug.\n\n(The references give, for example, (5).multifactorial(3) == 10, whereas Sage currently returns 5.)\n\nIssue created by migration from https://trac.sagemath.org/ticket/5415\n\n",
    "created_at": "2009-03-01T22:56:37Z",
    "labels": [
        "component: basic arithmetic",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-8.0",
    "title": "wrong definition of multifactorial?",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5415",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: @robertwb

The multifactorial method on integers is different than the one at http://mathworld.wolfram.com/Multifactorial.html and http://www.research.att.com/~njas/sequences/A007661; unless there are multiple competing definitions of multifactorial, this is a bug.

(The references give, for example, (5).multifactorial(3) == 10, whereas Sage currently returns 5.)

Issue created by migration from https://trac.sagemath.org/ticket/5415





---

archive/issue_comments_041798.json:
```json
{
    "body": "Better luck in Sage 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-02T06:40:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41798",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Better luck in Sage 3.4.1.

Cheers,

Michael



---

archive/issue_comments_041799.json:
```json
{
    "body": "I think the problem is that not enough factors are included.  Actually, there are two problems: in the base case, it should return n, not 1; that is, make this change:\n\n```\n         # base case\n         if 0 < n < k:\n-            return ONE\n+            return n\n```\n\nAfter making this change, I'm still getting the wrong answers for `a.multifactorial(3)` whenever a is congruent to 2 mod 3 (except for a=2), and for `a.multifactorial(4)` whenever a is congruent to 2 or 3 mod 4 (except for a=2,3).  It seems that not enough factors are used; for example, 10.multifactorial(4) should be 10 x 6 x 2 = 120, but Sage computes it as 10 x 6 = 60.\n\nIf we fix this, we can put in doctests like the following:\n\n```\nsage: L = sloane_sequence(6882)[2]  # optional - internet\nSearching Sloane's online database...\nsage: all([Integer(a).multifactorial(2) == L[a] for a in range(1,20)])    # optional - internet\nTrue\n```\n",
    "created_at": "2009-07-22T02:12:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41799",
    "user": "https://github.com/jhpalmieri"
}
```

I think the problem is that not enough factors are included.  Actually, there are two problems: in the base case, it should return n, not 1; that is, make this change:

```
         # base case
         if 0 < n < k:
-            return ONE
+            return n
```

After making this change, I'm still getting the wrong answers for `a.multifactorial(3)` whenever a is congruent to 2 mod 3 (except for a=2), and for `a.multifactorial(4)` whenever a is congruent to 2 or 3 mod 4 (except for a=2,3).  It seems that not enough factors are used; for example, 10.multifactorial(4) should be 10 x 6 x 2 = 120, but Sage computes it as 10 x 6 = 60.

If we fix this, we can put in doctests like the following:

```
sage: L = sloane_sequence(6882)[2]  # optional - internet
Searching Sloane's online database...
sage: all([Integer(a).multifactorial(2) == L[a] for a in range(1,20)])    # optional - internet
True
```




---

archive/issue_comments_041800.json:
```json
{
    "body": "A careful look at Sloane's functions reveals that the base case is indeed =1, according to his definitions.  I'm not sure if this is standard, but Mathworld doesn't seem to talk about those cases carefully.  On the other hand, Wikipedia [http://en.wikipedia.org/wiki/Factorial#Multifactorials](http://en.wikipedia.org/wiki/Factorial#Multifactorials) suggests that this is somewhat standard.",
    "created_at": "2009-09-29T15:34:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41800",
    "user": "https://github.com/kcrisman"
}
```

A careful look at Sloane's functions reveals that the base case is indeed =1, according to his definitions.  I'm not sure if this is standard, but Mathworld doesn't seem to talk about those cases carefully.  On the other hand, Wikipedia [http://en.wikipedia.org/wiki/Factorial#Multifactorials](http://en.wikipedia.org/wiki/Factorial#Multifactorials) suggests that this is somewhat standard.



---

archive/issue_comments_041801.json:
```json
{
    "body": "Or an even more careful look reveals that Sloane starts at n=0 - my bad.  So there is an inconsistency in the definitions.  Sloane's sequences agree with jhpalmieri, while Sage agrees with Wikipedia.\n\nI'm ccing: the author of multifactorial in Sage, who will hopefully weigh in on what definition is okay.",
    "created_at": "2009-09-29T15:45:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41801",
    "user": "https://github.com/kcrisman"
}
```

Or an even more careful look reveals that Sloane starts at n=0 - my bad.  So there is an inconsistency in the definitions.  Sloane's sequences agree with jhpalmieri, while Sage agrees with Wikipedia.

I'm ccing: the author of multifactorial in Sage, who will hopefully weigh in on what definition is okay.



---

archive/issue_comments_041802.json:
```json
{
    "body": "I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. \n\nI would ask on sage-combinat what the \"right\" definition is, they're more likely to know.",
    "created_at": "2009-09-29T18:18:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41802",
    "user": "https://github.com/robertwb"
}
```

I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. 

I would ask on sage-combinat what the "right" definition is, they're more likely to know.



---

archive/issue_comments_041803.json:
```json
{
    "body": "Can you do that?  I'm not subscribed to them.  Thanks.",
    "created_at": "2009-09-29T18:59:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41803",
    "user": "https://github.com/kcrisman"
}
```

Can you do that?  I'm not subscribed to them.  Thanks.



---

archive/issue_comments_041804.json:
```json
{
    "body": "I would certainly want (5).multifactorial(3) to be 10 and not 5.",
    "created_at": "2009-09-30T05:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41804",
    "user": "https://github.com/dandrake"
}
```

I would certainly want (5).multifactorial(3) to be 10 and not 5.



---

archive/issue_comments_041805.json:
```json
{
    "body": "Replying to [comment:5 robertwb]:\n> I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. \n(I think it was for making sure gamma(3/2) etc. were correct.)\n> \n> I would ask on sage-combinat what the \"right\" definition is, they're more likely to know. \n\nBut one should definitely document that there isn't a universally agreed-upon definition.\n\nCan you indicate what one would change in integer.pyx?   Changing things that seem right yield horrible allocation errors.",
    "created_at": "2009-09-30T17:18:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41805",
    "user": "https://github.com/kcrisman"
}
```

Replying to [comment:5 robertwb]:
> I needed the double factorial for something (I can't even remember what now) so I just wrote this. It sounds like there's several competing definitions, but wikipedia is not necessarily the most authoritative. 
(I think it was for making sure gamma(3/2) etc. were correct.)
> 
> I would ask on sage-combinat what the "right" definition is, they're more likely to know. 

But one should definitely document that there isn't a universally agreed-upon definition.

Can you indicate what one would change in integer.pyx?   Changing things that seem right yield horrible allocation errors.



---

archive/issue_comments_041806.json:
```json
{
    "body": "I have tried to redefine multifactorial function.\nPlease review.\nhttps://github.com/sagemath/sage/pull/52",
    "created_at": "2015-11-02T09:08:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41806",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

I have tried to redefine multifactorial function.
Please review.
https://github.com/sagemath/sage/pull/52



---

archive/issue_comments_041807.json:
```json
{
    "body": "Replying to [comment:14 prateek.cs14]:\n> I have tried to redefine multifactorial function.\n> Please review.\n> https://github.com/sagemath/sage/pull/52\n\nA few notes:\n- Python is notoriously (and if you believe some of Guido's commentary basicaly intentionally so) bad at recursion, so you should avoid it unless your really need it. Here you don't (and the current implementation carefully avoids deep recursion)\n- The current implementation does quite a bit of balancing of factors to ensure good multiplication performance. From what I see on your github branch, you've tacked on a new recursion case to what is called \"reflection\" there, essentially making the main body (everything below it) unreachable. That code looks like it's pretty carefully written. If you want to throw it out you should do so (and not just leave it in there as unreachable code) but then you should back up your proposal with some serious timings that show your code performs better under all circumstances.\n- Whenever you make a change like this you should adjust the documentation as well, ensuring that the new behaviour is reflected in the documentation and is properly tested (probably adding some new tests that differentiate between old and new behaviour.\n- Github presently really only is a mirror of the sage repository. It isn't really used for development. So before a change can be considered for inclusion, your change should be uploaded as a git branch here (using the `git-trac` command, probably).\n\nI suspect that the appropriate change to make is in line 3967:\n\n```diff\n-         for i from 1 <= i <= n//k:\n+         for i from 0 <= i <= n//k:\n```\n\nbut I didn't check in detail.",
    "created_at": "2015-11-02T16:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41807",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:14 prateek.cs14]:
> I have tried to redefine multifactorial function.
> Please review.
> https://github.com/sagemath/sage/pull/52

A few notes:
- Python is notoriously (and if you believe some of Guido's commentary basicaly intentionally so) bad at recursion, so you should avoid it unless your really need it. Here you don't (and the current implementation carefully avoids deep recursion)
- The current implementation does quite a bit of balancing of factors to ensure good multiplication performance. From what I see on your github branch, you've tacked on a new recursion case to what is called "reflection" there, essentially making the main body (everything below it) unreachable. That code looks like it's pretty carefully written. If you want to throw it out you should do so (and not just leave it in there as unreachable code) but then you should back up your proposal with some serious timings that show your code performs better under all circumstances.
- Whenever you make a change like this you should adjust the documentation as well, ensuring that the new behaviour is reflected in the documentation and is properly tested (probably adding some new tests that differentiate between old and new behaviour.
- Github presently really only is a mirror of the sage repository. It isn't really used for development. So before a change can be considered for inclusion, your change should be uploaded as a git branch here (using the `git-trac` command, probably).

I suspect that the appropriate change to make is in line 3967:

```diff
-         for i from 1 <= i <= n//k:
+         for i from 0 <= i <= n//k:
```

but I didn't check in detail.



---

archive/issue_comments_041808.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2015-11-02T22:25:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41808",
    "user": "https://github.com/nbruin"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_041809.json:
```json
{
    "body": "Thanks nbruin.\nPlease review the changes made.\nhttps://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c",
    "created_at": "2015-11-04T11:02:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41809",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

Thanks nbruin.
Please review the changes made.
https://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c



---

archive/issue_comments_041810.json:
```json
{
    "body": "Replying to [comment:17 prateek.cs14]:\n> Thanks nbruin.\n> Please review the changes made.\n> https://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c\n\nCurrently, the code is nicely interruptable with CTRL-C if a particularly long computation was being done. Does your code have that property? (you stripped out the `sig_on/sig_off`. On the other hand you revert to using (python?) integers instead of using gmp directly, so perhaps interrupts get enabled in that code)\n\nCurrently, the code is taking efforts to balance the size of the factors it was multiplying. This is a well-known technique to improve performance, because it reduces the number of multiplications where a particularly big number is involved (currently there is a 32/64 bit bug in that code, by the way) You strip that out. Do you have data to confirm this is not a problem?\n\nYou may want to try things like\n\n```\nsage: %timeit 10000001.multifactorial(2)\n1 loops, best of 3: 8.47 s per loop\n```\n\nand possibly with larger numbers too. You should compare the current implementation with the new one.",
    "created_at": "2015-11-06T16:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41810",
    "user": "https://github.com/nbruin"
}
```

Replying to [comment:17 prateek.cs14]:
> Thanks nbruin.
> Please review the changes made.
> https://github.com/prateekcs14/sage/commit/2cb944378c97bdad76a053e37d579d492f68d44c

Currently, the code is nicely interruptable with CTRL-C if a particularly long computation was being done. Does your code have that property? (you stripped out the `sig_on/sig_off`. On the other hand you revert to using (python?) integers instead of using gmp directly, so perhaps interrupts get enabled in that code)

Currently, the code is taking efforts to balance the size of the factors it was multiplying. This is a well-known technique to improve performance, because it reduces the number of multiplications where a particularly big number is involved (currently there is a 32/64 bit bug in that code, by the way) You strip that out. Do you have data to confirm this is not a problem?

You may want to try things like

```
sage: %timeit 10000001.multifactorial(2)
1 loops, best of 3: 8.47 s per loop
```

and possibly with larger numbers too. You should compare the current implementation with the new one.



---

archive/issue_comments_041811.json:
```json
{
    "body": "Please review the changes made.I increased the sub_products by 1 and set i in k*i+residue from 0.\nhttps://github.com/sagemath/sage/commit/8447058f8bb7f017bdefd7086300c4fc3b46ff21",
    "created_at": "2015-12-05T09:38:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41811",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

Please review the changes made.I increased the sub_products by 1 and set i in k*i+residue from 0.
https://github.com/sagemath/sage/commit/8447058f8bb7f017bdefd7086300c4fc3b46ff21



---

archive/issue_comments_041812.json:
```json
{
    "body": "Changing assignee from @robertwb to prateek.cs14.",
    "created_at": "2015-12-10T09:50:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41812",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

Changing assignee from @robertwb to prateek.cs14.



---

archive/issue_comments_041813.json:
```json
{
    "body": "Remove assignee prateek.cs14.",
    "created_at": "2015-12-10T09:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41813",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

Remove assignee prateek.cs14.



---

archive/issue_comments_041814.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-12T07:54:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41814",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_041815.json:
```json
{
    "body": "Congratulations on getting a branch attached. Todo list:\n- make sure documentation is changed to reflect new behaviour and include doctests that confirm it\n- clean up your branch: as you can see in the diffs: `52 files changed, 7057 insertions, 5 deletions`. That's due to your \"Merge\" commit.\n\nSince the intended change only touches 4 lines, it's probably easier to start with a fresh copy of current \"develop\", make the edits. and commit that. Then you need no merging at all.",
    "created_at": "2015-12-12T17:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41815",
    "user": "https://github.com/nbruin"
}
```

Congratulations on getting a branch attached. Todo list:
- make sure documentation is changed to reflect new behaviour and include doctests that confirm it
- clean up your branch: as you can see in the diffs: `52 files changed, 7057 insertions, 5 deletions`. That's due to your "Merge" commit.

Since the intended change only touches 4 lines, it's probably easier to start with a fresh copy of current "develop", make the edits. and commit that. Then you need no merging at all.



---

archive/issue_comments_041816.json:
```json
{
    "body": "Changing status from needs_info to needs_work.",
    "created_at": "2015-12-12T17:16:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41816",
    "user": "https://github.com/nbruin"
}
```

Changing status from needs_info to needs_work.



---

archive/issue_comments_041817.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-12-15T14:47:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41817",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_041818.json:
```json
{
    "body": "Your indentation is not really working well in your doctests - follow the developer guide and other code.  (Ask if you need help!)  I also agree with Nils' comments.",
    "created_at": "2015-12-17T03:50:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41818",
    "user": "https://github.com/kcrisman"
}
```

Your indentation is not really working well in your doctests - follow the developer guide and other code.  (Ask if you need help!)  I also agree with Nils' comments.



---

archive/issue_comments_041819.json:
```json
{
    "body": "Also note that, as was remarked previously, the original behaviour of multifactorial was consistent with the description in its documentation. So, by changing the behaviour but not the documentation you are basically introducing a bug. Ideally you'd include a reference to a literature source to document which convention you are following, along with a description of what the routine in sage does.",
    "created_at": "2015-12-17T05:09:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41819",
    "user": "https://github.com/nbruin"
}
```

Also note that, as was remarked previously, the original behaviour of multifactorial was consistent with the description in its documentation. So, by changing the behaviour but not the documentation you are basically introducing a bug. Ideally you'd include a reference to a literature source to document which convention you are following, along with a description of what the routine in sage does.



---

archive/issue_comments_041820.json:
```json
{
    "body": "Can I change the definition to \n\" Computes the k-th factorial `n!^{(k)}` of self. For k=1\n  this is the standard factorial, and for k greater than one it is\n  the product of every k-th terms down from self to the smallest possible positive integer. \n  The recursive definition is used to extend this function to the negative integers.\"\nIs this look fine ?",
    "created_at": "2015-12-17T14:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41820",
    "user": "https://trac.sagemath.org/admin/accounts/users/prateek.cs14"
}
```

Can I change the definition to 
" Computes the k-th factorial `n!^{(k)}` of self. For k=1
  this is the standard factorial, and for k greater than one it is
  the product of every k-th terms down from self to the smallest possible positive integer. 
  The recursive definition is used to extend this function to the negative integers."
Is this look fine ?



---

archive/issue_comments_041821.json:
```json
{
    "body": "Some people have complained about using \"self\" in the docstring, and they have a point: in the call\n`10.multifactorial(3)` there is never any mention of \"self\". I think it can be avoided here. Your description in words is pretty good, but requires careful reading to pry out the base cases. That might be difficult for non-native speakers. Perhaps\n\n```\nReturns the k-th multifactorial.\n\nThe k-th multifactorial n, denoted by n!^{(k)}, as implemented in Sage\n is defined by\n\nn!^{(k)} = n for 1 <= n < k and\nn!^{(k)} = n * ( (n-k)^{(k)} for n >= k\n\nThe recursive definition is used to extend this function to the negative\nintegers.\n```\n\n\nYou'd have to figure out how to ensure that the formulas are rendered acceptably in all output formats of the sage documentation, though.\n\nThat said, your proposal is in the style of the current docstring, so I don't think a positive review would be held back by it.\n\nNote that one of the doctests illustrates the behaviour:\n\n```\n      sage: 23.multifactorial(2)\n      316234143225\n      sage: prod([1..23, step=2])\n      316234143225\n```\n\nIt would be very instructive if you would change the parameters there to a case that distinguishes between the old and the new behaviour.",
    "created_at": "2015-12-17T18:18:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41821",
    "user": "https://github.com/nbruin"
}
```

Some people have complained about using "self" in the docstring, and they have a point: in the call
`10.multifactorial(3)` there is never any mention of "self". I think it can be avoided here. Your description in words is pretty good, but requires careful reading to pry out the base cases. That might be difficult for non-native speakers. Perhaps

```
Returns the k-th multifactorial.

The k-th multifactorial n, denoted by n!^{(k)}, as implemented in Sage
 is defined by

n!^{(k)} = n for 1 <= n < k and
n!^{(k)} = n * ( (n-k)^{(k)} for n >= k

The recursive definition is used to extend this function to the negative
integers.
```


You'd have to figure out how to ensure that the formulas are rendered acceptably in all output formats of the sage documentation, though.

That said, your proposal is in the style of the current docstring, so I don't think a positive review would be held back by it.

Note that one of the doctests illustrates the behaviour:

```
      sage: 23.multifactorial(2)
      316234143225
      sage: prod([1..23, step=2])
      316234143225
```

It would be very instructive if you would change the parameters there to a case that distinguishes between the old and the new behaviour.



---

archive/issue_comments_041822.json:
```json
{
    "body": "Looks like this ticket has been abandoned again.",
    "created_at": "2016-01-07T22:35:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41822",
    "user": "https://github.com/nbruin"
}
```

Looks like this ticket has been abandoned again.



---

archive/issue_comments_041823.json:
```json
{
    "body": "Set assignee to iconjack.",
    "created_at": "2016-08-16T06:46:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41823",
    "user": "https://trac.sagemath.org/admin/accounts/users/iconjack"
}
```

Set assignee to iconjack.



---

archive/issue_comments_041824.json:
```json
{
    "body": "The multifactorial implementation is optimized to limit large multiplications by computing e.g.  ((a*b)*(c*d))*((e*f)*(g*h)) instead of (((((((a*b)*c)*d)*e)*f)*g)*h). It's a little tricky, using bit patterns of the index to fold the multiplications, rather than doing it recursively. As others noted, there was an off-by-one error (two actually), which caused 5.factorial(3) to eval to 5 rather than 10.\n\nA different bug was that for example 11.multifactorial(17) was returning 1 instead of 11.\n\nWStein suggested using the already-existing prod function that already implements this balanced multiplication. However, prod is more general, not just integers. The current multifactorial uses GMP's integer functions, and may be faster. \n\nIn the long run, I think that multifactorial, prod, balanced_list_prod, and interator_prod should be refactored, but since this is my first commit, I've decided to simply fix the bugs addressed in this ticket. There's another bug, related to non-integer values being passed in, but I'll make another ticket for that.\n\nAlso added a test case.",
    "created_at": "2016-08-17T01:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41824",
    "user": "https://trac.sagemath.org/admin/accounts/users/iconjack"
}
```

The multifactorial implementation is optimized to limit large multiplications by computing e.g.  ((a*b)*(c*d))*((e*f)*(g*h)) instead of (((((((a*b)*c)*d)*e)*f)*g)*h). It's a little tricky, using bit patterns of the index to fold the multiplications, rather than doing it recursively. As others noted, there was an off-by-one error (two actually), which caused 5.factorial(3) to eval to 5 rather than 10.

A different bug was that for example 11.multifactorial(17) was returning 1 instead of 11.

WStein suggested using the already-existing prod function that already implements this balanced multiplication. However, prod is more general, not just integers. The current multifactorial uses GMP's integer functions, and may be faster. 

In the long run, I think that multifactorial, prod, balanced_list_prod, and interator_prod should be refactored, but since this is my first commit, I've decided to simply fix the bugs addressed in this ticket. There's another bug, related to non-integer values being passed in, but I'll make another ticket for that.

Also added a test case.



---

archive/issue_comments_041825.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-08-17T01:37:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41825",
    "user": "https://trac.sagemath.org/admin/accounts/users/iconjack"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041826.json:
```json
{
    "body": "It seems your branch does not exist. Don't you use git-trac as in the documentation?",
    "created_at": "2016-08-17T07:57:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41826",
    "user": "https://github.com/rwst"
}
```

It seems your branch does not exist. Don't you use git-trac as in the documentation?



---

archive/issue_comments_041827.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-08-18T03:54:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41827",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_041828.json:
```json
{
    "body": "Do you know why `residue` is not declared as `cdef int`?",
    "created_at": "2016-09-19T06:06:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41828",
    "user": "https://github.com/videlec"
}
```

Do you know why `residue` is not declared as `cdef int`?



---

archive/issue_comments_041829.json:
```json
{
    "body": "Replying to [comment:38 vdelecroix]:\n> Do you know why `residue` is not declared as `cdef int`?\n\nNo, I didn't change that line. I'll change it to cdef int and test but for now I'd like to get this change reviewed and committed.",
    "created_at": "2016-09-20T00:48:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41829",
    "user": "https://trac.sagemath.org/admin/accounts/users/iconjack"
}
```

Replying to [comment:38 vdelecroix]:
> Do you know why `residue` is not declared as `cdef int`?

No, I didn't change that line. I'll change it to cdef int and test but for now I'd like to get this change reviewed and committed.



---

archive/issue_comments_041830.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2016-09-21T06:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41830",
    "user": "https://github.com/videlec"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_041831.json:
```json
{
    "body": "Your changes look good. Two small things\n\n1. add your name in the \"Authors\" field of the ticket\n\n2. Add the following doctest in a `TESTS` block\n\n```\nsage: for a in range(1,20):\n....:     for b in range(1,20):\n....:         assert ZZ(a).multifactorial(b) == prod(x for x in range(a,0,-b))\n```\n",
    "created_at": "2016-09-21T06:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41831",
    "user": "https://github.com/videlec"
}
```

Your changes look good. Two small things

1. add your name in the "Authors" field of the ticket

2. Add the following doctest in a `TESTS` block

```
sage: for a in range(1,20):
....:     for b in range(1,20):
....:         assert ZZ(a).multifactorial(b) == prod(x for x in range(a,0,-b))
```




---

archive/issue_comments_041832.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2017-05-24T20:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41832",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_041833.json:
```json
{
    "body": "New commits:",
    "created_at": "2017-05-24T20:19:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41833",
    "user": "https://github.com/fchapoton"
}
```

New commits:



---

archive/issue_comments_041834.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-05-26T06:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41834",
    "user": "https://github.com/fchapoton"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_041835.json:
```json
{
    "body": "ok, this passes all tests. I am setting to positive.",
    "created_at": "2017-05-26T06:19:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41835",
    "user": "https://github.com/fchapoton"
}
```

ok, this passes all tests. I am setting to positive.



---

archive/issue_events_005672.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2017-05-27T23:42:49Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5415#event-5672"
}
```



---

archive/issue_comments_041836.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-05-27T23:42:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5415",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5415#issuecomment-41836",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
