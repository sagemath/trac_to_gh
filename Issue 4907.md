# Issue 4907: convert sage.crypto.* docstrings to Sphinx

archive/issues_004907.json:
```json
{
    "body": "Assignee: tba\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/4907\n\n",
    "created_at": "2009-01-01T22:49:37Z",
    "labels": [
        "documentation",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.4",
    "title": "convert sage.crypto.* docstrings to Sphinx",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4907",
    "user": "@mwhansen"
}
```
Assignee: tba



Issue created by migration from https://trac.sagemath.org/ticket/4907





---

archive/issue_comments_037247.json:
```json
{
    "body": "Attachment [trac_4907.patch](tarball://root/attachments/some-uuid/ticket4907/trac_4907.patch) by @mwhansen created at 2009-01-02 02:55:57",
    "created_at": "2009-01-02T02:55:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37247",
    "user": "@mwhansen"
}
```

Attachment [trac_4907.patch](tarball://root/attachments/some-uuid/ticket4907/trac_4907.patch) by @mwhansen created at 2009-01-02 02:55:57



---

archive/issue_comments_037248.json:
```json
{
    "body": "Looks good. There is one \"then\" which is caught in a latex math display mode. I wonder if changing\n\n\n```\n \t100\t.. math:: \n \t101\t \n \t102\t     f(x)=1,\\ \\ \\ \\ g(x)=x^4+x+1,  \n \t103\t \n \t104\t then \n```\n\nto\n\n\n```\n \t100\t.. math:: \n \t101\t \n \t102\t     f(x)=1,\\ \\ \\ \\ g(x)=x^4+x+1,  \n \t103\t \n\t104\t \n \t105\tthen \n```\n\nwould fix that? Ie, add a blank line and delete a space?",
    "created_at": "2009-01-02T11:30:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37248",
    "user": "@wdjoyner"
}
```

Looks good. There is one "then" which is caught in a latex math display mode. I wonder if changing


```
 	100	.. math:: 
 	101	 
 	102	     f(x)=1,\ \ \ \ g(x)=x^4+x+1,  
 	103	 
 	104	 then 
```

to


```
 	100	.. math:: 
 	101	 
 	102	     f(x)=1,\ \ \ \ g(x)=x^4+x+1,  
 	103	 
	104	 
 	105	then 
```

would fix that? Ie, add a blank line and delete a space?



---

archive/issue_comments_037249.json:
```json
{
    "body": "Good catch.  Just deleting the space should be enough.  ReST works with indentation levels.  I'll post an updated patch.",
    "created_at": "2009-01-02T11:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37249",
    "user": "@mwhansen"
}
```

Good catch.  Just deleting the space should be enough.  ReST works with indentation levels.  I'll post an updated patch.



---

archive/issue_comments_037250.json:
```json
{
    "body": "Attachment [trac_4907-2.patch](tarball://root/attachments/some-uuid/ticket4907/trac_4907-2.patch) by @mwhansen created at 2009-01-02 20:20:50\n\nI've attached a patch which fixes this.",
    "created_at": "2009-01-02T20:20:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37250",
    "user": "@mwhansen"
}
```

Attachment [trac_4907-2.patch](tarball://root/attachments/some-uuid/ticket4907/trac_4907-2.patch) by @mwhansen created at 2009-01-02 20:20:50

I've attached a patch which fixes this.



---

archive/issue_comments_037251.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-24T18:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37251",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_037252.json:
```json
{
    "body": "Attachment [sage.crypto-final.patch](tarball://root/attachments/some-uuid/ticket4907/sage.crypto-final.patch) by mabshoff created at 2009-02-24 18:36:09\n\nMerged in Sage 3.4.alpha0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-24T18:36:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4907",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4907#issuecomment-37252",
    "user": "mabshoff"
}
```

Attachment [sage.crypto-final.patch](tarball://root/attachments/some-uuid/ticket4907/sage.crypto-final.patch) by mabshoff created at 2009-02-24 18:36:09

Merged in Sage 3.4.alpha0.

Cheers,

Michael
