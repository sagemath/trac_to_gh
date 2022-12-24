# Issue 9730: A simple RC4 cipher implementation for Sage

archive/issues_009730.json:
```json
{
    "body": "Assignee: mvngu\n\nKeywords: RC4, Cryptosystem, Cipher\n\nThis is a standard RC4 implementation in the Cryptography directory for Sage. We do not consider advanced criteria to initialize the state bytearray, and hence this system may be prone to attacks (refer to relevant literature).\n\nThough this is not fully secure (upto industry standard), this is a full-version implementation of the cipher, and can be used for educational purpose as well as for small-scale encryptions.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9730\n\n",
    "created_at": "2010-08-11T21:55:35Z",
    "labels": [
        "cryptography",
        "minor",
        "enhancement"
    ],
    "title": "A simple RC4 cipher implementation for Sage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9730",
    "user": "sg.sourav"
}
```
Assignee: mvngu

Keywords: RC4, Cryptosystem, Cipher

This is a standard RC4 implementation in the Cryptography directory for Sage. We do not consider advanced criteria to initialize the state bytearray, and hence this system may be prone to attacks (refer to relevant literature).

Though this is not fully secure (upto industry standard), this is a full-version implementation of the cipher, and can be used for educational purpose as well as for small-scale encryptions.

Issue created by migration from https://trac.sagemath.org/ticket/9730





---

archive/issue_comments_095099.json:
```json
{
    "body": "A patch to incorporate an implementation of RC4 in Sage",
    "created_at": "2010-08-11T21:56:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95099",
    "user": "sg.sourav"
}
```

A patch to incorporate an implementation of RC4 in Sage



---

archive/issue_comments_095100.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-08-12T19:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95100",
    "user": "sg.sourav"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_095101.json:
```json
{
    "body": "Attachment [rc4.patch](tarball://root/attachments/some-uuid/ticket9730/rc4.patch) by sg.sourav created at 2010-08-12 19:12:08",
    "created_at": "2010-08-12T19:12:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95101",
    "user": "sg.sourav"
}
```

Attachment [rc4.patch](tarball://root/attachments/some-uuid/ticket9730/rc4.patch) by sg.sourav created at 2010-08-12 19:12:08



---

archive/issue_comments_095102.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-08-14T12:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95102",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_095103.json:
```json
{
    "body": "Running doctests over `rc4.py` fails with message:\n\n```sh\n[mvngu@sage sage-4.5.3.alpha0]$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py \nsage -t -long \"devel/sage-main/sage/crypto/rc4.py\"          \n**********************************************************************\nError: TAB character found.\n\n\t [1.9 s]\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t -long \"devel/sage-main/sage/crypto/rc4.py\"\nTotal time for all tests: 1.9 seconds\n```\n\nThis patch needs a lot of work.",
    "created_at": "2010-08-14T12:08:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95103",
    "user": "mvngu"
}
```

Running doctests over `rc4.py` fails with message:

```sh
[mvngu@sage sage-4.5.3.alpha0]$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py 
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
**********************************************************************
Error: TAB character found.

	 [1.9 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-main/sage/crypto/rc4.py"
Total time for all tests: 1.9 seconds
```

This patch needs a lot of work.



---

archive/issue_comments_095104.json:
```json
{
    "body": "Attaching a modified patch which passed all doctests successfully. Also added some sanity checks for types of inputs. \n\nApply rc4_mod1.patch directly (not over rc4.patch).\n\n\n\n```\nsourav@ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py\nsage -t -long \"devel/sage-main/sage/crypto/rc4.py\"          \n\t [6.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 6.7 seconds\nsourav@ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py\nsage -t -long \"devel/sage-main/sage/crypto/rc4.py\"          \n\t [6.7 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 6.7 seconds\n```\n",
    "created_at": "2010-08-16T08:22:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95104",
    "user": "sg.sourav"
}
```

Attaching a modified patch which passed all doctests successfully. Also added some sanity checks for types of inputs. 

Apply rc4_mod1.patch directly (not over rc4.patch).



```
sourav@ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
	 [6.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.7 seconds
sourav@ssg:~/sage4.5$ ./sage -t -long devel/sage-main/sage/crypto/rc4.py
sage -t -long "devel/sage-main/sage/crypto/rc4.py"          
	 [6.7 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 6.7 seconds
```




---

archive/issue_comments_095105.json:
```json
{
    "body": "Modified version of rc4.patch including sanity checks (passed doctests)",
    "created_at": "2010-08-16T08:23:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95105",
    "user": "sg.sourav"
}
```

Modified version of rc4.patch including sanity checks (passed doctests)



---

archive/issue_comments_095106.json:
```json
{
    "body": "Attachment [rc4_mod1.patch](tarball://root/attachments/some-uuid/ticket9730/rc4_mod1.patch) by @fchapoton created at 2013-08-22 17:17:55\n\napply rc4_mod1.patch",
    "created_at": "2013-08-22T17:17:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95106",
    "user": "@fchapoton"
}
```

Attachment [rc4_mod1.patch](tarball://root/attachments/some-uuid/ticket9730/rc4_mod1.patch) by @fchapoton created at 2013-08-22 17:17:55

apply rc4_mod1.patch



---

archive/issue_comments_095107.json:
```json
{
    "body": "apply only rc4_mod1.patch",
    "created_at": "2013-08-22T17:20:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95107",
    "user": "@fchapoton"
}
```

apply only rc4_mod1.patch



---

archive/issue_comments_095108.json:
```json
{
    "body": "Attachment [trac_9730_addon.patch](tarball://root/attachments/some-uuid/ticket9730/trac_9730_addon.patch) by @fchapoton created at 2013-08-22 17:31:12",
    "created_at": "2013-08-22T17:31:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95108",
    "user": "@fchapoton"
}
```

Attachment [trac_9730_addon.patch](tarball://root/attachments/some-uuid/ticket9730/trac_9730_addon.patch) by @fchapoton created at 2013-08-22 17:31:12



---

archive/issue_comments_095109.json:
```json
{
    "body": "New commits:",
    "created_at": "2014-01-06T20:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9730",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9730#issuecomment-95109",
    "user": "@fchapoton"
}
```

New commits:
