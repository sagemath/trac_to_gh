# Issue 6320: optional doctest failure -- combinat crystal code

archive/issues_006320.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @tscrim\n\nI have dot2tex installed but this doctest in combinat still fails:\n\n```\nwstein@sage:~/build/sage-4.0.2.alpha3$ which dot2tex\n/usr/bin/dot2tex\nwstein@sage:~/build/sage-4.0.2.alpha3$ ./sage -t -long --optional devel/sage/sage/combinat/crystals/crystals.py\nsage -t -long --optional \"devel/sage/sage/combinat/crystals/crystals.py\"\n\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py\", line 344:\n    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_10[3]>\", line 1, in <module>\n        C.latex_file('/tmp/test.tex') #optional requires dot2tex###line 344:\n    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex\n      File \"/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py\", line 363, in latex_file\n        f.write(header + self.latex() + footer)\n    TypeError: cannot concatenate 'str' and 'NoneType' objects\n**********************************************************************\nFile \"/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py\", line 422:\n    sage: C.latex() #optional requires dot2tex\nExpected nothing\nGot:\n    dot2tex not available.  Install after running 'sage -sh'\n**********************************************************************\n2 items had failures:\n   1 of   4 in __main__.example_10\n   1 of   4 in __main__.example_13\n***Test Failed*** 2 failures.\nFor whitespace errors, see the file /scratch/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_crystals.py\n         [7.2 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long --optional \"devel/sage/sage/combinat/crystals/crystals.py\"\nTotal time for all tests: 7.2 seconds\nwstein@sage:~/build/sage-4.0.2.alpha3$ \n\n\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6320\n\n",
    "created_at": "2009-06-16T14:50:46Z",
    "labels": [
        "component: packages: optional",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "optional doctest failure -- combinat crystal code",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6320",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @tscrim

I have dot2tex installed but this doctest in combinat still fails:

```
wstein@sage:~/build/sage-4.0.2.alpha3$ which dot2tex
/usr/bin/dot2tex
wstein@sage:~/build/sage-4.0.2.alpha3$ ./sage -t -long --optional devel/sage/sage/combinat/crystals/crystals.py
sage -t -long --optional "devel/sage/sage/combinat/crystals/crystals.py"

**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py", line 344:
    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex
Exception raised:
    Traceback (most recent call last):
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[3]>", line 1, in <module>
        C.latex_file('/tmp/test.tex') #optional requires dot2tex###line 344:
    sage: C.latex_file('/tmp/test.tex') #optional requires dot2tex
      File "/scratch/wstein/build/sage-4.0.2.alpha3/local/lib/python2.5/site-packages/sage/combinat/crystals/crystals.py", line 363, in latex_file
        f.write(header + self.latex() + footer)
    TypeError: cannot concatenate 'str' and 'NoneType' objects
**********************************************************************
File "/scratch/wstein/build/sage-4.0.2.alpha3/devel/sage/sage/combinat/crystals/crystals.py", line 422:
    sage: C.latex() #optional requires dot2tex
Expected nothing
Got:
    dot2tex not available.  Install after running 'sage -sh'
**********************************************************************
2 items had failures:
   1 of   4 in __main__.example_10
   1 of   4 in __main__.example_13
***Test Failed*** 2 failures.
For whitespace errors, see the file /scratch/wstein/build/sage-4.0.2.alpha3/tmp/.doctest_crystals.py
         [7.2 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long --optional "devel/sage/sage/combinat/crystals/crystals.py"
Total time for all tests: 7.2 seconds
wstein@sage:~/build/sage-4.0.2.alpha3$ 


```


Issue created by migration from https://trac.sagemath.org/ticket/6320





---

archive/issue_comments_050344.json:
```json
{
    "body": "Dot2tex may be installed on your system but still sage can't find it. You\nprobably don't want `/usr/bin/dot2tex` but rather `$SAGEROOT/local/bin/dot2tex`.\n\nTo install dot2tex start `sage -sh` then install pydot, pyparsing and dot2tex\nby going to their source directories and running `python setup.py install`.\n\nThere is some discussion of making dot2tex a sage spkg here:\n\nhttp://groups.google.com/group/sage-combinat-devel/browse_thread/thread/f682107dcc4ee3f2/ddea890fc5513d81?hl=en&lnk=gst&q=dot2tex#ddea890fc5513d81",
    "created_at": "2009-06-16T15:22:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6320#issuecomment-50344",
    "user": "https://github.com/dwbump"
}
```

Dot2tex may be installed on your system but still sage can't find it. You
probably don't want `/usr/bin/dot2tex` but rather `$SAGEROOT/local/bin/dot2tex`.

To install dot2tex start `sage -sh` then install pydot, pyparsing and dot2tex
by going to their source directories and running `python setup.py install`.

There is some discussion of making dot2tex a sage spkg here:

http://groups.google.com/group/sage-combinat-devel/browse_thread/thread/f682107dcc4ee3f2/ddea890fc5513d81?hl=en&lnk=gst&q=dot2tex#ddea890fc5513d81



---

archive/issue_comments_050345.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-09-26T13:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6320#issuecomment-50345",
    "user": "https://github.com/seblabbe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_050346.json:
```json
{
    "body": "On 7.4.beta5, running\n\n\n```\n./sage -t -l --optional=sage,dot2tex,graphviz src/sage/combinat/crystals/crystals.py\n```\n\n\ngives\n\n\n```\nRunning doctests with ID 2016-09-26-15-08-12-8d82066d.\nGit branch: 21490\nUsing --optional=dot2tex,graphviz,sage\nDoctesting 1 file.\nsage -t --long --warn-long 42.7 src/sage/combinat/crystals/crystals.py\n    [25 tests, 0.75 s]\n----------------------------------------------------------------------\nAll tests passed!\n----------------------------------------------------------------------\nTotal time for all tests: 0.8 seconds\n    cpu time: 1.0 seconds\n    cumulative wall time: 0.7 seconds\n```\n\n\nShould we close this ticket?",
    "created_at": "2016-09-26T13:10:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6320#issuecomment-50346",
    "user": "https://github.com/seblabbe"
}
```

On 7.4.beta5, running


```
./sage -t -l --optional=sage,dot2tex,graphviz src/sage/combinat/crystals/crystals.py
```


gives


```
Running doctests with ID 2016-09-26-15-08-12-8d82066d.
Git branch: 21490
Using --optional=dot2tex,graphviz,sage
Doctesting 1 file.
sage -t --long --warn-long 42.7 src/sage/combinat/crystals/crystals.py
    [25 tests, 0.75 s]
----------------------------------------------------------------------
All tests passed!
----------------------------------------------------------------------
Total time for all tests: 0.8 seconds
    cpu time: 1.0 seconds
    cumulative wall time: 0.7 seconds
```


Should we close this ticket?



---

archive/issue_comments_050347.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-09-26T13:19:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6320#issuecomment-50347",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_006566.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2017-01-21T18:03:11Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6320#event-6566"
}
```



---

archive/issue_comments_050348.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2017-01-21T18:03:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6320",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6320#issuecomment-50348",
    "user": "https://github.com/vbraun"
}
```

Resolution: invalid
