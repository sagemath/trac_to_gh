# Issue 7670: notebook -- evidently only the first 6 characters are significant???

archive/issues_007670.json:
```json
{
    "body": "Assignee: @williamstein\n\n\n```\nHi,\n\nThere is a password issue with sage notebook account. Please read below:\n\nSameer\n\nOn Fri, Dec 11, 2009 at 1:22 PM, Sameer Regmi <> wrote:\n> On Fri, Dec 11, 2009 at 1:16 PM, Ondrej Certik <> wrote:\n>> On Fri, Dec 11, 2009 at 1:12 PM, Sameer <> wrote:\n>>> Hi I have found a weird issue with FEMhub online lab account. Let's\n>>> say my password is \"nevada\". Then whenever I enter any text (in\n>>> password field) with nevada as the prefix it will login. That means if\n>>> I enter nevada123 (or whatever as the suffix) it will\n>>> login.\n>>\n>> Seems like a bug in the Sage notebook. Could you please try to verify\n>> this against sagenb.org and if the problem is in there as well,\n>> could you please report it to the sage notebook list?\n>\n> Exactly! Its the bug in Sage notebook. The issue is there in sagenb.org too.\n> I even can login with \"nevad\" if the password is of nevada. I am\n> reporting to sage notebook list\n>\n> Sameer\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/7670\n\n",
    "created_at": "2009-12-12T00:22:38Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "notebook -- evidently only the first 6 characters are significant???",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7670",
    "user": "@williamstein"
}
```
Assignee: @williamstein


```
Hi,

There is a password issue with sage notebook account. Please read below:

Sameer

On Fri, Dec 11, 2009 at 1:22 PM, Sameer Regmi <> wrote:
> On Fri, Dec 11, 2009 at 1:16 PM, Ondrej Certik <> wrote:
>> On Fri, Dec 11, 2009 at 1:12 PM, Sameer <> wrote:
>>> Hi I have found a weird issue with FEMhub online lab account. Let's
>>> say my password is "nevada". Then whenever I enter any text (in
>>> password field) with nevada as the prefix it will login. That means if
>>> I enter nevada123 (or whatever as the suffix) it will
>>> login.
>>
>> Seems like a bug in the Sage notebook. Could you please try to verify
>> this against sagenb.org and if the problem is in there as well,
>> could you please report it to the sage notebook list?
>
> Exactly! Its the bug in Sage notebook. The issue is there in sagenb.org too.
> I even can login with "nevad" if the password is of nevada. I am
> reporting to sage notebook list
>
> Sameer
```


Issue created by migration from https://trac.sagemath.org/ticket/7670





---

archive/issue_comments_065742.json:
```json
{
    "body": "Could the problem be `sagenb.notebook.user.User`'s use of [crypt](http://docs.python.org/library/crypt.html):\n\n```python\n>>> import crypt\n>>> crypt.crypt('abcdefgh', 'aa')\n'aaHHlPHAM4sjs'\n>>> crypt.crypt('abcdefghi', 'aa')\n'aaHHlPHAM4sjs'\n```\n\n?",
    "created_at": "2009-12-12T17:02:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65742",
    "user": "@qed777"
}
```

Could the problem be `sagenb.notebook.user.User`'s use of [crypt](http://docs.python.org/library/crypt.html):

```python
>>> import crypt
>>> crypt.crypt('abcdefgh', 'aa')
'aaHHlPHAM4sjs'
>>> crypt.crypt('abcdefghi', 'aa')
'aaHHlPHAM4sjs'
```

?



---

archive/issue_comments_065743.json:
```json
{
    "body": "But [crypt](http://docs.python.org/library/crypt.html) supports whatever the OS's underlying [crypt(3)](http://www.kernel.org/doc/man-pages/online/pages/man3/crypt.3.html) supports.  We could instead do, e.g.,\n\n```python\nimport crypt as c, random as r\nsalt = repr(r.random())[2:]\n'77551456940940877'\nc.crypt('abcdefgh', '$6$' + salt + '$')\n'$6$7755145694094087$uW0RGjvJG3I.BDFKIAieUTPZkD4IGI6b8RtLt1fZ9czR0TefjriLwRGPItgPyZogDFsy.YorN24v2GM4YrBwK0'\nc.crypt('abcdefghi', '$6$' + salt + '$')\n'$6$7755145694094087$txEQuYAJlZ.042gqmPTeLSczXBv1sI6kSjzpbmU7o89rh.Tk7qUGHhLHtL1GIrVXmUdFrQBuIefktTTptuEq31'\n```\n\nIf Linux and Mac OS X, at least, both support SHA-512, I suggest we use it by default.  Should we generate each user's pseudo-random \"salt\" --- [used to avoid clustering](http://stackoverflow.com/questions/536584/non-random-salt-for-password-hashes) --- differently than above?",
    "created_at": "2009-12-12T19:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65743",
    "user": "@qed777"
}
```

But [crypt](http://docs.python.org/library/crypt.html) supports whatever the OS's underlying [crypt(3)](http://www.kernel.org/doc/man-pages/online/pages/man3/crypt.3.html) supports.  We could instead do, e.g.,

```python
import crypt as c, random as r
salt = repr(r.random())[2:]
'77551456940940877'
c.crypt('abcdefgh', '$6$' + salt + '$')
'$6$7755145694094087$uW0RGjvJG3I.BDFKIAieUTPZkD4IGI6b8RtLt1fZ9czR0TefjriLwRGPItgPyZogDFsy.YorN24v2GM4YrBwK0'
c.crypt('abcdefghi', '$6$' + salt + '$')
'$6$7755145694094087$txEQuYAJlZ.042gqmPTeLSczXBv1sI6kSjzpbmU7o89rh.Tk7qUGHhLHtL1GIrVXmUdFrQBuIefktTTptuEq31'
```

If Linux and Mac OS X, at least, both support SHA-512, I suggest we use it by default.  Should we generate each user's pseudo-random "salt" --- [used to avoid clustering](http://stackoverflow.com/questions/536584/non-random-salt-for-password-hashes) --- differently than above?



---

archive/issue_comments_065744.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2014-09-17T02:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65744",
    "user": "@kcrisman"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065745.json:
```json
{
    "body": "I cannot replicate this, and it is so old I am going to ask to close this.",
    "created_at": "2014-09-17T02:15:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65745",
    "user": "@kcrisman"
}
```

I cannot replicate this, and it is so old I am going to ask to close this.



---

archive/issue_comments_065746.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2014-09-17T02:15:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65746",
    "user": "@kcrisman"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065747.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2014-09-18T17:58:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7670",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7670#issuecomment-65747",
    "user": "@vbraun"
}
```

Resolution: invalid
