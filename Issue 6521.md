# Issue 6521: replace .copy() with .__copy__() in matrix/matrix0.pyx

archive/issues_006521.json:
```json
{
    "body": "Assignee: was\n\nSee also #111, where this originates.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6521\n\n",
    "created_at": "2009-07-13T10:20:55Z",
    "labels": [
        "user interface",
        "minor",
        "enhancement"
    ],
    "title": "replace .copy() with .__copy__() in matrix/matrix0.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6521",
    "user": "AlexGhitza"
}
```
Assignee: was

See also #111, where this originates.


Issue created by migration from https://trac.sagemath.org/ticket/6521





---

archive/issue_comments_053164.json:
```json
{
    "body": "Based on 4.1.1",
    "created_at": "2009-08-26T19:41:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53164",
    "user": "kcrisman"
}
```

Based on 4.1.1



---

archive/issue_comments_053165.json:
```json
{
    "body": "Attachment [trac_6521-copy-matrix.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-copy-matrix.patch) by kcrisman created at 2009-08-26 19:42:58\n\nThis passed all doctests in sage.matrix, sage.modules, and sage.groups.matrix_gps, so hopefully I got all of them.",
    "created_at": "2009-08-26T19:42:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53165",
    "user": "kcrisman"
}
```

Attachment [trac_6521-copy-matrix.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-copy-matrix.patch) by kcrisman created at 2009-08-26 19:42:58

This passed all doctests in sage.matrix, sage.modules, and sage.groups.matrix_gps, so hopefully I got all of them.



---

archive/issue_comments_053166.json:
```json
{
    "body": "Is there a deprecation warning now on .copy()?  I didn't see one on this patch.",
    "created_at": "2009-09-15T04:39:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53166",
    "user": "jason"
}
```

Is there a deprecation warning now on .copy()?  I didn't see one on this patch.



---

archive/issue_comments_053167.json:
```json
{
    "body": "Replying to [comment:2 jason]:\n> Is there a deprecation warning now on .copy()?  I didn't see one on this patch.\nDoes there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?",
    "created_at": "2009-09-15T12:14:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53167",
    "user": "kcrisman"
}
```

Replying to [comment:2 jason]:
> Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?



---

archive/issue_comments_053168.json:
```json
{
    "body": "Replying to [comment:3 kcrisman]:\n> Replying to [comment:2 jason]:\n> > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.\n> Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  \n\nYes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.",
    "created_at": "2009-09-15T15:11:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53168",
    "user": "jason"
}
```

Replying to [comment:3 kcrisman]:
> Replying to [comment:2 jason]:
> > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
> Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  

Yes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.



---

archive/issue_comments_053169.json:
```json
{
    "body": "Replying to [comment:4 jason]:\n> Replying to [comment:3 kcrisman]:\n> > Replying to [comment:2 jason]:\n> > > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.\n> > Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  \n> \n> Yes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.\nUnfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...",
    "created_at": "2009-09-15T15:18:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53169",
    "user": "kcrisman"
}
```

Replying to [comment:4 jason]:
> Replying to [comment:3 kcrisman]:
> > Replying to [comment:2 jason]:
> > > Is there a deprecation warning now on .copy()?  I didn't see one on this patch.
> > Does there need to be?  I don't recall that in #111 there was, but maybe there is supposed to be?  
> 
> Yes, there does need to be a deprecation warning.  #111 was *way* before we had the deprecation warning policy, so that's why it wasn't mentioned there.  Unfortunately, I think a lot of code (including my code!) has used the .copy() function since then that would break.  We need to give us poor folks a warning that things are changing.
Unfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...



---

archive/issue_comments_053170.json:
```json
{
    "body": "Replying to [comment:5 kcrisman]:\n\n> Unfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...\n\nOuch, okay.  I'll post a quick patch to this ticket (since I know at least some of my stuff will break) and open up a follow-up ticket for the rest of the stuff in #111.",
    "created_at": "2009-09-15T15:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53170",
    "user": "jason"
}
```

Replying to [comment:5 kcrisman]:

> Unfortunately, the patch for #111 was only merged a few weeks ago, and is new in 4.1.1!   That means that you should probably open a followup patch for putting deprecation warnings in for all of those.   And then opening another patch that says to remove them in 6 months...

Ouch, okay.  I'll post a quick patch to this ticket (since I know at least some of my stuff will break) and open up a follow-up ticket for the rest of the stuff in #111.



---

archive/issue_comments_053171.json:
```json
{
    "body": "Attachment [trac_6521-deprecation.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-deprecation.patch) by jason created at 2009-09-15 16:42:07\n\napply on top of previous patch",
    "created_at": "2009-09-15T16:42:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53171",
    "user": "jason"
}
```

Attachment [trac_6521-deprecation.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-deprecation.patch) by jason created at 2009-09-15 16:42:07

apply on top of previous patch



---

archive/issue_comments_053172.json:
```json
{
    "body": "positive review for kcrisman's patch.\n\nkcrisman, can you review my patch?  It adds the deprecation warning.",
    "created_at": "2009-09-15T16:43:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53172",
    "user": "jason"
}
```

positive review for kcrisman's patch.

kcrisman, can you review my patch?  It adds the deprecation warning.



---

archive/issue_comments_053173.json:
```json
{
    "body": "Looks okay, passes relevant tests.  I hadn't seen that doctest:...: thing before, it's good to know about.",
    "created_at": "2009-09-15T17:13:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53173",
    "user": "kcrisman"
}
```

Looks okay, passes relevant tests.  I hadn't seen that doctest:...: thing before, it's good to know about.



---

archive/issue_comments_053174.json:
```json
{
    "body": "I got the following doctest failures. Except for the twist.py related failure, these are all a direct consequence of having deprecated the method `.copy()`.\n\n```\nsage -t -long devel/sage/sage/server/simple/twist.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/simple/twist.py\", line 51:\n    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))\nExpected:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    4\nGot:\n    {\n    \"status\": \"done\",\n    \"files\": [],\n    \"cell_id\": 1\n    }\n    ___S_A_G_E___\n    <BLANKLINE>\n    4\n    \ufffde0\n**********************************************************************\n1 items had failures:\n   1 of  24 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_twist.py\n\t [8.5 s]\n\n<SNIP>\n\nsage -t -long devel/sage/sage/geometry/lattice_polytope.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/geometry/lattice_polytope.py\", line 233:\n    sage: p = LatticePolytope(m, \"A lattice polytope with WRONG vertices\",\n                            compute_vertices=False)\nExpected nothing\nGot:\n    doctest:259: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n**********************************************************************\n1 items had failures:\n   1 of  18 in __main__.example_3\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_lattice_polytope.py\n\t [11.9 s]\n\n<SNIP>\n\nsage -t -long devel/sage/sage/plot/plot3d/base.pyx\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/plot/plot3d/base.pyx\", line 1509:\n    sage: T.get_matrix()\nExpected:\n    [100.0   0.0   0.0   0.0]\n    [  0.0 100.0   0.0   0.0]\n    [  0.0   0.0 100.0   0.0]\n    [  0.0   0.0   0.0   1.0]\nGot:\n    doctest:1172: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n    [100.0   0.0   0.0   0.0]\n    [  0.0 100.0   0.0   0.0]\n    [  0.0   0.0 100.0   0.0]\n    [  0.0   0.0   0.0   1.0]\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_55\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_base.py\n\t [8.0 s]\n\t \n<SNIP>\n\nsage -t -long devel/sage/sage/crypto/mq/sbox.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py\", line 420:\n    sage: S.maximal_difference_probability_absolute()\nExpected:\n    2\nGot:\n    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n    2\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py\", line 440:\n    sage: S.maximal_difference_probability()\nExpected:\n    0.25\nGot:\n    doctest:443: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n    0.25\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py\", line 518:\n    sage: S.maximal_linear_bias_absolute()\nExpected:\n    2\nGot:\n    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n    2\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py\", line 533:\n    sage: S.maximal_linear_bias_relative()\nExpected:\n    0.25\nGot:\n    doctest:536: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)\n    0.25\n**********************************************************************\n4 items had failures:\n   1 of   4 in __main__.example_14\n   1 of   4 in __main__.example_15\n   1 of   4 in __main__.example_17\n   1 of   4 in __main__.example_18\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_sbox.py\n\t [3.0 s]\n```\n",
    "created_at": "2009-09-16T00:25:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53174",
    "user": "mvngu"
}
```

I got the following doctest failures. Except for the twist.py related failure, these are all a direct consequence of having deprecated the method `.copy()`.

```
sage -t -long devel/sage/sage/server/simple/twist.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Expected:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    4
Got:
    {
    "status": "done",
    "files": [],
    "cell_id": 1
    }
    ___S_A_G_E___
    <BLANKLINE>
    4
    �e0
**********************************************************************
1 items had failures:
   1 of  24 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_twist.py
	 [8.5 s]

<SNIP>

sage -t -long devel/sage/sage/geometry/lattice_polytope.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/geometry/lattice_polytope.py", line 233:
    sage: p = LatticePolytope(m, "A lattice polytope with WRONG vertices",
                            compute_vertices=False)
Expected nothing
Got:
    doctest:259: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
**********************************************************************
1 items had failures:
   1 of  18 in __main__.example_3
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_lattice_polytope.py
	 [11.9 s]

<SNIP>

sage -t -long devel/sage/sage/plot/plot3d/base.pyx
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/plot/plot3d/base.pyx", line 1509:
    sage: T.get_matrix()
Expected:
    [100.0   0.0   0.0   0.0]
    [  0.0 100.0   0.0   0.0]
    [  0.0   0.0 100.0   0.0]
    [  0.0   0.0   0.0   1.0]
Got:
    doctest:1172: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    [100.0   0.0   0.0   0.0]
    [  0.0 100.0   0.0   0.0]
    [  0.0   0.0 100.0   0.0]
    [  0.0   0.0   0.0   1.0]
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_55
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_base.py
	 [8.0 s]
	 
<SNIP>

sage -t -long devel/sage/sage/crypto/mq/sbox.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 420:
    sage: S.maximal_difference_probability_absolute()
Expected:
    2
Got:
    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    2
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 440:
    sage: S.maximal_difference_probability()
Expected:
    0.25
Got:
    doctest:443: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    0.25
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 518:
    sage: S.maximal_linear_bias_absolute()
Expected:
    2
Got:
    doctest:1: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    2
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha1/devel/sage-main/sage/crypto/mq/sbox.py", line 533:
    sage: S.maximal_linear_bias_relative()
Expected:
    0.25
Got:
    doctest:536: DeprecationWarning: the .copy() method is deprecated; please use the copy() function instead, for example, copy(M)
    0.25
**********************************************************************
4 items had failures:
   1 of   4 in __main__.example_14
   1 of   4 in __main__.example_15
   1 of   4 in __main__.example_17
   1 of   4 in __main__.example_18
***Test Failed*** 4 failures.
For whitespace errors, see the file /scratch/mvngu/release/sage-4.1.2.alpha1/tmp/.doctest_sbox.py
	 [3.0 s]
```




---

archive/issue_comments_053175.json:
```json
{
    "body": "Attachment [trac_6521-deprecation-fixes.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-deprecation-fixes.patch) by jason created at 2009-09-17 08:39:32\n\napply on top of previous patches",
    "created_at": "2009-09-17T08:39:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53175",
    "user": "jason"
}
```

Attachment [trac_6521-deprecation-fixes.patch](tarball://root/attachments/some-uuid/ticket6521/trac_6521-deprecation-fixes.patch) by jason created at 2009-09-17 08:39:32

apply on top of previous patches



---

archive/issue_comments_053176.json:
```json
{
    "body": "The -fixes.patch should take care of all of those doctest failures.",
    "created_at": "2009-09-17T08:40:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53176",
    "user": "jason"
}
```

The -fixes.patch should take care of all of those doctest failures.



---

archive/issue_comments_053177.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-17T10:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53177",
    "user": "mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_053178.json:
```json
{
    "body": "Merged patches in this order:\n\n1. `trac_6521-copy-matrix.patch`\n2. `trac_6521-deprecation.patch`\n3. `trac_6521-deprecation-fixes.patch`\n\nAll doctests pass.",
    "created_at": "2009-09-17T10:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6521",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6521#issuecomment-53178",
    "user": "mvngu"
}
```

Merged patches in this order:

1. `trac_6521-copy-matrix.patch`
2. `trac_6521-deprecation.patch`
3. `trac_6521-deprecation-fixes.patch`

All doctests pass.
