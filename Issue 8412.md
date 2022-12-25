# Issue 8412: Trivial Center of Matrix Group

archive/issues_008412.json:
```json
{
    "body": "Assignee: joyner\n\nWhen calculating the center of a group, GAP returns an empty list of generators if the center is trivial.  This however throws off the creation of the MatrixGroup in Sage which checks to ensure that there is at least one generator.\n\n\n```\nsage: a=Matrix(FiniteField(5),\n....: [[2,0,0],\n....: [0,3,0],\n....: [0,0,1]])\nsage: \nsage: b=Matrix(FiniteField(5),\n....: [[0,1,0],\n....: [4,0,0],\n....: [0,0,1]])\nsage: \nsage: c=Matrix(FiniteField(5),\n....: [[1,0,0],\n....: [0,1,0],\n....: [0,1,1]])\nsage: \nsage: d=Matrix(FiniteField(5),\n....: [[1,0,0],\n....: [0,1,0],\n....: [1,0,1]])\nsage: \nsage: G = MatrixGroup([a,b,c,d])\nsage: G.center()\n---------------------------------------------------------------------------\nValueError                                Traceback (most recent call last)\n\n/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/<ipython console> in <module>()\n\n/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in center(self)\n    733         F = self.field_of_definition()\n    734         from sage.groups.matrix_gps.matrix_group import MatrixGroup\n--> 735         self.__center = MatrixGroup([g._matrix_(F) for g in G])\n    736         return self.__center\n    737     \n\n/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in MatrixGroup(gens)\n    156     \"\"\"\n    157     if len(gens) == 0:\n--> 158         raise ValueError, \"gens must have positive length\"\n    159     try:\n    160         R = gens[0].base_ring()\n\nValueError: gens must have positive length\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8412\n\n",
    "created_at": "2010-03-01T22:46:04Z",
    "labels": [
        "component: group theory",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "Trivial Center of Matrix Group",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8412",
    "user": "https://github.com/gvol"
}
```
Assignee: joyner

When calculating the center of a group, GAP returns an empty list of generators if the center is trivial.  This however throws off the creation of the MatrixGroup in Sage which checks to ensure that there is at least one generator.


```
sage: a=Matrix(FiniteField(5),
....: [[2,0,0],
....: [0,3,0],
....: [0,0,1]])
sage: 
sage: b=Matrix(FiniteField(5),
....: [[0,1,0],
....: [4,0,0],
....: [0,0,1]])
sage: 
sage: c=Matrix(FiniteField(5),
....: [[1,0,0],
....: [0,1,0],
....: [0,1,1]])
sage: 
sage: d=Matrix(FiniteField(5),
....: [[1,0,0],
....: [0,1,0],
....: [1,0,1]])
sage: 
sage: G = MatrixGroup([a,b,c,d])
sage: G.center()
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/<ipython console> in <module>()

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in center(self)
    733         F = self.field_of_definition()
    734         from sage.groups.matrix_gps.matrix_group import MatrixGroup
--> 735         self.__center = MatrixGroup([g._matrix_(F) for g in G])
    736         return self.__center
    737     

/Users/gvol/Desktop/Sage-4.3.1.rc1.app/Contents/Resources/sage/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in MatrixGroup(gens)
    156     """
    157     if len(gens) == 0:
--> 158         raise ValueError, "gens must have positive length"
    159     try:
    160         R = gens[0].base_ring()

ValueError: gens must have positive length
```


Issue created by migration from https://trac.sagemath.org/ticket/8412





---

archive/issue_comments_075241.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-01T23:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75241",
    "user": "https://github.com/gvol"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075242.json:
```json
{
    "body": "I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  \n\nSorry for the trailing whitespace differences.",
    "created_at": "2010-03-01T23:07:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75242",
    "user": "https://github.com/gvol"
}
```

I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  

Sorry for the trailing whitespace differences.



---

archive/issue_comments_075243.json:
```json
{
    "body": "Replying to [comment:1 iandrus]:\n> I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  \n> \n> Sorry for the trailing whitespace differences.\n\nThank you for noticing this problem and submitting a patch.\n\nI have not tested your patch yet, but it does not seem form reading the patch code that you have also added an example to the docstring which *tests* your new patch. If this is correct, can you please consider doing that?",
    "created_at": "2010-03-01T23:15:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75243",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:1 iandrus]:
> I added a patch which checks for a trivial center, and uses the identity for the group as a generator in this case.  
> 
> Sorry for the trailing whitespace differences.

Thank you for noticing this problem and submitting a patch.

I have not tested your patch yet, but it does not seem form reading the patch code that you have also added an example to the docstring which *tests* your new patch. If this is correct, can you please consider doing that?



---

archive/issue_comments_075244.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-03-01T23:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75244",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_075245.json:
```json
{
    "body": "Oops, you're absolutely right.  I'll get to it tomorrow.",
    "created_at": "2010-03-01T23:35:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75245",
    "user": "https://github.com/gvol"
}
```

Oops, you're absolutely right.  I'll get to it tomorrow.



---

archive/issue_comments_075246.json:
```json
{
    "body": "Attachment [trac_8412_trivial_center.patch](tarball://root/attachments/some-uuid/ticket8412/trac_8412_trivial_center.patch) by @gvol created at 2010-03-02 11:05:07",
    "created_at": "2010-03-02T11:05:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75246",
    "user": "https://github.com/gvol"
}
```

Attachment [trac_8412_trivial_center.patch](tarball://root/attachments/some-uuid/ticket8412/trac_8412_trivial_center.patch) by @gvol created at 2010-03-02 11:05:07



---

archive/issue_comments_075247.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-03-02T11:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75247",
    "user": "https://github.com/gvol"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_075248.json:
```json
{
    "body": "Okay, new patch up.",
    "created_at": "2010-03-02T11:06:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75248",
    "user": "https://github.com/gvol"
}
```

Okay, new patch up.



---

archive/issue_comments_075249.json:
```json
{
    "body": "Seems to apply okay (there was some \"fuzz\") to sage 4.3.3.a1 on a 10.6.2 mac. Pases sage -testall.\n\nPatch looks good to me.",
    "created_at": "2010-03-03T00:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75249",
    "user": "https://github.com/wdjoyner"
}
```

Seems to apply okay (there was some "fuzz") to sage 4.3.3.a1 on a 10.6.2 mac. Pases sage -testall.

Patch looks good to me.



---

archive/issue_comments_075250.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-03-03T00:37:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75250",
    "user": "https://github.com/wdjoyner"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_075251.json:
```json
{
    "body": "properly folded patch; apply only this one",
    "created_at": "2010-03-03T02:51:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75251",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

properly folded patch; apply only this one



---

archive/issue_comments_075252.json:
```json
{
    "body": "Attachment [trac_8412-folded.patch](tarball://root/attachments/some-uuid/ticket8412/trac_8412-folded.patch) by mvngu created at 2010-03-03 02:53:32\n\nIt looks like [trac_8412_trivial_center.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412_trivial_center.patch) consists of two patch files rolled into one, as evident from this snippet:\n\n```\n     ::\n-    \n+\n         sage: F = GF(5); MS = MatrixSpace(F,2,2)\n         sage: G = MatrixGroup([MS.0])\n         Traceback (most recent call last):\n# HG changeset patch\n# User Ivan Andrus <darthandrus@gmail.com>\n# Date 1267527460 -3600\n# Node ID fa0a59cf132bca55c4500e7c134157e57a23dc3d\n# Parent  023d02e0af46ae4e4450e3f2f14db54345aa8774\nAdded doctest for trivial center patch\n\ndiff -r 023d02e0af46 -r fa0a59cf132b sage/groups/matrix_gps/matrix_group.py\n--- a/sage/groups/matrix_gps/matrix_group.py\tMon Mar 01 23:52:39 2010 +0100\n+++ b/sage/groups/matrix_gps/matrix_group.py\tTue Mar 02 11:57:40 2010 +0100\n@@ -739,6 +739,11 @@\n```\n\nA patch file shouldn't be like that. I have attached the same patch, which also include the ticket number in the commit message. (Every commit message must have a ticket number.)",
    "created_at": "2010-03-03T02:53:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75252",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_8412-folded.patch](tarball://root/attachments/some-uuid/ticket8412/trac_8412-folded.patch) by mvngu created at 2010-03-03 02:53:32

It looks like [trac_8412_trivial_center.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412_trivial_center.patch) consists of two patch files rolled into one, as evident from this snippet:

```
     ::
-    
+
         sage: F = GF(5); MS = MatrixSpace(F,2,2)
         sage: G = MatrixGroup([MS.0])
         Traceback (most recent call last):
# HG changeset patch
# User Ivan Andrus <darthandrus@gmail.com>
# Date 1267527460 -3600
# Node ID fa0a59cf132bca55c4500e7c134157e57a23dc3d
# Parent  023d02e0af46ae4e4450e3f2f14db54345aa8774
Added doctest for trivial center patch

diff -r 023d02e0af46 -r fa0a59cf132b sage/groups/matrix_gps/matrix_group.py
--- a/sage/groups/matrix_gps/matrix_group.py	Mon Mar 01 23:52:39 2010 +0100
+++ b/sage/groups/matrix_gps/matrix_group.py	Tue Mar 02 11:57:40 2010 +0100
@@ -739,6 +739,11 @@
```

A patch file shouldn't be like that. I have attached the same patch, which also include the ticket number in the commit message. (Every commit message must have a ticket number.)



---

archive/issue_comments_075253.json:
```json
{
    "body": "Merged [trac_8412-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412-folded.patch).",
    "created_at": "2010-03-03T13:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75253",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged [trac_8412-folded.patch](http://trac.sagemath.org/sage_trac/attachment/ticket/8412/trac_8412-folded.patch).



---

archive/issue_comments_075254.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-03T13:54:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8412#issuecomment-75254",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_008597.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-03-03T13:54:42Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8412",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8412#event-8597"
}
```
