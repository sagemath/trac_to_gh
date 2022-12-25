# Issue 5629: refactor dimension() of schemes

archive/issues_005629.json:
```json
{
    "body": "Assignee: @williamstein\n\nKeywords: dimension scheme\n\nThe dimension() method for schemes is confusing and sometimes inconsistent or plain broken when working over bases that are not fields.  The attached patch implements methods dimension_absolute() and dimension_relative() and makes dimension() into an alias for dimension_absolute().\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5629\n\n",
    "created_at": "2009-03-29T03:58:49Z",
    "labels": [
        "component: algebraic geometry",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "refactor dimension() of schemes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5629",
    "user": "https://github.com/aghitza"
}
```
Assignee: @williamstein

Keywords: dimension scheme

The dimension() method for schemes is confusing and sometimes inconsistent or plain broken when working over bases that are not fields.  The attached patch implements methods dimension_absolute() and dimension_relative() and makes dimension() into an alias for dimension_absolute().


Issue created by migration from https://trac.sagemath.org/ticket/5629





---

archive/issue_comments_043872.json:
```json
{
    "body": "Attachment [trac_5629.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629.patch) by @aghitza created at 2009-03-29 03:59:51",
    "created_at": "2009-03-29T03:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43872",
    "user": "https://github.com/aghitza"
}
```

Attachment [trac_5629.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629.patch) by @aghitza created at 2009-03-29 03:59:51



---

archive/issue_comments_043873.json:
```json
{
    "body": "See the following thread for more details:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/cab22c1376251540",
    "created_at": "2009-03-29T04:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43873",
    "user": "https://github.com/aghitza"
}
```

See the following thread for more details:

http://groups.google.com/group/sage-devel/browse_thread/thread/cab22c1376251540



---

archive/issue_comments_043874.json:
```json
{
    "body": "Changing assignee from @williamstein to @aghitza.",
    "created_at": "2009-03-29T08:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43874",
    "user": "https://github.com/aghitza"
}
```

Changing assignee from @williamstein to @aghitza.



---

archive/issue_comments_043875.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T08:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43875",
    "user": "https://github.com/aghitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043876.json:
```json
{
    "body": "REFEREE REPORT.\n\nLooks great.  I rebased this patch against 3.4.1.alpha0 and added a doctest for the following new function.  I also doctested this patch against the schemes directory.\n\n```\n \t137\t    def is_noetherian(self): \n \t138\t        \"\"\" \n \t139\t        Return True if this scheme is Noetherian. \n \t140\t        \"\"\" \n \t141\t        return self.__R.is_noetherian() \n```\n",
    "created_at": "2009-03-29T17:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43876",
    "user": "https://github.com/williamstein"
}
```

REFEREE REPORT.

Looks great.  I rebased this patch against 3.4.1.alpha0 and added a doctest for the following new function.  I also doctested this patch against the schemes directory.

```
 	137	    def is_noetherian(self): 
 	138	        """ 
 	139	        Return True if this scheme is Noetherian. 
 	140	        """ 
 	141	        return self.__R.is_noetherian() 
```




---

archive/issue_comments_043877.json:
```json
{
    "body": "rebased against 3.4.1.alpha0 and added a missing doctst",
    "created_at": "2009-03-29T17:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43877",
    "user": "https://github.com/williamstein"
}
```

rebased against 3.4.1.alpha0 and added a missing doctst



---

archive/issue_comments_043878.json:
```json
{
    "body": "Attachment [trac_5629-rebase.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629-rebase.patch) by @williamstein created at 2009-03-29 17:27:04",
    "created_at": "2009-03-29T17:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43878",
    "user": "https://github.com/williamstein"
}
```

Attachment [trac_5629-rebase.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629-rebase.patch) by @williamstein created at 2009-03-29 17:27:04



---

archive/issue_comments_043879.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T08:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43879",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043880.json:
```json
{
    "body": "Merged trac_5629-rebase.patch in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43880",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged trac_5629-rebase.patch in Sage 3.4.1.rc0.

Cheers,

Michael
