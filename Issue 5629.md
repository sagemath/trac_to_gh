# Issue 5629: refactor dimension() of schemes

archive/issues_005629.json:
```json
{
    "body": "Assignee: was\n\nKeywords: dimension scheme\n\nThe dimension() method for schemes is confusing and sometimes inconsistent or plain broken when working over bases that are not fields.  The attached patch implements methods dimension_absolute() and dimension_relative() and makes dimension() into an alias for dimension_absolute().\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5629\n\n",
    "created_at": "2009-03-29T03:58:49Z",
    "labels": [
        "algebraic geometry",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4.1",
    "title": "refactor dimension() of schemes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5629",
    "user": "AlexGhitza"
}
```
Assignee: was

Keywords: dimension scheme

The dimension() method for schemes is confusing and sometimes inconsistent or plain broken when working over bases that are not fields.  The attached patch implements methods dimension_absolute() and dimension_relative() and makes dimension() into an alias for dimension_absolute().


Issue created by migration from https://trac.sagemath.org/ticket/5629





---

archive/issue_comments_043957.json:
```json
{
    "body": "Attachment [trac_5629.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629.patch) by AlexGhitza created at 2009-03-29 03:59:51",
    "created_at": "2009-03-29T03:59:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43957",
    "user": "AlexGhitza"
}
```

Attachment [trac_5629.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629.patch) by AlexGhitza created at 2009-03-29 03:59:51



---

archive/issue_comments_043958.json:
```json
{
    "body": "See the following thread for more details:\n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/cab22c1376251540",
    "created_at": "2009-03-29T04:02:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43958",
    "user": "AlexGhitza"
}
```

See the following thread for more details:

http://groups.google.com/group/sage-devel/browse_thread/thread/cab22c1376251540



---

archive/issue_comments_043959.json:
```json
{
    "body": "Changing assignee from was to AlexGhitza.",
    "created_at": "2009-03-29T08:16:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43959",
    "user": "AlexGhitza"
}
```

Changing assignee from was to AlexGhitza.



---

archive/issue_comments_043960.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-03-29T08:16:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43960",
    "user": "AlexGhitza"
}
```

Changing status from new to assigned.



---

archive/issue_comments_043961.json:
```json
{
    "body": "REFEREE REPORT.\n\nLooks great.  I rebased this patch against 3.4.1.alpha0 and added a doctest for the following new function.  I also doctested this patch against the schemes directory.\n\n```\n \t137\t    def is_noetherian(self): \n \t138\t        \"\"\" \n \t139\t        Return True if this scheme is Noetherian. \n \t140\t        \"\"\" \n \t141\t        return self.__R.is_noetherian() \n```\n",
    "created_at": "2009-03-29T17:25:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43961",
    "user": "was"
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

archive/issue_comments_043962.json:
```json
{
    "body": "rebased against 3.4.1.alpha0 and added a missing doctst",
    "created_at": "2009-03-29T17:26:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43962",
    "user": "was"
}
```

rebased against 3.4.1.alpha0 and added a missing doctst



---

archive/issue_comments_043963.json:
```json
{
    "body": "Attachment [trac_5629-rebase.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629-rebase.patch) by was created at 2009-03-29 17:27:04",
    "created_at": "2009-03-29T17:27:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43963",
    "user": "was"
}
```

Attachment [trac_5629-rebase.patch](tarball://root/attachments/some-uuid/ticket5629/trac_5629-rebase.patch) by was created at 2009-03-29 17:27:04



---

archive/issue_comments_043964.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-03-31T08:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43964",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_043965.json:
```json
{
    "body": "Merged trac_5629-rebase.patch in Sage 3.4.1.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-03-31T08:49:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5629",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5629#issuecomment-43965",
    "user": "mabshoff"
}
```

Merged trac_5629-rebase.patch in Sage 3.4.1.rc0.

Cheers,

Michael
