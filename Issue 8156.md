# Issue 8156: [with code] new function readdata

archive/issues_008156.json:
```json
{
    "body": "Assignee: @williamstein\n\nCC:  mvngu\n\nI'm missing in Sage a function equivalent to \"readdata\" in Maple,\nwhich reads a file with one object per line, and convert it to a\nlist of the given type. Here is a tentative implementation:\n\n```\ndef readdata(f,typ):\n   fp = open(f,\"r\")\n   l = []\n   while true:\n      s = fp.readline()\n      if s == '':\n         break\n      l.append(typ(s))\n   fp.close()\n   return l\n```\nFor example readdata(\"integers\", ZZ) will read a file containing one\ninteger per line, and convert it to a list of integers. One could\nalso extend the function to read n objects per line.\n\nIf a similar function already exists in Sage, please forgive me.\n\nThe function name might be renamed to read_data.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8156\n\n",
    "created_at": "2010-02-02T20:57:48Z",
    "labels": [
        "component: interfaces",
        "minor"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.5.2",
    "title": "[with code] new function readdata",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8156",
    "user": "https://github.com/zimmermann6"
}
```
Assignee: @williamstein

CC:  mvngu

I'm missing in Sage a function equivalent to "readdata" in Maple,
which reads a file with one object per line, and convert it to a
list of the given type. Here is a tentative implementation:

```
def readdata(f,typ):
   fp = open(f,"r")
   l = []
   while true:
      s = fp.readline()
      if s == '':
         break
      l.append(typ(s))
   fp.close()
   return l
```
For example readdata("integers", ZZ) will read a file containing one
integer per line, and convert it to a list of integers. One could
also extend the function to read n objects per line.

If a similar function already exists in Sage, please forgive me.

The function name might be renamed to read_data.

Issue created by migration from https://trac.sagemath.org/ticket/8156





---

archive/issue_comments_071580.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-02-02T20:58:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71580",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071581.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-02-22T09:32:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71581",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_071582.json:
```json
{
    "body": "I'd like to propose a patch, but since I never created a new function in Sage I don't know in\nwhich file I should add this function (and how to do so that it is available to the user).\nShould I add it in a specialized package (like io)? Any advice would be welcome.\nShould I add it in misc/misc.py??",
    "created_at": "2010-02-22T21:48:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71582",
    "user": "https://github.com/zimmermann6"
}
```

I'd like to propose a patch, but since I never created a new function in Sage I don't know in
which file I should add this function (and how to do so that it is available to the user).
Should I add it in a specialized package (like io)? Any advice would be welcome.
Should I add it in misc/misc.py??



---

archive/issue_comments_071583.json:
```json
{
    "body": "Replying to [comment:2 mpatel]:\n\nSounds like a useful addition to me. Are you saying this will only read in files for which data entries are separated by newline characters? It seems to me that this could be made more general rather easily, though without more details it is hard to say how exactly.\n\nIn any case, I would like to suggest adding it to the interfaces subdirectory.",
    "created_at": "2010-02-22T21:52:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71583",
    "user": "https://github.com/wdjoyner"
}
```

Replying to [comment:2 mpatel]:

Sounds like a useful addition to me. Are you saying this will only read in files for which data entries are separated by newline characters? It seems to me that this could be made more general rather easily, though without more details it is hard to say how exactly.

In any case, I would like to suggest adding it to the interfaces subdirectory.



---

archive/issue_comments_071584.json:
```json
{
    "body": "> In any case, I would like to suggest adding it to the interfaces subdirectory. \n\n\nok, I have prepared a patch with a new file interfaces/readdata.py. However hg_sage.diff()\ndoes not show this new file. How to tell Mercurial to consider it?",
    "created_at": "2010-02-23T07:55:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71584",
    "user": "https://github.com/zimmermann6"
}
```

> In any case, I would like to suggest adding it to the interfaces subdirectory. 


ok, I have prepared a patch with a new file interfaces/readdata.py. However hg_sage.diff()
does not show this new file. How to tell Mercurial to consider it?



---

archive/issue_comments_071585.json:
```json
{
    "body": "Just do `hg add name_of_the_file`.  Before doing this you can try `hg status`, which should show this file with a question mark in front.  After doing `hg add`, it should show the file with a capital A in front.",
    "created_at": "2010-02-23T08:33:19Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71585",
    "user": "https://github.com/aghitza"
}
```

Just do `hg add name_of_the_file`.  Before doing this you can try `hg status`, which should show this file with a question mark in front.  After doing `hg add`, it should show the file with a capital A in front.



---

archive/issue_comments_071586.json:
```json
{
    "body": "Attachment [trac_8156.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156.patch) by @zimmermann6 created at 2010-02-23 09:47:36",
    "created_at": "2010-02-23T09:47:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71586",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8156.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156.patch) by @zimmermann6 created at 2010-02-23 09:47:36



---

archive/issue_comments_071587.json:
```json
{
    "body": "thanks Alex. I have attached my patch, which is ready for review.",
    "created_at": "2010-02-23T09:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71587",
    "user": "https://github.com/zimmermann6"
}
```

thanks Alex. I have attached my patch, which is ready for review.



---

archive/issue_comments_071588.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-02-23T09:49:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71588",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071589.json:
```json
{
    "body": "LGTM.",
    "created_at": "2010-04-18T10:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71589",
    "user": "https://github.com/TimDumol"
}
```

LGTM.



---

archive/issue_comments_071590.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-18T10:19:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71590",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071591.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-04-18T15:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71591",
    "user": "https://github.com/jhpalmieri"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_071592.json:
```json
{
    "body": "On sage.math, I get doctest failures:\n\n```\nsage -t  \"devel/sage/sage/interfaces/read_data.py\"          \n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py\", line 24:\n    sage: !echo \"17\" > in.data; echo \"42\" >> in.data\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1\n         !echo \"17\" > in.data; echo \"42\" >> in.data###line 24:\n    sage: !echo \"17\" > in.data; echo \"42\" >> in.data\n         ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py\", line 25:\n    sage: cat in.data\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[3]>\", line 1\n         cat in.data###line 25:\n    sage: cat in.data\n               ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py\", line 28:\n    sage: l = read_data(\"in.data\", ZZ); l\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[4]>\", line 1, in <module>\n        l = read_data(\"in.data\", ZZ); l###line 28:\n    sage: l = read_data(\"in.data\", ZZ); l\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/lib/python/site-packages/sage/interfaces/read_data.py\", line 34, in read_data\n        fp = open(f,\"r\")\n    IOError: [Errno 2] No such file or directory: 'in.data'\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py\", line 30:\n    sage: !echo \"1.234\" > in.data; echo \"5.678\" >> in.data\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[5]>\", line 1\n         !echo \"1.234\" > in.data; echo \"5.678\" >> in.data###line 30:\n    sage: !echo \"1.234\" > in.data; echo \"5.678\" >> in.data\n         ^\n     SyntaxError: invalid syntax\n**********************************************************************\nFile \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py\", line 31:\n    sage: l = read_data(\"in.data\", RealField(17)); l\nException raised:\n    Traceback (most recent call last):\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[6]>\", line 1, in <module>\n        l = read_data(\"in.data\", RealField(Integer(17))); l###line 31:\n    sage: l = read_data(\"in.data\", RealField(17)); l\n      File \"/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/lib/python/site-packages/sage/interfaces/read_data.py\", line 34, in read_data\n        fp = open(f,\"r\")\n    IOError: [Errno 2] No such file or directory: 'in.data'\n**********************************************************************\n1 items had failures:\n   5 of   7 in __main__.example_1\n***Test Failed*** 5 failures.\n```\nFor portability, it might be better to use Python for the doctests: something like\n\n```\nsage: f = open(\"in.data\", \"w\")\nsage: f.write(\"17\\n42\")\nsage: f.close()\n   etc.\n```\nAlso, line 29, `[17. 42]` looks suspicious: should that period be a comma?",
    "created_at": "2010-04-18T15:59:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71592",
    "user": "https://github.com/jhpalmieri"
}
```

On sage.math, I get doctest failures:

```
sage -t  "devel/sage/sage/interfaces/read_data.py"          
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py", line 24:
    sage: !echo "17" > in.data; echo "42" >> in.data
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1
         !echo "17" > in.data; echo "42" >> in.data###line 24:
    sage: !echo "17" > in.data; echo "42" >> in.data
         ^
     SyntaxError: invalid syntax
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py", line 25:
    sage: cat in.data
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[3]>", line 1
         cat in.data###line 25:
    sage: cat in.data
               ^
     SyntaxError: invalid syntax
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py", line 28:
    sage: l = read_data("in.data", ZZ); l
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[4]>", line 1, in <module>
        l = read_data("in.data", ZZ); l###line 28:
    sage: l = read_data("in.data", ZZ); l
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/lib/python/site-packages/sage/interfaces/read_data.py", line 34, in read_data
        fp = open(f,"r")
    IOError: [Errno 2] No such file or directory: 'in.data'
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py", line 30:
    sage: !echo "1.234" > in.data; echo "5.678" >> in.data
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[5]>", line 1
         !echo "1.234" > in.data; echo "5.678" >> in.data###line 30:
    sage: !echo "1.234" > in.data; echo "5.678" >> in.data
         ^
     SyntaxError: invalid syntax
**********************************************************************
File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/devel/sage/sage/interfaces/read_data.py", line 31:
    sage: l = read_data("in.data", RealField(17)); l
Exception raised:
    Traceback (most recent call last):
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        l = read_data("in.data", RealField(Integer(17))); l###line 31:
    sage: l = read_data("in.data", RealField(17)); l
      File "/mnt/usb1/scratch/palmieri/sage-4.4.alpha0-testing/local/lib/python/site-packages/sage/interfaces/read_data.py", line 34, in read_data
        fp = open(f,"r")
    IOError: [Errno 2] No such file or directory: 'in.data'
**********************************************************************
1 items had failures:
   5 of   7 in __main__.example_1
***Test Failed*** 5 failures.
```
For portability, it might be better to use Python for the doctests: something like

```
sage: f = open("in.data", "w")
sage: f.write("17\n42")
sage: f.close()
   etc.
```
Also, line 29, `[17. 42]` looks suspicious: should that period be a comma?



---

archive/issue_comments_071593.json:
```json
{
    "body": "Oh, also please include an \"INPUT\" block in the docstring.  For instance, what exactly do you mean by a \"type\" for the argument \"t\"?",
    "created_at": "2010-04-18T16:01:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71593",
    "user": "https://github.com/jhpalmieri"
}
```

Oh, also please include an "INPUT" block in the docstring.  For instance, what exactly do you mean by a "type" for the argument "t"?



---

archive/issue_comments_071594.json:
```json
{
    "body": "One more thing: if you're going to create a file in a doctest, then create it in a temporary directory.  See the second point here: [http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples](http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples).",
    "created_at": "2010-04-18T16:33:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71594",
    "user": "https://github.com/jhpalmieri"
}
```

One more thing: if you're going to create a file in a doctest, then create it in a temporary directory.  See the second point here: [http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples](http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples).



---

archive/issue_comments_071595.json:
```json
{
    "body": "My bad on the false positive. Sorry.",
    "created_at": "2010-04-18T16:42:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71595",
    "user": "https://github.com/TimDumol"
}
```

My bad on the false positive. Sorry.



---

archive/issue_comments_071596.json:
```json
{
    "body": "No problem.",
    "created_at": "2010-04-18T18:04:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71596",
    "user": "https://github.com/jhpalmieri"
}
```

No problem.



---

archive/issue_comments_071597.json:
```json
{
    "body": "Attachment [trac_8156a.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156a.patch) by @zimmermann6 created at 2010-04-19 16:33:47",
    "created_at": "2010-04-19T16:33:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71597",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8156a.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156a.patch) by @zimmermann6 created at 2010-04-19 16:33:47



---

archive/issue_comments_071598.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-04-19T16:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71598",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_071599.json:
```json
{
    "body": "thank you Tim and John for your review. I've attached a new patch (to be applied alone). I've\ntested it on 4.3.5. A minor issue is that in the documentation f.write(\"17\\n42\") is split\nalong two lines... Should I put \\\\ in the docstring?\n\nPaul",
    "created_at": "2010-04-19T16:37:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71599",
    "user": "https://github.com/zimmermann6"
}
```

thank you Tim and John for your review. I've attached a new patch (to be applied alone). I've
tested it on 4.3.5. A minor issue is that in the documentation f.write("17\n42") is split
along two lines... Should I put \\ in the docstring?

Paul



---

archive/issue_comments_071600.json:
```json
{
    "body": "Replying to [comment:14 zimmerma]:\n> Should I put \\\\ in the docstring?\n\n\nFirst try changing \"\"\" to r\"\"\" at the beginning of the docstring.  That might fix it.",
    "created_at": "2010-04-19T17:11:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71600",
    "user": "https://github.com/jhpalmieri"
}
```

Replying to [comment:14 zimmerma]:
> Should I put \\ in the docstring?


First try changing """ to r""" at the beginning of the docstring.  That might fix it.



---

archive/issue_comments_071601.json:
```json
{
    "body": "Attachment [trac_8156b.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156b.patch) by @zimmermann6 created at 2010-04-20 09:38:09",
    "created_at": "2010-04-20T09:38:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71601",
    "user": "https://github.com/zimmermann6"
}
```

Attachment [trac_8156b.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156b.patch) by @zimmermann6 created at 2010-04-20 09:38:09



---

archive/issue_comments_071602.json:
```json
{
    "body": "> First try changing \"\"\" to r\"\"\" at the beginning of the docstring. That might fix it. \n\n\nnot quite. It solves the line break problem, but \"17\\n42\\n\" appears as \"17n42n\" in the ascii\ndocumentation. Anyway this is a different issue, since it also happens with (for example):\n\n```\nsage: from sage.combinat.matrices.latin import *\nsage: B = back_circulant(4)\nsage: B.find_disjoint_mates?\n```\nwhere `print B0, \"\\n,\\n\", B1` appears as `print B0, \"n,n\", B1`.\n\nTo reviewers and release manager: only apply the last patch `trac_8156b.patch`.",
    "created_at": "2010-04-20T09:43:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71602",
    "user": "https://github.com/zimmermann6"
}
```

> First try changing """ to r""" at the beginning of the docstring. That might fix it. 


not quite. It solves the line break problem, but "17\n42\n" appears as "17n42n" in the ascii
documentation. Anyway this is a different issue, since it also happens with (for example):

```
sage: from sage.combinat.matrices.latin import *
sage: B = back_circulant(4)
sage: B.find_disjoint_mates?
```
where `print B0, "\n,\n", B1` appears as `print B0, "n,n", B1`.

To reviewers and release manager: only apply the last patch `trac_8156b.patch`.



---

archive/issue_comments_071603.json:
```json
{
    "body": "Doctests pass. Positive review.\n\nManager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.",
    "created_at": "2010-06-23T08:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71603",
    "user": "https://github.com/TimDumol"
}
```

Doctests pass. Positive review.

Manager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.



---

archive/issue_comments_071604.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-06-23T08:49:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71604",
    "user": "https://github.com/TimDumol"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071605.json:
```json
{
    "body": "Changing status from positive_review to needs_info.",
    "created_at": "2010-07-21T03:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71605",
    "user": "https://github.com/qed777"
}
```

Changing status from positive_review to needs_info.



---

archive/issue_comments_071606.json:
```json
{
    "body": "Replying to [comment:17 timdumol]:\n> Doctests pass. Positive review.\n> \n> Manager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.\n\nI think it's OK if we don't delete the file explicitly.  But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?\n\nMinh, what do you think?",
    "created_at": "2010-07-21T03:07:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71606",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:17 timdumol]:
> Doctests pass. Positive review.
> 
> Manager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.

I think it's OK if we don't delete the file explicitly.  But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?

Minh, what do you think?



---

archive/issue_comments_071607.json:
```json
{
    "body": "Replying to [comment:18 mpatel]:\n> I think it's OK if we don't delete the file explicitly. \n\n\nIt saves a lot of headache for a program to clean up after itself. This happens when you exit a Sage session; temporary files/directories created under `SAGE_TMP` would automatically be deleted when Sage exits. So there's no need to explicitly delete stuff under `SAGE_TMP`.\n\n\n\n\n> But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?\n\n\nThat's a very neat idea, especially considering that a lot of doctests do create temporary files. It's very easy to have name clashes when you doctest in parallel. Another useful command is `tmp_dir()` for creating a temporary directory. Both `tmp_filename()` and `tmp_dir()` are highly recommended for use in doctests.",
    "created_at": "2010-07-21T06:36:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71607",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:18 mpatel]:
> I think it's OK if we don't delete the file explicitly. 


It saves a lot of headache for a program to clean up after itself. This happens when you exit a Sage session; temporary files/directories created under `SAGE_TMP` would automatically be deleted when Sage exits. So there's no need to explicitly delete stuff under `SAGE_TMP`.




> But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?


That's a very neat idea, especially considering that a lot of doctests do create temporary files. It's very easy to have name clashes when you doctest in parallel. Another useful command is `tmp_dir()` for creating a temporary directory. Both `tmp_filename()` and `tmp_dir()` are highly recommended for use in doctests.



---

archive/issue_comments_071608.json:
```json
{
    "body": "Use `tmp_filename`.  Apply only this patch.",
    "created_at": "2010-07-21T10:39:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71608",
    "user": "https://github.com/qed777"
}
```

Use `tmp_filename`.  Apply only this patch.



---

archive/issue_comments_071609.json:
```json
{
    "body": "Attachment [trac_8156c.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156c.patch) by @qed777 created at 2010-07-21 10:41:22\n\nI've attached a patch that uses `tmp_filename`.",
    "created_at": "2010-07-21T10:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71609",
    "user": "https://github.com/qed777"
}
```

Attachment [trac_8156c.patch](tarball://root/attachments/some-uuid/ticket8156/trac_8156c.patch) by @qed777 created at 2010-07-21 10:41:22

I've attached a patch that uses `tmp_filename`.



---

archive/issue_comments_071610.json:
```json
{
    "body": "Changing status from needs_info to needs_review.",
    "created_at": "2010-07-21T10:41:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71610",
    "user": "https://github.com/qed777"
}
```

Changing status from needs_info to needs_review.



---

archive/issue_comments_071611.json:
```json
{
    "body": "Replying to [comment:20 mpatel]:\n> I've attached a patch that uses `tmp_filename`.\n\n\nam I allowed to review that patch, being the author of the original patch?\n\nPaul",
    "created_at": "2010-07-21T19:29:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71611",
    "user": "https://github.com/zimmermann6"
}
```

Replying to [comment:20 mpatel]:
> I've attached a patch that uses `tmp_filename`.


am I allowed to review that patch, being the author of the original patch?

Paul



---

archive/issue_comments_071612.json:
```json
{
    "body": "Replying to [comment:21 zimmerma]:\n> Replying to [comment:20 mpatel]:\n> > I've attached a patch that uses `tmp_filename`.\n\n> \n> am I allowed to review that patch, being the author of the original patch?\n\n\nSure!",
    "created_at": "2010-07-21T19:39:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71612",
    "user": "https://github.com/qed777"
}
```

Replying to [comment:21 zimmerma]:
> Replying to [comment:20 mpatel]:
> > I've attached a patch that uses `tmp_filename`.

> 
> am I allowed to review that patch, being the author of the original patch?


Sure!



---

archive/issue_comments_071613.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-07-22T08:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71613",
    "user": "https://github.com/zimmermann6"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071614.json:
```json
{
    "body": "all doctests still pass, and using tmp_filename is indeed better. Positive review.\n\nPaul",
    "created_at": "2010-07-22T08:00:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71614",
    "user": "https://github.com/zimmermann6"
}
```

all doctests still pass, and using tmp_filename is indeed better. Positive review.

Paul



---

archive/issue_comments_071615.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-07-22T23:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71615",
    "user": "https://github.com/dandrake"
}
```

Resolution: fixed



---

archive/issue_events_019538.json:
```json
{
    "actor": "https://github.com/dandrake",
    "created_at": "2010-07-22T23:37:01Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8156#event-19538"
}
```



---

archive/issue_comments_071616.json:
```json
{
    "body": "Merged trac_8156c.patch in 4.5.2.alpha1.",
    "created_at": "2010-07-22T23:37:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8156",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8156#issuecomment-71616",
    "user": "https://github.com/dandrake"
}
```

Merged trac_8156c.patch in 4.5.2.alpha1.
