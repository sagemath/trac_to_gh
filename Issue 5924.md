# Issue 5924: Proposed new method for the OverconvergentModularForms class

archive/issues_005924.json:
```json
{
    "body": "Assignee: @craigcitro\n\nI would like to propose the addition of a method which will give the slopes of the U_p operator acting on a space of overconvergent modular forms. Here is my suggested code:\n\n```\n def slopes(self, n, use_recurrence=False):\n        r\"\"\"\n        Compute the slopes of the `U_p` operator acting on self, using an n x n matrix.\n\n        EXAMPLES::\n             sage: OverconvergentModularForms(5,2,1/3,base_ring=Qp(5),prec=100).slopes(5)\n             [0, 2, 5, 6, 9]\n             sage: sage: OverconvergentModularForms(2,1,1/3,char=DirichletGroup(4,QQ).0)\n             [0, 2, 4, 6, 8]\n        \"\"\" \n        if self.base_ring() == QQ:\n             slopelist=self.cps_u(n).truncate().newton_slopes(self.prime())\n        elif is_pAdicField(self.base_ring()):\n             slopelist=self.cps_u(n).truncate().newton_slopes()\n        else:\n             print \"slopes are only defined for base field QQ or a p-adic field\"\n        return [-i for i in slopelist]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5924\n\n",
    "created_at": "2009-04-28T22:55:05Z",
    "labels": [
        "component: modular forms",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.0",
    "title": "Proposed new method for the OverconvergentModularForms class",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5924",
    "user": "https://trac.sagemath.org/admin/accounts/users/ljpk"
}
```
Assignee: @craigcitro

I would like to propose the addition of a method which will give the slopes of the U_p operator acting on a space of overconvergent modular forms. Here is my suggested code:

```
 def slopes(self, n, use_recurrence=False):
        r"""
        Compute the slopes of the `U_p` operator acting on self, using an n x n matrix.

        EXAMPLES::
             sage: OverconvergentModularForms(5,2,1/3,base_ring=Qp(5),prec=100).slopes(5)
             [0, 2, 5, 6, 9]
             sage: sage: OverconvergentModularForms(2,1,1/3,char=DirichletGroup(4,QQ).0)
             [0, 2, 4, 6, 8]
        """ 
        if self.base_ring() == QQ:
             slopelist=self.cps_u(n).truncate().newton_slopes(self.prime())
        elif is_pAdicField(self.base_ring()):
             slopelist=self.cps_u(n).truncate().newton_slopes()
        else:
             print "slopes are only defined for base field QQ or a p-adic field"
        return [-i for i in slopelist]
```


Issue created by migration from https://trac.sagemath.org/ticket/5924





---

archive/issue_comments_046746.json:
```json
{
    "body": "Changing assignee from @craigcitro to @loefflerd.",
    "created_at": "2009-05-01T08:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46746",
    "user": "https://github.com/loefflerd"
}
```

Changing assignee from @craigcitro to @loefflerd.



---

archive/issue_comments_046747.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-05-01T08:02:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46747",
    "user": "https://github.com/loefflerd"
}
```

Changing status from new to assigned.



---

archive/issue_comments_046748.json:
```json
{
    "body": "patch against 3.4.2.rc0",
    "created_at": "2009-05-01T11:13:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46748",
    "user": "https://github.com/loefflerd"
}
```

patch against 3.4.2.rc0



---

archive/issue_comments_046749.json:
```json
{
    "body": "Attachment [trac_5924.patch](tarball://root/attachments/some-uuid/ticket5924/trac_5924.patch) by @loefflerd created at 2009-05-01 11:16:36\n\nPositive review. The above code works fine for me (modulo a tiny typo fix), so I've made a proper patch for it. Note that although this has my mercurial username on the patch, credit should go to Lloyd.",
    "created_at": "2009-05-01T11:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46749",
    "user": "https://github.com/loefflerd"
}
```

Attachment [trac_5924.patch](tarball://root/attachments/some-uuid/ticket5924/trac_5924.patch) by @loefflerd created at 2009-05-01 11:16:36

Positive review. The above code works fine for me (modulo a tiny typo fix), so I've made a proper patch for it. Note that although this has my mercurial username on the patch, credit should go to Lloyd.



---

archive/issue_comments_046750.json:
```json
{
    "body": "Lloyd,\n\nnext time you open a ticket please use a descriptive summary. \"Proposed new methord ...\" is next to useless ;)\n\nCheers,\n\nMichael",
    "created_at": "2009-05-07T23:57:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46750",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Lloyd,

next time you open a ticket please use a descriptive summary. "Proposed new methord ..." is next to useless ;)

Cheers,

Michael



---

archive/issue_comments_046751.json:
```json
{
    "body": "Lloyd's summary is a little mysterious, but there was already functionality for computing the U_p operator -- that's what the entire overconvergent forms class is there for -- it was just an easy shortcut to access the list of slopes that was missing.",
    "created_at": "2009-05-08T07:27:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46751",
    "user": "https://github.com/loefflerd"
}
```

Lloyd's summary is a little mysterious, but there was already functionality for computing the U_p operator -- that's what the entire overconvergent forms class is there for -- it was just an easy shortcut to access the list of slopes that was missing.



---

archive/issue_comments_046752.json:
```json
{
    "body": "Merged in Sage 4.0.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-05-12T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46752",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 4.0.alpha0.

Cheers,

Michael



---

archive/issue_comments_046753.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-05-12T22:15:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5924",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5924#issuecomment-46753",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed
