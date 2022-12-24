# Issue 9455: Dimensions of eigenspaces for the Atkin-Lehner operator acting on modular forms

archive/issues_009455.json:
```json
{
    "body": "Assignee: craigcitro\n\nCC:  was\n\nThis is a port of David Kohel's MAGMA code to compute dimensions of the eigenspaces for the Atkin-Lehner operators acting on spaces of cusp forms of weight 2 (see here for the original):\n\nhttp://echidna.maths.usyd.edu.au/echidna/dbs/atkin-lehner/index.html\n\nThese methods do not rely on computing explicit bases of newforms, instead using formulae about the ramification points of the Atkin-Lehner operator. \n\nThese functions use the class number method qfbclassno() from Pari/GP.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9455\n\n",
    "created_at": "2010-07-08T15:10:40Z",
    "labels": [
        "modular forms",
        "minor",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-6.9",
    "title": "Dimensions of eigenspaces for the Atkin-Lehner operator acting on modular forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9455",
    "user": "ljpk"
}
```
Assignee: craigcitro

CC:  was

This is a port of David Kohel's MAGMA code to compute dimensions of the eigenspaces for the Atkin-Lehner operators acting on spaces of cusp forms of weight 2 (see here for the original):

http://echidna.maths.usyd.edu.au/echidna/dbs/atkin-lehner/index.html

These methods do not rely on computing explicit bases of newforms, instead using formulae about the ramification points of the Atkin-Lehner operator. 

These functions use the class number method qfbclassno() from Pari/GP.

Issue created by migration from https://trac.sagemath.org/ticket/9455





---

archive/issue_comments_090599.json:
```json
{
    "body": "Attachment [atkin_lehner_decomposition_dimensions.sage](tarball://root/attachments/some-uuid/ticket9455/atkin_lehner_decomposition_dimensions.sage) by ljpk created at 2010-07-09 19:08:16\n\nCode to implement dimensions of Atkin-Lehner eigenspaces for the ModularForms class",
    "created_at": "2010-07-09T19:08:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90599",
    "user": "ljpk"
}
```

Attachment [atkin_lehner_decomposition_dimensions.sage](tarball://root/attachments/some-uuid/ticket9455/atkin_lehner_decomposition_dimensions.sage) by ljpk created at 2010-07-09 19:08:16

Code to implement dimensions of Atkin-Lehner eigenspaces for the ModularForms class



---

archive/issue_comments_090600.json:
```json
{
    "body": "Changing assignee from craigcitro to ljpk.",
    "created_at": "2010-08-11T15:18:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90600",
    "user": "ljpk"
}
```

Changing assignee from craigcitro to ljpk.



---

archive/issue_comments_090601.json:
```json
{
    "body": "Changing assignee from ljpk to craigcitro.",
    "created_at": "2010-08-11T15:18:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90601",
    "user": "ljpk"
}
```

Changing assignee from ljpk to craigcitro.



---

archive/issue_comments_090602.json:
```json
{
    "body": "Attachment [trac_9455_atkin_lehner_dim.patch](tarball://root/attachments/some-uuid/ticket9455/trac_9455_atkin_lehner_dim.patch) by chapoton created at 2013-08-08 19:56:19",
    "created_at": "2013-08-08T19:56:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90602",
    "user": "chapoton"
}
```

Attachment [trac_9455_atkin_lehner_dim.patch](tarball://root/attachments/some-uuid/ticket9455/trac_9455_atkin_lehner_dim.patch) by chapoton created at 2013-08-08 19:56:19



---

archive/issue_comments_090603.json:
```json
{
    "body": "I have tried to maker a clean patch starting with the given file\n\nSome doctests are still failing.\n\nfor the bot: apply only trac_9455_atkin_lehner_dim.patch\u200b",
    "created_at": "2013-08-08T19:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90603",
    "user": "chapoton"
}
```

I have tried to maker a clean patch starting with the given file

Some doctests are still failing.

for the bot: apply only trac_9455_atkin_lehner_dim.patch​



---

archive/issue_comments_090604.json:
```json
{
    "body": "Changing keywords from \"\" to \"atkin lehner\".",
    "created_at": "2013-08-08T19:57:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90604",
    "user": "chapoton"
}
```

Changing keywords from "" to "atkin lehner".



---

archive/issue_comments_090605.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-09T19:53:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90605",
    "user": "chapoton"
}
```

New commits:



---

archive/issue_comments_090606.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2014-11-14T16:09:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90606",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090607.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-18T10:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90607",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090608.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-02-18T10:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90608",
    "user": "chapoton"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_090609.json:
```json
{
    "body": "Now all tests pass. But maybe this is too slow.",
    "created_at": "2015-02-18T10:34:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90609",
    "user": "chapoton"
}
```

Now all tests pass. But maybe this is too slow.



---

archive/issue_comments_090610.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-02-19T11:00:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90610",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090611.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2015-03-22T11:09:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90611",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_090612.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-22T14:05:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90612",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090613.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2015-03-22T15:09:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90613",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090614.json:
```json
{
    "body": "This needs some serious work.\n\n- Most of this new code is added via methods of Gamma0 modular forms space objects. However, these objects can have any weight, but the implementations here only work for weight 2, so you can type something like\n\n```\n sage: ModularForms(1000003, 4).atkin_lehner_eigenspace_dimensions()\n```\n\n and it will silently return wrong output. More importantly, lots of these methods (e.g. `atkin_lehner_ramification`) are computing geometric properties of the underlying modular curves, so they belong in `sage.modular.arithgroup.congroup_gamma0`. Similarly, \"primitive_ideal_number\" should probably be a method of order objects, not a standalone function.\n\n- Many function names are mysterious or downright misleading, e.g. the method `modular_genus_X0` is not actually computing the genus of anything in most cases. \n\n- The documentation is poor. What on earth is the \"(M, R)-old subspace\"? What are \"cyclic ideals\"?  Docstrings for each method should explain what the arguments mean. The docstring for `old_subspace_dimension(self, M, R, w)` does not even mention Atkin--Lehner involutions!\n\n- Why is a line of code in the number fields module (in `absolute_order_from_module_generators`) deleted without explanation?",
    "created_at": "2015-12-04T16:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90614",
    "user": "davidloeffler"
}
```

This needs some serious work.

- Most of this new code is added via methods of Gamma0 modular forms space objects. However, these objects can have any weight, but the implementations here only work for weight 2, so you can type something like

```
 sage: ModularForms(1000003, 4).atkin_lehner_eigenspace_dimensions()
```

 and it will silently return wrong output. More importantly, lots of these methods (e.g. `atkin_lehner_ramification`) are computing geometric properties of the underlying modular curves, so they belong in `sage.modular.arithgroup.congroup_gamma0`. Similarly, "primitive_ideal_number" should probably be a method of order objects, not a standalone function.

- Many function names are mysterious or downright misleading, e.g. the method `modular_genus_X0` is not actually computing the genus of anything in most cases. 

- The documentation is poor. What on earth is the "(M, R)-old subspace"? What are "cyclic ideals"?  Docstrings for each method should explain what the arguments mean. The docstring for `old_subspace_dimension(self, M, R, w)` does not even mention Atkin--Lehner involutions!

- Why is a line of code in the number fields module (in `absolute_order_from_module_generators`) deleted without explanation?



---

archive/issue_comments_090615.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-12-04T16:37:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90615",
    "user": "davidloeffler"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_090616.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-03-01T11:26:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90616",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090617.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-04-13T19:03:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90617",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090618.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2016-07-29T18:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90618",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090619.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2017-03-01T15:05:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90619",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:



---

archive/issue_comments_090620.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. New commits:",
    "created_at": "2018-03-11T19:59:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9455",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9455#issuecomment-90620",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. New commits:
