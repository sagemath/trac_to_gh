# Issue 1290: [with patch] add computationg of Rencontres numbers to Sage

archive/issues_001290.json:
```json
{
    "body": "Assignee: mhansen\n\nCC:  sage-combinat\n\nDan Drake posted this on sage-devel, and I reformatted it into a proper patch.\n\nI rewrote the patch to avoid using any symbolic computation (e.g., maxima) for speed and to be correct when the input/output is very large. \n\nIssue created by migration from https://trac.sagemath.org/ticket/1290\n\n",
    "created_at": "2007-11-27T14:43:43Z",
    "labels": [
        "combinatorics",
        "major",
        "enhancement"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.8.15",
    "title": "[with patch] add computationg of Rencontres numbers to Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/1290",
    "user": "was"
}
```
Assignee: mhansen

CC:  sage-combinat

Dan Drake posted this on sage-devel, and I reformatted it into a proper patch.

I rewrote the patch to avoid using any symbolic computation (e.g., maxima) for speed and to be correct when the input/output is very large. 

Issue created by migration from https://trac.sagemath.org/ticket/1290





---

archive/issue_comments_008102.json:
```json
{
    "body": "Attachment [trac1290.patch](tarball://root/attachments/some-uuid/ticket1290/trac1290.patch) by jsp created at 2007-11-27 20:49:26\n\nSee my alternative on the mailing list sage-devel: derangements = rencontres\n\n\n```\ndef derangements(n, k):\n     if n == 0 and k == 0:\n         return 1\n     if n == 1 and k == 0:\n         return 0\n\n     if k == 0:\n         lst = [(-1)^r * binomial(n, r) * (n-r)^r * (n-r-1)^(n-r) for r in range(n)]\n         return sum(lst)\n     else:\n         return binomial(n, k) * derangements(n-k, 0)\n```\n\n\nSomeone should check the implications!?\nEventually translate it into Cython, etcetera.",
    "created_at": "2007-11-27T20:49:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1290#issuecomment-8102",
    "user": "jsp"
}
```

Attachment [trac1290.patch](tarball://root/attachments/some-uuid/ticket1290/trac1290.patch) by jsp created at 2007-11-27 20:49:26

See my alternative on the mailing list sage-devel: derangements = rencontres


```
def derangements(n, k):
     if n == 0 and k == 0:
         return 1
     if n == 1 and k == 0:
         return 0

     if k == 0:
         lst = [(-1)^r * binomial(n, r) * (n-r)^r * (n-r-1)^(n-r) for r in range(n)]
         return sum(lst)
     else:
         return binomial(n, k) * derangements(n-k, 0)
```


Someone should check the implications!?
Eventually translate it into Cython, etcetera.



---

archive/issue_comments_008103.json:
```json
{
    "body": "Looks good to me.",
    "created_at": "2007-12-02T05:02:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1290#issuecomment-8103",
    "user": "mhansen"
}
```

Looks good to me.



---

archive/issue_comments_008104.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-12-02T05:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1290#issuecomment-8104",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_008105.json:
```json
{
    "body": "Merged in 2.8.15.alpha2.",
    "created_at": "2007-12-02T05:56:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/1290",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/1290#issuecomment-8105",
    "user": "mabshoff"
}
```

Merged in 2.8.15.alpha2.
