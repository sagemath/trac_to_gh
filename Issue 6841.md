# Issue 6841: the shift cryptosystem

archive/issues_006841.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  @rbeezer\n\nImplement the shift cryptosystem for educational purposes. This adds to the classical cryptosystems already implemented.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6841\n\n",
    "created_at": "2009-08-29T08:55:28Z",
    "labels": [
        "component: cryptography"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "the shift cryptosystem",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6841",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```
Assignee: somebody

CC:  @rbeezer

Implement the shift cryptosystem for educational purposes. This adds to the classical cryptosystems already implemented.

Issue created by migration from https://trac.sagemath.org/ticket/6841





---

archive/issue_comments_056332.json:
```json
{
    "body": "The patch `trac_6841-shift-cipher.patch` implements the shift cryptosystem. It also adds some doctests and documentation to existing crypto modules.",
    "created_at": "2009-08-29T09:07:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56332",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch `trac_6841-shift-cipher.patch` implements the shift cryptosystem. It also adds some doctests and documentation to existing crypto modules.



---

archive/issue_comments_056333.json:
```json
{
    "body": "Here are some of rbeezer's comments on sanity checking the key value:\n\n```\n23:24 < mvngu-6971> rbeezer: Going back to shift cipher: The callable of \n                    ShiftCryptosystem (i.e. __call__) takes care of converting \n                    any value of key to 0 <= key < alphabet_size.\n23:24 < mvngu-6971> rbeezer: Perhaps I should make that clear in the \n                    documentation.\n23:27 < rbeezer> mvngu-6971: yes, I see it being Mod'ed, but I think you should \n                 disallow bad keys on input\n23:27 < rbeezer> S(29) for \"regular\" alphabet just churns along, I'd prefer an \n                 error\n23:27 < mvngu-6971> rbeezer: New patch coming up... in a hour or so. I'm still \n                    doing some release manage work...\n23:28 < mvngu-6971> rbeezer: Thank you *very* much for the valuable feedback!\n23:28 < rbeezer> For example with binary strings, my S(5) could have thrown an \n                 error, and I would have had to think about it right then, \n                 instead of looking for a positional shift of 5.  ;-)\n23:29 < rbeezer> mvngu-6971: no rush, probably be tomorrow night before I get \n                 to it\n23:29 < mvngu-6971> rbeezer: Cool.\n```\n",
    "created_at": "2009-09-23T06:31:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56333",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Here are some of rbeezer's comments on sanity checking the key value:

```
23:24 < mvngu-6971> rbeezer: Going back to shift cipher: The callable of 
                    ShiftCryptosystem (i.e. __call__) takes care of converting 
                    any value of key to 0 <= key < alphabet_size.
23:24 < mvngu-6971> rbeezer: Perhaps I should make that clear in the 
                    documentation.
23:27 < rbeezer> mvngu-6971: yes, I see it being Mod'ed, but I think you should 
                 disallow bad keys on input
23:27 < rbeezer> S(29) for "regular" alphabet just churns along, I'd prefer an 
                 error
23:27 < mvngu-6971> rbeezer: New patch coming up... in a hour or so. I'm still 
                    doing some release manage work...
23:28 < mvngu-6971> rbeezer: Thank you *very* much for the valuable feedback!
23:28 < rbeezer> For example with binary strings, my S(5) could have thrown an 
                 error, and I would have had to think about it right then, 
                 instead of looking for a positional shift of 5.  ;-)
23:29 < rbeezer> mvngu-6971: no rush, probably be tomorrow night before I get 
                 to it
23:29 < mvngu-6971> rbeezer: Cool.
```




---

archive/issue_comments_056334.json:
```json
{
    "body": "based on Sage 4.1.2.alpha2",
    "created_at": "2009-09-24T03:19:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56334",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

based on Sage 4.1.2.alpha2



---

archive/issue_comments_056335.json:
```json
{
    "body": "Attachment [trac_6841-shift-cipher.patch](tarball://root/attachments/some-uuid/ticket6841/trac_6841-shift-cipher.patch) by mvngu created at 2009-09-24 03:26:33\n\nThe updated patch addresses rbeezer's comments on sanity checking the value of the encryption/decryption key. The sanity checking is done in the callable `__call__()` of the class `ShiftCryptosystem`. I have added doctests to that callable. Currently, methods beginning with an underscore \"`_`\" don't show up in the reference manual, so I have also added the doctests for checking key value to the docstring for the class `ShiftCryptosystem`. In this way, reading the reference manual for the shift cryptosystem should make it clear (hopefully) that the value of an encryption/decryption key must lie within the range of acceptable values, i.e. must be within the key space.",
    "created_at": "2009-09-24T03:26:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56335",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6841-shift-cipher.patch](tarball://root/attachments/some-uuid/ticket6841/trac_6841-shift-cipher.patch) by mvngu created at 2009-09-24 03:26:33

The updated patch addresses rbeezer's comments on sanity checking the value of the encryption/decryption key. The sanity checking is done in the callable `__call__()` of the class `ShiftCryptosystem`. I have added doctests to that callable. Currently, methods beginning with an underscore "`_`" don't show up in the reference manual, so I have also added the doctests for checking key value to the docstring for the class `ShiftCryptosystem`. In this way, reading the reference manual for the shift cryptosystem should make it clear (hopefully) that the value of an encryption/decryption key must lie within the range of acceptable values, i.e. must be within the key space.



---

archive/issue_comments_056336.json:
```json
{
    "body": "Builds and runs on 4.1.2.alpha2.  Passes tests, docs build without warnings.  Great documentation.\n\nWould you want to put similar input protections on `inverse_key()`?  Your call.\n\nPositive review, either way.",
    "created_at": "2009-09-25T05:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56336",
    "user": "https://github.com/rbeezer"
}
```

Builds and runs on 4.1.2.alpha2.  Passes tests, docs build without warnings.  Great documentation.

Would you want to put similar input protections on `inverse_key()`?  Your call.

Positive review, either way.



---

archive/issue_comments_056337.json:
```json
{
    "body": "Replying to [comment:7 rbeezer]:\n> Would you want to put similar input protections on `inverse_key()`?  Your call.\nYes, I like your idea: be consistent. Please see ticket #7010 for sanity checking the value of the inverse key.",
    "created_at": "2009-09-25T07:16:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56337",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:7 rbeezer]:
> Would you want to put similar input protections on `inverse_key()`?  Your call.
Yes, I like your idea: be consistent. Please see ticket #7010 for sanity checking the value of the inverse key.



---

archive/issue_comments_056338.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-25T08:12:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56338",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_events_016106.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-25T08:12:46Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6841#event-16106"
}
```



---

archive/issue_comments_056339.json:
```json
{
    "body": "There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.",
    "created_at": "2009-09-27T10:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6841",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6841#issuecomment-56339",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

There is no 4.1.2.alpha3. Sage 4.1.2.alpha3 was William Stein's release for working on making the notebook a standalone package.
