# Issue 2626: useless __list__ methods

archive/issues_002626.json:
```json
{
    "body": "Assignee: cwitty\n\nSage 2.10.4 contains 5 `__list__` methods, which are never called.  Apparently the authors of these methods thought that list(x) would call `x.__list__()`, but it does not; the Python source code contains no instance of the string \"`__list__`\".\n\nlist(x) does call `x.__iter__()`, which is how the doctests on these methods manage to work.\n\nThe methods should be removed, so as not to mislead future developers into thinking they do something.\n\n\n```\nsage: search_src('__list__')\n----------------------------------------------------------------------\n----------------------------------------------------------------------\ncrypto/mq/mpolynomialsystem.py:    def __list__(self):\ncrypto/mq/mpolynomialsystem.py:    def __list__(self):\ncrypto/mq/sbox.py:    def __list__(self):\nschemes/elliptic_curves/ell_point.py:    def __list__(self):\nschemes/generic/morphism.py:    def __list__(self):\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/2626\n\n",
    "created_at": "2008-03-21T02:28:51Z",
    "labels": [
        "component: misc",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-2.11",
    "title": "useless __list__ methods",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/2626",
    "user": "https://trac.sagemath.org/admin/accounts/users/cwitty"
}
```
Assignee: cwitty

Sage 2.10.4 contains 5 `__list__` methods, which are never called.  Apparently the authors of these methods thought that list(x) would call `x.__list__()`, but it does not; the Python source code contains no instance of the string "`__list__`".

list(x) does call `x.__iter__()`, which is how the doctests on these methods manage to work.

The methods should be removed, so as not to mislead future developers into thinking they do something.


```
sage: search_src('__list__')
----------------------------------------------------------------------
----------------------------------------------------------------------
crypto/mq/mpolynomialsystem.py:    def __list__(self):
crypto/mq/mpolynomialsystem.py:    def __list__(self):
crypto/mq/sbox.py:    def __list__(self):
schemes/elliptic_curves/ell_point.py:    def __list__(self):
schemes/generic/morphism.py:    def __list__(self):
```


Issue created by migration from https://trac.sagemath.org/ticket/2626





---

archive/issue_comments_018005.json:
```json
{
    "body": "fixes the issue for crypto.mq",
    "created_at": "2008-03-21T11:11:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18005",
    "user": "https://github.com/malb"
}
```

fixes the issue for crypto.mq



---

archive/issue_comments_018006.json:
```json
{
    "body": "Attachment [crypto_mq__list__.patch](tarball://root/attachments/some-uuid/ticket2626/crypto_mq__list__.patch) by @malb created at 2008-03-21 11:16:56\n\nfixes the issue for elliptic curve points over fields",
    "created_at": "2008-03-21T11:16:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18006",
    "user": "https://github.com/malb"
}
```

Attachment [crypto_mq__list__.patch](tarball://root/attachments/some-uuid/ticket2626/crypto_mq__list__.patch) by @malb created at 2008-03-21 11:16:56

fixes the issue for elliptic curve points over fields



---

archive/issue_comments_018007.json:
```json
{
    "body": "Attachment [morphism__list__.patch](tarball://root/attachments/some-uuid/ticket2626/morphism__list__.patch) by @malb created at 2008-03-21 11:19:05",
    "created_at": "2008-03-21T11:19:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18007",
    "user": "https://github.com/malb"
}
```

Attachment [morphism__list__.patch](tarball://root/attachments/some-uuid/ticket2626/morphism__list__.patch) by @malb created at 2008-03-21 11:19:05



---

archive/issue_comments_018008.json:
```json
{
    "body": "The attached patches remove all `__list__` instances mentioned above. I don't know how I got the idea that there is a special method called `__list__` in the first place. \n\nPS: I refuse to write a doctest for `SchemeMorphism_coordinates` because I don't even know how to construct such a thing! This class doesn't have a single line of documentation (though it is short to be fair).",
    "created_at": "2008-03-21T11:21:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18008",
    "user": "https://github.com/malb"
}
```

The attached patches remove all `__list__` instances mentioned above. I don't know how I got the idea that there is a special method called `__list__` in the first place. 

PS: I refuse to write a doctest for `SchemeMorphism_coordinates` because I don't even know how to construct such a thing! This class doesn't have a single line of documentation (though it is short to be fair).



---

archive/issue_comments_018009.json:
```json
{
    "body": "Nice patches, all the doctests pass [with known exception]. malb is correct in skipping doctests for `SchemeMorphism_coordinates` - hopefully somebody else will take care of that in a subsequent patch. Positive review.\n\nCheers,\n\nMichael",
    "created_at": "2008-03-22T09:47:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18009",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Nice patches, all the doctests pass [with known exception]. malb is correct in skipping doctests for `SchemeMorphism_coordinates` - hopefully somebody else will take care of that in a subsequent patch. Positive review.

Cheers,

Michael



---

archive/issue_comments_018010.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-03-22T09:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18010",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_018011.json:
```json
{
    "body": "Merged in Sage 2.11.alpha1",
    "created_at": "2008-03-22T09:48:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/2626#issuecomment-18011",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Merged in Sage 2.11.alpha1



---

archive/issue_events_002817.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mabshoff",
    "created_at": "2008-03-22T09:48:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/2626",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/2626#event-2817"
}
```
