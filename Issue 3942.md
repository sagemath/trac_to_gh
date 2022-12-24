# Issue 3942: Sage interfaces vs. pyprocessing

archive/issues_003942.json:
```json
{
    "body": "Assignee: was\n\nCC:  cwitty\n\nWhen using pyprocessing, if you use an interface to some external function, such as GAP, sometimes the separate subprocesses will collide, since they all share the same temporary file.\n\nA temporary fix (due to cwitty) was to add\n\n`sage.interfaces.expect.tmp_expect_interface_local = '/tmp/interface' + str(os.getpid())`\n\nto the beginning of the function succeeding the ``@`parallel` decorator. This way, the temp files are separate. This should probably be part of the `parallel` function itself.\n\nIssue created by migration from https://trac.sagemath.org/ticket/3942\n\n",
    "created_at": "2008-08-24T05:16:36Z",
    "labels": [
        "interfaces",
        "major",
        "bug"
    ],
    "title": "Sage interfaces vs. pyprocessing",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3942",
    "user": "rlm"
}
```
Assignee: was

CC:  cwitty

When using pyprocessing, if you use an interface to some external function, such as GAP, sometimes the separate subprocesses will collide, since they all share the same temporary file.

A temporary fix (due to cwitty) was to add

`sage.interfaces.expect.tmp_expect_interface_local = '/tmp/interface' + str(os.getpid())`

to the beginning of the function succeeding the ``@`parallel` decorator. This way, the temp files are separate. This should probably be part of the `parallel` function itself.

Issue created by migration from https://trac.sagemath.org/ticket/3942





---

archive/issue_comments_028265.json:
```json
{
    "body": "How about replacing tmp_expect_interface_local by a function that returns, \n\n  `'/tmp/interface' + str(os.getpid())`\n\nthis way, it should always just work?",
    "created_at": "2008-08-24T11:40:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28265",
    "user": "malb"
}
```

How about replacing tmp_expect_interface_local by a function that returns, 

  `'/tmp/interface' + str(os.getpid())`

this way, it should always just work?



---

archive/issue_comments_028266.json:
```json
{
    "body": "\n```\nrank4:sage-main rlmill$ ../../sage -tp 2 sage/interfaces/\nGlobal iterations: 1\nFile iterations: 1\nTeX files: 0\n \n----------------------------------------------------------------------\nsage -t  devel/sage-main/sage/interfaces/tachyon.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/tests.py\n\t [3.5 s]\nsage -t  devel/sage-main/sage/interfaces/singular.py\n\t [3.5 s]\nsage -t  devel/sage-main/sage/interfaces/sage0.py\n\t [9.4 s]\nsage -t  devel/sage-main/sage/interfaces/r.py\n\t [7.0 s]\nsage -t  devel/sage-main/sage/interfaces/rubik.py\n\t [15.8 s]\nsage -t  devel/sage-main/sage/interfaces/qsieve.py\n\t [3.4 s]\nsage -t  devel/sage-main/sage/interfaces/povray.py\n\t [2.2 s]\nsage -t  devel/sage-main/sage/interfaces/phc.py\n\t [3.2 s]\nsage -t  devel/sage-main/sage/interfaces/octave.py\n\t [2.9 s]\nsage -t  devel/sage-main/sage/interfaces/psage.py\n\t [11.8 s]\nsage -t  devel/sage-main/sage/interfaces/mwrank.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/mupad.py\n\t [2.1 s]\nsage -t  devel/sage-main/sage/interfaces/monitor.py\n\t [2.1 s]\nsage -t  devel/sage-main/sage/interfaces/matlab.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/mathematica.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/maple.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/magma_sim.py\n\t [1.9 s]\nsage -t  devel/sage-main/sage/interfaces/magma_free.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/magma.py\n\t [1.9 s]\nsage -t  devel/sage-main/sage/interfaces/macaulay2.py\n\t [1.9 s]\nsage -t  devel/sage-main/sage/interfaces/lie.py\n\t [2.1 s]\nsage -t  devel/sage-main/sage/interfaces/maxima.py\n\t [17.0 s]\nsage -t  devel/sage-main/sage/interfaces/kash.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/gnuplot.py\n\t [2.1 s]\nsage -t  devel/sage-main/sage/interfaces/gp.py\n\t [3.4 s]\nsage -t  devel/sage-main/sage/interfaces/gfan.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/get_sigs.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/genus2reduction.py\n\t [2.7 s]\nsage -t  devel/sage-main/sage/interfaces/gap.py\n\t [3.4 s]\nsage -t  devel/sage-main/sage/interfaces/frobby.py\n\t [2.0 s]\nsage -t  devel/sage-main/sage/interfaces/expect.py\n\t [6.9 s]\nsage -t  devel/sage-main/sage/interfaces/axiom.py\n\t [1.9 s]\nsage -t  devel/sage-main/sage/interfaces/ecm.py\n\t [14.5 s]\nAll tests passed!\nTotal time for all tests: 76.7 seconds\nrank4:sage-main rlmill$ \n```\n",
    "created_at": "2008-08-24T14:40:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28266",
    "user": "rlm"
}
```


```
rank4:sage-main rlmill$ ../../sage -tp 2 sage/interfaces/
Global iterations: 1
File iterations: 1
TeX files: 0
 
----------------------------------------------------------------------
sage -t  devel/sage-main/sage/interfaces/tachyon.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/tests.py
	 [3.5 s]
sage -t  devel/sage-main/sage/interfaces/singular.py
	 [3.5 s]
sage -t  devel/sage-main/sage/interfaces/sage0.py
	 [9.4 s]
sage -t  devel/sage-main/sage/interfaces/r.py
	 [7.0 s]
sage -t  devel/sage-main/sage/interfaces/rubik.py
	 [15.8 s]
sage -t  devel/sage-main/sage/interfaces/qsieve.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/povray.py
	 [2.2 s]
sage -t  devel/sage-main/sage/interfaces/phc.py
	 [3.2 s]
sage -t  devel/sage-main/sage/interfaces/octave.py
	 [2.9 s]
sage -t  devel/sage-main/sage/interfaces/psage.py
	 [11.8 s]
sage -t  devel/sage-main/sage/interfaces/mwrank.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/mupad.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/monitor.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/matlab.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/mathematica.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/maple.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/magma_sim.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/magma_free.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/magma.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/macaulay2.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/lie.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/maxima.py
	 [17.0 s]
sage -t  devel/sage-main/sage/interfaces/kash.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/gnuplot.py
	 [2.1 s]
sage -t  devel/sage-main/sage/interfaces/gp.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/gfan.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/get_sigs.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/genus2reduction.py
	 [2.7 s]
sage -t  devel/sage-main/sage/interfaces/gap.py
	 [3.4 s]
sage -t  devel/sage-main/sage/interfaces/frobby.py
	 [2.0 s]
sage -t  devel/sage-main/sage/interfaces/expect.py
	 [6.9 s]
sage -t  devel/sage-main/sage/interfaces/axiom.py
	 [1.9 s]
sage -t  devel/sage-main/sage/interfaces/ecm.py
	 [14.5 s]
All tests passed!
Total time for all tests: 76.7 seconds
rank4:sage-main rlmill$ 
```




---

archive/issue_comments_028267.json:
```json
{
    "body": "Attachment [trac_3942_pid-interfaces.patch](tarball://root/attachments/some-uuid/ticket3942/trac_3942_pid-interfaces.patch) by rlm created at 2008-08-24 14:40:24",
    "created_at": "2008-08-24T14:40:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28267",
    "user": "rlm"
}
```

Attachment [trac_3942_pid-interfaces.patch](tarball://root/attachments/some-uuid/ticket3942/trac_3942_pid-interfaces.patch) by rlm created at 2008-08-24 14:40:24



---

archive/issue_comments_028268.json:
```json
{
    "body": "My one concern with this patch is that the temp files should be cleaned up properly. I don't know the mechanisms for this...",
    "created_at": "2008-08-24T14:41:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28268",
    "user": "rlm"
}
```

My one concern with this patch is that the temp files should be cleaned up properly. I don't know the mechanisms for this...



---

archive/issue_comments_028269.json:
```json
{
    "body": "> My one concern with this patch is that the temp files should be cleaned up properly. \n> I don't know the mechanisms for this... \n\nThat's all taken care of because the files are in SAGE_TMP.  No worries.\n\nI think this is a good patch.",
    "created_at": "2008-08-24T17:15:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28269",
    "user": "was"
}
```

> My one concern with this patch is that the temp files should be cleaned up properly. 
> I don't know the mechanisms for this... 

That's all taken care of because the files are in SAGE_TMP.  No worries.

I think this is a good patch.



---

archive/issue_comments_028270.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-08-25T03:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28270",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_028271.json:
```json
{
    "body": "Merged in Sage 3.1.2.alpha1",
    "created_at": "2008-08-25T03:52:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3942",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3942#issuecomment-28271",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.2.alpha1
