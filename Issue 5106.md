# Issue 5106: preparse bug with time and generator assignment naming

archive/issues_005106.json:
```json
{
    "body": "Assignee: cwitty\n\nCC:  boothby mhansen\n\nThe Sage `.<a>` notation doesn't properly deal with `time foo`.\n\n\n```\nsage: time K.<a> = GF(9)\n------------------------------------------------------------\n   File \"<timed exec>\", line 1\n     K = GF(Integer(Integer(9)),names=(u'a',)); (a,) = time K._first_ngens(Integer(1))\n                                                            ^\nSyntaxError: invalid syntax\n```\n\n\nNote that the Ipython magic %time works fine:\n\n```\nsage: %time K.<a> = GF(9)\nCPU times: user 0.11 s, sys: 0.09 s, total: 0.19 s\nWall time: 2.17 s\n```\n\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5106\n\n",
    "created_at": "2009-01-26T19:10:38Z",
    "labels": [
        "misc",
        "major",
        "bug"
    ],
    "title": "preparse bug with time and generator assignment naming",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5106",
    "user": "was"
}
```
Assignee: cwitty

CC:  boothby mhansen

The Sage `.<a>` notation doesn't properly deal with `time foo`.


```
sage: time K.<a> = GF(9)
------------------------------------------------------------
   File "<timed exec>", line 1
     K = GF(Integer(Integer(9)),names=(u'a',)); (a,) = time K._first_ngens(Integer(1))
                                                            ^
SyntaxError: invalid syntax
```


Note that the Ipython magic %time works fine:

```
sage: %time K.<a> = GF(9)
CPU times: user 0.11 s, sys: 0.09 s, total: 0.19 s
Wall time: 2.17 s
```




Issue created by migration from https://trac.sagemath.org/ticket/5106





---

archive/issue_comments_038997.json:
```json
{
    "body": "Simplifies the generator and calculus preparsing, fixing the above bug. Depends on #5079.",
    "created_at": "2009-01-27T23:52:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-38997",
    "user": "robertwb"
}
```

Simplifies the generator and calculus preparsing, fixing the above bug. Depends on #5079.



---

archive/issue_comments_038998.json:
```json
{
    "body": "This would be nice to have in 3.3. Can someone review this?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T08:08:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-38998",
    "user": "mabshoff"
}
```

This would be nice to have in 3.3. Can someone review this?

Cheers,

Michael



---

archive/issue_comments_038999.json:
```json
{
    "body": "One ought to check if this patch fixes #4454.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-11T08:18:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-38999",
    "user": "mabshoff"
}
```

One ought to check if this patch fixes #4454.

Cheers,

Michael



---

archive/issue_comments_039000.json:
```json
{
    "body": "works for me",
    "created_at": "2009-02-13T20:50:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39000",
    "user": "boothby"
}
```

works for me



---

archive/issue_comments_039001.json:
```json
{
    "body": "Hmm, I have the dependency applies, but the patch does not apply:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5106-preparse-gens.patch \npatching file sage/misc/preparser.py\nHunk #7 FAILED at 739.\nHunk #8 FAILED at 825.\n2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej\n```\n\nCan someone rebase for 3.3.rc0?\n\nCheers,\n\nMichael",
    "created_at": "2009-02-14T01:52:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39001",
    "user": "mabshoff"
}
```

Hmm, I have the dependency applies, but the patch does not apply:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < trac_5106-preparse-gens.patch 
patching file sage/misc/preparser.py
Hunk #7 FAILED at 739.
Hunk #8 FAILED at 825.
2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
```

Can someone rebase for 3.3.rc0?

Cheers,

Michael



---

archive/issue_comments_039002.json:
```json
{
    "body": "Robert, what is the patch based on?  I can't get it to apply to 3.2.3 or 3.3.alpha1/2 ?",
    "created_at": "2009-02-15T04:20:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39002",
    "user": "mhansen"
}
```

Robert, what is the patch based on?  I can't get it to apply to 3.2.3 or 3.3.alpha1/2 ?



---

archive/issue_comments_039003.json:
```json
{
    "body": "It's based on 3.2.3, with #5079, and perhaps another patch or two. I haven't upgraded to the latest alpha yet, which is why I haven't rebased this. I'll look into that later tonight if someone else doesn't beat me to it.",
    "created_at": "2009-02-15T05:22:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39003",
    "user": "robertwb"
}
```

It's based on 3.2.3, with #5079, and perhaps another patch or two. I haven't upgraded to the latest alpha yet, which is why I haven't rebased this. I'll look into that later tonight if someone else doesn't beat me to it.



---

archive/issue_comments_039004.json:
```json
{
    "body": "Changing assignee from cwitty to was.",
    "created_at": "2009-02-15T09:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39004",
    "user": "robertwb"
}
```

Changing assignee from cwitty to was.



---

archive/issue_comments_039005.json:
```json
{
    "body": "Changing component from misc to user interface.",
    "created_at": "2009-02-15T09:01:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39005",
    "user": "robertwb"
}
```

Changing component from misc to user interface.



---

archive/issue_comments_039006.json:
```json
{
    "body": "The rebase issue was #4405, which was independently resolved by this patch.",
    "created_at": "2009-02-15T09:08:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39006",
    "user": "robertwb"
}
```

The rebase issue was #4405, which was independently resolved by this patch.



---

archive/issue_comments_039007.json:
```json
{
    "body": "Attachment [5106-preparse-gens.patch](tarball://root/attachments/some-uuid/ticket5106/5106-preparse-gens.patch) by robertwb created at 2009-02-15 09:19:31",
    "created_at": "2009-02-15T09:19:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39007",
    "user": "robertwb"
}
```

Attachment [5106-preparse-gens.patch](tarball://root/attachments/some-uuid/ticket5106/5106-preparse-gens.patch) by robertwb created at 2009-02-15 09:19:31



---

archive/issue_comments_039008.json:
```json
{
    "body": "Hi Robert,\n\nthis patch is either not the right one or something else went wrong since it does not apply:\n\n```\nmabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < 5106-preparse-gens.patch \npatching file sage/misc/preparser.py\nHunk #7 FAILED at 739.\nHunk #8 FAILED at 825.\n2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej\n```\n\n\nAt SD 12 there were some issues merging the preparser patches including #4405, so it sounds like a very good idea to rebase this against 3.3.rc1 which will be out by the time you get this email on Monday :).\n\nCheers,\n\nMichael",
    "created_at": "2009-02-15T13:50:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39008",
    "user": "mabshoff"
}
```

Hi Robert,

this patch is either not the right one or something else went wrong since it does not apply:

```
mabshoff@sage:/scratch/mabshoff/sage-3.3.rc1/devel/sage$ patch -p1 --dry-run < 5106-preparse-gens.patch 
patching file sage/misc/preparser.py
Hunk #7 FAILED at 739.
Hunk #8 FAILED at 825.
2 out of 8 hunks FAILED -- saving rejects to file sage/misc/preparser.py.rej
```


At SD 12 there were some issues merging the preparser patches including #4405, so it sounds like a very good idea to rebase this against 3.3.rc1 which will be out by the time you get this email on Monday :).

Cheers,

Michael



---

archive/issue_comments_039009.json:
```json
{
    "body": "Attachment [5106-preparse-gens-rebase.patch](tarball://root/attachments/some-uuid/ticket5106/5106-preparse-gens-rebase.patch) by robertwb created at 2009-02-17 06:37:28",
    "created_at": "2009-02-17T06:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39009",
    "user": "robertwb"
}
```

Attachment [5106-preparse-gens-rebase.patch](tarball://root/attachments/some-uuid/ticket5106/5106-preparse-gens-rebase.patch) by robertwb created at 2009-02-17 06:37:28



---

archive/issue_comments_039010.json:
```json
{
    "body": "OK, new patch rebased against 3.3rc1",
    "created_at": "2009-02-17T06:37:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39010",
    "user": "robertwb"
}
```

OK, new patch rebased against 3.3rc1



---

archive/issue_comments_039011.json:
```json
{
    "body": "New patch applied cleanly, and works on the commandline, but I get this error in the notebook when trying to time anything:\n\n\n```\ntime a = number_of_partitions(10^6)\n\nTraceback (most recent call last):\n  File \"<stdin>\", line 1, in <module>\n  File \"/Users/mh/.sage/sage_notebook/worksheets/admin/182/code/1.py\", line 9, in <module>\n    _time__=misc.cputime(); __wall__=misc.walltime(); a = number_of_partitions(_sage_const_10 **_sage_const_6 ); print \"Time: CPU %.2f s, Wall: %.2f s\"%(misc.cputime(__time__), misc.walltime(__wall__))\n  File \"/Users/mh/sagestuff/sage-3.3.rc0/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/\", line 1, in <module>\n    \nNameError: name '__time__' is not defined\n```\n",
    "created_at": "2009-02-17T11:45:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39011",
    "user": "mhampton"
}
```

New patch applied cleanly, and works on the commandline, but I get this error in the notebook when trying to time anything:


```
time a = number_of_partitions(10^6)

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/Users/mh/.sage/sage_notebook/worksheets/admin/182/code/1.py", line 9, in <module>
    _time__=misc.cputime(); __wall__=misc.walltime(); a = number_of_partitions(_sage_const_10 **_sage_const_6 ); print "Time: CPU %.2f s, Wall: %.2f s"%(misc.cputime(__time__), misc.walltime(__wall__))
  File "/Users/mh/sagestuff/sage-3.3.rc0/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/", line 1, in <module>
    
NameError: name '__time__' is not defined
```




---

archive/issue_comments_039012.json:
```json
{
    "body": "Hmm... I'll look at this in a moment.",
    "created_at": "2009-02-17T11:51:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39012",
    "user": "robertwb"
}
```

Hmm... I'll look at this in a moment.



---

archive/issue_comments_039013.json:
```json
{
    "body": "Attachment [5106-fix.patch](tarball://root/attachments/some-uuid/ticket5106/5106-fix.patch) by robertwb created at 2009-02-17 12:16:23\n\nOK, I've resolved the issue above.",
    "created_at": "2009-02-17T12:16:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39013",
    "user": "robertwb"
}
```

Attachment [5106-fix.patch](tarball://root/attachments/some-uuid/ticket5106/5106-fix.patch) by robertwb created at 2009-02-17 12:16:23

OK, I've resolved the issue above.



---

archive/issue_comments_039014.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-17T19:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39014",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_039015.json:
```json
{
    "body": "Merged\n\n* 5106-preparse-gens-rebase.patch\n* 5106-fix.patch\n\nin Sage 3.3.rc2.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-17T19:50:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5106",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5106#issuecomment-39015",
    "user": "mabshoff"
}
```

Merged

* 5106-preparse-gens-rebase.patch
* 5106-fix.patch

in Sage 3.3.rc2.

Cheers,

Michael
