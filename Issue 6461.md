# Issue 6461: Schaefer's Simplified Data Encryption Standard for educational purposes

archive/issues_006461.json:
```json
{
    "body": "Assignee: somebody\n\nCC:  malb\n\nKeywords: cryptography, DES, S-DES\n\nThis is a follow-up to #6164. The goal here is to implement the S-DES block cipher of Schaefer as described in the paper:\n\nE. Schaefer. A simplified data encryption algorithm. Cryptologia, 20(1):77--84, 1996.\n\nThis is a simplified variant of the Data Encryption Standard (DES) to be used for cryptography education.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6461\n\n",
    "created_at": "2009-07-04T09:44:37Z",
    "labels": [
        "cryptography",
        "major",
        "enhancement"
    ],
    "title": "Schaefer's Simplified Data Encryption Standard for educational purposes",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6461",
    "user": "mvngu"
}
```
Assignee: somebody

CC:  malb

Keywords: cryptography, DES, S-DES

This is a follow-up to #6164. The goal here is to implement the S-DES block cipher of Schaefer as described in the paper:

E. Schaefer. A simplified data encryption algorithm. Cryptologia, 20(1):77--84, 1996.

This is a simplified variant of the Data Encryption Standard (DES) to be used for cryptography education.

Issue created by migration from https://trac.sagemath.org/ticket/6461





---

archive/issue_comments_052217.json:
```json
{
    "body": "**Review**:\n\n* I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?\n* The code looks good and is nicely documented (coverage: 100%)\n* `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html\n*  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper\n* it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1\n* patch applies cleanly against 4.1.\n* reference manual builds without warnings and the result looks okay.\n* doctests pass on sage.math\n\nBottomline: positive review except some nitpicks.",
    "created_at": "2009-07-16T12:19:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52217",
    "user": "malb"
}
```

**Review**:

* I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?
* The code looks good and is nicely documented (coverage: 100%)
* `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html
*  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper
* it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1
* patch applies cleanly against 4.1.
* reference manual builds without warnings and the result looks okay.
* doctests pass on sage.math

Bottomline: positive review except some nitpicks.



---

archive/issue_comments_052218.json:
```json
{
    "body": "Replying to [comment:2 malb]:\n>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?\nUnfortunately, I don't have access to the original paper by Schaefer, and neither do my institution. I relied on the note at\n\nhttp://bitterroot.vancouver.wsu.edu/cs427_Spring09/docs/sdes.pdf\n\n\n\n\n>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html\nBefore switching to using `__cmp__()`, I used `==` for comparing objects. But then doing `a == loads(dumps(a))` consistently returned `False` for me. Let me try it again.\n\n\n\n>  *  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper\nAh... the notes I referenced above uses `IP` to denote the initial permutation and `IP^-1` for its inverse. Perhaps that is less confusing you think?\n\n\n\n>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1\nThat can be done.",
    "created_at": "2009-07-16T12:52:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52218",
    "user": "mvngu"
}
```

Replying to [comment:2 malb]:
>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?
Unfortunately, I don't have access to the original paper by Schaefer, and neither do my institution. I relied on the note at

http://bitterroot.vancouver.wsu.edu/cs427_Spring09/docs/sdes.pdf




>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html
Before switching to using `__cmp__()`, I used `==` for comparing objects. But then doing `a == loads(dumps(a))` consistently returned `False` for me. Let me try it again.



>  *  it is a bit confusing that P is often the plaintext (cf. C for ciphertext) and the permutation, but that might be a problem in the paper
Ah... the notes I referenced above uses `IP` to denote the initial permutation and `IP^-1` for its inverse. Perhaps that is less confusing you think?



>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1
That can be done.



---

archive/issue_comments_052219.json:
```json
{
    "body": "I just found this: http://buzzard.ups.edu/sdes/sdes.html :)",
    "created_at": "2009-07-16T13:18:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52219",
    "user": "malb"
}
```

I just found this: http://buzzard.ups.edu/sdes/sdes.html :)



---

archive/issue_comments_052220.json:
```json
{
    "body": "based on Sage 4.1.1.alpha0",
    "created_at": "2009-07-24T20:56:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52220",
    "user": "mvngu"
}
```

based on Sage 4.1.1.alpha0



---

archive/issue_comments_052221.json:
```json
{
    "body": "Attachment [trac_6461-sdes.patch](tarball://root/attachments/some-uuid/ticket6461/trac_6461-sdes.patch) by mvngu created at 2009-07-24 21:05:06\n\nReplying to [comment:2 malb]:\n>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?\n\nThere are no official test vectors for simplified DES. Even the original paper by Schaefer doesn't contain any such vectors.\n\n\n\n\n>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html\n\nThe latest patch `trac_6461-sdes.patch` now uses `__eq__()`. I have also modified the class `MiniAES` in `sage/crypto/block_cipher/miniaes.py` so it now also uses `__eq__()`.\n\n\n\n\n>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1\n\nDone.",
    "created_at": "2009-07-24T21:05:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52221",
    "user": "mvngu"
}
```

Attachment [trac_6461-sdes.patch](tarball://root/attachments/some-uuid/ticket6461/trac_6461-sdes.patch) by mvngu created at 2009-07-24 21:05:06

Replying to [comment:2 malb]:
>  * I assume that the specification implemented is correct, I didn't check against the paper, are there official test vectors?

There are no official test vectors for simplified DES. Even the original paper by Schaefer doesn't contain any such vectors.




>  * `__cmp__` expects you to return an integer (-1,0,1) and not `True` or `False`, cf. http://docs.python.org/reference/datamodel.html

The latest patch `trac_6461-sdes.patch` now uses `__eq__()`. I have also modified the class `MiniAES` in `sage/crypto/block_cipher/miniaes.py` so it now also uses `__eq__()`.




>  * it would be nice to have an `sbox(n)` function to return the S-Boxes 0 and 1

Done.



---

archive/issue_comments_052222.json:
```json
{
    "body": "Looks good to me, and Martin says it's ok if it fixes the nitpicks, which I think it does.",
    "created_at": "2009-07-27T15:32:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52222",
    "user": "was"
}
```

Looks good to me, and Martin says it's ok if it fixes the nitpicks, which I think it does.



---

archive/issue_comments_052223.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-08-23T14:01:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6461",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6461#issuecomment-52223",
    "user": "mvngu"
}
```

Resolution: fixed
