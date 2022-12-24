# Issue 3777: notebook -- issue parsing out <script> tags

archive/issues_003777.json:
```json
{
    "body": "Assignee: boothby\n\nThis input to the notebook results in pain:\n\n\n```\nhtml('<script>alert(\"</script>\");</script>')\n```\n\n\nThis should only be looked at after #3735 is applied.  Then look at this code in \ncell.py\n\n```\n        if ncols == 0:\n            while True:\n                i = t.lower().find('<script>')\n                if i == -1: break\n                j = t[i:].lower().find('</script>')\n                if j == -1: break\n                t = t[:i] + t[i+j+len('</script>'):]\n                \n```\n\nand also `function eval_script_tags(text)` in js.py.\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3777\n\n",
    "created_at": "2008-08-05T21:30:45Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.1",
    "title": "notebook -- issue parsing out <script> tags",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3777",
    "user": "was"
}
```
Assignee: boothby

This input to the notebook results in pain:


```
html('<script>alert("</script>");</script>')
```


This should only be looked at after #3735 is applied.  Then look at this code in 
cell.py

```
        if ncols == 0:
            while True:
                i = t.lower().find('<script>')
                if i == -1: break
                j = t[i:].lower().find('</script>')
                if j == -1: break
                t = t[:i] + t[i+j+len('</script>'):]
                
```

and also `function eval_script_tags(text)` in js.py.


Issue created by migration from https://trac.sagemath.org/ticket/3777





---

archive/issue_comments_026859.json:
```json
{
    "body": "Changing priority from major to minor.",
    "created_at": "2008-08-05T21:30:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26859",
    "user": "was"
}
```

Changing priority from major to minor.



---

archive/issue_comments_026860.json:
```json
{
    "body": "It looks like the problem here is that we don't have a full HTML/Javascript parser built in to cell.py?",
    "created_at": "2009-01-21T07:43:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26860",
    "user": "jason"
}
```

It looks like the problem here is that we don't have a full HTML/Javascript parser built in to cell.py?



---

archive/issue_comments_026861.json:
```json
{
    "body": "Attachment [foo.html](tarball://root/attachments/some-uuid/ticket3777/foo.html) by timdumol created at 2010-01-19 06:51:42\n\nSample failure of </script> tags.",
    "created_at": "2010-01-19T06:51:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26861",
    "user": "timdumol"
}
```

Attachment [foo.html](tarball://root/attachments/some-uuid/ticket3777/foo.html) by timdumol created at 2010-01-19 06:51:42

Sample failure of </script> tags.



---

archive/issue_comments_026862.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-01-19T06:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26862",
    "user": "acleone"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_026863.json:
```json
{
    "body": "Apparently this is invalid javascript.\n\nfoo.html shows that firefox gives the same behavior.",
    "created_at": "2010-01-19T06:56:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26863",
    "user": "acleone"
}
```

Apparently this is invalid javascript.

foo.html shows that firefox gives the same behavior.



---

archive/issue_comments_026864.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2010-01-19T06:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3777",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3777#issuecomment-26864",
    "user": "acleone"
}
```

Resolution: invalid
