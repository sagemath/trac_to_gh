# Issue 6315: optional doctest failure -- caused by mistakes in lectures on number theory rst book

archive/issues_006315.json:
```json
{
    "body": "Assignee: tbd\n\n\n```\nsage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst\", line 243:\n    sage: magma.eval(s)     #optional - magma\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_6[12]>\", line 1, in <module>\n        magma.eval(s)     #optional - magma###line 243:\n    sage: magma.eval(s)     #optional - magma\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 471, in eval\n        raise RuntimeError, \"Error evaluating Magma code.\\nIN:%s\\nOUT:%s\"%(x, ans)\n    RuntimeError: Error evaluating Magma code.\n    IN:time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];\n    OUT:\n    >> time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];\n                                        ^\n    User error: bad syntax\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst\", line 265:\n    sage: magma.eval(s) #optional - magma\nExpected:\n    'Time: 1.480'\nGot:\n    'Time: 0.210'\n**********************************************************************\n2 items had failures:\n   1 of  14 in __main__.example_6\n   1 of   9 in __main__.example_7\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_birds_other.py\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6315\n\n",
    "created_at": "2009-06-16T14:44:11Z",
    "labels": [
        "packages: optional",
        "major",
        "bug"
    ],
    "title": "optional doctest failure -- caused by mistakes in lectures on number theory rst book",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6315",
    "user": "was"
}
```
Assignee: tbd


```
sage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst", line 243:
    sage: magma.eval(s)     #optional - magma
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[12]>", line 1, in <module>
        magma.eval(s)     #optional - magma###line 243:
    sage: magma.eval(s)     #optional - magma
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 471, in eval
        raise RuntimeError, "Error evaluating Magma code.\nIN:%s\nOUT:%s"%(x, ans)
    RuntimeError: Error evaluating Magma code.
    IN:time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];
    OUT:
    >> time v := [_sage_[3] * _sage_[4] for _ in [1..10^5]];
                                        ^
    User error: bad syntax
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage-main/doc/en/bordeaux_2008/birds_other.rst", line 265:
    sage: magma.eval(s) #optional - magma
Expected:
    'Time: 1.480'
Got:
    'Time: 0.210'
**********************************************************************
2 items had failures:
   1 of  14 in __main__.example_6
   1 of   9 in __main__.example_7
***Test Failed*** 2 failures.
For whitespace errors, see the file /home/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_birds_other.py
```


Issue created by migration from https://trac.sagemath.org/ticket/6315





---

archive/issue_comments_050405.json:
```json
{
    "body": "Attachment",
    "created_at": "2011-05-25T17:27:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50405",
    "user": "mariah"
}
```

Attachment



---

archive/issue_comments_050406.json:
```json
{
    "body": "[attachment:trac_6315.patch] fixes the \"bad syntax\" error.  However I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.  With the patch, I currently get:\n\n\n```\neno% ./sage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst\nsage -t -long --optional \"devel/sage/doc/en/bordeaux_2008/birds_other.rst\"\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst\", line 244:\n    sage: magma.eval(s)     #optional - magma\nExpected:\n    'Time: 17.120'\nGot:\n    'Time: 3.560'\n**********************************************************************\nFile \"/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst\", line 266:\n    sage: magma.eval(s) #optional - magma\nExpected:\n    'Time: 1.480'\nGot:\n    'Time: 0.200'\n**********************************************************************\n2 items had failures:\n```\n\n\nWilliam - what do you want done?",
    "created_at": "2011-05-25T17:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50406",
    "user": "mariah"
}
```

[attachment:trac_6315.patch] fixes the "bad syntax" error.  However I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.  With the patch, I currently get:


```
eno% ./sage -t -long --optional devel/sage/doc/en/bordeaux_2008/birds_other.rst
sage -t -long --optional "devel/sage/doc/en/bordeaux_2008/birds_other.rst"
**********************************************************************
File "/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst", line 244:
    sage: magma.eval(s)     #optional - magma
Expected:
    'Time: 17.120'
Got:
    'Time: 3.560'
**********************************************************************
File "/home/mariah/sage/sage-4.7.rc4-x86_64-Linux-core2-fc-work-magma/devel/sage/doc/en/bordeaux_2008/birds_other.rst", line 266:
    sage: magma.eval(s) #optional - magma
Expected:
    'Time: 1.480'
Got:
    'Time: 0.200'
**********************************************************************
2 items had failures:
```


William - what do you want done?



---

archive/issue_comments_050407.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2011-05-25T17:33:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50407",
    "user": "mariah"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_050408.json:
```json
{
    "body": "Replying to [comment:1 mariah]:\n> [...] I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.\n\n\nWhy not just append \"`, random output`\" to \"`#optional - magma`\"? That way, the output is ignored, just like the timings in this rst file that don't use magma.\n\nAre the authors of the book aware of this error?",
    "created_at": "2011-06-29T14:37:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50408",
    "user": "mstreng"
}
```

Replying to [comment:1 mariah]:
> [...] I do not know what to do about the difference between the Expected time and the Got time.  Timings will be dependent on the computer system.


Why not just append "`, random output`" to "`#optional - magma`"? That way, the output is ignored, just like the timings in this rst file that don't use magma.

Are the authors of the book aware of this error?



---

archive/issue_comments_050409.json:
```json
{
    "body": "Attachment\n\nReplying to [comment:2 mstreng]:\n> Are the authors of the book aware of this error?\n\nThe authors \"= me\" is aware now.  I've posted a part2 patch that puts ...'s in for the timings, explains that the doctest is showing the reader *how* to compare timings with Magma (which is good to know how to do easily), and remarks that in fact the timings may change over time.",
    "created_at": "2011-08-23T08:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50409",
    "user": "was"
}
```

Attachment

Replying to [comment:2 mstreng]:
> Are the authors of the book aware of this error?

The authors "= me" is aware now.  I've posted a part2 patch that puts ...'s in for the timings, explains that the doctest is showing the reader *how* to compare timings with Magma (which is good to know how to do easily), and remarks that in fact the timings may change over time.



---

archive/issue_comments_050410.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2011-08-23T08:10:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50410",
    "user": "was"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_050411.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2011-08-23T08:29:20Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50411",
    "user": "mstreng"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_050412.json:
```json
{
    "body": "Changing keywords from \"\" to \"sd32\".",
    "created_at": "2011-08-24T23:46:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50412",
    "user": "was"
}
```

Changing keywords from "" to "sd32".



---

archive/issue_comments_050413.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2011-09-12T19:41:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6315",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6315#issuecomment-50413",
    "user": "leif"
}
```

Resolution: fixed
