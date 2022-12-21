# Issue 8464: add FAQ to standard documentation

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-03-07 01:52:58

Assignee: mvngu

CC:  jhpalmieri

Add the [FAQ](http://wiki.sagemath.org/faq) on the Sage wiki to the Sage [standard documentation](http://www.sagemath.org/doc/). The original proposal can be found on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/95afb345e872f9af) and [sage-combinat-devel](http://groups.google.com/group/sage-combinat-devel/msg/662eb0246c7bf9fc).


---

Comment by mvngu created at 2010-03-07 02:03:34

Changing keywords from "" to "FAQ".


---

Comment by jhpalmieri created at 2010-03-10 23:50:25

I don't know if this is ready for review yet, but here are a few comments:

 - there is a typo in one of the links (found by using "sage -docbuild faq linkcheck", which I just discovered!).  This is fixed in my small patch.  

 - should this be added to the "website" docbuild target?  (I'm not sure; arguments could be made either way, I think.)

 - this document doesn't match up very well with the FAQ on the wiki.  Why?


---

Comment by mvngu created at 2010-03-11 01:10:51

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

Comment by mvngu created at 2010-03-11 04:29:34

reviewer patch


---

Attachment


---

Comment by mvngu created at 2010-03-11 04:32:45

Changing status from new to needs_review.


---

Comment by JGuzman created at 2010-04-04 15:13:39

Sage 4.3.5, One more question added to the FAQ


---

Comment by mvngu created at 2010-04-04 15:29:42

Changing status from needs_review to needs_work.


---

Attachment

CalTech is using Sage. See http://www.its.caltech.edu/~awalker/sage.html. Update the FAQ with that institutional user.


---

Comment by jhpalmieri created at 2010-04-06 21:16:36

The documents build without error and they look good, in both html and pdf.  I have a few comments about the content:

 - in faq-general.rst, at the end: do we need to include instructions for building the documentation, since it is downloadable, included in any binary distribution, and automatically built when building any source distribution?  Note that you can also build the docs using

```
make doc   or    make doc-html 
make doc-pdf
```

 I don't know if it's worth mentioning these alternatives.  In the same part, I would suggest changing the path to the documentation: replace "sage-main" by "sage".   Also in the same part, in the spirit of #21 and standard GNU-style command line options, how about changing `sage -docbuild ...` to `sage --docbuild ...`, and similarly for `sage -help` and `sage -advanced`?  (Same issue with "you need to invoke Sage with the option ``-python``" in faq-usage.rst, and perhaps elsewhere -- I haven't done a careful search.)

 - for faq-usage.rst, the prerequisites: should we mention LaTeX as a suggested package?


---

Comment by mvngu created at 2010-04-08 14:09:07

The following institutions are using Sage:

 * Clemson https://clemix.clemson.edu:34567/
 
 * Chang Gung http://diffusion.cgu.edu.tw:8000/


---

Comment by mjordan7 created at 2010-05-04 05:40:16

I tested all 5 patches including the general2 patch and everything builds fine. On the documentation homepage there is a big white space in between constructions and reference manual. It would be nice to bring reference manual up in line with the new FAQ section.
Other than that and John's comments I would say its ready.
~Mark


---

Comment by mjordan7 created at 2010-05-04 06:14:28

Just letting people know that when you patch with 8465 it adds a new section to where the white space was, so don't worry about that. I think we're good now.
~Mark


---

Comment by mvngu created at 2010-05-05 12:58:42

Changing status from needs_work to needs_review.


---

Attachment

Needs a final review before we can merge the new FAQ into the standard documentation of Sage.


---

Comment by pang created at 2010-05-12 11:10:40

For a list of FAQs, they are very difficult to find. Maybe I'm missing an obvious FAQ link but, how is a first time user supposed to find them?


---

Comment by pang created at 2010-05-12 16:02:48

If I hit the "index" button on the top right, a page appears with a link to "Full index on one page  (can be huge)", which then yields a blank page. It also happens in the thematic tutorials, as they don't add words from the faq to the index.

That's perfectly normal, so I give a positive review.


---

Comment by pang created at 2010-05-12 16:02:48

Changing status from needs_review to positive_review.


---

Attachment

After applying all three patches to Sage 4.4.2.rc0, running doctests resulted in the following failure:


```
[mvngu`@`sage sage-4.4.2.rc0]$ ./sage -t -long devel/sage-main/doc/en/faq/faq-usage.rstsage -t -long "devel/sage-main/doc/en/faq/faq-usage.rst"    
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

Comment by mvngu created at 2010-05-17 05:31:22

Changing status from positive_review to needs_work.


---

Comment by mvngu created at 2010-05-17 05:31:38

Changing status from needs_work to needs_review.


---

Comment by pang created at 2010-05-20 10:57:02

Changing status from needs_review to positive_review.


---

Comment by mhansen created at 2010-06-09 03:38:32

Resolution: fixed
