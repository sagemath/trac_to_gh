# Issue 6348: gap4.4.10->gap4.4.12 revisited

Issue created by migration from Trac.

Original creator: wdj

Original creation time: 2009-06-17 15:40:44

Assignee: joyner

CC:  awebb

Keywords: gap

From an email:

> I think we can upgrade gap to 4.12 now too, since I worked around 
> the problem we had before with 4.12 on itanium.
> William

Background: Some months ago, we upgraded from gap 4.4.10 to gap 4.4.12 (gap 4.4.11 was skipped due to some technical problems). This
caused some docstrings to break, since some of gap's print methods were changed.

The patch at 
http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.p0.spkg
will also break some docstrings. However, it applies fine (using sage -f) to sage 4.0.2.rc1. 

A patch fixing the breaks will be posted later.



---

Attachment

applies to 4.0.2.rc1


---

Comment by wdj created at 2009-06-17 20:31:54

First do 
sage -f http://sage.math.washington.edu/home/wdj/patches/gap-4.4.12.p0.spkg
This will cause several (minor) docstring test failures. All are fixed in this patch,
which passes sage -testall.


---

Comment by robertwb created at 2009-06-25 10:37:16

I have looked at the patch, and it indeed is just printing/ordering issues. Spkg looks fine, SPKG.txt updated. Tests are still running...


---

Comment by robertwb created at 2009-06-26 03:53:50

Seems to have broken my install... maybe it was something else, but now I've got to fix my Sage :(.


---

Comment by wdj created at 2009-06-27 11:41:13

Just curious what happened. You installed the spkg using sage -f then maybe ran sage -b and then sage -testall? This failed somehow and rendered your Sage unusable?


---

Comment by robertwb created at 2009-06-27 17:09:25

Yep--segfaulted on startup (so you can imagine how many tests failed...). It was acting a bit weird beforehand, so I'm not blaming this spkg for sure.


---

Comment by rlm created at 2009-07-04 02:08:49

This seems to be not quite a positive review. I'm changing this back to "needs work," at least for now.


---

Comment by robertwb created at 2009-07-04 05:06:54

I think my sage was messed up from elsewhere, so the spkg probably doesn't need work, but it still needs to be reviewed.


---

Comment by awebb created at 2009-07-16 07:19:35

The file sage/graphs/graph_isom.pyx was removed in ticket #6112. That breaks this patch so I guess I will switch it back to needs work.


---

Comment by wdj created at 2009-07-16 14:15:16

I'm not sure how to fix the patch. Can I take the patch, open it in an editor, and delete the section containing the fixes for graph_isom.pyx, save it and rename the patch?


---

Comment by awebb created at 2009-07-16 15:40:27

I believe that you can. I tried cutting out that part and I was able to apply the patch but I don't know anything about Mercurial or if this is the "proper" way to do it. My first thought is to apply the "cut" patch and then export a new one to replace the one here. 

I see that graph_isom.pxd is still there although it is not needed. Should it be deleted? On this or a new ticket?


---

Comment by rlm created at 2009-07-16 18:54:33

Replying to [comment:10 awebb]:
> I see that graph_isom.pxd is still there although it is not needed. Should it be deleted? On this or a new ticket?

`graph_isom.pxd` should also be deleted. This is a new ticket: #6544


---

Comment by awebb created at 2009-07-16 19:04:49

I installed the spkg and applied a modified patch (removed the graph_isom.pyx part). I ran 'sage -ptest and everything passed. I could not change the patch but otherwise it looks positive.


---

Comment by wdj created at 2009-07-16 19:22:54

apply only this patch


---

Attachment

Replying to [comment:12 awebb]:
> I installed the spkg and applied a modified patch (removed the graph_isom.pyx part). 
> I ran 'sage -ptest and everything passed. I could not change the patch but otherwise it looks positive.

New patch (removed the graph_isom.pyx part) seems to solve the problem, passes sage -testall.


---

Comment by rlm created at 2009-07-16 21:07:07

By the way, the best way to fix a patch is to use Mercurial queues. First, you use `hg qimport` to import the patch, then `hg qpush` to get it in the queue. Rebuild, edit, do whatever you like, and then you can use `hg qrefresh` to incorporate the changes into the patch, and `hg export tip > filename.patch` to get the new patch, and finally `hg qpop` if you want the patch back off the queue again.


---

Comment by rlm created at 2009-07-16 21:20:11

After installing this spkg and applying the patch, I get the following:

```
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: gap('2+2')
A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
| Sage Version 4.1, Release Date: 2009-07-09                         |
| Type notebook() for the GUI, and license() for information.        |
/home/rlmill/.sage/temp/geom/22741/_home_rlmill__sage_init_sage_0.py in <module>()

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
   1019
   1020         if isinstance(x, basestring):
-> 1021             return cls(self, x, name=name)
   1022         try:
   1023             return self._coerce_from_special_method(x)

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
   1420         else:
   1421             try:
-> 1422                 self._name = parent._create(value, name=name)
   1423             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
   1424                 self._session_number = -1

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _create(self, value, name)
   1188     def _create(self, value, name=None):
   1189         name = self._next_var_name() if name is None else name
-> 1190         self.set(name, value)
   1191         return name
   1192

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in set(self, var, value)
    529         """
    530         cmd = ('%s:=%s;;'%(var,value)).replace('\n','')
--> 531         out = self._eval_line(cmd, allow_use_file=True)
    532
    533     def get(self, var, use_file=False):

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
    690             try:
    691                 (normal, error) = self._execute_line(line, wait_for_prompt=wait_for_prompt,
--> 692                                                  expect_eof= (self._quit_string() in line))
    693
    694                 if len(error)> 0:

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _execute_line(self, line, wait_for_prompt, expect_eof)
    590             current_outputs = normal_outputs
    591             while True:
--> 592                 x = E.expect_list(self._compiled_full_pattern)
    593                 current_outputs.append(E.before)
    594                 if x == 0:   # `@`p

/space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __getattr__(self, attrname)
   1309     def __getattr__(self, attrname):
   1310         if attrname[:1] == "_":
-> 1311             raise AttributeError
   1312         return self._function_class()(self, attrname)
   1313

AttributeError:
```



---

Comment by rlm created at 2009-07-16 21:21:27

Also, after quitting the session above, I get a seemingly infinite cascade of the following:

```
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
<bound method GapElement.__del__ of (invalid object -- defined in terms of closed session)> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.AttributeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.RuntimeError'> ignored
Exception RuntimeError: RuntimeError('maximum recursion depth exceeded',) in Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
<bound method GapElement.__del__ of (invalid object -- defined in terms of closed session)> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.AttributeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded in __subclasscheck__' in <type 'exceptions.RuntimeError'> ignored
Exception RuntimeError: RuntimeError('maximum recursion depth exceeded',) in Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
```



---

Comment by wdj created at 2009-07-16 21:25:35

Replying to [comment:15 rlm]:
> After installing this spkg and applying the patch, I get the following:
> {{{
> ----------------------------------------------------------------------
> | Sage Version 4.1, Release Date: 2009-07-09                         |
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
> sage: gap('2+2')
> A workspace appears to have been corrupted... automatically rebuilding (this is harmless).
> ---------------------------------------------------------------------------
> AttributeError                            Traceback (most recent call last)
> 
> /home/rlmill/.sage/temp/geom/22741/_home_rlmill__sage_init_sage_0.py in <module>()
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __call__(self, x, name)
>    1019
>    1020         if isinstance(x, basestring):
> -> 1021             return cls(self, x, name=name)
>    1022         try:
>    1023             return self._coerce_from_special_method(x)
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __init__(self, parent, value, is_name, name)
>    1420         else:
>    1421             try:
> -> 1422                 self._name = parent._create(value, name=name)
>    1423             except (TypeError, KeyboardInterrupt, RuntimeError, ValueError), x:
>    1424                 self._session_number = -1
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in _create(self, value, name)
>    1188     def _create(self, value, name=None):
>    1189         name = self._next_var_name() if name is None else name
> -> 1190         self.set(name, value)
>    1191         return name
>    1192
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in set(self, var, value)
>     529         """
>     530         cmd = ('%s:=%s;;'%(var,value)).replace('\n','')
> --> 531         out = self._eval_line(cmd, allow_use_file=True)
>     532
>     533     def get(self, var, use_file=False):
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _eval_line(self, line, allow_use_file, wait_for_prompt)
>     690             try:
>     691                 (normal, error) = self._execute_line(line, wait_for_prompt=wait_for_prompt,
> --> 692                                                  expect_eof= (self._quit_string() in line))
>     693
>     694                 if len(error)> 0:
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/gap.pyc in _execute_line(self, line, wait_for_prompt, expect_eof)
>     590             current_outputs = normal_outputs
>     591             while True:
> --> 592                 x = E.expect_list(self._compiled_full_pattern)
>     593                 current_outputs.append(E.before)
>     594                 if x == 0:   # `@`p
> 
> /space/rlm/sage-4.1/local/lib/python2.6/site-packages/sage/interfaces/expect.pyc in __getattr__(self, attrname)
>    1309     def __getattr__(self, attrname):
>    1310         if attrname[:1] == "_":
> -> 1311             raise AttributeError
>    1312         return self._function_class()(self, attrname)
>    1313
> 
> AttributeError:
> }}}


Details???

I get:


```
wdj`@`hera:~/sagefiles/sage-4.1.rc0$ ./sage
----------------------------------------------------------------------
----------------------------------------------------------------------
Loading Sage library. Current Mercurial branch is: gap
sage: gap("2+2")
4
```

This is in amd64 ubuntu 9.04, phemon chip.


---

Comment by rlm created at 2009-07-16 21:48:17

On sage.math.


---

Comment by wdj created at 2009-07-17 01:12:42

Replying to [comment:18 rlm]:
> On sage.math.

I had no problem on an amd64 ubuntu 9.04 machine and likewise for an intel macbook running 10.4.11.

I tried to build sage 4.1 from source on sage.math and ran into some compiling errors. Can you tell me what version of sage you used on sage.math?


---

Comment by rlm created at 2009-07-17 01:45:33

This was a fresh build of Sage-4.1. What errors did you run into when building sage-4.1?


---

Comment by wdj created at 2009-07-17 01:54:28

I ran into an error building atlas. I don't know how to replicate your error so don't know how to try to fix this ticket. As I said, it works on my 2 machines. Do you have any suggestions?


---

Comment by rlm created at 2009-07-17 01:59:47

Strangely, doing the exact same thing again gave different results.

I was able to install `gap-4.4.12.p0` on top of `sage-4.1` on sage.math, and after applying the patch, I'm running long doctests everywhere. Will post the results shortly.


---

Comment by rlm created at 2009-07-17 02:01:37

All tests pass!


---

Comment by wdj created at 2009-07-17 02:03:45

Replying to [comment:23 rlm]:
> All tests pass!

Whew (with hand wiping sweating brow:-)!

Does this mean it gets a positive review?


---

Comment by rlm created at 2009-07-17 02:16:29

The Mercurial repo is corrupted, but I am posting an spkg that will fix this. Tell me, what is the purpose of the `patch` file that was added? I can't read it in plain text, and I don't know what format it is...


---

Comment by rlm created at 2009-07-17 02:26:00

Hmm, I've deleted that `patch` file, reinstalled (this time on 32-bit OS X), and I'm running long doctests on this. Next I'll test 64-bit OS X. I don't know what `patch` was, but it doesn't seem necessary.


---

Comment by rlm created at 2009-07-17 03:02:58

Oops, the `AttributeError` rears its ugly head again: this time on OS X.

My modified spkg can be found here: http://sage.math.washington.edu/home/rlmill/gap-4.4.12.p1.spkg

Here is one example of what is happening:


```
sage -t -long sage/combinat/partition.py
*** *** Error: TIMED OUT! PROCESS KILLED! *** ***
*** *** Error: TIMED OUT! *** ***
**********************************************************************
File "/Users/rlmill/sage-4.1.32bit/devel/sage-main/sage/combinat/partition.py", line 523:
    sage: Partition([5,3]).sign()
Exception raised:
    Traceback (most recent call last):
      File "/Users/rlmill/sage-4.1.32bit/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.1.32bit/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/Users/rlmill/sage-4.1.32bit/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_10[2]>", line 1, in <module>
        Partition([Integer(5),Integer(3)]).sign()###line 523:
    sage: Partition([5,3]).sign()
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/combinat/partition.py", line 580, in sign
        ans=gap.eval("SignPartition(%s)"%(self))
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/interfaces/gap.py", line 480, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/interfaces/expect.py", line 972, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/interfaces/gap.py", line 692, in _eval_line
        expect_eof= (self._quit_string() in line))
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/interfaces/gap.py", line 592, in _execute_line
        x = E.expect_list(self._compiled_full_pattern)
      File "/Users/rlmill/sage-4.1.32bit/local/lib/python/site-packages/sage/interfaces/expect.py", line 1311, in __getattr__
        raise AttributeError
    AttributeError
**********************************************************************
```



---

Comment by rlm created at 2009-07-17 03:07:52

These tests also ended with the seemingly infinite barrage of


```
Exception RuntimeError: 'maximum recursion depth exceeded while calling a Python object' in <type 'exceptions.AttributeError'> ignored
```



---

Comment by rlm created at 2009-07-17 04:58:43

These tests also pass the second time around. Could this have something to do with temp files or workspaces or something?


---

Comment by wdj created at 2009-07-17 09:51:43

I don't see how that problem can arise. There were reasons why 4.4.12 was downgraded to 4.4.10. Maybe these problems persist?

The "patch" was (as described in one of the comments above) simply the original patch but with the section on graph_isom.pyx removed (I opened up the old patch, deleted the lines in the graph_isom.pyx section in emacs, and saved that as a new file). The problem was that the original patch would not apply since graph_isom.pyx has since been removed. Fortunately the edited patch worked (at least for me).


---

Comment by rlm created at 2009-07-17 16:25:44

Patches to the Sage library don't belong in spkgs-- but this is gone in `gap-4.4.12.p1`.

My guess is that you can reproduce this behavior on sage.math as follows:

Install a fresh `sage-4.1`, and when it is finished, run the full doctest suite on long. This will guarantee that `gap-4.4.10` gets used nontrivially. Then upgrade to `gap-4.4.12.p1`. Run the doctests again.

If I copy over a sage-4.1 install and run long doctests, after having successfully used gap-4.4.12, the gap-4.4.10 in there has problems which look just like the problems I had going the other way:


```
Traceback (most recent call last):
  File "/space/rlm/sage-4.1.gap/tmp/all.py", line 2, in <module>
    from sage.all_cmdline import *;
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/all_cmdline.py", line 14, in <module>
    from sage.all import *
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/misc/all.py", line 70, in <module>
    from sage_input import sage_input
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/misc/sage_input.py", line 163, in <module>
    from sage.misc.functional import parent
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/misc/functional.py", line 37, in <module>
    from sage.rings.complex_double import CDF
  File "complex_double.pyx", line 88, in sage.rings.complex_double (sage/rings/complex_double.c:13486)
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/rings/complex_field.py", line 86, in ComplexField
    C = ComplexField_class(prec)
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/rings/complex_field.py", line 177, in __init__
    self._populate_coercion_lists_(coerce_list=[complex_number.RRtoCC(self._real_field(), self)])
  File "complex_number.pyx", line 1937, in sage.rings.complex_number.RRtoCC.__init__ (sage/rings/complex_number.c:12660)
  File "map.pyx", line 41, in sage.categories.map.Map.__init__ (sage/categories/map.c:1909)
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/categories/homset.py", line 149, in Hom
    from sage.rings.homset import RingHomset
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/rings/homset.py", line 17, in <module>
    import quotient_ring
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/rings/quotient_ring.py", line 32, in <module>
    import sage.rings.polynomial.multi_polynomial_ideal
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 229, in <module>
    from sage.interfaces.all import (singular as singular_default,
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/interfaces/all.py", line 8, in <module>
    from gap import gap, gap_reset_workspace, gap_console, gap_version, is_GapElement, Gap
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/interfaces/gap.py", line 960, in <module>
    gap_reset_workspace(verbose=False)
  File "/space/rlm/sage-4.1.gap/local/lib/python/site-packages/sage/interfaces/gap.py", line 938, in gap_reset_workspace
    os.unlink(WORKSPACE)
OSError: [Errno 2] No such file or directory: '/home/rlmill/.sage//gap/workspace-3758812723191186113'
```


It looks like this happens whenever the version of GAP used is changed. This is why I was hinting at temp files and workspaces before. Something is ringing a bell, about GAP failing to reset its own workspace on upgrade.


---

Comment by rlm created at 2009-07-17 16:56:31

Hmm, after doing the above, upgrading went just fine. I just can't reproduce the `AssertionError`, even though I've seen it on Linux and OS X. Maybe it's because of the state of my `DOT_SAGE` directories.

I'm almost ready to give this a positive review, but it makes me uneasy, since it seems each user will experience this once on upgrade, possibly even if they've just installed a new version from scratch...


---

Comment by mvngu created at 2010-02-02 07:37:02

Resolution: duplicate


---

Comment by mvngu created at 2010-02-02 07:37:02

Closing this as a duplicate of #8076.
