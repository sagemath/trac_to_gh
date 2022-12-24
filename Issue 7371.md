# Issue 7371: rename quotient_group() to quotient() in groups/perm_gps/permgroup.py

archive/issues_007371.json:
```json
{
    "body": "Assignee: joyner\n\nThere is a generic group method called `quotient`, which is meant to return the quotient group by a normal subgroup, and is meant to be overridden by inheriting classes.  However, the corresponding method for permutation groups is called `quotient_group` instead:\n\n\n```\nsage: S = SymmetricGroup(6)\nsage: N = S.normal_subgroups()[1]\nsage: S.quotient(N)\n---------------------------------------------------------------------------\nNotImplementedError                       Traceback (most recent call last)\n\n/home/ghitza/.sage/temp/artin/674/_home_ghitza__sage_init_sage_0.py in <module>()\n\n/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.Group.quotient (sage/groups/group.c:1719)()\n\nNotImplementedError: \nsage: S.quotient_group(N)\nPermutation Group with generators [(), (1,2)]\n```\n\n\nThe attached patch renames the permutation group method to `quotient` and deprecates `quotient_group`.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7371\n\n",
    "created_at": "2009-11-01T22:29:41Z",
    "labels": [
        "group theory",
        "minor",
        "bug"
    ],
    "title": "rename quotient_group() to quotient() in groups/perm_gps/permgroup.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7371",
    "user": "AlexGhitza"
}
```
Assignee: joyner

There is a generic group method called `quotient`, which is meant to return the quotient group by a normal subgroup, and is meant to be overridden by inheriting classes.  However, the corresponding method for permutation groups is called `quotient_group` instead:


```
sage: S = SymmetricGroup(6)
sage: N = S.normal_subgroups()[1]
sage: S.quotient(N)
---------------------------------------------------------------------------
NotImplementedError                       Traceback (most recent call last)

/home/ghitza/.sage/temp/artin/674/_home_ghitza__sage_init_sage_0.py in <module>()

/home/ghitza/sage-stable/local/lib/python2.6/site-packages/sage/groups/group.so in sage.groups.group.Group.quotient (sage/groups/group.c:1719)()

NotImplementedError: 
sage: S.quotient_group(N)
Permutation Group with generators [(), (1,2)]
```


The attached patch renames the permutation group method to `quotient` and deprecates `quotient_group`.


Issue created by migration from https://trac.sagemath.org/ticket/7371





---

archive/issue_comments_061764.json:
```json
{
    "body": "Attachment [trac_7371.patch](tarball://root/attachments/some-uuid/ticket7371/trac_7371.patch) by AlexGhitza created at 2009-11-01 23:13:44",
    "created_at": "2009-11-01T23:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7371#issuecomment-61764",
    "user": "AlexGhitza"
}
```

Attachment [trac_7371.patch](tarball://root/attachments/some-uuid/ticket7371/trac_7371.patch) by AlexGhitza created at 2009-11-01 23:13:44



---

archive/issue_comments_061765.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-11-01T23:13:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7371#issuecomment-61765",
    "user": "AlexGhitza"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_061766.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-17T12:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7371#issuecomment-61766",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_061767.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-17T12:10:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7371",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7371#issuecomment-61767",
    "user": "mhansen"
}
```

Resolution: fixed
