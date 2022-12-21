# Issue 5141: tinymce should be disabled on published worksheets

Issue created by migration from Trac.

Original creator: jason

Original creation time: 2009-01-30 21:51:19

Assignee: boothby

Otherwise bad things happen.


---

Comment by mabshoff created at 2009-02-02 04:59:55

Positive review.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 05:01:15

Resolution: fixed


---

Comment by mabshoff created at 2009-02-02 05:01:15

Merged in Sage 3.3.alpha4.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-02 05:25:12

Resolution changed from fixed to 


---

Comment by mabshoff created at 2009-02-02 05:25:12

Changing status from closed to reopened.


---

Comment by mabshoff created at 2009-02-02 05:25:12

Ooops, this did break some doctests in cell.py:

```
sage -t -long "devel/sage/sage/server/notebook/cell.py"     
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py", line 175:
    sage: C.html()
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[3]>", line 1, in <module>
        C.html()###line 175:
    sage: C.html()
      File "/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 184, in html
        if JEDITABLE_TINYMCE and not self.worksheet().is_published():
    AttributeError: 'NoneType' object has no attribute 'is_published'
**********************************************************************
File "/scratch/mabshoff/sage-3.3.alpha4/devel/sage/sage/server/notebook/cell.py", line 178:
    sage: C.html(do_math_parse=True)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_9[5]>", line 1, in <module>
        C.html(do_math_parse=True)###line 178:
    sage: C.html(do_math_parse=True)
      File "/scratch/mabshoff/sage-3.3.alpha4/local/lib/python2.5/site-packages/sage/server/notebook/cell.py", line 184, in html
        if JEDITABLE_TINYMCE and not self.worksheet().is_published():
    AttributeError: 'NoneType' object has no attribute 'is_published'
**********************************************************************
```


Shame on me for giving this a positive review :p

Reopened. 

Cheers,

Michel


---

Attachment


---

Comment by jason created at 2009-02-02 20:20:21

patch updated to check for the existence of the .is_published() method.  It should work now.


---

Comment by jason created at 2009-02-03 08:19:34

Changing priority from major to critical.


---

Comment by jason created at 2009-02-03 09:25:24

Changing status from reopened to new.


---

Comment by jason created at 2009-02-03 09:25:24

Changing assignee from boothby to jason.


---

Comment by mabshoff created at 2009-02-04 01:16:59

Merged in Sage 3.3.alpha5.

Cheers,

Michael


---

Comment by mabshoff created at 2009-02-04 01:16:59

Resolution: fixed
