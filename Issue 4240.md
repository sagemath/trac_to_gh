# Issue 4240: magma -- increase doctest coverage of magma.py from current 17% to 100%.

archive/issues_004240.json:
```json
{
    "body": "Assignee: was\n\nCC:  georgsweber\n\nRight now the doctest coverage of devel/sage/sage/interfaces/magma.py is a pitiful 17%.  Increase this to 100%.   This will involving adding about 59 doctests and docstrings.  See also #4231, which adds two docstrings/doctests.\n\nIssue created by migration from https://trac.sagemath.org/ticket/4240\n\n",
    "created_at": "2008-10-04T03:42:48Z",
    "labels": [
        "interfaces",
        "major",
        "enhancement"
    ],
    "title": "magma -- increase doctest coverage of magma.py from current 17% to 100%.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4240",
    "user": "was"
}
```
Assignee: was

CC:  georgsweber

Right now the doctest coverage of devel/sage/sage/interfaces/magma.py is a pitiful 17%.  Increase this to 100%.   This will involving adding about 59 doctests and docstrings.  See also #4231, which adds two docstrings/doctests.

Issue created by migration from https://trac.sagemath.org/ticket/4240





---

archive/issue_comments_030814.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2008-10-04T03:42:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30814",
    "user": "was"
}
```

Changing status from new to assigned.



---

archive/issue_comments_030815.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-04T05:43:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30815",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_030816.json:
```json
{
    "body": "coverage up to 69% -- all non underscore methods are now documented.",
    "created_at": "2008-10-11T15:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30816",
    "user": "was"
}
```

coverage up to 69% -- all non underscore methods are now documented.



---

archive/issue_comments_030817.json:
```json
{
    "body": "Attachment\n\ninsert all needed # optional's",
    "created_at": "2008-10-11T15:38:29Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30817",
    "user": "was"
}
```

Attachment

insert all needed # optional's



---

archive/issue_comments_030818.json:
```json
{
    "body": "Attachment",
    "created_at": "2008-10-11T15:39:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30818",
    "user": "was"
}
```

Attachment



---

archive/issue_comments_030819.json:
```json
{
    "body": "Hi,\n\nseveral issues.\nOn the one hand, the first patch does not apply cleanly against 3.1.3 alpha series, since the hunk in gap.py does not fit (the \"prompt\" funtion to be removed did get a doctest, so the automatism breaks).\nMore severely, there are invalid absolute paths in beginning with \"/home/wstein/\", specific to your local install, see what I get:\n\n\n```\nsage -t -long devel/sage-main/sage/interfaces/magma.py      **********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py\", line 598:\n    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)\nExpected:\n    Traceback (most recent call last):\n    ...\n    RuntimeError: Can't open package spec file /home/wstein/sage/data/extcode/magma/spec2 for reading (No such file or directory)\nGot:\n    Traceback (most recent call last):\n      File \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/doctest.py\", line 1228, in __run\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_18[3]>\", line 1, in <module>\n        magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)###line 598:\n    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)\n      File \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/interfaces/magma.py\", line 605, in attach_spec\n        raise RuntimeError, s.strip()\n    RuntimeError: Can't open package spec file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/data/extcode/magma/spec2 for reading (No such file or directory)\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py\", line 626:\n    sage: print magma.load(SAGE_TMP + 'a.m')\nExpected:\n    Loading \"/home/wstein/.sage//temp/one/.../a.m\"\n    hi\nGot:\n    Loading \"/Users/georgweber/.sage//temp/susanne_webers_computer.local/602/a.m\"\n    hi\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py\", line 930:\n    sage: magma.get_verbose(\"Groebner\")\nExpected:\n    2\nGot:\n    0\n**********************************************************************\nFile \"/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py\", line 948:\n    sage: magma.GetVerbose(\"Groebner\")\nExpected:\n    2\nGot:\n    0\n**********************************************************************\n4 items had failures:\n   1 of   4 in __main__.example_18\n   1 of   5 in __main__.example_19\n   1 of   3 in __main__.example_27\n   1 of   3 in __main__.example_28\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/.doctest_magma.py\n         [34.6 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n        sage -t -long devel/sage-main/sage/interfaces/magma.py\nTotal time for all tests: 34.6 seconds\n```\n\n\nThe path issues should go away with some triple dots.\n\nHowever, I have no idea yet what that last \"Groebner\" issue is (Expected: 2; Got: 0).\n\nMy Magma install says: \"Magma V2.14-9\", what does yours say?\n\nCheers,\ngsw",
    "created_at": "2008-10-11T22:00:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30819",
    "user": "GeorgSWeber"
}
```

Hi,

several issues.
On the one hand, the first patch does not apply cleanly against 3.1.3 alpha series, since the hunk in gap.py does not fit (the "prompt" funtion to be removed did get a doctest, so the automatism breaks).
More severely, there are invalid absolute paths in beginning with "/home/wstein/", specific to your local install, see what I get:


```
sage -t -long devel/sage-main/sage/interfaces/magma.py      **********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 598:
    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError: Can't open package spec file /home/wstein/sage/data/extcode/magma/spec2 for reading (No such file or directory)
Got:
    Traceback (most recent call last):
      File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_18[3]>", line 1, in <module>
        magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)###line 598:
    sage: magma.attach_spec('%s/data/extcode/magma/spec2'%SAGE_ROOT)
      File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/local/lib/python2.5/site-packages/sage/interfaces/magma.py", line 605, in attach_spec
        raise RuntimeError, s.strip()
    RuntimeError: Can't open package spec file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/data/extcode/magma/spec2 for reading (No such file or directory)
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 626:
    sage: print magma.load(SAGE_TMP + 'a.m')
Expected:
    Loading "/home/wstein/.sage//temp/one/.../a.m"
    hi
Got:
    Loading "/Users/georgweber/.sage//temp/susanne_webers_computer.local/602/a.m"
    hi
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 930:
    sage: magma.get_verbose("Groebner")
Expected:
    2
Got:
    0
**********************************************************************
File "/Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/magma.py", line 948:
    sage: magma.GetVerbose("Groebner")
Expected:
    2
Got:
    0
**********************************************************************
4 items had failures:
   1 of   4 in __main__.example_18
   1 of   5 in __main__.example_19
   1 of   3 in __main__.example_27
   1 of   3 in __main__.example_28
***Test Failed*** 4 failures.
For whitespace errors, see the file /Users/georgweber/Public/sage/sage-3.1.3.alpha1/tmp/.doctest_magma.py
         [34.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


        sage -t -long devel/sage-main/sage/interfaces/magma.py
Total time for all tests: 34.6 seconds
```


The path issues should go away with some triple dots.

However, I have no idea yet what that last "Groebner" issue is (Expected: 2; Got: 0).

My Magma install says: "Magma V2.14-9", what does yours say?

Cheers,
gsw



---

archive/issue_comments_030820.json:
```json
{
    "body": "Ah,\n\nwe try to load a package, that can't be found.\nThis does not go away just using triple dots in paths, instead some environment variable magic has to be used, but might explain the Groebner thing.",
    "created_at": "2008-10-11T22:04:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30820",
    "user": "GeorgSWeber"
}
```

Ah,

we try to load a package, that can't be found.
This does not go away just using triple dots in paths, instead some environment variable magic has to be used, but might explain the Groebner thing.



---

archive/issue_comments_030821.json:
```json
{
    "body": "> not apply cleanly against 3.1.3 alpha \n\nIt's against 3.1.2.\n\nRegarding the Groebner output, I think you didn't apply all the patches, since you have\n\n```\nsage: magma.get_verbose(\"Groebner\")\n```\n\nin your log above, but the input line should be\n\n```\nsage: magma.get_verbose(\"Groebner\")        # optional\n```\n\n\nIn particular, you are doing\n\n```\n        sage -t -long devel/sage-main/sage/interfaces/magma.py\n```\n\nwhich with the third patch above should essentially do almost nothing, since\nyou forgot to put --optional.\n\n\nRegarding\n> we try to load a package, that can't be found. This does not go away \n> just using triple dots in paths, instead some environment variable magic \n> has to be used, but might explain the Groebner thing. \n\nIt is unrelated to Groebner.  This will go away by putting in some ...'s.",
    "created_at": "2008-10-12T12:30:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30821",
    "user": "was"
}
```

> not apply cleanly against 3.1.3 alpha 

It's against 3.1.2.

Regarding the Groebner output, I think you didn't apply all the patches, since you have

```
sage: magma.get_verbose("Groebner")
```

in your log above, but the input line should be

```
sage: magma.get_verbose("Groebner")        # optional
```


In particular, you are doing

```
        sage -t -long devel/sage-main/sage/interfaces/magma.py
```

which with the third patch above should essentially do almost nothing, since
you forgot to put --optional.


Regarding
> we try to load a package, that can't be found. This does not go away 
> just using triple dots in paths, instead some environment variable magic 
> has to be used, but might explain the Groebner thing. 

It is unrelated to Groebner.  This will go away by putting in some ...'s.



---

archive/issue_comments_030822.json:
```json
{
    "body": "I fixed all the problems and a trivial reviewer patch is coming up. I did delete two hunks from the part3 patch since it contained fixes already done independently due to a previous patch. Tests pass with and without optional except two failures due to using Magma 2.13 instead of 2.14 on the test machine, but I can live with that:\n\n```\nsage -t -long -optional devel/sage/sage/interfaces/magma.py \n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py\", line 90:\n    sage: print M2\nExpected:\n    Space of modular forms on Gamma_1(5) with character $.1, weight 2, and dimension 2 over Integer Ring.\nGot:\n    Space of modular forms on Gamma_1(5) with character all conjugates of [$.1], weight 2, and dimension 2 over Integer Ring.\n**********************************************************************\nFile \"/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py\", line 92:\n    sage: print M2.Basis()   # note -- this has been changed to be *wrong* as below in Magma 2.14!!\nExpected:\n    [\n    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + 50*q^8 + 30*q^10 + O(q^12),\n    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + 5*q^8 + 7*q^9 + 5*q^10 + 12*q^11 + O(q^12)\n    ]\nGot:\n    [\n    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + O(q^8),\n    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + O(q^8)\n    ]\n**********************************************************************\n```\n",
    "created_at": "2008-10-12T15:28:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30822",
    "user": "mabshoff"
}
```

I fixed all the problems and a trivial reviewer patch is coming up. I did delete two hunks from the part3 patch since it contained fixes already done independently due to a previous patch. Tests pass with and without optional except two failures due to using Magma 2.13 instead of 2.14 on the test machine, but I can live with that:

```
sage -t -long -optional devel/sage/sage/interfaces/magma.py 
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py", line 90:
    sage: print M2
Expected:
    Space of modular forms on Gamma_1(5) with character $.1, weight 2, and dimension 2 over Integer Ring.
Got:
    Space of modular forms on Gamma_1(5) with character all conjugates of [$.1], weight 2, and dimension 2 over Integer Ring.
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.1.3.rc0/tmp/magma.py", line 92:
    sage: print M2.Basis()   # note -- this has been changed to be *wrong* as below in Magma 2.14!!
Expected:
    [
    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + 50*q^8 + 30*q^10 + O(q^12),
    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + 5*q^8 + 7*q^9 + 5*q^10 + 12*q^11 + O(q^12)
    ]
Got:
    [
    1 + 10*q^2 + 20*q^3 + 20*q^5 + 60*q^7 + O(q^8),
    q + q^2 + 2*q^3 + 3*q^4 + 5*q^5 + 2*q^6 + 6*q^7 + O(q^8)
    ]
**********************************************************************
```




---

archive/issue_comments_030823.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-10-12T15:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30823",
    "user": "mabshoff"
}
```

Resolution: fixed



---

archive/issue_comments_030824.json:
```json
{
    "body": "Merged in Sage 3.1.3.rc0",
    "created_at": "2008-10-12T15:33:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4240",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4240#issuecomment-30824",
    "user": "mabshoff"
}
```

Merged in Sage 3.1.3.rc0
