# Issue 8790: improve doctest coverage of logic/logic.py

archive/issues_008790.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @rwst\n\nKeywords: beginner doctest documentation\n\nAs the subject says. Currently, the coverage of `sage/logic/logic.py` in Sage 4.4 is:\n\n```\n[mvngu@sage sage-4.4]$ ./sage -coverage devel/sage-main/sage/logic/logic.py \n----------------------------------------------------------------------\ndevel/sage-main/sage/logic/logic.py\nERROR: Please add a `TestSuite(s).run()` doctest.\nSCORE devel/sage-main/sage/logic/logic.py: 16% (3 of 18)\n\nMissing documentation:\n * combine(self, statement1, statement2):   see #15262\n * simplify(self, table):\n * prove(self, statement):\n\n\nMissing doctests:\n * get_bit(x, c):\n * eval(toks):\n * eval_ltor_toks(lrtoks):\n * reduce_bins(lrtoks):\n * reduce_monos(lrtoks):\n * eval_mon_op(args):\n * eval_bin_op(args):\n * eval_and_op(lval, rval):\n * eval_or_op(lval, rval):\n * eval_ifthen_op(lval, rval):\n * eval_iff_op(lval, rval):\n * tokenize(s, toks):\n```\nThis needs to be coordinated with #8797.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8790\n\n",
    "closed_at": "2014-06-23T19:16:25Z",
    "created_at": "2010-04-28T04:35:34Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "improve doctest coverage of logic/logic.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8790",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: mvngu

CC:  @rwst

Keywords: beginner doctest documentation

As the subject says. Currently, the coverage of `sage/logic/logic.py` in Sage 4.4 is:

```
[mvngu@sage sage-4.4]$ ./sage -coverage devel/sage-main/sage/logic/logic.py 
----------------------------------------------------------------------
devel/sage-main/sage/logic/logic.py
ERROR: Please add a `TestSuite(s).run()` doctest.
SCORE devel/sage-main/sage/logic/logic.py: 16% (3 of 18)

Missing documentation:
 * combine(self, statement1, statement2):   see #15262
 * simplify(self, table):
 * prove(self, statement):


Missing doctests:
 * get_bit(x, c):
 * eval(toks):
 * eval_ltor_toks(lrtoks):
 * reduce_bins(lrtoks):
 * reduce_monos(lrtoks):
 * eval_mon_op(args):
 * eval_bin_op(args):
 * eval_and_op(lval, rval):
 * eval_or_op(lval, rval):
 * eval_ifthen_op(lval, rval):
 * eval_iff_op(lval, rval):
 * tokenize(s, toks):
```
This needs to be coordinated with #8797.

Issue created by migration from https://trac.sagemath.org/ticket/8790





---

archive/issue_comments_080351.json:
```json
{
    "body": "Changing keywords from \"\" to \"beginner doctest documentation\".",
    "created_at": "2013-03-09T07:24:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80351",
    "user": "https://github.com/KPanComputes"
}
```

Changing keywords from "" to "beginner doctest documentation".



---

archive/issue_events_021424.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21424"
}
```



---

archive/issue_comments_080352.json:
```json
{
    "body": "Add docstring to functions `combine`, `simplify` and `prove`.",
    "created_at": "2013-08-25T11:09:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80352",
    "user": "https://github.com/riccardomurri"
}
```

Add docstring to functions `combine`, `simplify` and `prove`.



---

archive/issue_comments_080353.json:
```json
{
    "body": "Attachment [sage-issue-8790-not-implemented.diff](tarball://root/attachments/some-uuid/ticket8790/sage-issue-8790-not-implemented.diff) by @riccardomurri created at 2013-08-25 11:45:19\n\nFunctions `simplify`, `combine` and `prove` are actually not implemented: the code is a stub. Patch ` sage-issue-8790-not-implemented.diff` provides a docstring stating that.\n\nI'm not sure how doctests should be provided here: one could probably change the code to raise a `NotImplemented` exception and look for that in the doctest.",
    "created_at": "2013-08-25T11:45:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80353",
    "user": "https://github.com/riccardomurri"
}
```

Attachment [sage-issue-8790-not-implemented.diff](tarball://root/attachments/some-uuid/ticket8790/sage-issue-8790-not-implemented.diff) by @riccardomurri created at 2013-08-25 11:45:19

Functions `simplify`, `combine` and `prove` are actually not implemented: the code is a stub. Patch ` sage-issue-8790-not-implemented.diff` provides a docstring stating that.

I'm not sure how doctests should be provided here: one could probably change the code to raise a `NotImplemented` exception and look for that in the doctest.



---

archive/issue_comments_080354.json:
```json
{
    "body": "Rename internal functions to start with an underscore",
    "created_at": "2013-08-25T11:46:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80354",
    "user": "https://github.com/riccardomurri"
}
```

Rename internal functions to start with an underscore



---

archive/issue_comments_080355.json:
```json
{
    "body": "Attachment [sage-issue-8790-module-private-funcs.diff](tarball://root/attachments/some-uuid/ticket8790/sage-issue-8790-module-private-funcs.diff) by @riccardomurri created at 2013-08-25 11:51:49\n\nThe `get_bits`, `eval_*`, `reduce_*` and `tokenize` functions are\nexplictly described as \"for internal use only\".  It is inconvenient to\nprovide a doctest for them, as arguments are the internal\ndata structures used in the `SymbolicLogic` class.  \n\nPatch ` sage-issue-8790-module-private-funcs.diff\u200b`\nrenames the functions to begin with an underscore to make their\nnon-public nature more evident, in the hope to silence the coverage\nwarning.",
    "created_at": "2013-08-25T11:51:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80355",
    "user": "https://github.com/riccardomurri"
}
```

Attachment [sage-issue-8790-module-private-funcs.diff](tarball://root/attachments/some-uuid/ticket8790/sage-issue-8790-module-private-funcs.diff) by @riccardomurri created at 2013-08-25 11:51:49

The `get_bits`, `eval_*`, `reduce_*` and `tokenize` functions are
explictly described as "for internal use only".  It is inconvenient to
provide a doctest for them, as arguments are the internal
data structures used in the `SymbolicLogic` class.  

Patch ` sage-issue-8790-module-private-funcs.diff​`
renames the functions to begin with an underscore to make their
non-public nature more evident, in the hope to silence the coverage
warning.



---

archive/issue_comments_080356.json:
```json
{
    "body": "fix for the combine function #15262",
    "created_at": "2013-10-07T17:20:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80356",
    "user": "https://trac.sagemath.org/admin/accounts/users/LostPw"
}
```

fix for the combine function #15262



---

archive/issue_events_021425.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21425"
}
```



---

archive/issue_events_021426.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21426"
}
```



---

archive/issue_events_021427.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21427"
}
```



---

archive/issue_events_021428.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21428"
}
```



---

archive/issue_events_021429.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-06-22T14:27:26Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21429"
}
```



---

archive/issue_events_021430.json:
```json
{
    "actor": "https://github.com/a-andre",
    "created_at": "2014-06-22T14:27:26Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21430"
}
```



---

archive/issue_comments_080357.json:
```json
{
    "body": "I get\n\n```\n./sage --coverage src/sage/logic/logic.py \n------------------------------------------------------------------------\nSCORE src/sage/logic/logic.py: 100.0% (18 of 18)\n------------------------------------------------------------------------\n```",
    "created_at": "2014-06-22T14:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80357",
    "user": "https://github.com/a-andre"
}
```

I get

```
./sage --coverage src/sage/logic/logic.py 
------------------------------------------------------------------------
SCORE src/sage/logic/logic.py: 100.0% (18 of 18)
------------------------------------------------------------------------
```



---

archive/issue_comments_080358.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-06-22T14:27:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80358",
    "user": "https://github.com/a-andre"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080359.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-06-22T14:36:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80359",
    "user": "https://github.com/rwst"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080360.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2014-06-23T19:16:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8790#issuecomment-80360",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_events_021431.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2014-06-23T19:16:25Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8790",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8790#event-21431"
}
```
