# Issue 5372: [with patch, needs review] Fix mwrank doctest in 3.4.alpha0

archive/issues_005372.json:
```json
{
    "body": "Assignee: mabshoff\n\n\n```\nsage -t -long \"devel/sage/sage/libs/mwrank/all.py\"\n**********************************************************************\nFile \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/\nsage/libs/mwrank/all.py\", line 26:\n   sage: file= Sage_TMP + '/PRIMES'\nException raised:\n   Traceback (most recent call last):\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1231, in run_one_test\n       self.run_one_example(test, example, filename, compileflags)\n     File \"/Applications/sage_builds/sage-3.3.rc1/local/bin/\nsagedoctest.py\", line 38, in run_one_example\n       OrigDocTestRunner.run_one_example(self, test, example,\nfilename, compileflags)\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1172, in run_one_example\n       compileflags, 1) in test.globs\n     File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n       file= Sage_TMP + '/PRIMES'###line 26:\n   sage: file= Sage_TMP + '/PRIMES'\n   NameError: name 'Sage_TMP' is not defined\n**********************************************************************\nFile \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/\nsage/libs/mwrank/all.py\", line 27:\n   sage: open(file,'w').write(' '.join([str(p) for p in prime_range\n(10^6)]))\nException raised:\n   Traceback (most recent call last):\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1231, in run_one_test\n       self.run_one_example(test, example, filename, compileflags)\n     File \"/Applications/sage_builds/sage-3.3.rc1/local/bin/\nsagedoctest.py\", line 38, in run_one_example\n       OrigDocTestRunner.run_one_example(self, test, example,\nfilename, compileflags)\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1172, in run_one_example\n       compileflags, 1) in test.globs\n     File \"<doctest __main__.example_1[3]>\", line 1, in <module>\n       open(file,'w').write(' '.join([str(p) for p in prime_range\n(Integer(10)**Integer(6))]))###line 27:\n   sage: open(file,'w').write(' '.join([str(p) for p in prime_range\n(10^6)]))\n   TypeError: coercing to Unicode: need string or buffer, type found\n**********************************************************************\nFile \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/\nsage/libs/mwrank/all.py\", line 28:\n   sage: mwrank_initprimes(file, verb=False)\nException raised:\n   Traceback (most recent call last):\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1231, in run_one_test\n       self.run_one_example(test, example, filename, compileflags)\n     File \"/Applications/sage_builds/sage-3.3.rc1/local/bin/\nsagedoctest.py\", line 38, in run_one_example\n       OrigDocTestRunner.run_one_example(self, test, example,\nfilename, compileflags)\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nbin/ncadoctest.py\", line 1172, in run_one_example\n       compileflags, 1) in test.globs\n     File \"<doctest __main__.example_1[4]>\", line 1, in <module>\n       mwrank_initprimes(file, verb=False)###line 28:\n   sage: mwrank_initprimes(file, verb=False)\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nlib/python2.5/site-packages/sage/libs/mwrank/all.py\", line 31, in\nmwrank_initprimes\n       return mwrank_initprimes(filename, verb)\n     File \"mwrank.pyx\", line 119, in\nsage.libs.mwrank.mwrank.initprimes (sage/libs/mwrank/mwrank.c:630)\n     File \"/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/\nlib/python2.5/posixpath.py\", line 171, in exists\n       st = os.stat(path)\n   TypeError: coercing to Unicode: need string or buffer, type found\n```\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/5372\n\n",
    "created_at": "2009-02-25T18:28:43Z",
    "labels": [
        "doctest coverage",
        "minor",
        "bug"
    ],
    "title": "[with patch, needs review] Fix mwrank doctest in 3.4.alpha0",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/5372",
    "user": "mhansen"
}
```
Assignee: mabshoff


```
sage -t -long "devel/sage/sage/libs/mwrank/all.py"
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 26:
   sage: file= Sage_TMP + '/PRIMES'
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[2]>", line 1, in <module>
       file= Sage_TMP + '/PRIMES'###line 26:
   sage: file= Sage_TMP + '/PRIMES'
   NameError: name 'Sage_TMP' is not defined
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 27:
   sage: open(file,'w').write(' '.join([str(p) for p in prime_range
(10^6)]))
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[3]>", line 1, in <module>
       open(file,'w').write(' '.join([str(p) for p in prime_range
(Integer(10)**Integer(6))]))###line 27:
   sage: open(file,'w').write(' '.join([str(p) for p in prime_range
(10^6)]))
   TypeError: coercing to Unicode: need string or buffer, type found
**********************************************************************
File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/devel/sage/
sage/libs/mwrank/all.py", line 28:
   sage: mwrank_initprimes(file, verb=False)
Exception raised:
   Traceback (most recent call last):
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1231, in run_one_test
       self.run_one_example(test, example, filename, compileflags)
     File "/Applications/sage_builds/sage-3.3.rc1/local/bin/
sagedoctest.py", line 38, in run_one_example
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
bin/ncadoctest.py", line 1172, in run_one_example
       compileflags, 1) in test.globs
     File "<doctest __main__.example_1[4]>", line 1, in <module>
       mwrank_initprimes(file, verb=False)###line 28:
   sage: mwrank_initprimes(file, verb=False)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
lib/python2.5/site-packages/sage/libs/mwrank/all.py", line 31, in
mwrank_initprimes
       return mwrank_initprimes(filename, verb)
     File "mwrank.pyx", line 119, in
sage.libs.mwrank.mwrank.initprimes (sage/libs/mwrank/mwrank.c:630)
     File "/Applications/sage_builds/sage-3.4.alpha0-upgrade/local/
lib/python2.5/posixpath.py", line 171, in exists
       st = os.stat(path)
   TypeError: coercing to Unicode: need string or buffer, type found
```


Issue created by migration from https://trac.sagemath.org/ticket/5372





---

archive/issue_comments_041380.json:
```json
{
    "body": "Attachment [trac_5372.patch](tarball://root/attachments/some-uuid/ticket5372/trac_5372.patch) by mhansen created at 2009-02-25 18:29:35",
    "created_at": "2009-02-25T18:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41380",
    "user": "mhansen"
}
```

Attachment [trac_5372.patch](tarball://root/attachments/some-uuid/ticket5372/trac_5372.patch) by mhansen created at 2009-02-25 18:29:35



---

archive/issue_comments_041381.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-02-25T18:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41381",
    "user": "mhansen"
}
```

Changing status from new to assigned.



---

archive/issue_comments_041382.json:
```json
{
    "body": "Changing assignee from mabshoff to mhansen.",
    "created_at": "2009-02-25T18:45:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41382",
    "user": "mhansen"
}
```

Changing assignee from mabshoff to mhansen.



---

archive/issue_comments_041383.json:
```json
{
    "body": "After applying the patch:\n\n\n\n```\nsage -t -long \"devel/sage/sage/libs/mwrank/all.py\"          \n\t [7.5 s]\n \n----------------------------------------------------------------------\nAll tests passed!\nTotal time for all tests: 7.5 seconds\n\n```\n\n\nSo a positive review.\n\nJaap",
    "created_at": "2009-02-26T14:31:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41383",
    "user": "jsp"
}
```

After applying the patch:



```
sage -t -long "devel/sage/sage/libs/mwrank/all.py"          
	 [7.5 s]
 
----------------------------------------------------------------------
All tests passed!
Total time for all tests: 7.5 seconds

```


So a positive review.

Jaap



---

archive/issue_comments_041384.json:
```json
{
    "body": "Merged in Sage 3.4.rc0.\n\nCheers,\n\nMichael",
    "created_at": "2009-02-28T16:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41384",
    "user": "mabshoff"
}
```

Merged in Sage 3.4.rc0.

Cheers,

Michael



---

archive/issue_comments_041385.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-02-28T16:22:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/5372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/5372#issuecomment-41385",
    "user": "mabshoff"
}
```

Resolution: fixed
