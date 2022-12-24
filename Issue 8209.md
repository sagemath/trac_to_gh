# Issue 8209: make docstring processing available for introspection, and fix mathtt

archive/issues_008209.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mpatel\n\nTwo issues: several docstrings contain `\\mathtt{self`}, and jsMath doesn't recognize this command, so it's not typeset correctly, either with introspection from the notebook or in the reference manual.  Do this in the notebook, for example:\n\n```\nsage: a = 5\nsage: a.is_power_of?\n```\n\nOr look at the docstring for `is_power_of` in sage.rings.integer in the reference manual (assuming you've built the ref manual with the '--jsmath' option).\n\nSecond, several docstrings use dollar signs, and while these are processed correctly for the reference manual (turning `$x=y$` into ``x=y``), they are not dealt with in introspection in the notebook.  Evaluate `sage.categories.g_sets.GSets?`, for example: you'll see `$G$` rather than *G*.\n\nThe attached patch therefore does these things:\n\n- moves the function `process_dollars` from SAGE_ROOT/devel/sage/doc/common/conf.py to SAGE_ROOT/devel/sage/sage/misc/sagedoc.py, where it can be used to format each docstring before displaying it.\n\n- implements a similar function `process_mathtt` which converts `\\mathtt{blah`} to `\\verb|blah|`, which jsMath can handle.  Oh, except on the command line, it just turns `\\mathtt{blah`} to `blah`, which I think is easier to read.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8209\n\n",
    "created_at": "2010-02-07T17:56:20Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.3",
    "title": "make docstring processing available for introspection, and fix mathtt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8209",
    "user": "jhpalmieri"
}
```
Assignee: mvngu

CC:  mpatel

Two issues: several docstrings contain `\mathtt{self`}, and jsMath doesn't recognize this command, so it's not typeset correctly, either with introspection from the notebook or in the reference manual.  Do this in the notebook, for example:

```
sage: a = 5
sage: a.is_power_of?
```

Or look at the docstring for `is_power_of` in sage.rings.integer in the reference manual (assuming you've built the ref manual with the '--jsmath' option).

Second, several docstrings use dollar signs, and while these are processed correctly for the reference manual (turning `$x=y$` into ``x=y``), they are not dealt with in introspection in the notebook.  Evaluate `sage.categories.g_sets.GSets?`, for example: you'll see `$G$` rather than *G*.

The attached patch therefore does these things:

- moves the function `process_dollars` from SAGE_ROOT/devel/sage/doc/common/conf.py to SAGE_ROOT/devel/sage/sage/misc/sagedoc.py, where it can be used to format each docstring before displaying it.

- implements a similar function `process_mathtt` which converts `\mathtt{blah`} to `\verb|blah|`, which jsMath can handle.  Oh, except on the command line, it just turns `\mathtt{blah`} to `blah`, which I think is easier to read.

Issue created by migration from https://trac.sagemath.org/ticket/8209





---

archive/issue_comments_072397.json:
```json
{
    "body": "Attachment [trac_8209-mathtt.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.patch) by jhpalmieri created at 2010-02-07 17:57:19",
    "created_at": "2010-02-07T17:57:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72397",
    "user": "jhpalmieri"
}
```

Attachment [trac_8209-mathtt.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.patch) by jhpalmieri created at 2010-02-07 17:57:19



---

archive/issue_comments_072398.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-07T17:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72398",
    "user": "jhpalmieri"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_072399.json:
```json
{
    "body": "Note: this patch fixes the problem reported in #8196 with tty doc output, thus a (partial)\npositive review for that issue.",
    "created_at": "2010-02-07T21:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72399",
    "user": "zimmerma"
}
```

Note: this patch fixes the problem reported in #8196 with tty doc output, thus a (partial)
positive review for that issue.



---

archive/issue_comments_072400.json:
```json
{
    "body": "Call `process_mathtt` with `embedded=True` in docbuild.  Apply only this patch.  sage repo.",
    "created_at": "2010-02-09T04:16:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72400",
    "user": "mpatel"
}
```

Call `process_mathtt` with `embedded=True` in docbuild.  Apply only this patch.  sage repo.



---

archive/issue_comments_072401.json:
```json
{
    "body": "Attachment [trac_8209-mathtt.2.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.2.patch) by mpatel created at 2010-02-09 04:30:06\n\nShould we call `process_mathtt` with `embedded=True` when building the reference manual?  V2 makes this change, but it's for both jsMath and PNG math modes.  Is that OK?",
    "created_at": "2010-02-09T04:30:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72401",
    "user": "mpatel"
}
```

Attachment [trac_8209-mathtt.2.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.2.patch) by mpatel created at 2010-02-09 04:30:06

Should we call `process_mathtt` with `embedded=True` when building the reference manual?  V2 makes this change, but it's for both jsMath and PNG math modes.  Is that OK?



---

archive/issue_comments_072402.json:
```json
{
    "body": "Good catch about using `embedded=True`.  How about this version: it changes the first line of process_mathtt in conf.py from\n\n```\nif len(docstringlines) > 0:\n```\n\nto\n\n```\nif len(docstringlines) > 0 and 'SAGE_DOC_JSMATH' in os.environ:\n```\n",
    "created_at": "2010-02-09T07:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72402",
    "user": "jhpalmieri"
}
```

Good catch about using `embedded=True`.  How about this version: it changes the first line of process_mathtt in conf.py from

```
if len(docstringlines) > 0:
```

to

```
if len(docstringlines) > 0 and 'SAGE_DOC_JSMATH' in os.environ:
```




---

archive/issue_comments_072403.json:
```json
{
    "body": "Attachment [trac_8209-mathtt.3.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.3.patch) by jhpalmieri created at 2010-02-09 07:07:46\n\napply only this patch (sage repo)",
    "created_at": "2010-02-09T07:07:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72403",
    "user": "jhpalmieri"
}
```

Attachment [trac_8209-mathtt.3.patch](tarball://root/attachments/some-uuid/ticket8209/trac_8209-mathtt.3.patch) by jhpalmieri created at 2010-02-09 07:07:46

apply only this patch (sage repo)



---

archive/issue_comments_072404.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-02-10T14:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72404",
    "user": "mpatel"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_072405.json:
```json
{
    "body": "Oops.  Of course, that's the right way.",
    "created_at": "2010-02-10T14:08:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72405",
    "user": "mpatel"
}
```

Oops.  Of course, that's the right way.



---

archive/issue_comments_072406.json:
```json
{
    "body": "For the record: Applying the patch 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives\n\n```\napplying trac_8209-mathtt.3.patch\npatching file sage/misc/sagedoc.py\nHunk #1 succeeded at 191 with fuzz 1 (offset 2 lines).\nHunk #2 succeeded at 396 with fuzz 2 (offset 2 lines).\n```\n\npossibly because I've haven't yet applied #8161.",
    "created_at": "2010-02-10T15:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72406",
    "user": "mpatel"
}
```

For the record: Applying the patch 4.3.2 + [a long queue](http://trac.sagemath.org/sage_trac/ticket/8186#comment:6) gives

```
applying trac_8209-mathtt.3.patch
patching file sage/misc/sagedoc.py
Hunk #1 succeeded at 191 with fuzz 1 (offset 2 lines).
Hunk #2 succeeded at 396 with fuzz 2 (offset 2 lines).
```

possibly because I've haven't yet applied #8161.



---

archive/issue_comments_072407.json:
```json
{
    "body": "Replying to [comment:6 mpatel]:\n> [...]possibly because I've haven't yet applied #8161.\nYes.",
    "created_at": "2010-02-10T23:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72407",
    "user": "mpatel"
}
```

Replying to [comment:6 mpatel]:
> [...]possibly because I've haven't yet applied #8161.
Yes.



---

archive/issue_comments_072408.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-02-11T14:54:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8209",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8209#issuecomment-72408",
    "user": "mpatel"
}
```

Resolution: fixed
