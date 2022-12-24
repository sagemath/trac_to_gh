# Issue 2926: Minilistic change password page for notebook user

archive/issues_002926.json:
```json
{
    "body": "Assignee: TimothyClemans\n\n* Write resource \"passwd\" with inspiration from RegistrationPage\n* Add resource \"passwd\" to UserTopLevel\n* Add link to \"change password\" in the list entries in the function _html_body in notebook.py\n\nIssue created by migration from https://trac.sagemath.org/ticket/2926\n\n",
    "created_at": "2008-04-15T03:46:38Z",
    "labels": [
        "notebook",
        "major",
        "enhancement"
    ],
    "title": "Minilistic change password page for notebook user",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2926",
    "user": "TimothyClemans"
}
```
Assignee: TimothyClemans

* Write resource "passwd" with inspiration from RegistrationPage
* Add resource "passwd" to UserTopLevel
* Add link to "change password" in the list entries in the function _html_body in notebook.py

Issue created by migration from https://trac.sagemath.org/ticket/2926





---

archive/issue_comments_020143.json:
```json
{
    "body": "Attachment [2926.patch](tarball://root/attachments/some-uuid/ticket2926/2926.patch) by TimothyClemans created at 2008-04-15 18:39:35",
    "created_at": "2008-04-15T18:39:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20143",
    "user": "TimothyClemans"
}
```

Attachment [2926.patch](tarball://root/attachments/some-uuid/ticket2926/2926.patch) by TimothyClemans created at 2008-04-15 18:39:35



---

archive/issue_comments_020144.json:
```json
{
    "body": "This might be superseded by #2936, but if the functionality is not in there it can probably ported to the new codebase.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-16T01:16:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20144",
    "user": "mabshoff"
}
```

This might be superseded by #2936, but if the functionality is not in there it can probably ported to the new codebase.

Cheers,

Michael



---

archive/issue_comments_020145.json:
```json
{
    "body": "This just works.  There's no way for a user to actually use it short of explicitly typing\n/passwd in the URL.  But it does work correctly and the underlying code looks good.\n\nI wish it were somehow tested, but I don't know how to test it (yet).\n\nSo it's a preliminary and solid step to this functionality, so it should go in.  \n\nI don't think it overlaps with #2936 which is more backend stuff, whereas this is more UI oriented.",
    "created_at": "2008-05-11T08:49:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20145",
    "user": "was"
}
```

This just works.  There's no way for a user to actually use it short of explicitly typing
/passwd in the URL.  But it does work correctly and the underlying code looks good.

I wish it were somehow tested, but I don't know how to test it (yet).

So it's a preliminary and solid step to this functionality, so it should go in.  

I don't think it overlaps with #2936 which is more backend stuff, whereas this is more UI oriented.



---

archive/issue_comments_020146.json:
```json
{
    "body": "Merged in Sage 3.0.2.alpha0",
    "created_at": "2008-05-11T10:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20146",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.2.alpha0



---

archive/issue_comments_020147.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-05-11T10:47:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2926",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2926#issuecomment-20147",
    "user": "mabshoff"
}
```

Resolution: fixed
