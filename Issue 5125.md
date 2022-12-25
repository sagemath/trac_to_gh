# Issue 5125: Ideal.basis_is_groebner() may return wrong results

archive/issues_005125.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @johnperry-math\n\nFor the attached list, `Ideal(gb).basis_is_groebner()` returns `True` but the basis is not a Gr\u00f6bner basis!\n\nThe code in question:\n\n\n```\n    def basis_is_groebner(self, singular=singular_default):\n        self.ring()._singular_().set_ring()\n\n        F = singular( self.gens(), \"module\" )\n        LTF = singular( [f.lt() for f in self.gens()] , \"module\" )\n\n        M = (F * LTF.syz()).reduce(self._singular_())\n\n        for i in range(M.nrows()):\n            if int(singular.eval(\"%s[1][%s+1]!=0\"%(M.name(),i))):\n                return False\n\n        self._singular_().attrib('isSB',1)\n        return True\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5125\n\n",
    "created_at": "2009-01-29T00:02:15Z",
    "labels": [
        "component: commutative algebra",
        "critical",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.3",
    "title": "Ideal.basis_is_groebner() may return wrong results",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5125",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @johnperry-math

For the attached list, `Ideal(gb).basis_is_groebner()` returns `True` but the basis is not a Gröbner basis!

The code in question:


```
    def basis_is_groebner(self, singular=singular_default):
        self.ring()._singular_().set_ring()

        F = singular( self.gens(), "module" )
        LTF = singular( [f.lt() for f in self.gens()] , "module" )

        M = (F * LTF.syz()).reduce(self._singular_())

        for i in range(M.nrows()):
            if int(singular.eval("%s[1][%s+1]!=0"%(M.name(),i))):
                return False

        self._singular_().attrib('isSB',1)
        return True
```


Issue created by migration from https://trac.sagemath.org/ticket/5125





---

archive/issue_comments_039094.json:
```json
{
    "body": "Attachment [B.sobj](tarball://root/attachments/some-uuid/ticket5125/B.sobj) by @malb created at 2009-01-29 00:02:41\n\nload(\"B.sobj\") this file to test if the bug is fixed.",
    "created_at": "2009-01-29T00:02:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39094",
    "user": "https://github.com/malb"
}
```

Attachment [B.sobj](tarball://root/attachments/some-uuid/ticket5125/B.sobj) by @malb created at 2009-01-29 00:02:41

load("B.sobj") this file to test if the bug is fixed.



---

archive/issue_comments_039095.json:
```json
{
    "body": "Wait-- sorry, that doesn't work either. Now things that **are** Groebner bases are considered not to be.",
    "created_at": "2009-01-30T23:09:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39095",
    "user": "https://github.com/johnperry-math"
}
```

Wait-- sorry, that doesn't work either. Now things that **are** Groebner bases are considered not to be.



---

archive/issue_comments_039096.json:
```json
{
    "body": "Attachment [basis_is_groebner.patch](tarball://root/attachments/some-uuid/ticket5125/basis_is_groebner.patch) by @johnperry-math created at 2009-01-30 23:24:11\n\nnow it works on `B.sobj` as well as on its groebner basis",
    "created_at": "2009-01-30T23:24:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39096",
    "user": "https://github.com/johnperry-math"
}
```

Attachment [basis_is_groebner.patch](tarball://root/attachments/some-uuid/ticket5125/basis_is_groebner.patch) by @johnperry-math created at 2009-01-30 23:24:11

now it works on `B.sobj` as well as on its groebner basis



---

archive/issue_comments_039097.json:
```json
{
    "body": "There were two subtle bugs.\n* The first was that `M` only had one row. Thus, `i` would check only the first element of `M`. Hence unpredictable behavior: sometimes the correct answer, sometimes not.\n* The second was that Singular (for whatever reason) expects the arrays to be indexed by `[row,col]` and not by `[row][col]`.",
    "created_at": "2009-01-30T23:27:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39097",
    "user": "https://github.com/johnperry-math"
}
```

There were two subtle bugs.
* The first was that `M` only had one row. Thus, `i` would check only the first element of `M`. Hence unpredictable behavior: sometimes the correct answer, sometimes not.
* The second was that Singular (for whatever reason) expects the arrays to be indexed by `[row,col]` and not by `[row][col]`.



---

archive/issue_comments_039098.json:
```json
{
    "body": "apply after basis_is_groebner.patch",
    "created_at": "2009-01-31T15:29:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39098",
    "user": "https://github.com/malb"
}
```

apply after basis_is_groebner.patch



---

archive/issue_comments_039099.json:
```json
{
    "body": "Attachment [basis_is_groebner_doctest.patch](tarball://root/attachments/some-uuid/ticket5125/basis_is_groebner_doctest.patch) by @malb created at 2009-01-31 15:30:33\n\nThe attached patch fixes the issue for me. I've added a second patch which documents that the bug is indeed fixed. mabshoff, this patch should definitely go in for 3.3 because right now Sage gives wrong answers!",
    "created_at": "2009-01-31T15:30:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39099",
    "user": "https://github.com/malb"
}
```

Attachment [basis_is_groebner_doctest.patch](tarball://root/attachments/some-uuid/ticket5125/basis_is_groebner_doctest.patch) by @malb created at 2009-01-31 15:30:33

The attached patch fixes the issue for me. I've added a second patch which documents that the bug is indeed fixed. mabshoff, this patch should definitely go in for 3.3 because right now Sage gives wrong answers!



---

archive/issue_events_005374.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2009-02-02T02:46:16Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/5125#event-5374"
}
```



---

archive/issue_comments_039100.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-02T02:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39100",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039101.json:
```json
{
    "body": "Merged both patches in Sage 3.3.alpha4.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-02T02:46:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5125",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5125#issuecomment-39101",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged both patches in Sage 3.3.alpha4.

Cheers,

Michael
