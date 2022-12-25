# Issue 7381: Coercion of HyperellipticCurve over pAdicField to an extension

archive/issues_007381.json:
```json
{
    "body": "Assignee: @roed314\n\nCC:  @jbalakrishnan\n\n\n```\nsage: R.<x> = QQ['x']\nsage: H = HyperellipticCurve(x^3-10*x+9)\nsage: K = Qp(3,5)\nsage: J.<a> = K.extension(x^30-3)\nsage: HK = H.change_ring(K)\nsage: HJ = HK.change_ring(J)\nERROR: An unexpected error occurred while tokenizing input\nThe following traceback may be corrupted or invalid\nThe error message is: ('EOF in multi-line statement', (8, 0))\n\n[snip]\n\nValueError: variable names must be alphanumeric, but one is '(1 + O(3^5))*x' which is not.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7381\n\n",
    "created_at": "2009-11-03T17:54:12Z",
    "labels": [
        "component: number theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Coercion of HyperellipticCurve over pAdicField to an extension",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7381",
    "user": "https://github.com/jbalakrishnan"
}
```
Assignee: @roed314

CC:  @jbalakrishnan


```
sage: R.<x> = QQ['x']
sage: H = HyperellipticCurve(x^3-10*x+9)
sage: K = Qp(3,5)
sage: J.<a> = K.extension(x^30-3)
sage: HK = H.change_ring(K)
sage: HJ = HK.change_ring(J)
ERROR: An unexpected error occurred while tokenizing input
The following traceback may be corrupted or invalid
The error message is: ('EOF in multi-line statement', (8, 0))

[snip]

ValueError: variable names must be alphanumeric, but one is '(1 + O(3^5))*x' which is not.
```


Issue created by migration from https://trac.sagemath.org/ticket/7381





---

archive/issue_comments_061975.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-04T07:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61975",
    "user": "https://github.com/mwhansen"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061976.json:
```json
{
    "body": "Attachment [trac_7381.patch](tarball://root/attachments/some-uuid/ticket7381/trac_7381.patch) by @mwhansen created at 2009-11-04 07:27:30",
    "created_at": "2009-11-04T07:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61976",
    "user": "https://github.com/mwhansen"
}
```

Attachment [trac_7381.patch](tarball://root/attachments/some-uuid/ticket7381/trac_7381.patch) by @mwhansen created at 2009-11-04 07:27:30



---

archive/issue_comments_061977.json:
```json
{
    "body": "If you look at the error, you'll see that it is expecting an\nalphanumeric variable name, but got '(1 + O(3^5))*x' instead.  This\nis because it is using the .gen() method and that's how the\ngenerator prints out.  The patch changes it so that it uses the\nvariable_name() method instead which doesn't have the (1 + O(3^5))\npart.",
    "created_at": "2009-12-07T08:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61977",
    "user": "https://github.com/mwhansen"
}
```

If you look at the error, you'll see that it is expecting an
alphanumeric variable name, but got '(1 + O(3^5))*x' instead.  This
is because it is using the .gen() method and that's how the
generator prints out.  The patch changes it so that it uses the
variable_name() method instead which doesn't have the (1 + O(3^5))
part.



---

archive/issue_comments_061978.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-12-07T09:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61978",
    "user": "https://github.com/nathanncohen"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_061979.json:
```json
{
    "body": "Applies fine, passes the tests.. It took me 10 times the amount of time somebody knowing this class would have needed, but it is ok :-)\n\nNathann",
    "created_at": "2009-12-07T09:07:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61979",
    "user": "https://github.com/nathanncohen"
}
```

Applies fine, passes the tests.. It took me 10 times the amount of time somebody knowing this class would have needed, but it is ok :-)

Nathann



---

archive/issue_events_017451.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-12-07T23:23:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7381#event-17451"
}
```



---

archive/issue_comments_061980.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-12-07T23:23:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7381",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7381#issuecomment-61980",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
