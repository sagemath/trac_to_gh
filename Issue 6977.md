# Issue 6977: Implement __len__ to add support for MuPAD objects as Python containers

archive/issues_006977.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mhansen@gmail.com sage-combinat\n\nKeywords: MuPAD len\n\nThe title says it all; after the patch, one can do:\n\n            sage: len(mupad([1,2,3]))\n            3\n            sage: map(ZZ, list(mupad([1,2,3])))\n            [1, 2, 3]\n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/6977\n\n",
    "created_at": "2009-09-21T13:43:23Z",
    "labels": [
        "component: interfaces"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.2",
    "title": "Implement __len__ to add support for MuPAD objects as Python containers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6977",
    "user": "https://github.com/nthiery"
}
```
Assignee: @williamstein

CC:  mhansen@gmail.com sage-combinat

Keywords: MuPAD len

The title says it all; after the patch, one can do:

            sage: len(mupad([1,2,3]))
            3
            sage: map(ZZ, list(mupad([1,2,3])))
            [1, 2, 3]



Issue created by migration from https://trac.sagemath.org/ticket/6977





---

archive/issue_comments_057591.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2009-09-21T19:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57591",
    "user": "https://github.com/nthiery"
}
```

Changing status from new to assigned.



---

archive/issue_comments_057592.json:
```json
{
    "body": "Changing assignee from @williamstein to @nthiery.",
    "created_at": "2009-09-21T19:35:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57592",
    "user": "https://github.com/nthiery"
}
```

Changing assignee from @williamstein to @nthiery.



---

archive/issue_comments_057593.json:
```json
{
    "body": "Looks good to me.  There should be double colons after EXAMPLES, but since the rest of the file hasn't been converted over, we can wait to fix it then.",
    "created_at": "2009-09-26T03:44:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57593",
    "user": "https://github.com/mwhansen"
}
```

Looks good to me.  There should be double colons after EXAMPLES, but since the rest of the file hasn't been converted over, we can wait to fix it then.



---

archive/issue_comments_057594.json:
```json
{
    "body": "Any doctest involving MuPAD must be tagged as optional, otherwise one would get doctest failures. For example, for the patch `trac_6977_mupad_len.patch` the test\n\n```\nsage: len(mupad([1,2,3])) # indirect doctest\n```\ndepends on having MuPAD one's local machine, so it should be written as\n\n```\nsage: len(mupad([1,2,3])) # optional indirect doctest\n```\nAfter applying the patch, I got these doctest failures:\n\n```\nsage -t -long devel/sage/sage/interfaces/mupad.py\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 599:\n    sage: len(mupad([1,2,3])) # indirect doctest\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[2]>\", line 1, in <module>\n        len(mupad([Integer(1),Integer(2),Integer(3)])) # indirect doctest###line 599:\n    sage: len(mupad([1,2,3])) # indirect doctest\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1044, in __call__\n        raise TypeError, msg\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 601:\n    sage: type(len(mupad([1,2,3])))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[3]>\", line 1, in <module>\n        type(len(mupad([Integer(1),Integer(2),Integer(3)])))###line 601:\n    sage: type(len(mupad([1,2,3])))\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1044, in __call__\n        raise TypeError, msg\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 604:\n    sage: len(mupad(4))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[4]>\", line 1, in <module>\n        len(mupad(Integer(4)))###line 604:\n    sage: len(mupad(4))\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1033, in __call__\n        return self._coerce_from_special_method(x)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1059, in _coerce_from_special_method\n        return self(x._interface_init_())\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1031, in __call__\n        return cls(self, x, name=name)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1447, in __init__\n        raise TypeError, x\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 610:\n    sage: map(ZZ, list(mupad([1,2,3])))\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[5]>\", line 1, in <module>\n        map(ZZ, list(mupad([Integer(1),Integer(2),Integer(3)])))###line 610:\n    sage: map(ZZ, list(mupad([1,2,3])))\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1044, in __call__\n        raise TypeError, msg\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 613:\n    sage: [int(x) for x in mupad([1,2,3]) ]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[6]>\", line 1, in <module>\n        [int(x) for x in mupad([Integer(1),Integer(2),Integer(3)]) ]###line 613:\n    sage: [int(x) for x in mupad([1,2,3]) ]\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1044, in __call__\n        raise TypeError, msg\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\nFile \"/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py\", line 616:\n    sage: [int(x) for x in mupad(\"{1,2,3,5}\") ]\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_34[7]>\", line 1, in <module>\n        [int(x) for x in mupad(\"{1,2,3,5}\") ]###line 616:\n    sage: [int(x) for x in mupad(\"{1,2,3,5}\") ]\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1031, in __call__\n        return cls(self, x, name=name)\n      File \"/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py\", line 1447, in __init__\n        raise TypeError, x\n    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.\n\n    In order to use the MuPAD interface you need to have MuPAD installed\n    and have a script in your PATH called \"mupkern\" that runs the\n    command-line version of MuPAD. \n\n      (1) You might have to buy MuPAD.\n          \n      (2) * LINUX: The mupkern script comes standard with your Mupad install.\n            \n          * APPLE OS X:\n             ???\n\n**********************************************************************\n1 items had failures:\n   6 of   8 in __main__.example_34\n***Test Failed*** 6 failures.\nFor whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_mupad.py\n\t [2.0 s]\n```",
    "created_at": "2009-09-26T08:40:08Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57594",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Any doctest involving MuPAD must be tagged as optional, otherwise one would get doctest failures. For example, for the patch `trac_6977_mupad_len.patch` the test

```
sage: len(mupad([1,2,3])) # indirect doctest
```
depends on having MuPAD one's local machine, so it should be written as

```
sage: len(mupad([1,2,3])) # optional indirect doctest
```
After applying the patch, I got these doctest failures:

```
sage -t -long devel/sage/sage/interfaces/mupad.py
**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 599:
    sage: len(mupad([1,2,3])) # indirect doctest
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[2]>", line 1, in <module>
        len(mupad([Integer(1),Integer(2),Integer(3)])) # indirect doctest###line 599:
    sage: len(mupad([1,2,3])) # indirect doctest
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 601:
    sage: type(len(mupad([1,2,3])))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[3]>", line 1, in <module>
        type(len(mupad([Integer(1),Integer(2),Integer(3)])))###line 601:
    sage: type(len(mupad([1,2,3])))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 604:
    sage: len(mupad(4))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[4]>", line 1, in <module>
        len(mupad(Integer(4)))###line 604:
    sage: len(mupad(4))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1033, in __call__
        return self._coerce_from_special_method(x)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1059, in _coerce_from_special_method
        return self(x._interface_init_())
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1031, in __call__
        return cls(self, x, name=name)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1447, in __init__
        raise TypeError, x
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 610:
    sage: map(ZZ, list(mupad([1,2,3])))
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[5]>", line 1, in <module>
        map(ZZ, list(mupad([Integer(1),Integer(2),Integer(3)])))###line 610:
    sage: map(ZZ, list(mupad([1,2,3])))
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 613:
    sage: [int(x) for x in mupad([1,2,3]) ]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[6]>", line 1, in <module>
        [int(x) for x in mupad([Integer(1),Integer(2),Integer(3)]) ]###line 613:
    sage: [int(x) for x in mupad([1,2,3]) ]
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1044, in __call__
        raise TypeError, msg
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
File "/scratch/mvngu/release/sage-4.1.2.alpha2/devel/sage-main/sage/interfaces/mupad.py", line 616:
    sage: [int(x) for x in mupad("{1,2,3,5}") ]
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_34[7]>", line 1, in <module>
        [int(x) for x in mupad("{1,2,3,5}") ]###line 616:
    sage: [int(x) for x in mupad("{1,2,3,5}") ]
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1031, in __call__
        return cls(self, x, name=name)
      File "/scratch/mvngu/release/sage-4.1.2.alpha2/local/lib/python/site-packages/sage/interfaces/expect.py", line 1447, in __init__
        raise TypeError, x
    TypeError: Unable to start MuPAD because the command 'mupkern -P e -U SAGE=TRUE' failed.

    In order to use the MuPAD interface you need to have MuPAD installed
    and have a script in your PATH called "mupkern" that runs the
    command-line version of MuPAD. 

      (1) You might have to buy MuPAD.
          
      (2) * LINUX: The mupkern script comes standard with your Mupad install.
            
          * APPLE OS X:
             ???

**********************************************************************
1 items had failures:
   6 of   8 in __main__.example_34
***Test Failed*** 6 failures.
For whitespace errors, see the file /home/mvngu/.sage//tmp/.doctest_mupad.py
	 [2.0 s]
```



---

archive/issue_comments_057595.json:
```json
{
    "body": "Attachment [trac_6977_mupad_len.patch](tarball://root/attachments/some-uuid/ticket6977/trac_6977_mupad_len.patch) by @nthiery created at 2009-09-30 10:19:15",
    "created_at": "2009-09-30T10:19:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57595",
    "user": "https://github.com/nthiery"
}
```

Attachment [trac_6977_mupad_len.patch](tarball://root/attachments/some-uuid/ticket6977/trac_6977_mupad_len.patch) by @nthiery created at 2009-09-30 10:19:15



---

archive/issue_comments_057596.json:
```json
{
    "body": "The updated version adds\n- The missing #optional flags, the missing '::' (Oops, thanks Minh & Mike for the review and spotting those)\n- Fixes the implementation of len (bigger Oops: with MuPAD-Combinat, l := [1,2,3]; l::nops gives FAIL!!!!)\n- Add a comment about another failing test\n\nNow: should this be seen as a bug fix or enhancement ? I.e. go through the feature freeze for 4.1.2? It does not risk to break much anyway.",
    "created_at": "2009-09-30T10:23:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57596",
    "user": "https://github.com/nthiery"
}
```

The updated version adds
- The missing #optional flags, the missing '::' (Oops, thanks Minh & Mike for the review and spotting those)
- Fixes the implementation of len (bigger Oops: with MuPAD-Combinat, l := [1,2,3]; l::nops gives FAIL!!!!)
- Add a comment about another failing test

Now: should this be seen as a bug fix or enhancement ? I.e. go through the feature freeze for 4.1.2? It does not risk to break much anyway.



---

archive/issue_comments_057597.json:
```json
{
    "body": "Looks good.",
    "created_at": "2009-10-05T07:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57597",
    "user": "https://github.com/mwhansen"
}
```

Looks good.



---

archive/issue_events_016389.json:
```json
{
    "actor": "https://github.com/mwhansen",
    "created_at": "2009-10-15T08:53:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6977#event-16389"
}
```



---

archive/issue_comments_057598.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-10-15T08:53:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6977",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6977#issuecomment-57598",
    "user": "https://github.com/mwhansen"
}
```

Resolution: fixed
