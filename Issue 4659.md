# Issue 4659: remove an extra 'cdef class Integer' line from integer.pyx

archive/issues_004659.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @robertwb\n\nKeywords: integer\n\nIn the file sage/rings/integer.pyx, line 288 says \n\n```\n    cdef class Integer (sage.structure.element.EuclideanDomainElement): \n```\n\nfollowed by documentation and the various methods for this class.  But earlier in the file, line 137 says \n\n```\n    cdef class Integer(sage.structure.element.EuclideanDomainElement) \n```\n\nThe attached patch removes line 137.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4659\n\n",
    "created_at": "2008-11-30T00:44:16Z",
    "labels": [
        "component: basic arithmetic",
        "trivial",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.2.1",
    "title": "remove an extra 'cdef class Integer' line from integer.pyx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4659",
    "user": "https://github.com/jhpalmieri"
}
```
Assignee: somebody

CC:  @robertwb

Keywords: integer

In the file sage/rings/integer.pyx, line 288 says 

```
    cdef class Integer (sage.structure.element.EuclideanDomainElement): 
```

followed by documentation and the various methods for this class.  But earlier in the file, line 137 says 

```
    cdef class Integer(sage.structure.element.EuclideanDomainElement) 
```

The attached patch removes line 137.

Issue created by migration from https://trac.sagemath.org/ticket/4659





---

archive/issue_comments_035025.json:
```json
{
    "body": "Attachment [integer-pyx.patch](tarball://root/attachments/some-uuid/ticket4659/integer-pyx.patch) by mabshoff created at 2008-11-30 03:44:20\n\nLooks good to me. As RobertWB said in http://groups.google.com/group/sage-devel/t/3d76203eeed29ec5 this can go in.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T03:44:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4659#issuecomment-35025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Attachment [integer-pyx.patch](tarball://root/attachments/some-uuid/ticket4659/integer-pyx.patch) by mabshoff created at 2008-11-30 03:44:20

Looks good to me. As RobertWB said in http://groups.google.com/group/sage-devel/t/3d76203eeed29ec5 this can go in.

Cheers,

Michael



---

archive/issue_comments_035026.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T05:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4659#issuecomment-35026",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_004907.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-11-30T05:39:02Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4659",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4659#event-4907"
}
```



---

archive/issue_comments_035027.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1. Reviewer credit goes to RobertWB",
    "created_at": "2008-11-30T05:39:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4659",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4659#issuecomment-35027",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.2.1.rc1. Reviewer credit goes to RobertWB
