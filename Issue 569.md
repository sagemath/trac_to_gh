# Issue 569: fix many broken --long doctests in functions/piecewise.py

archive/issues_000569.json:
```json
{
    "body": "Assignee: wdjoyner\n\nNone of the following should fail:\n\n\n```\nsage -t --long functions/piecewise.py                       **********************************************************************\nFile \"piecewise.py\", line 954:\n    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_26[5]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 954:\n    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 972, in plot_fourier_series_partial_sum\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 958:\n    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_26[9]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 958:\n    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 972, in plot_fourier_series_partial_sum\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 992:\n    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_27[5]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_cesaro(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 992:\n    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1010, in plot_fourier_series_partial_sum_cesaro\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 996:\n    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_27[9]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_cesaro(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 996:\n    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1010, in plot_fourier_series_partial_sum_cesaro\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 1030:\n    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_28[5]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_hann(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 1030:\n    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1048, in plot_fourier_series_partial_sum_hann\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 1034:\n    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_28[9]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_hann(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 1034:\n    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1048, in plot_fourier_series_partial_sum_hann\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 1070:\n    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_29[5]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_filtered(Integer(3),pi,[Integer(1)]*Integer(3),-Integer(5),Integer(5))    # long time###line 1070:\n    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1088, in plot_fourier_series_partial_sum_filtered\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\nFile \"piecewise.py\", line 1074:\n    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/s/local/lib/python2.5/doctest.py\", line 1212, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_29[9]>\", line 1, in <module>\n        P = f.plot_fourier_series_partial_sum_filtered(Integer(15),pi,[Integer(1)]*Integer(15),-Integer(5),Integer(5))   # long time###line 1074:\n    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time\n      File \"/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py\", line 1088, in plot_fourier_series_partial_sum_filtered\n        yi = ff.replace(\"pi\",repr(RR(pi)))\n    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'\n**********************************************************************\n4 items had failures:\n   2 of  10 in __main__.example_26\n   2 of  10 in __main__.example_27\n   2 of  10 in __main__.example_28\n   2 of  10 in __main__.example_29\n***Test Failed*** 8 failures.\nFor whitespace errors, see the file .doctest_piecewise.py\n         [53.6 s]\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/569\n\n",
    "created_at": "2007-09-02T17:37:50Z",
    "labels": [
        "calculus",
        "major",
        "bug"
    ],
    "title": "fix many broken --long doctests in functions/piecewise.py",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/569",
    "user": "was"
}
```
Assignee: wdjoyner

None of the following should fail:


```
sage -t --long functions/piecewise.py                       **********************************************************************
File "piecewise.py", line 954:
    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 954:
    sage: P = f.plot_fourier_series_partial_sum(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 972, in plot_fourier_series_partial_sum
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 958:
    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_26[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 958:
    sage: P = f.plot_fourier_series_partial_sum(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 972, in plot_fourier_series_partial_sum
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 992:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_27[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_cesaro(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 992:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1010, in plot_fourier_series_partial_sum_cesaro
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 996:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_27[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_cesaro(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 996:
    sage: P = f.plot_fourier_series_partial_sum_cesaro(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1010, in plot_fourier_series_partial_sum_cesaro
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1030:
    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_hann(Integer(3),pi,-Integer(5),Integer(5))    # long time###line 1030:
    sage: P = f.plot_fourier_series_partial_sum_hann(3,pi,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1048, in plot_fourier_series_partial_sum_hann
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1034:
    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_28[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_hann(Integer(15),pi,-Integer(5),Integer(5))   # long time###line 1034:
    sage: P = f.plot_fourier_series_partial_sum_hann(15,pi,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1048, in plot_fourier_series_partial_sum_hann
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1070:
    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[5]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_filtered(Integer(3),pi,[Integer(1)]*Integer(3),-Integer(5),Integer(5))    # long time###line 1070:
    sage: P = f.plot_fourier_series_partial_sum_filtered(3,pi,[1]*3,-5,5)    # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1088, in plot_fourier_series_partial_sum_filtered
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
File "piecewise.py", line 1074:
    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time
Exception raised:
    Traceback (most recent call last):
      File "/home/was/s/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_29[9]>", line 1, in <module>
        P = f.plot_fourier_series_partial_sum_filtered(Integer(15),pi,[Integer(1)]*Integer(15),-Integer(5),Integer(5))   # long time###line 1074:
    sage: P = f.plot_fourier_series_partial_sum_filtered(15,pi,[1]*15,-5,5)   # long time
      File "/home/was/s/local/lib/python2.5/site-packages/sage/functions/piecewise.py", line 1088, in plot_fourier_series_partial_sum_filtered
        yi = ff.replace("pi",repr(RR(pi)))
    AttributeError: 'SymbolicArithmetic' object has no attribute 'replace'
**********************************************************************
4 items had failures:
   2 of  10 in __main__.example_26
   2 of  10 in __main__.example_27
   2 of  10 in __main__.example_28
   2 of  10 in __main__.example_29
***Test Failed*** 8 failures.
For whitespace errors, see the file .doctest_piecewise.py
         [53.6 s]
```


Issue created by migration from https://trac.sagemath.org/ticket/569





---

archive/issue_comments_002949.json:
```json
{
    "body": "hg patch to fix this report",
    "created_at": "2007-09-06T00:33:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/569#issuecomment-2949",
    "user": "wdj"
}
```

hg patch to fix this report



---

archive/issue_comments_002950.json:
```json
{
    "body": "Attachment\n\nI had some comments here but adding the attachment deleted by remarks!\nHopefully the diff file will explain the idea. The fix was very easy.",
    "created_at": "2007-09-06T00:36:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/569#issuecomment-2950",
    "user": "wdj"
}
```

Attachment

I had some comments here but adding the attachment deleted by remarks!
Hopefully the diff file will explain the idea. The fix was very easy.



---

archive/issue_comments_002951.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2007-09-06T17:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/569#issuecomment-2951",
    "user": "was"
}
```

Resolution: fixed



---

archive/issue_comments_002952.json:
```json
{
    "body": "looks good",
    "created_at": "2007-09-06T17:26:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/569",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/569#issuecomment-2952",
    "user": "was"
}
```

looks good
