# Issue 8156: [with code] new function readdata

Issue created by migration from https://trac.sagemath.org/ticket/8156

Original creator: zimmerma

Original creation time: 2010-02-02 20:57:48

Assignee: was

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


---

Comment by zimmerma created at 2010-02-02 20:58:07

Changing status from new to needs_review.


---

Comment by mpatel created at 2010-02-22 09:32:11

Changing status from needs_review to needs_work.


---

Comment by zimmerma created at 2010-02-22 21:48:09

I'd like to propose a patch, but since I never created a new function in Sage I don't know in
which file I should add this function (and how to do so that it is available to the user).
Should I add it in a specialized package (like io)? Any advice would be welcome.
Should I add it in misc/misc.py??


---

Comment by wdj created at 2010-02-22 21:52:36

Replying to [comment:2 mpatel]:

Sounds like a useful addition to me. Are you saying this will only read in files for which data entries are separated by newline characters? It seems to me that this could be made more general rather easily, though without more details it is hard to say how exactly.

In any case, I would like to suggest adding it to the interfaces subdirectory.


---

Comment by zimmerma created at 2010-02-23 07:55:11

> In any case, I would like to suggest adding it to the interfaces subdirectory. 

ok, I have prepared a patch with a new file interfaces/readdata.py. However hg_sage.diff()
does not show this new file. How to tell Mercurial to consider it?


---

Comment by AlexGhitza created at 2010-02-23 08:33:19

Just do `hg add name_of_the_file`.  Before doing this you can try `hg status`, which should show this file with a question mark in front.  After doing `hg add`, it should show the file with a capital A in front.


---

Attachment


---

Comment by zimmerma created at 2010-02-23 09:49:25

thanks Alex. I have attached my patch, which is ready for review.


---

Comment by zimmerma created at 2010-02-23 09:49:25

Changing status from needs_work to needs_review.


---

Comment by timdumol created at 2010-04-18 10:19:13

LGTM.


---

Comment by timdumol created at 2010-04-18 10:19:13

Changing status from needs_review to positive_review.


---

Comment by jhpalmieri created at 2010-04-18 15:59:41

Changing status from positive_review to needs_work.


---

Comment by jhpalmieri created at 2010-04-18 15:59:41

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

Comment by jhpalmieri created at 2010-04-18 16:01:25

Oh, also please include an "INPUT" block in the docstring.  For instance, what exactly do you mean by a "type" for the argument "t"?


---

Comment by jhpalmieri created at 2010-04-18 16:33:00

One more thing: if you're going to create a file in a doctest, then create it in a temporary directory.  See the second point here: [http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples](http://www.sagemath.org/doc/developer/conventions.html#further-conventions-for-automated-testing-of-examples).


---

Comment by timdumol created at 2010-04-18 16:42:50

My bad on the false positive. Sorry.


---

Comment by jhpalmieri created at 2010-04-18 18:04:53

No problem.


---

Attachment


---

Comment by zimmerma created at 2010-04-19 16:37:10

Changing status from needs_work to needs_review.


---

Comment by zimmerma created at 2010-04-19 16:37:10

thank you Tim and John for your review. I've attached a new patch (to be applied alone). I've
tested it on 4.3.5. A minor issue is that in the documentation f.write("17\n42") is split
along two lines... Should I put \\ in the docstring?

Paul


---

Comment by jhpalmieri created at 2010-04-19 17:11:18

Replying to [comment:14 zimmerma]:
> Should I put \\ in the docstring?

First try changing """ to r""" at the beginning of the docstring.  That might fix it.


---

Attachment


---

Comment by zimmerma created at 2010-04-20 09:43:59

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

Comment by timdumol created at 2010-06-23 08:49:42

Doctests pass. Positive review.

Manager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.


---

Comment by timdumol created at 2010-06-23 08:49:42

Changing status from needs_review to positive_review.


---

Comment by mpatel created at 2010-07-21 03:07:27

Changing status from positive_review to needs_info.


---

Comment by mpatel created at 2010-07-21 03:07:27

Replying to [comment:17 timdumol]:
> Doctests pass. Positive review.
> 
> Manager note: Does the tempfile in $SAGE_TMP need to be explicitly deleted? I don't think so, but if that's the case, please mark as needs work.
I think it's OK if we don't delete the file explicitly.  But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?

Minh, what do you think?


---

Comment by mvngu created at 2010-07-21 06:36:13

Replying to [comment:18 mpatel]:
> I think it's OK if we don't delete the file explicitly. 

It saves a lot of headache for a program to clean up after itself. This happens when you exit a Sage session; temporary files/directories created under `SAGE_TMP` would automatically be deleted when Sage exits. So there's no need to explicitly delete stuff under `SAGE_TMP`.




> But maybe it's better to use `tmp_filename`, which increments an internal counter and checks whether the file already exists?

That's a very neat idea, especially considering that a lot of doctests do create temporary files. It's very easy to have name clashes when you doctest in parallel. Another useful command is `tmp_dir()` for creating a temporary directory. Both `tmp_filename()` and `tmp_dir()` are highly recommended for use in doctests.


---

Comment by mpatel created at 2010-07-21 10:39:57

Use `tmp_filename`.  Apply only this patch.


---

Attachment

I've attached a patch that uses `tmp_filename`.


---

Comment by mpatel created at 2010-07-21 10:41:22

Changing status from needs_info to needs_review.


---

Comment by zimmerma created at 2010-07-21 19:29:26

Replying to [comment:20 mpatel]:
> I've attached a patch that uses `tmp_filename`.

am I allowed to review that patch, being the author of the original patch?

Paul


---

Comment by mpatel created at 2010-07-21 19:39:44

Replying to [comment:21 zimmerma]:
> Replying to [comment:20 mpatel]:
> > I've attached a patch that uses `tmp_filename`.
> 
> am I allowed to review that patch, being the author of the original patch?

Sure!


---

Comment by zimmerma created at 2010-07-22 08:00:25

Changing status from needs_review to positive_review.


---

Comment by zimmerma created at 2010-07-22 08:00:25

all doctests still pass, and using tmp_filename is indeed better. Positive review.

Paul


---

Comment by ddrake created at 2010-07-22 23:37:01

Resolution: fixed


---

Comment by ddrake created at 2010-07-22 23:37:01

Merged trac_8156c.patch in 4.5.2.alpha1.
