# Issue 5665: Bug in ShrinkingGeneratorCipher

archive/issues_005665.json:
```json
{
    "body": "Assignee: kohel\n\nKeywords: stream cipher, shrinking generator\n\nIn class ShrinkingGeneratorCipher, function `__call__` the initialization and update of the initial states is buggy. Namely in the peace of code\n\n```\ng1 = e1.connection_polynomial()\nn1 = g1.degree()\nIS_1 = e1.initial_state()\ng2 = e2.connection_polynomial()\nn2 = g2.degree()\nIS_2 = e1.initial_state()\n```\n\nthe last line 'IS_2 = e1.initial_state()' should be 'IS_2 = e2.initial_state()'. \nAlso at the end in\n\n```\n  IS_1 = KStream[r-n-1:r-n+n1]\n  IS_2 = KStream[r-n-1:r-n+n2]\n```\n\nthe last line should be 'IS_2 = DStream[r-n-1:r-n+n2]'\nThe corrected file is attached.\n\nIssue created by migration from https://trac.sagemath.org/ticket/5665\n\n",
    "created_at": "2009-04-02T07:54:42Z",
    "labels": [
        "cryptography",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1",
    "title": "Bug in ShrinkingGeneratorCipher",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5665",
    "user": "sbulygin"
}
```
Assignee: kohel

Keywords: stream cipher, shrinking generator

In class ShrinkingGeneratorCipher, function `__call__` the initialization and update of the initial states is buggy. Namely in the peace of code

```
g1 = e1.connection_polynomial()
n1 = g1.degree()
IS_1 = e1.initial_state()
g2 = e2.connection_polynomial()
n2 = g2.degree()
IS_2 = e1.initial_state()
```

the last line 'IS_2 = e1.initial_state()' should be 'IS_2 = e2.initial_state()'. 
Also at the end in

```
  IS_1 = KStream[r-n-1:r-n+n1]
  IS_2 = KStream[r-n-1:r-n+n2]
```

the last line should be 'IS_2 = DStream[r-n-1:r-n+n2]'
The corrected file is attached.

Issue created by migration from https://trac.sagemath.org/ticket/5665





---

archive/issue_comments_044319.json:
```json
{
    "body": "bugs in initialization and update of initial state are fixed",
    "created_at": "2009-04-02T07:55:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44319",
    "user": "sbulygin"
}
```

bugs in initialization and update of initial state are fixed



---

archive/issue_comments_044320.json:
```json
{
    "body": "Attachment [stream_cipher.py](tarball://root/attachments/some-uuid/ticket5665/stream_cipher.py) by mabshoff created at 2009-04-23 08:06:02",
    "created_at": "2009-04-23T08:06:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44320",
    "user": "mabshoff"
}
```

Attachment [stream_cipher.py](tarball://root/attachments/some-uuid/ticket5665/stream_cipher.py) by mabshoff created at 2009-04-23 08:06:02



---

archive/issue_comments_044321.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-04-23T09:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44321",
    "user": "kohel"
}
```

Resolution: fixed



---

archive/issue_comments_044322.json:
```json
{
    "body": "The two changes are necessary and correct.",
    "created_at": "2009-04-23T09:17:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44322",
    "user": "kohel"
}
```

The two changes are necessary and correct.



---

archive/issue_comments_044323.json:
```json
{
    "body": "Thanks for the review David, but tickets only get closed once a patch has actually been merged :).\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T09:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44323",
    "user": "mabshoff"
}
```

Thanks for the review David, but tickets only get closed once a patch has actually been merged :).

Cheers,

Michael



---

archive/issue_comments_044324.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2009-04-23T09:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44324",
    "user": "mabshoff"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_044325.json:
```json
{
    "body": "Changing status from closed to reopened.",
    "created_at": "2009-04-23T09:33:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44325",
    "user": "mabshoff"
}
```

Changing status from closed to reopened.



---

archive/issue_comments_044326.json:
```json
{
    "body": "On top of this someone needs to make a proper patch out of this and check in the changes in sbulygin's name. One would also need to check if doctests have been added since that is unclear to me without taking a closer look and comparing to the file that is in 3.4.1.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T09:34:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44326",
    "user": "mabshoff"
}
```

On top of this someone needs to make a proper patch out of this and check in the changes in sbulygin's name. One would also need to check if doctests have been added since that is unclear to me without taking a closer look and comparing to the file that is in 3.4.1.

Cheers,

Michael



---

archive/issue_comments_044327.json:
```json
{
    "body": "Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. \n\nCreating a patch seems overkill, since only two characters have changed (1->2 and K->D).  \n\nHowever, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. \n\nCheers,\n\nDavid",
    "created_at": "2009-04-23T10:34:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44327",
    "user": "kohel"
}
```

Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. 

Creating a patch seems overkill, since only two characters have changed (1->2 and K->D).  

However, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. 

Cheers,

David



---

archive/issue_comments_044328.json:
```json
{
    "body": "Replying to [comment:6 kohel]:\n> Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. \n\nWell, a fixed ticket no longer appears on the default view and just because someone does give a ticket a positive review does not mean it will be merged since any doctest failure will bounce the ticket right back. Closing tickets once a patch has been merged is the only sane way to keep track of which fix was merged in Sage.\n\n> Creating a patch seems overkill, since only two characters have changed (1->2 and K->D).  \n\nNo, creating a patch is essential for credit, etc. \n\n> However, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. \n\nIt is essential to run doctests and to add additional doctests in case the problem was not previously covered by a doctest. This does not seem to be the case here, but I will find out in the morning.\n\n> Cheers,\n> \n> David\n\nCheers,\n\nMichael",
    "created_at": "2009-04-23T10:40:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44328",
    "user": "mabshoff"
}
```

Replying to [comment:6 kohel]:
> Maybe I shouldn't have clicked on 'fixed' (although the two changes fix the problem). This indeed told me that the ticket would then be set to closed. 

Well, a fixed ticket no longer appears on the default view and just because someone does give a ticket a positive review does not mean it will be merged since any doctest failure will bounce the ticket right back. Closing tickets once a patch has been merged is the only sane way to keep track of which fix was merged in Sage.

> Creating a patch seems overkill, since only two characters have changed (1->2 and K->D).  

No, creating a patch is essential for credit, etc. 

> However, you are correct about the doctests; it looks like the ciphertext in line 229 will have to be substituted with the new output. 

It is essential to run doctests and to add additional doctests in case the problem was not previously covered by a doctest. This does not seem to be the case here, but I will find out in the morning.

> Cheers,
> 
> David

Cheers,

Michael



---

archive/issue_comments_044329.json:
```json
{
    "body": "This ticket needs at least a doctest fix:\n\n```\nsage -t -long \"devel/sage/sage/crypto/stream_cipher.py\"     \n**********************************************************************\nFile \"/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/crypto/stream_cipher.py\", line 228:\n    sage: c.decoding()\nExpected:\n    '\\xac\\xfa\\xfd\\xc6\\xa7\\xe5\\x16\\x8f\\xa2Q\\xb8\\xb7\\xbe\\xab'\nGot:\n    \"t\\xb6\\xc1'\\x83\\x17\\xae\\xc9ZO\\x84V\\x7fX\"\n**********************************************************************\n1 items had failures:\n   1 of  17 in __main__.example_8\n```\n\n\nIt would also be nice if someone posted a patch giving credit to Stanislav.\n\nCheers,\n\nMichael",
    "created_at": "2009-04-24T02:52:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44329",
    "user": "mabshoff"
}
```

This ticket needs at least a doctest fix:

```
sage -t -long "devel/sage/sage/crypto/stream_cipher.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.4.2.alpha0/devel/sage/sage/crypto/stream_cipher.py", line 228:
    sage: c.decoding()
Expected:
    '\xac\xfa\xfd\xc6\xa7\xe5\x16\x8f\xa2Q\xb8\xb7\xbe\xab'
Got:
    "t\xb6\xc1'\x83\x17\xae\xc9ZO\x84V\x7fX"
**********************************************************************
1 items had failures:
   1 of  17 in __main__.example_8
```


It would also be nice if someone posted a patch giving credit to Stanislav.

Cheers,

Michael



---

archive/issue_comments_044330.json:
```json
{
    "body": "Attachment [trac_5665.patch](tarball://root/attachments/some-uuid/ticket5665/trac_5665.patch) by mvngu created at 2009-06-26 04:35:29\n\nbased on Sage 4.1.alpha1",
    "created_at": "2009-06-26T04:35:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44330",
    "user": "mvngu"
}
```

Attachment [trac_5665.patch](tarball://root/attachments/some-uuid/ticket5665/trac_5665.patch) by mvngu created at 2009-06-26 04:35:29

based on Sage 4.1.alpha1



---

archive/issue_comments_044331.json:
```json
{
    "body": "Only apply `trac_5665.patch`.",
    "created_at": "2009-06-26T04:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44331",
    "user": "mvngu"
}
```

Only apply `trac_5665.patch`.



---

archive/issue_comments_044332.json:
```json
{
    "body": "Note: the patch `trac_5665.patch` is due to Stanislav Bulygin. I produced the patch file from the Python file.",
    "created_at": "2009-06-26T21:42:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44332",
    "user": "mvngu"
}
```

Note: the patch `trac_5665.patch` is due to Stanislav Bulygin. I produced the patch file from the Python file.



---

archive/issue_comments_044333.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-07-04T01:31:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5665",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5665#issuecomment-44333",
    "user": "@rlmill"
}
```

Resolution: fixed
