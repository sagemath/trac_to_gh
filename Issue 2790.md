# Issue 2790: very annoying output of new "sage -tp"

archive/issues_002790.json:
```json
{
    "body": "Assignee: failure\n\nThe new sage -tp has output like this:\n\n```\n\nThe following tests failed:\n\n\tsage -t  devel/sage-modabvar/sage/modular/modform/space.py: 8 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/modform/eisenstein_submodule.py: 1 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/modform/element.py: 1 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/abvar/morphism.py: 8 doctests failed\n\tsage -t  devel/sage-modabvar/sage/modular/abvar/homspace.py: 8 doctests failed\n----------------------------------------------------------------------\nTotal time for all tests: 1586.7 seconds\nteragon:sage was$ \n```\n\n\nThis is very annoying because I typically *paste* in the output in order to rerun broken doctests.\n\nEasy fix insert a #, i.e., change : x doctests failed to # : x doctests failed.\n\nIssue created by migration from https://trac.sagemath.org/ticket/2790\n\n",
    "created_at": "2008-04-03T04:19:57Z",
    "labels": [
        "doctest coverage",
        "major",
        "bug"
    ],
    "title": "very annoying output of new \"sage -tp\"",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2790",
    "user": "was"
}
```
Assignee: failure

The new sage -tp has output like this:

```

The following tests failed:

	sage -t  devel/sage-modabvar/sage/modular/modform/space.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/eisenstein_submodule.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/modform/element.py: 1 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/morphism.py: 8 doctests failed
	sage -t  devel/sage-modabvar/sage/modular/abvar/homspace.py: 8 doctests failed
----------------------------------------------------------------------
Total time for all tests: 1586.7 seconds
teragon:sage was$ 
```


This is very annoying because I typically *paste* in the output in order to rerun broken doctests.

Easy fix insert a #, i.e., change : x doctests failed to # : x doctests failed.

Issue created by migration from https://trac.sagemath.org/ticket/2790





---

archive/issue_comments_019164.json:
```json
{
    "body": "Patch coming up.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19164",
    "user": "mabshoff"
}
```

Patch coming up.

Cheers,

Michael



---

archive/issue_comments_019165.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19165",
    "user": "mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_019166.json:
```json
{
    "body": "Changing assignee from failure to mabshoff.",
    "created_at": "2008-04-03T14:52:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19166",
    "user": "mabshoff"
}
```

Changing assignee from failure to mabshoff.



---

archive/issue_comments_019167.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-04-03T15:09:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19167",
    "user": "mabshoff"
}
```

Attachment



---

archive/issue_comments_019168.json:
```json
{
    "body": "Patch looks good.",
    "created_at": "2008-04-03T15:29:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19168",
    "user": "dfdeshom"
}
```

Patch looks good.



---

archive/issue_comments_019169.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19169",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019170.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1",
    "created_at": "2008-04-03T15:35:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2790",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2790#issuecomment-19170",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.alpha1
