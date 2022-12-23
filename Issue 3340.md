# Issue 3340: update givaro to 3.2.10 release

archive/issues_003340.json:
```json
{
    "body": "Assignee: mabshoff\n\nWe're currently using the givaro 3.2.10rc3 release candidate; we should update to the actual release.  \n\nThe differences are somewhat substantial:\n\n[tabbott`@`debuild tmp$] diff -ur givaro-3.2.10/ ../givaro-3.2.10~rc3/ | diffstat\n<SNIP>\n 123 files changed, 883 insertions(+), 1413 deletions(-)\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3340\n\n",
    "created_at": "2008-05-30T17:40:22Z",
    "labels": [
        "packages: standard",
        "major",
        "enhancement"
    ],
    "title": "update givaro to 3.2.10 release",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3340",
    "user": "tabbott"
}
```
Assignee: mabshoff

We're currently using the givaro 3.2.10rc3 release candidate; we should update to the actual release.  

The differences are somewhat substantial:

[tabbott`@`debuild tmp$] diff -ur givaro-3.2.10/ ../givaro-3.2.10~rc3/ | diffstat
<SNIP>
 123 files changed, 883 insertions(+), 1413 deletions(-)


Issue created by migration from https://trac.sagemath.org/ticket/3340





---

archive/issue_comments_023195.json:
```json
{
    "body": "Clement Pernet's latest Givaro.spkg is at\n\nhttp://sage.math.washington.edu/home/pernet/givaro-3.2.11.spkg\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T03:25:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3340#issuecomment-23195",
    "user": "mabshoff"
}
```

Clement Pernet's latest Givaro.spkg is at

http://sage.math.washington.edu/home/pernet/givaro-3.2.11.spkg

Cheers,

Michael



---

archive/issue_comments_023196.json:
```json
{
    "body": "The spkg builds fine on OSX and x86-64 Linux and doctests fine. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-06-26T03:42:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3340#issuecomment-23196",
    "user": "mabshoff"
}
```

The spkg builds fine on OSX and x86-64 Linux and doctests fine. Positive review.

Cheers,

Michael



---

archive/issue_comments_023197.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-06-26T03:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3340#issuecomment-23197",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_023198.json:
```json
{
    "body": "Merged in Sage 3.0.4.alpha1",
    "created_at": "2008-06-26T03:42:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3340",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3340#issuecomment-23198",
    "user": "mabshoff"
}
```

Merged in Sage 3.0.4.alpha1
