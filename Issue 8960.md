# Issue 8960: doctest coverage for real_mpfr.pyx

archive/issues_008960.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @robertwb @williamstein\n\nThis patch works on doctest coverage.\n\nIt also changes the latex representation of a real field to indicate the precision and rounding\n\nIssue created by migration from https://trac.sagemath.org/ticket/8960\n\n",
    "created_at": "2010-05-14T09:27:18Z",
    "labels": [
        "component: basic arithmetic"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.4.4",
    "title": "doctest coverage for real_mpfr.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8960",
    "user": "https://github.com/jasongrout"
}
```
Assignee: @aghitza

CC:  @robertwb @williamstein

This patch works on doctest coverage.

It also changes the latex representation of a real field to indicate the precision and rounding

Issue created by migration from https://trac.sagemath.org/ticket/8960





---

archive/issue_events_021878.json:
```json
{
    "actor": "https://github.com/jasongrout",
    "created_at": "2010-05-14T09:27:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "milestone": "sage-4.4.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8960#event-21878"
}
```



---

archive/issue_comments_082455.json:
```json
{
    "body": "The patch brings coverage in the file from 75% to 93%.",
    "created_at": "2010-05-14T09:31:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82455",
    "user": "https://github.com/jasongrout"
}
```

The patch brings coverage in the file from 75% to 93%.



---

archive/issue_comments_082456.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-05-14T13:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82456",
    "user": "https://github.com/jasongrout"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_082457.json:
```json
{
    "body": "CCing possible reviewers; this patch increases real_mpfr.pyx doctest coverage from ~75% to about 93%",
    "created_at": "2010-05-14T13:40:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82457",
    "user": "https://github.com/jasongrout"
}
```

CCing possible reviewers; this patch increases real_mpfr.pyx doctest coverage from ~75% to about 93%



---

archive/issue_comments_082458.json:
```json
{
    "body": "Attachment [trac-8960-RealField-docs.patch](tarball://root/attachments/some-uuid/ticket8960/trac-8960-RealField-docs.patch) by @jasongrout created at 2010-05-14 16:05:38\n\nI've split off changing the latex representation to #8962.\n\nThis patch also changes a deprecated call to MPFR, and redefines several functions to be aliases when it is more appropriate (e.g., self.prec is an alias to self.precision)",
    "created_at": "2010-05-14T16:05:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82458",
    "user": "https://github.com/jasongrout"
}
```

Attachment [trac-8960-RealField-docs.patch](tarball://root/attachments/some-uuid/ticket8960/trac-8960-RealField-docs.patch) by @jasongrout created at 2010-05-14 16:05:38

I've split off changing the latex representation to #8962.

This patch also changes a deprecated call to MPFR, and redefines several functions to be aliases when it is more appropriate (e.g., self.prec is an alias to self.precision)



---

archive/issue_comments_082459.json:
```json
{
    "body": "Attachment [trac_8960-reviewer.patch](tarball://root/attachments/some-uuid/ticket8960/trac_8960-reviewer.patch) by mvngu created at 2010-05-15 04:03:14\n\nChanges in the reviewer patch include:\n\n* Typo fixes.\n* Fix errors/warnings with LaTeX markups in docstrings.\n* Use error types, e.g. IndexError, etc., as callables in accordance with Python 3.x.\n* Don't LaTeX expressions wherever that makes sense. For example, something like\n {{{\n`self`\n }}}\n would actually LaTeX the word \"self\".\n\nIncidentally, I came across the following line\n\n```\nelif PY_TYPE_CHECK(x, gen) and typ((<gen>x).g) == t_REAL:\n```\nfrom the function\n\n```\ncdef _set(self, x, int base):\n        # This should not be called except when the number is being created.    \n        # Real Numbers are supposed to be immutable.\n<...>\n```\nNotice the call\n\n```\ntyp((<gen>x).g)\n```\nShould this be\n\n```\ntype((<gen>x).g)\n```\nThat is, use \"type\" instead of \"typ\"?\n\n\n\nApart from the above, I'm OK with Jason's changes. So only my patch needs review by anyone but me.",
    "created_at": "2010-05-15T04:03:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82459",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8960-reviewer.patch](tarball://root/attachments/some-uuid/ticket8960/trac_8960-reviewer.patch) by mvngu created at 2010-05-15 04:03:14

Changes in the reviewer patch include:

* Typo fixes.
* Fix errors/warnings with LaTeX markups in docstrings.
* Use error types, e.g. IndexError, etc., as callables in accordance with Python 3.x.
* Don't LaTeX expressions wherever that makes sense. For example, something like
 {{{
`self`
 }}}
 would actually LaTeX the word "self".

Incidentally, I came across the following line

```
elif PY_TYPE_CHECK(x, gen) and typ((<gen>x).g) == t_REAL:
```
from the function

```
cdef _set(self, x, int base):
        # This should not be called except when the number is being created.    
        # Real Numbers are supposed to be immutable.
<...>
```
Notice the call

```
typ((<gen>x).g)
```
Should this be

```
type((<gen>x).g)
```
That is, use "type" instead of "typ"?



Apart from the above, I'm OK with Jason's changes. So only my patch needs review by anyone but me.



---

archive/issue_comments_082460.json:
```json
{
    "body": "I applied the two patches to 4.4.3 and all is well.  And I took literally the advice that only the review patch needed to be reviewed, I did not look at the other in any detail.  Tests pass and docbuild gave no errors.",
    "created_at": "2010-06-06T20:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82460",
    "user": "https://github.com/JohnCremona"
}
```

I applied the two patches to 4.4.3 and all is well.  And I took literally the advice that only the review patch needed to be reviewed, I did not look at the other in any detail.  Tests pass and docbuild gave no errors.



---

archive/issue_comments_082461.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-06T20:07:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82461",
    "user": "https://github.com/JohnCremona"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_082462.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-07T04:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8960#issuecomment-82462",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_021879.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2010-06-07T04:48:09Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8960",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8960#event-21879"
}
```
