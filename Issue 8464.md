# Issue 8464: add FAQ to standard documentation

archive/issues_008464.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  jhpalmieri\n\nAdd the [FAQ](http://wiki.sagemath.org/faq) on the Sage wiki to the Sage [standard documentation](http://www.sagemath.org/doc/). The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).\n\nIssue created by migration from https://trac.sagemath.org/ticket/8464\n\n",
    "created_at": "2010-03-07T01:52:58Z",
    "labels": [
        "documentation",
        "major",
        "enhancement"
    ],
    "title": "add FAQ to standard documentation",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8464",
    "user": "mvngu"
}
```
Assignee: mvngu

CC:  jhpalmieri

Add the [FAQ](http://wiki.sagemath.org/faq) on the Sage wiki to the Sage [standard documentation](http://www.sagemath.org/doc/). The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).

Issue created by migration from https://trac.sagemath.org/ticket/8464





---

archive/issue_comments_076183.json:
```json
{
    "body": "Changing keywords from \"\" to \"FAQ\".",
    "created_at": "2010-03-07T02:03:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76183",
    "user": "mvngu"
}
```

Changing keywords from "" to "FAQ".



---

archive/issue_comments_076184.json:
```json
{
    "body": "I don't know if this is ready for review yet, but here are a few comments:\n\n- there is a typo in one of the links (found by using \"sage -docbuild faq linkcheck\", which I just discovered!).  This is fixed in my small patch.  \n\n- should this be added to the \"website\" docbuild target?  (I'm not sure; arguments could be made either way, I think.)\n\n- this document doesn't match up very well with the FAQ on the wiki.  Why?",
    "created_at": "2010-03-10T23:50:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76184",
    "user": "jhpalmieri"
}
```

I don't know if this is ready for review yet, but here are a few comments:

- there is a typo in one of the links (found by using "sage -docbuild faq linkcheck", which I just discovered!).  This is fixed in my small patch.  

- should this be added to the "website" docbuild target?  (I'm not sure; arguments could be made either way, I think.)

- this document doesn't match up very well with the FAQ on the wiki.  Why?



---

archive/issue_comments_076185.json:
```json
{
    "body": "Replying to [comment:5 jhpalmieri]:\n> I don't know if this is ready for review yet, but here are a few comments:\n\nThis is a work in progress.\n\n\n\n\n>  - there is a typo in one of the links (found by using \"sage -docbuild faq linkcheck\", which I just discovered!).  This is fixed in my small patch.  \n\nThank you.\n\n\n\n\n>  - should this be added to the \"website\" docbuild target?  (I'm not sure; arguments could be made either way, I think.)\n\nThe docbuild target \"faq\" is automatically added. The index.html page of the website has been changed to include the FAQ.\n\n\n\n\n>  - this document doesn't match up very well with the FAQ on the wiki.  Why?\n\nThe FAQ on the Sage wiki is a mess. The current ticket is an attempt to pull together information from the FAQ on the wiki and other sources. The resulting information is then to be organized following the model of the [Django FAQ](http://docs.djangoproject.com/en/1.1/faq/).",
    "created_at": "2010-03-11T01:10:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76185",
    "user": "mvngu"
}
```

Replying to [comment:5 jhpalmieri]:
> I don't know if this is ready for review yet, but here are a few comments:

This is a work in progress.




>  - there is a typo in one of the links (found by using "sage -docbuild faq linkcheck", which I just discovered!).  This is fixed in my small patch.  

Thank you.




>  - should this be added to the "website" docbuild target?  (I'm not sure; arguments could be made either way, I think.)

The docbuild target "faq" is automatically added. The index.html page of the website has been changed to include the FAQ.




>  - this document doesn't match up very well with the FAQ on the wiki.  Why?

The FAQ on the Sage wiki is a mess. The current ticket is an attempt to pull together information from the FAQ on the wiki and other sources. The resulting information is then to be organized following the model of the [Django FAQ](http://docs.djangoproject.com/en/1.1/faq/).



---

archive/issue_comments_076186.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2010-03-11T04:29:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76186",
    "user": "mvngu"
}
```

reviewer patch



---

archive/issue_comments_076187.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-03-11T04:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76187",
    "user": "mvngu"
}
```

Attachment



---

archive/issue_comments_076188.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-11T04:32:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76188",
    "user": "mvngu"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_076189.json:
```json
{
    "body": "Sage 4.3.5, One more question added to the FAQ",
    "created_at": "2010-04-04T15:13:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76189",
    "user": "JGuzman"
}
```

Sage 4.3.5, One more question added to the FAQ



---

archive/issue_comments_076190.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2010-04-04T15:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76190",
    "user": "mvngu"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_076191.json:
```json
{
    "body": "Attachment\n\nCalTech is using Sage. See http://www.its.caltech.edu/~awalker/sage.html. Update the FAQ with that institutional user.",
    "created_at": "2010-04-04T15:29:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76191",
    "user": "mvngu"
}
```

Attachment

CalTech is using Sage. See http://www.its.caltech.edu/~awalker/sage.html. Update the FAQ with that institutional user.



---

archive/issue_comments_076192.json:
```json
{
    "body": "The documents build without error and they look good, in both html and pdf.  I have a few comments about the content:\n\n- in faq-general.rst, at the end: do we need to include instructions for building the documentation, since it is downloadable, included in any binary distribution, and automatically built when building any source distribution?  Note that you can also build the docs using\n\n```\nmake doc   or    make doc-html \nmake doc-pdf\n```\n\n I don't know if it's worth mentioning these alternatives.  In the same part, I would suggest changing the path to the documentation: replace \"sage-main\" by \"sage\".   Also in the same part, in the spirit of #21 and standard GNU-style command line options, how about changing `sage -docbuild ...` to `sage --docbuild ...`, and similarly for `sage -help` and `sage -advanced`?  (Same issue with \"you need to invoke Sage with the option ``-python``\" in faq-usage.rst, and perhaps elsewhere -- I haven't done a careful search.)\n\n- for faq-usage.rst, the prerequisites: should we mention LaTeX as a suggested package?",
    "created_at": "2010-04-06T21:16:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76192",
    "user": "jhpalmieri"
}
```

The documents build without error and they look good, in both html and pdf.  I have a few comments about the content:

- in faq-general.rst, at the end: do we need to include instructions for building the documentation, since it is downloadable, included in any binary distribution, and automatically built when building any source distribution?  Note that you can also build the docs using

```
make doc   or    make doc-html 
make doc-pdf
```

 I don't know if it's worth mentioning these alternatives.  In the same part, I would suggest changing the path to the documentation: replace "sage-main" by "sage".   Also in the same part, in the spirit of #21 and standard GNU-style command line options, how about changing `sage -docbuild ...` to `sage --docbuild ...`, and similarly for `sage -help` and `sage -advanced`?  (Same issue with "you need to invoke Sage with the option ``-python``" in faq-usage.rst, and perhaps elsewhere -- I haven't done a careful search.)

- for faq-usage.rst, the prerequisites: should we mention LaTeX as a suggested package?



---

archive/issue_comments_076193.json:
```json
{
    "body": "The following institutions are using Sage:\n\n* Clemson https://clemix.clemson.edu:34567/\n \n* Chang Gung http://diffusion.cgu.edu.tw:8000/",
    "created_at": "2010-04-08T14:09:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76193",
    "user": "mvngu"
}
```

The following institutions are using Sage:

* Clemson https://clemix.clemson.edu:34567/
 
* Chang Gung http://diffusion.cgu.edu.tw:8000/



---

archive/issue_comments_076194.json:
```json
{
    "body": "I tested all 5 patches including the general2 patch and everything builds fine. On the documentation homepage there is a big white space in between constructions and reference manual. It would be nice to bring reference manual up in line with the new FAQ section.\nOther than that and John's comments I would say its ready.\n~Mark",
    "created_at": "2010-05-04T05:40:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76194",
    "user": "mjordan7"
}
```

I tested all 5 patches including the general2 patch and everything builds fine. On the documentation homepage there is a big white space in between constructions and reference manual. It would be nice to bring reference manual up in line with the new FAQ section.
Other than that and John's comments I would say its ready.
~Mark



---

archive/issue_comments_076195.json:
```json
{
    "body": "Just letting people know that when you patch with 8465 it adds a new section to where the white space was, so don't worry about that. I think we're good now.\n~Mark",
    "created_at": "2010-05-04T06:14:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76195",
    "user": "mjordan7"
}
```

Just letting people know that when you patch with 8465 it adds a new section to where the white space was, so don't worry about that. I think we're good now.
~Mark



---

archive/issue_comments_076196.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-05T12:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76196",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076197.json:
```json
{
    "body": "Attachment\n\nNeeds a final review before we can merge the new FAQ into the standard documentation of Sage.",
    "created_at": "2010-05-05T12:58:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76197",
    "user": "mvngu"
}
```

Attachment

Needs a final review before we can merge the new FAQ into the standard documentation of Sage.



---

archive/issue_comments_076198.json:
```json
{
    "body": "For a list of FAQs, they are very difficult to find. Maybe I'm missing an obvious FAQ link but, how is a first time user supposed to find them?",
    "created_at": "2010-05-12T11:10:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76198",
    "user": "pang"
}
```

For a list of FAQs, they are very difficult to find. Maybe I'm missing an obvious FAQ link but, how is a first time user supposed to find them?



---

archive/issue_comments_076199.json:
```json
{
    "body": "If I hit the \"index\" button on the top right, a page appears with a link to \"Full index on one page  (can be huge)\", which then yields a blank page. It also happens in the thematic tutorials, as they don't add words from the faq to the index.\n\nThat's perfectly normal, so I give a positive review.",
    "created_at": "2010-05-12T16:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76199",
    "user": "pang"
}
```

If I hit the "index" button on the top right, a page appears with a link to "Full index on one page  (can be huge)", which then yields a blank page. It also happens in the thematic tutorials, as they don't add words from the faq to the index.

That's perfectly normal, so I give a positive review.



---

archive/issue_comments_076200.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-12T16:02:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76200",
    "user": "pang"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076201.json:
```json
{
    "body": "Attachment\n\nAfter applying all three patches to Sage 4.4.2.rc0, running doctests resulted in the following failure:\n\n\n```\n[mvngu@sage sage-4.4.2.rc0]$ ./sage -t -long devel/sage-main/doc/en/faq/faq-usage.rstsage -t -long \"devel/sage-main/doc/en/faq/faq-usage.rst\"    \n**********************************************************************\nFile \"/dev/shm/mvngu/release/sage-4.4.2.rc0/devel/sage-main/doc/en/faq/faq-usage.rst\", line 134:\n    sage: load(\"simple.py\")\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[2]>\", line 1, in <module>\n        load(\"simple.py\")###line 134:\n    sage: load(\"simple.py\")\n      File \"sage_object.pyx\", line 698, in sage.structure.sage_object.load (sage/structure/sage_object.c:7304)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/lib/python/site-packages/sage/misc/preparser.py\", line 1501, in load\n        execfile(filename, globals)\n    IOError: [Errno 2] No such file or directory: 'simple.py'\n**********************************************************************\nFile \"/dev/shm/mvngu/release/sage-4.4.2.rc0/devel/sage-main/doc/en/faq/faq-usage.rst\", line 138:\n    sage: attach(\"simple.py\")\nException raised:\n    Traceback (most recent call last):\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        attach(\"simple.py\")###line 138:\n    sage: attach(\"simple.py\")\n      File \"session.pyx\", line 425, in sage.misc.session.attach (sage/misc/session.c:2017)\n      File \"/dev/shm/mvngu/release/sage-4.4.2.rc0/local/lib/python/site-packages/sage/misc/preparser.py\", line 1501, in load\n        execfile(filename, globals)\n    IOError: [Errno 2] No such file or directory: 'simple.py'\n```\n\n\nI have attached a patch to resolve this. Anyone care for another trivial review?",
    "created_at": "2010-05-17T05:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76201",
    "user": "mvngu"
}
```

Attachment

After applying all three patches to Sage 4.4.2.rc0, running doctests resulted in the following failure:


```
[mvngu@sage sage-4.4.2.rc0]$ ./sage -t -long devel/sage-main/doc/en/faq/faq-usage.rstsage -t -long "devel/sage-main/doc/en/faq/faq-usage.rst"    
**********************************************************************
File "/dev/shm/mvngu/release/sage-4.4.2.rc0/devel/sage-main/doc/en/faq/faq-usage.rst", line 134:
    sage: load("simple.py")
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[2]>", line 1, in <module>
        load("simple.py")###line 134:
    sage: load("simple.py")
      File "sage_object.pyx", line 698, in sage.structure.sage_object.load (sage/structure/sage_object.c:7304)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/lib/python/site-packages/sage/misc/preparser.py", line 1501, in load
        execfile(filename, globals)
    IOError: [Errno 2] No such file or directory: 'simple.py'
**********************************************************************
File "/dev/shm/mvngu/release/sage-4.4.2.rc0/devel/sage-main/doc/en/faq/faq-usage.rst", line 138:
    sage: attach("simple.py")
Exception raised:
    Traceback (most recent call last):
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        attach("simple.py")###line 138:
    sage: attach("simple.py")
      File "session.pyx", line 425, in sage.misc.session.attach (sage/misc/session.c:2017)
      File "/dev/shm/mvngu/release/sage-4.4.2.rc0/local/lib/python/site-packages/sage/misc/preparser.py", line 1501, in load
        execfile(filename, globals)
    IOError: [Errno 2] No such file or directory: 'simple.py'
```


I have attached a patch to resolve this. Anyone care for another trivial review?



---

archive/issue_comments_076202.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-05-17T05:31:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76202",
    "user": "mvngu"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_076203.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2010-05-17T05:31:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76203",
    "user": "mvngu"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_076204.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-05-20T10:57:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76204",
    "user": "pang"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_076205.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-06-09T03:38:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8464",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8464#issuecomment-76205",
    "user": "mhansen"
}
```

Resolution: fixed
