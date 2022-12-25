# Issue 7716: sage -coverage enhancement

archive/issues_007716.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: coverage\n\nAdds features to the sage-coverage script.\n\n- rewrite for modularity and easier addition of features\n- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.\n- adds option to check cdef'd functions\n- adds option to check docstrings on classes\n- adds option to check for the existence of INPUT block\n- adds option to check that parameters are all listed in the INPUT block.\n- adds option to check for the existence of OUTPUT block\n\nSo that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)\n\nIssue created by migration from https://trac.sagemath.org/ticket/7716\n\n",
    "created_at": "2009-12-17T01:39:31Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.4",
    "title": "sage -coverage enhancement",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7716",
    "user": "https://github.com/roed314"
}
```
Assignee: mvngu

Keywords: coverage

Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
- adds option to check cdef'd functions
- adds option to check docstrings on classes
- adds option to check for the existence of INPUT block
- adds option to check that parameters are all listed in the INPUT block.
- adds option to check for the existence of OUTPUT block

So that we don't bring our coverage level way down, these aren't turned on automatically.  Instead, they can be invoked from the command line by using options ( -cdefs, -classes, -input, -output and -params)

Issue created by migration from https://trac.sagemath.org/ticket/7716





---

archive/issue_comments_066150.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-12-17T01:45:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66150",
    "user": "https://github.com/roed314"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_066151.json:
```json
{
    "body": "What if a function does not return anything, but uses \"return\" to exit from the function in the middle? From looking at the patch it seems to me that it will be reported as \"bad\".",
    "created_at": "2009-12-17T17:02:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66151",
    "user": "https://github.com/novoselt"
}
```

What if a function does not return anything, but uses "return" to exit from the function in the middle? From looking at the patch it seems to me that it will be reported as "bad".



---

archive/issue_comments_066152.json:
```json
{
    "body": "Looks very useful -- but for me it would not apply to a fresh clone of 4.3.rc0.",
    "created_at": "2009-12-17T17:04:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66152",
    "user": "https://github.com/JohnCremona"
}
```

Looks very useful -- but for me it would not apply to a fresh clone of 4.3.rc0.



---

archive/issue_comments_066153.json:
```json
{
    "body": "Overall looks good.  A few comments: It doesn't look like this will detect Sphinx/reST markup for input and output, as described [here](http://sagemath.org/doc/developer/conventions.html#documentation-strings) -- a block like\n\n```\n:param x: the length of the rectangle\n:type x: float\n:param w: the width of the rectangle\n:type w: float\n:return: the area of the rectange\n:rtype: float\n```\nOr am I missing something?\n\nAlso, as I've said on #4323, it takes a certain amount of hubris, or maybe (as mabshoff pointed out) just a strong sense of irony, to put functions with no docstrings into a file like \"sage-coverage\".\n\nFinally, I couldn't get it to apply cleanly, either.  When applying to the scripts repository in 4.3.rc0, I got the message\n\n```\napplying /Users/palmieri/Downloads/7716_coverage.patch\npatching file sage-coverage\nHunk #2 FAILED at 15\n1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej\n```",
    "created_at": "2009-12-17T21:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66153",
    "user": "https://github.com/jhpalmieri"
}
```

Overall looks good.  A few comments: It doesn't look like this will detect Sphinx/reST markup for input and output, as described [here](http://sagemath.org/doc/developer/conventions.html#documentation-strings) -- a block like

```
:param x: the length of the rectangle
:type x: float
:param w: the width of the rectangle
:type w: float
:return: the area of the rectange
:rtype: float
```
Or am I missing something?

Also, as I've said on #4323, it takes a certain amount of hubris, or maybe (as mabshoff pointed out) just a strong sense of irony, to put functions with no docstrings into a file like "sage-coverage".

Finally, I couldn't get it to apply cleanly, either.  When applying to the scripts repository in 4.3.rc0, I got the message

```
applying /Users/palmieri/Downloads/7716_coverage.patch
patching file sage-coverage
Hunk #2 FAILED at 15
1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej
```



---

archive/issue_comments_066154.json:
```json
{
    "body": "New patch, which should address all the concerns so far (and apply against 4.3.rc0 in particular)",
    "created_at": "2009-12-18T00:47:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66154",
    "user": "https://github.com/roed314"
}
```

New patch, which should address all the concerns so far (and apply against 4.3.rc0 in particular)



---

archive/issue_comments_066155.json:
```json
{
    "body": "Changes behavior for functions with underscores beginning and ending the name.  Apply on top of previous patch.",
    "created_at": "2009-12-19T18:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66155",
    "user": "https://github.com/roed314"
}
```

Changes behavior for functions with underscores beginning and ending the name.  Apply on top of previous patch.



---

archive/issue_comments_066156.json:
```json
{
    "body": "Attachment [7716_underscores.patch](tarball://root/attachments/some-uuid/ticket7716/7716_underscores.patch) by @williamstein created at 2009-12-24 07:05:01\n\nI'm declaring a total feature freeze on sage-4.3.",
    "created_at": "2009-12-24T07:05:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66156",
    "user": "https://github.com/williamstein"
}
```

Attachment [7716_underscores.patch](tarball://root/attachments/some-uuid/ticket7716/7716_underscores.patch) by @williamstein created at 2009-12-24 07:05:01

I'm declaring a total feature freeze on sage-4.3.



---

archive/issue_events_018439.json:
```json
{
    "actor": "https://github.com/williamstein",
    "created_at": "2009-12-24T07:05:01Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18439"
}
```



---

archive/issue_comments_066157.json:
```json
{
    "body": "Fails to apply to sage-4.3:\n\n```\nwstein@boxen:~/build/referee/sage-4.3/local/bin$ hgimport http://trac.sagemath.org/sage_trac/attachment/ticket/7716/7716_coverage.patch\n--08:41:18--  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7716/7716_coverage.patch\n           => `7716_coverage.patch'\nResolving trac.sagemath.org... 128.208.160.197\nConnecting to trac.sagemath.org|128.208.160.197|:80... connected.\nHTTP request sent, awaiting response... 200 Ok\nLength: 58,082 (57K) [text/x-diff]\n\n100%[====================================================================>] 58,082        --.--K/s             \n\n08:41:18 (220.36 MB/s) - `7716_coverage.patch' saved [58082/58082]\n\napplying 7716_coverage.patch\npatching file sage-coverage\nHunk #2 FAILED at 15\n1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej\npatching file sage-coverage\nHunk #1 FAILED at 0\nHunk #4 FAILED at 622\n2 out of 4 hunks FAILED -- saving rejects to file sage-coverage.rej\npatching file sage-coverageall\nHunk #1 FAILED at 0\nHunk #2 FAILED at 22\nHunk #3 FAILED at 38\n3 out of 3 hunks FAILED -- saving rejects to file sage-coverageall.rej\nabort: patch failed to apply\n```\n\nMaybe the patch is broken/corrupt?  It starts\n\n```\n# HG changeset patch\n# User David Roe <roed@math.harvard.edu>\n# Date 1261014209 18000\n# Node ID da454b36cda7a92a4cbee40317e86f970a04dd8e\n# Parent  e4aff87d1aa188834f14c6f4643beff69879512f\nAdds features to the sage-coverage script.\n\n- rewrite for modularity and easier addition of features\n...\n```\nthen line 604 is suddenly:\n\n```\n# HG changeset patch\n# User David Roe <roed@math.harvard.edu>\n# Date 1261014209 18000\n# Node ID e5314d3c2ba2b0ec34d8226ee80db4526a8a5678\n# Parent  2c17a7cee6e7b76fe67053f34c20ed7c6c33d7cb\nAdds features to the sage-coverage script.\n\n- rewrite for modularity and easier addition of features\n- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.\n...\n```\n\nwhich involves exactly the same changeset comment and changes to the same file (sage-coverage).\n\nAnyway, I'm pretty confused by this, and can't even referee it.",
    "created_at": "2009-12-31T16:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66157",
    "user": "https://github.com/williamstein"
}
```

Fails to apply to sage-4.3:

```
wstein@boxen:~/build/referee/sage-4.3/local/bin$ hgimport http://trac.sagemath.org/sage_trac/attachment/ticket/7716/7716_coverage.patch
--08:41:18--  http://trac.sagemath.org/sage_trac/raw-attachment/ticket/7716/7716_coverage.patch
           => `7716_coverage.patch'
Resolving trac.sagemath.org... 128.208.160.197
Connecting to trac.sagemath.org|128.208.160.197|:80... connected.
HTTP request sent, awaiting response... 200 Ok
Length: 58,082 (57K) [text/x-diff]

100%[====================================================================>] 58,082        --.--K/s             

08:41:18 (220.36 MB/s) - `7716_coverage.patch' saved [58082/58082]

applying 7716_coverage.patch
patching file sage-coverage
Hunk #2 FAILED at 15
1 out of 3 hunks FAILED -- saving rejects to file sage-coverage.rej
patching file sage-coverage
Hunk #1 FAILED at 0
Hunk #4 FAILED at 622
2 out of 4 hunks FAILED -- saving rejects to file sage-coverage.rej
patching file sage-coverageall
Hunk #1 FAILED at 0
Hunk #2 FAILED at 22
Hunk #3 FAILED at 38
3 out of 3 hunks FAILED -- saving rejects to file sage-coverageall.rej
abort: patch failed to apply
```

Maybe the patch is broken/corrupt?  It starts

```
# HG changeset patch
# User David Roe <roed@math.harvard.edu>
# Date 1261014209 18000
# Node ID da454b36cda7a92a4cbee40317e86f970a04dd8e
# Parent  e4aff87d1aa188834f14c6f4643beff69879512f
Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
...
```
then line 604 is suddenly:

```
# HG changeset patch
# User David Roe <roed@math.harvard.edu>
# Date 1261014209 18000
# Node ID e5314d3c2ba2b0ec34d8226ee80db4526a8a5678
# Parent  2c17a7cee6e7b76fe67053f34c20ed7c6c33d7cb
Adds features to the sage-coverage script.

- rewrite for modularity and easier addition of features
- changes the score of the file to reflect the presence or absence of a TestSuite.run or equivalent test.
...
```

which involves exactly the same changeset comment and changes to the same file (sage-coverage).

Anyway, I'm pretty confused by this, and can't even referee it.



---

archive/issue_comments_066158.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-12-31T16:46:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66158",
    "user": "https://github.com/williamstein"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066159.json:
```json
{
    "body": "Attachment [7716_coverage.patch](tarball://root/attachments/some-uuid/ticket7716/7716_coverage.patch) by @roed314 created at 2010-01-01 00:34:20\n\nYeah, I don't know what that was.  Here's a new patch (against 4.3.rc0) that gets rid of the weird double header problem.  7716_coverage.patch should be applied first, then 7716_underscores.patch\n\nIt doesn't need to be rebased against 4.3, since there are no changes to sage-coverage or sage-coverageall since 4.3.rc0.  William, are you up for reviewing this now that it should apply?",
    "created_at": "2010-01-01T00:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66159",
    "user": "https://github.com/roed314"
}
```

Attachment [7716_coverage.patch](tarball://root/attachments/some-uuid/ticket7716/7716_coverage.patch) by @roed314 created at 2010-01-01 00:34:20

Yeah, I don't know what that was.  Here's a new patch (against 4.3.rc0) that gets rid of the weird double header problem.  7716_coverage.patch should be applied first, then 7716_underscores.patch

It doesn't need to be rebased against 4.3, since there are no changes to sage-coverage or sage-coverageall since 4.3.rc0.  William, are you up for reviewing this now that it should apply?



---

archive/issue_comments_066160.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-01-01T00:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66160",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_066161.json:
```json
{
    "body": "Some issues:\n\n- sage-coverageall doesn't deal with unrecognized options well, since it just parses the output from sage-coverage.  So if you pass an unrecognized option, it ends up saying \"No files in ...\".  Instead of doing\n\n```\n    r = os.popen('sage -coverage %s * | grep SCORE'%opt).readlines()\n```\n we should probably set P to be the process and check its return status before asking for its output.\n\n- the options should work with either one or two hyphens.\n\n- We should have a \"--help\" option for sage-coverage which does the same thing as running sage-coverage with no arguments: print the usage.  I think we should also expand this usage message.\n\nI'm attaching a \"diff\" which makes these changes.  I haven't looked at the rest of the code in detail yet, but I may soon.",
    "created_at": "2011-09-19T21:47:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66161",
    "user": "https://github.com/jhpalmieri"
}
```

Some issues:

- sage-coverageall doesn't deal with unrecognized options well, since it just parses the output from sage-coverage.  So if you pass an unrecognized option, it ends up saying "No files in ...".  Instead of doing

```
    r = os.popen('sage -coverage %s * | grep SCORE'%opt).readlines()
```
 we should probably set P to be the process and check its return status before asking for its output.

- the options should work with either one or two hyphens.

- We should have a "--help" option for sage-coverage which does the same thing as running sage-coverage with no arguments: print the usage.  I think we should also expand this usage message.

I'm attaching a "diff" which makes these changes.  I haven't looked at the rest of the code in detail yet, but I may soon.



---

archive/issue_comments_066162.json:
```json
{
    "body": "Attachment [trac_7716-ref.patch](tarball://root/attachments/some-uuid/ticket7716/trac_7716-ref.patch) by @jhpalmieri created at 2011-10-13 16:59:40\n\napply on top of other patches",
    "created_at": "2011-10-13T16:59:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66162",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_7716-ref.patch](tarball://root/attachments/some-uuid/ticket7716/trac_7716-ref.patch) by @jhpalmieri created at 2011-10-13 16:59:40

apply on top of other patches



---

archive/issue_comments_066163.json:
```json
{
    "body": "Another change to sage-coverage that I want to request (and possibly implement later): it should be able to run on .pxi files.",
    "created_at": "2012-03-02T23:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66163",
    "user": "https://github.com/roed314"
}
```

Another change to sage-coverage that I want to request (and possibly implement later): it should be able to run on .pxi files.



---

archive/issue_comments_066164.json:
```json
{
    "body": "Also #14061 seems to have fixed #8699.",
    "created_at": "2013-02-06T12:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66164",
    "user": "https://github.com/tscrim"
}
```

Also #14061 seems to have fixed #8699.



---

archive/issue_comments_066165.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2013-02-17T20:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66165",
    "user": "https://github.com/roed314"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_066166.json:
```json
{
    "body": "This should be rebased to #14061, which will take some work.",
    "created_at": "2013-02-17T20:45:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7716#issuecomment-66166",
    "user": "https://github.com/roed314"
}
```

This should be rebased to #14061, which will take some work.



---

archive/issue_events_018440.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-4.3.1",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18440"
}
```



---

archive/issue_events_018441.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18441"
}
```



---

archive/issue_events_018442.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18442"
}
```



---

archive/issue_events_018443.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18443"
}
```



---

archive/issue_events_018444.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18444"
}
```



---

archive/issue_events_018445.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18445"
}
```



---

archive/issue_events_018446.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18446"
}
```



---

archive/issue_events_018447.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/7716",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7716#event-18447"
}
```
