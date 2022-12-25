# Issue 6846: [with patch, positive review] follow up to #6751: fix warnings when building reference manual

archive/issues_006846.json:
```json
{
    "body": "Assignee: tba\n\nCC:  @williamstein @JohnCremona\n\nThe following section of the patch `trac_6751.patch` from #6751 results in two warnings when building the reference manual:\n\n```\n1202\t            - QuadraticForm \n1203\t \n1204\t        This function computes the positive definition quadratic form \n1205\t        obtained by letting G be the trace zero subspace of ZZ + \n1206\t        2*self, which had rank 3, and restricting the pairing \n1207\t           (x,y) = (x.conjugate()*y).reduced_trace() \n1208\t        to G. \n```\nThe warning messages are:\n\n```\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra:7: (ERROR/3) Unexpected indentation.\nWARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.ternary_quadratic_form:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6846\n\n",
    "closed_at": "2009-08-31T08:05:27Z",
    "created_at": "2009-08-30T09:50:11Z",
    "labels": [
        "component: documentation",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "[with patch, positive review] follow up to #6751: fix warnings when building reference manual",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6846",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: tba

CC:  @williamstein @JohnCremona

The following section of the patch `trac_6751.patch` from #6751 results in two warnings when building the reference manual:

```
1202	            - QuadraticForm 
1203	 
1204	        This function computes the positive definition quadratic form 
1205	        obtained by letting G be the trace zero subspace of ZZ + 
1206	        2*self, which had rank 3, and restricting the pairing 
1207	           (x,y) = (x.conjugate()*y).reduced_trace() 
1208	        to G. 
```
The warning messages are:

```
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra:7: (ERROR/3) Unexpected indentation.
WARNING: /scratch/mvngu/release/sage-4.1.1/local/lib/python2.6/site-packages/sage/algebras/quatalg/quaternion_algebra.py:docstring of sage.algebras.quatalg.quaternion_algebra.QuaternionOrder.ternary_quadratic_form:11: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
```


Issue created by migration from https://trac.sagemath.org/ticket/6846





---

archive/issue_comments_056359.json:
```json
{
    "body": "fix docstring warnings",
    "created_at": "2009-08-30T09:52:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6846#issuecomment-56359",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

fix docstring warnings



---

archive/issue_comments_056360.json:
```json
{
    "body": "Attachment [trac_6846-docstring.patch](tarball://root/attachments/some-uuid/ticket6846/trac_6846-docstring.patch) by mvngu created at 2009-08-30 09:54:26\n\nThe patch `trac_6846-docstring.patch` should fix the reported warnings. It depends on #6751.",
    "created_at": "2009-08-30T09:54:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6846#issuecomment-56360",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6846-docstring.patch](tarball://root/attachments/some-uuid/ticket6846/trac_6846-docstring.patch) by mvngu created at 2009-08-30 09:54:26

The patch `trac_6846-docstring.patch` should fix the reported warnings. It depends on #6751.



---

archive/issue_comments_056361.json:
```json
{
    "body": "Thanks!",
    "created_at": "2009-08-30T21:51:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6846#issuecomment-56361",
    "user": "https://github.com/williamstein"
}
```

Thanks!



---

archive/issue_comments_056362.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-31T08:05:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6846",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6846#issuecomment-56362",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016112.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-31T08:05:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6846",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6846#event-16112"
}
```
