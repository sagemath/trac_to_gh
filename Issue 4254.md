# Issue 4254: [with patch, needs review] better parameter parsing for mq.SR

archive/issues_004254.json:
```json
{
    "body": "Assignee: malb\n\n`correct_only` is only valid for GF(2). Make sure it is passed on correctly.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4254\n\n",
    "created_at": "2008-10-08T14:18:45Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "[with patch, needs review] better parameter parsing for mq.SR",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4254",
    "user": "malb"
}
```
Assignee: malb

`correct_only` is only valid for GF(2). Make sure it is passed on correctly.

Issue created by migration from https://trac.sagemath.org/ticket/4254





---

archive/issue_comments_030941.json:
```json
{
    "body": "This patch should probably have some doctests.",
    "created_at": "2008-11-23T15:40:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30941",
    "user": "cwitty"
}
```

This patch should probably have some doctests.



---

archive/issue_comments_030942.json:
```json
{
    "body": "apply before other patch",
    "created_at": "2008-11-23T22:25:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30942",
    "user": "malb"
}
```

apply before other patch



---

archive/issue_comments_030943.json:
```json
{
    "body": "Attachment\n\nadded doctests",
    "created_at": "2008-11-23T22:25:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30943",
    "user": "malb"
}
```

Attachment

added doctests



---

archive/issue_comments_030944.json:
```json
{
    "body": "Attachment\n\nI added doctests and the patch this patch depends on which I forgot to submit last time.",
    "created_at": "2008-11-23T22:26:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30944",
    "user": "malb"
}
```

Attachment

I added doctests and the patch this patch depends on which I forgot to submit last time.



---

archive/issue_comments_030945.json:
```json
{
    "body": "REFEREE REPORT:\nI tried to figure out how to apply the above patches in their confusing order, but I guess I failed or something. See below (last patch fails to apply).  Please clarify, and I'll referee this:\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage\n----------------------------------------------------------------------\n----------------------------------------------------------------------\nhgsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/15295/tmp_0.patch\"\napplying /home/was/.sage/temp/sage/15295/tmp_0.patch\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/15295/tmp_1.patch\"\napplying /home/was/.sage/temp/sage/15295/tmp_1.patch\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/15295/tmp_2.patch\"\napplying /home/was/.sage/temp/sage/15295/tmp_2.patch\npatching file sage/crypto/mq/sr.py\nHunk #2 FAILED at 288\n1 out of 2 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej\nabort: patch failed to apply\n```\n\n| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |\n| Type notebook() for the GUI, and license() for information.        |\nand \n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ more devel/sage/sage/crypto/mq/sr.py.rej\n--- sr.py\n+++ sr.py\n@@ -284,8 +289,20 @@\n             polybori = self._polybori\n         except AttributeError:\n             polybori = False\n+        kwds.setdefault(\"polybori\", polybori)\n \n-        kwds.setdefault(\"polybori\", polybori)\n+        try:\n+            correct_only = self._correct_only\n+        except AttributeError:\n+            correct_only = False\n+        kwds.setdefault(\"correct_only\", correct_only)\n+\n+        try:\n+            biaffine_only = self._biaffine_only\n+        except AttributeError:\n+            biaffine_only = False\n+        kwds.setdefault(\"biaffine_only\", biaffine_only)\n+\n         return SR(**kwds)\n \n     def __getattr__(self, attr):\n```\n",
    "created_at": "2008-11-28T22:11:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30945",
    "user": "was"
}
```

REFEREE REPORT:
I tried to figure out how to apply the above patches in their confusing order, but I guess I failed or something. See below (last patch fails to apply).  Please clarify, and I'll referee this:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
hgsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_convenience.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_0.patch"
applying /home/was/.sage/temp/sage/15295/tmp_0.patch
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_1.patch"
applying /home/was/.sage/temp/sage/15295/tmp_1.patch
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4254/sr_parameters.2.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/15295/tmp_2.patch"
applying /home/was/.sage/temp/sage/15295/tmp_2.patch
patching file sage/crypto/mq/sr.py
Hunk #2 FAILED at 288
1 out of 2 hunks FAILED -- saving rejects to file sage/crypto/mq/sr.py.rej
abort: patch failed to apply
```

| Sage Version 3.2.1.alpha1, Release Date: 2008-11-26                |
| Type notebook() for the GUI, and license() for information.        |
and 

```
was@sage:~/build/sage-3.2.1.alpha1$ more devel/sage/sage/crypto/mq/sr.py.rej
--- sr.py
+++ sr.py
@@ -284,8 +289,20 @@
             polybori = self._polybori
         except AttributeError:
             polybori = False
+        kwds.setdefault("polybori", polybori)
 
-        kwds.setdefault("polybori", polybori)
+        try:
+            correct_only = self._correct_only
+        except AttributeError:
+            correct_only = False
+        kwds.setdefault("correct_only", correct_only)
+
+        try:
+            biaffine_only = self._biaffine_only
+        except AttributeError:
+            biaffine_only = False
+        kwds.setdefault("biaffine_only", biaffine_only)
+
         return SR(**kwds)
 
     def __getattr__(self, attr):
```




---

archive/issue_comments_030946.json:
```json
{
    "body": "Here is how to apply the patches:\n\n\n```\n$ hg qimport sr_convenience.patch\nadding sr_convenience.patch to series file\n$ hg qpush\napplying sr_convenience.patch\nNow at: sr_convenience.patch\n$ hg qimport sr_parameters.patch\nadding sr_parameters.patch to series file\n$ hg qpush\napplying sr_parameters.patch\nNow at: sr_parameters.patch\n$ sage -b\n```\n\n\nNote that `sr_parameters.2.patch` is `sr_parameters.patch`",
    "created_at": "2008-11-30T20:27:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30946",
    "user": "malb"
}
```

Here is how to apply the patches:


```
$ hg qimport sr_convenience.patch
adding sr_convenience.patch to series file
$ hg qpush
applying sr_convenience.patch
Now at: sr_convenience.patch
$ hg qimport sr_parameters.patch
adding sr_parameters.patch to series file
$ hg qpush
applying sr_parameters.patch
Now at: sr_parameters.patch
$ sage -b
```


Note that `sr_parameters.2.patch` is `sr_parameters.patch`



---

archive/issue_comments_030947.json:
```json
{
    "body": "If this passes doctests, then I give it a positive review.",
    "created_at": "2008-11-30T23:30:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30947",
    "user": "was"
}
```

If this passes doctests, then I give it a positive review.



---

archive/issue_comments_030948.json:
```json
{
    "body": "Doctests pass, so this is a positive review by William.\n\nCheers,\n\nMichael",
    "created_at": "2008-11-30T23:49:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30948",
    "user": "mabshoff"
}
```

Doctests pass, so this is a positive review by William.

Cheers,

Michael



---

archive/issue_comments_030949.json:
```json
{
    "body": "Merged in Sage 3.2.1.rc1",
    "created_at": "2008-11-30T23:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30949",
    "user": "mabshoff"
}
```

Merged in Sage 3.2.1.rc1



---

archive/issue_comments_030950.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-11-30T23:49:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4254",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4254#issuecomment-30950",
    "user": "mabshoff"
}
```

Resolution: fixed
