# Issue 1736: sturm_bound() not working on spaces of cusp forms

archive/issues_001736.json:
```json
{
    "body": "Assignee: @aghitza\n\nThis was part of #1612: the sturm_bound() method seems not to work\n\n\n```\nsage: S37=CuspForms(37,2)\nsage: S37.sturm_bound()\n---------------------------------------------------------------------------\n<type 'exceptions.AttributeError'>        Traceback (most recent call last)\n\n/opt/sage-2.9.3/devel/sage-alex/sage/<ipython console> in <module>()\n\n/opt/sage/local/lib/python2.5/site-packages/sage/modular/modform/space.py in sturm_bound(self, M)\n    919         if M != None:\n    920             raise NotImplementedError\n--> 921         if self.__sturm_bound == None:\n    922             # the +1 below is because O(q^prec) has precision prec.\n    923             self.__sturm_bound = int(\\\n\n<type 'exceptions.AttributeError'>: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'\n```\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/1736\n\n",
    "created_at": "2008-01-09T12:40:32Z",
    "labels": [
        "modular forms",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.10",
    "title": "sturm_bound() not working on spaces of cusp forms",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1736",
    "user": "@aghitza"
}
```
Assignee: @aghitza

This was part of #1612: the sturm_bound() method seems not to work


```
sage: S37=CuspForms(37,2)
sage: S37.sturm_bound()
---------------------------------------------------------------------------
<type 'exceptions.AttributeError'>        Traceback (most recent call last)

/opt/sage-2.9.3/devel/sage-alex/sage/<ipython console> in <module>()

/opt/sage/local/lib/python2.5/site-packages/sage/modular/modform/space.py in sturm_bound(self, M)
    919         if M != None:
    920             raise NotImplementedError
--> 921         if self.__sturm_bound == None:
    922             # the +1 below is because O(q^prec) has precision prec.
    923             self.__sturm_bound = int(\

<type 'exceptions.AttributeError'>: 'CuspidalSubmodule_g0_Q' object has no attribute '_ModularFormsSpace__sturm_bound'
```



Issue created by migration from https://trac.sagemath.org/ticket/1736





---

archive/issue_comments_010986.json:
```json
{
    "body": "Attachment [1736.patch](tarball://root/attachments/some-uuid/ticket1736/1736.patch) by @aghitza created at 2008-01-09 13:00:17",
    "created_at": "2008-01-09T13:00:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1736#issuecomment-10986",
    "user": "@aghitza"
}
```

Attachment [1736.patch](tarball://root/attachments/some-uuid/ticket1736/1736.patch) by @aghitza created at 2008-01-09 13:00:17



---

archive/issue_comments_010987.json:
```json
{
    "body": "Trivial fix; in fact, I changed the method sturm_bound() so that it uses the function sturm_bound(level, weight) from dims.py.",
    "created_at": "2008-01-09T13:02:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1736#issuecomment-10987",
    "user": "@aghitza"
}
```

Trivial fix; in fact, I changed the method sturm_bound() so that it uses the function sturm_bound(level, weight) from dims.py.



---

archive/issue_comments_010988.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2008-01-16T17:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1736#issuecomment-10988",
    "user": "@williamstein"
}
```

Looks good to me.



---

archive/issue_comments_010989.json:
```json
{
    "body": "Merged in Sage 2.10.alpha4",
    "created_at": "2008-01-16T18:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1736#issuecomment-10989",
    "user": "mabshoff"
}
```

Merged in Sage 2.10.alpha4



---

archive/issue_comments_010990.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-01-16T18:02:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1736",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1736#issuecomment-10990",
    "user": "mabshoff"
}
```

Resolution: fixed
