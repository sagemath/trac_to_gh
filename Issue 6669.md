# Issue 6669: Homomorphisms from matrix groups don't have to have matrix groups as codomain

archive/issues_006669.json:
```json
{
    "body": "Assignee: mraum\n\nCC:  @mwhansen alexghitza\n\nThis is an error which occurs if one tries to construct coercing from a matrix group into an algebra. The current implementation of homomorphisms with domain a matrix group require the codomain to be a matrix group, too.\n \n```\n/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/categories/homset.pyc in Hom(X, Y, cat)\n     64     \"\"\"\n     65     if hasattr(X, '_Hom_'):\n---> 66         return X._Hom_(Y, cat)\n     67 \n     68     global _cache\n\n/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _Hom_(self, G, cat)\n    230             raise NotImplementedError\n    231         if not is_MatrixGroup(G):\n--> 232             raise TypeError, \"G (=%s) must be a matrix group.\"%G\n    233         import homset\n    234         return homset.MatrixGroupHomset(self, G)\n\nTypeError: G (=Group algebra of group \"General Linear Group of degree 3 over Finite Field of size 7\" over base ring Integer Ring) must be a matrix group.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6669\n\n",
    "created_at": "2009-08-03T20:36:35Z",
    "labels": [
        "component: coercion",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3",
    "title": "Homomorphisms from matrix groups don't have to have matrix groups as codomain",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6669",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```
Assignee: mraum

CC:  @mwhansen alexghitza

This is an error which occurs if one tries to construct coercing from a matrix group into an algebra. The current implementation of homomorphisms with domain a matrix group require the codomain to be a matrix group, too.
 
```
/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/categories/homset.pyc in Hom(X, Y, cat)
     64     """
     65     if hasattr(X, '_Hom_'):
---> 66         return X._Hom_(Y, cat)
     67 
     68     global _cache

/home/martin/sage-4.1_compiled/local/lib/python2.6/site-packages/sage/groups/matrix_gps/matrix_group.pyc in _Hom_(self, G, cat)
    230             raise NotImplementedError
    231         if not is_MatrixGroup(G):
--> 232             raise TypeError, "G (=%s) must be a matrix group."%G
    233         import homset
    234         return homset.MatrixGroupHomset(self, G)

TypeError: G (=Group algebra of group "General Linear Group of degree 3 over Finite Field of size 7" over base ring Integer Ring) must be a matrix group.
```


Issue created by migration from https://trac.sagemath.org/ticket/6669





---

archive/issue_comments_054653.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2009-10-22T16:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54653",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_054654.json:
```json
{
    "body": "Attachment [trac-6669-matrix_hom.patch](tarball://root/attachments/some-uuid/ticket6669/trac-6669-matrix_hom.patch) by mraum created at 2009-10-22 16:50:07",
    "created_at": "2009-10-22T16:50:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54654",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-6669-matrix_hom.patch](tarball://root/attachments/some-uuid/ticket6669/trac-6669-matrix_hom.patch) by mraum created at 2009-10-22 16:50:07



---

archive/issue_comments_054655.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2009-11-15T10:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54655",
    "user": "https://github.com/aghitza"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_054656.json:
```json
{
    "body": "This looks good, applies cleanly and passes long tests under sage-4.2.  I will test on sage-4.2.1 as soon as sage.math binaries are available.\n\nOne thing needs to be fixed: please add some doctests with examples of homomorphisms between matrix groups, and from matrix groups to other types of groups.  (I do realise that the method patched here did not have doctests to start with.)",
    "created_at": "2009-11-15T10:01:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54656",
    "user": "https://github.com/aghitza"
}
```

This looks good, applies cleanly and passes long tests under sage-4.2.  I will test on sage-4.2.1 as soon as sage.math binaries are available.

One thing needs to be fixed: please add some doctests with examples of homomorphisms between matrix groups, and from matrix groups to other types of groups.  (I do realise that the method patched here did not have doctests to start with.)



---

archive/issue_comments_054657.json:
```json
{
    "body": "Attachment [trac-6669-2-matrix_hom.patch](tarball://root/attachments/some-uuid/ticket6669/trac-6669-2-matrix_hom.patch) by mraum created at 2009-11-16 13:31:53\n\nPatch with doctests.",
    "created_at": "2009-11-16T13:31:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54657",
    "user": "https://trac.sagemath.org/admin/accounts/users/mraum"
}
```

Attachment [trac-6669-2-matrix_hom.patch](tarball://root/attachments/some-uuid/ticket6669/trac-6669-2-matrix_hom.patch) by mraum created at 2009-11-16 13:31:53

Patch with doctests.



---

archive/issue_comments_054658.json:
```json
{
    "body": "Yep, doctests look fine.",
    "created_at": "2009-11-20T05:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54658",
    "user": "https://github.com/robertwb"
}
```

Yep, doctests look fine.



---

archive/issue_comments_054659.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2009-11-20T05:17:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54659",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_054660.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2009-11-20T05:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54660",
    "user": "https://github.com/robertwb"
}
```

Looks good to me.



---

archive/issue_comments_054661.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2009-11-20T05:17:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54661",
    "user": "https://github.com/robertwb"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_054662.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-11-20T05:30:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6669#issuecomment-54662",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed



---

archive/issue_events_015739.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-11-20T05:30:12Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6669",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6669#event-15739"
}
```
