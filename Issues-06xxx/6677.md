# Issue 6677: [with patch, positive review] Sequence doesn't know how to typeset itself

archive/issues_006677.json:
```json
{
    "body": "Assignee: @burcin\n\nIt seems that Sequence objects forgot how to typeset themselves somewhere between 3.4.2 and 4.1.\n\nIn 3.4.2:\n\n```\nsage: res = solve(x^2-2,x)\nsage: latex(res)\n\n\\left[x  =  -\\sqrt{ 2 }, \n x  =  \\sqrt{ 2 }\\right]\n```\n\nIn 4.1:\n\n```\nsage: latex(res)\n\n\\text{[\nx == -sqrt(2),\nx == sqrt(2)\n]}\nsage: latex(res[0])\nx = -\\sqrt{2}\n```\n\nAttached patch adds a `_latex_` method to `sage.structure.sequence.Sequence`.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6677\n\n",
    "closed_at": "2009-08-25T04:29:52Z",
    "created_at": "2009-08-06T11:49:04Z",
    "labels": [
        "component: misc",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] Sequence doesn't know how to typeset itself",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6677",
    "user": "https://github.com/burcin"
}
```
Assignee: @burcin

It seems that Sequence objects forgot how to typeset themselves somewhere between 3.4.2 and 4.1.

In 3.4.2:

```
sage: res = solve(x^2-2,x)
sage: latex(res)

\left[x  =  -\sqrt{ 2 }, 
 x  =  \sqrt{ 2 }\right]
```

In 4.1:

```
sage: latex(res)

\text{[
x == -sqrt(2),
x == sqrt(2)
]}
sage: latex(res[0])
x = -\sqrt{2}
```

Attached patch adds a `_latex_` method to `sage.structure.sequence.Sequence`.

Issue created by migration from https://trac.sagemath.org/ticket/6677





---

archive/issue_comments_054776.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-08-06T12:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54776",
    "user": "https://github.com/burcin"
}
```

Changing status from new to assigned.



---

archive/issue_comments_054777.json:
```json
{
    "body": "Trac doesn't let me upload the patch. Here it is if anybody wants to review it in the meantime:\n\nhttp://sage.math.washington.edu/home/burcin/trac_6677-sequence_latex.patch",
    "created_at": "2009-08-06T12:03:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54777",
    "user": "https://github.com/burcin"
}
```

Trac doesn't let me upload the patch. Here it is if anybody wants to review it in the meantime:

http://sage.math.washington.edu/home/burcin/trac_6677-sequence_latex.patch



---

archive/issue_comments_054778.json:
```json
{
    "body": "Attachment [trac_6677-sequence_latex.patch](tarball://root/attachments/some-uuid/ticket6677/trac_6677-sequence_latex.patch) by @burcin created at 2009-08-09 19:50:46",
    "created_at": "2009-08-09T19:50:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54778",
    "user": "https://github.com/burcin"
}
```

Attachment [trac_6677-sequence_latex.patch](tarball://root/attachments/some-uuid/ticket6677/trac_6677-sequence_latex.patch) by @burcin created at 2009-08-09 19:50:46



---

archive/issue_comments_054779.json:
```json
{
    "body": "Okay, I see why this used to work and doesn't anymore: we used to test elements when formatting for LaTeX using `isinstance(x, list)`, and sequences returned True for this.  Now we test using `type(x)` and looking it up in a dictionary, and there is no entry for \"sage.structure.sequence.Sequence\".  The patch here solves the problem for sequences and includes a doctest.  I have a trivial referee's patch (adds 'r' to the triple quotes at the beginning of the docstring, since there are backslashes in it).",
    "created_at": "2009-08-20T21:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54779",
    "user": "https://github.com/jhpalmieri"
}
```

Okay, I see why this used to work and doesn't anymore: we used to test elements when formatting for LaTeX using `isinstance(x, list)`, and sequences returned True for this.  Now we test using `type(x)` and looking it up in a dictionary, and there is no entry for "sage.structure.sequence.Sequence".  The patch here solves the problem for sequences and includes a doctest.  I have a trivial referee's patch (adds 'r' to the triple quotes at the beginning of the docstring, since there are backslashes in it).



---

archive/issue_comments_054780.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2009-08-20T21:06:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54780",
    "user": "https://github.com/jhpalmieri"
}
```

Changing priority from major to minor.



---

archive/issue_comments_054781.json:
```json
{
    "body": "Attachment [trac_6677-referee.patch](tarball://root/attachments/some-uuid/ticket6677/trac_6677-referee.patch) by @jhpalmieri created at 2009-08-20 21:06:42\n\napply on top of the other patch",
    "created_at": "2009-08-20T21:06:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54781",
    "user": "https://github.com/jhpalmieri"
}
```

Attachment [trac_6677-referee.patch](tarball://root/attachments/some-uuid/ticket6677/trac_6677-referee.patch) by @jhpalmieri created at 2009-08-20 21:06:42

apply on top of the other patch



---

archive/issue_comments_054782.json:
```json
{
    "body": "Merged both patches.",
    "created_at": "2009-08-25T04:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54782",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged both patches.



---

archive/issue_events_015750.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-25T04:29:52Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6677#event-15750"
}
```



---

archive/issue_comments_054783.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-25T04:29:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6677",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6677#issuecomment-54783",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed
