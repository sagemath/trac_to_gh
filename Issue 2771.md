# Issue 2771: [with patch, needs review] PolyBoRi doctest coverage at 54%

archive/issues_002771.json:
```json
{
    "body": "Assignee: @malb\n\nCC:  @burcin\n\nKeywords: coverage, polybori\n\n... working towards 100% :-)\n\nIssue created by migration from https://trac.sagemath.org/ticket/2771\n\n",
    "created_at": "2008-04-02T13:41:42Z",
    "labels": [
        "component: documentation"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "[with patch, needs review] PolyBoRi doctest coverage at 54%",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2771",
    "user": "https://github.com/malb"
}
```
Assignee: @malb

CC:  @burcin

Keywords: coverage, polybori

... working towards 100% :-)

Issue created by migration from https://trac.sagemath.org/ticket/2771





---

archive/issue_comments_019006.json:
```json
{
    "body": "Attachment [pbori_54.patch](tarball://root/attachments/some-uuid/ticket2771/pbori_54.patch) by @malb created at 2008-04-02 13:41:53",
    "created_at": "2008-04-02T13:41:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19006",
    "user": "https://github.com/malb"
}
```

Attachment [pbori_54.patch](tarball://root/attachments/some-uuid/ticket2771/pbori_54.patch) by @malb created at 2008-04-02 13:41:53



---

archive/issue_comments_019007.json:
```json
{
    "body": "Hi malb,\n\nI skimmed the code, so no final review yet. But I noticed that you use\n\n```\nsage: from polybori import BooleSet \n```\n\nfor imports. This will cause trouble once  #2746, i.e. \"Support for writing test-related files in SAGE_TESTDIR\", is applied. \n\nCheers,\n\nMichael",
    "created_at": "2008-04-02T15:18:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19007",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Hi malb,

I skimmed the code, so no final review yet. But I noticed that you use

```
sage: from polybori import BooleSet 
```

for imports. This will cause trouble once  #2746, i.e. "Support for writing test-related files in SAGE_TESTDIR", is applied. 

Cheers,

Michael



---

archive/issue_comments_019008.json:
```json
{
    "body": "Replying to [comment:1 mabshoff]:\n> Hi malb,\n> \n> I skimmed the code, so no final review yet. But I noticed that you use\n> {{{\n> sage: from polybori import BooleSet \n> }}}\n> for imports. This will cause trouble once  #2746, i.e. \"Support for writing test-related files in SAGE_TESTDIR\", is applied. \n\nIt won't. There is `sage.rings.polynomial.pbori` and there is `polybori`. `polybori` is indeed at the global top-level.\n\n\n```\nmalb@XXX:~$ sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nLoading SAGE library. Current Mercurial branch is: polybori\nsage: from polybori import *\nsage:\n```\n",
    "created_at": "2008-04-02T15:27:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19008",
    "user": "https://github.com/malb"
}
```

Replying to [comment:1 mabshoff]:
> Hi malb,
> 
> I skimmed the code, so no final review yet. But I noticed that you use
> {{{
> sage: from polybori import BooleSet 
> }}}
> for imports. This will cause trouble once  #2746, i.e. "Support for writing test-related files in SAGE_TESTDIR", is applied. 

It won't. There is `sage.rings.polynomial.pbori` and there is `polybori`. `polybori` is indeed at the global top-level.


```
malb@XXX:~$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading SAGE library. Current Mercurial branch is: polybori
sage: from polybori import *
sage:
```




---

archive/issue_comments_019009.json:
```json
{
    "body": "I found two small issues:\n\n* One time you use \"Gr\u00f6bner\" while in all other places you use Groebner\n* I would use a verb for \"The opposite of navigation down a ZDD using navigators is to\" \n\nCheers,\n\nMichael",
    "created_at": "2008-04-03T20:29:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

I found two small issues:

* One time you use "Gröbner" while in all other places you use Groebner
* I would use a verb for "The opposite of navigation down a ZDD using navigators is to" 

Cheers,

Michael



---

archive/issue_comments_019010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-03T21:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_019011.json:
```json
{
    "body": "Merged in Sage 3.0.alpha1 with the two above mentioned minimal changes.",
    "created_at": "2008-04-03T21:14:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2771",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2771#issuecomment-19011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 3.0.alpha1 with the two above mentioned minimal changes.
