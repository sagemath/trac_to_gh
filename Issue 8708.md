# Issue 8708: allow doctest script to handle docstrings with triple single quotes

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2010-04-18 00:46:47

Assignee: tbd

CC:  ranosch

As the subject says. This is related to #8699. See this [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/54de5b70bc7b18e3) thread for some background information.


---

Comment by burcin created at 2011-08-11 08:41:37

Changing status from new to needs_review.


---

Attachment

attachment:trac_8708-doctest_quotes.patch fixes this problem.


---

Comment by jhpalmieri created at 2011-08-15 22:36:06

This doesn't work for me: it skips all doctests in a typical file.  The issue is the line

```
min_ind = min(dq_ind, sq_ind)
```

which means that if either (not just both) search fails, then `min_ind` is `-1`, so the loop exits.

I also don't think we need to modify `doc_prefix` and `doc_suffix`, since this is part of the string written to the temporary doctesting file.  Do the triple quotes in that file have to match the original ones, or can they all be `"""`?

I'm attaching a new patch which uses regular expressions instead, and which doesn't modify `doc_prefix` and `doc_suffix`.  I'm also attaching a small file for testing purposes; testing on this file should produce three failures, and if you add some print statements to the function `extract_doc`, it should extract the correct string.


---

Comment by burcin created at 2011-08-16 09:16:40

Replying to [comment:2 jhpalmieri]:
> This doesn't work for me: it skips all doctests in a typical file.  The issue is the line
> {{{
> min_ind = min(dq_ind, sq_ind)
> }}}
> which means that if either (not just both) search fails, then `min_ind` is `-1`, so the loop exits.

Good catch! Thanks for looking into this.

> I also don't think we need to modify `doc_prefix` and `doc_suffix`, since this is part of the string written to the temporary doctesting file.  Do the triple quotes in that file have to match the original ones, or can they all be `"""`?

What happens if you have something like:


```
def f(arg):
    '''
    some text
        
    """
    some more text
    """

    '''
```



---

Comment by jhpalmieri created at 2011-08-16 15:16:27

Oh, you're right.  I'm replacing my patch with a new one, the difference being

```diff
diff --git a/sage-doctest b/sage-doctest
--- a/sage-doctest
+++ b/sage-doctest
`@``@` -452,8 +452,10 `@``@` def change_warning_output(file):
             tmpfiles.append(os.path.join(SAGE_TESTDIR, name + '.pyc'))
 
     # Prefix/suffix for all doctests replacing the starting/ending """
-    doc_prefix = 'r""">>> set_random_seed(0L)\n\n>>> change_warning_output(sys.stdout)\n\n'
-    doc_suffix = '\n>>> sig_on_count()\n0\n"""'
+    doc_prefix_dq = 'r""">>> set_random_seed(0L)\n\n>>> change_warning_output(sys.stdout)\n\n'
+    doc_prefix_sq = doc_prefix_dq.replace('"""',"'''")
+    doc_suffix_dq = '\n>>> sig_on_count()\n0\n"""'
+    doc_suffix_sq = doc_suffix_dq.replace('"""',"'''")
 
     n = 0
     # Now extract the docstring by using a regular expression search
`@``@` -499,7 +501,10 `@``@` def change_warning_output(file):
             name = "example"
             s += "def %s_%s():"%(name,n_str)
             n += 1
-            s += "\t"+ doc_prefix + doc + doc_suffix + "\n\n"
+            if m.groups()[0].find("'") > -1: # single quotes
+                s += "\t"+ doc_prefix_sq + doc + doc_suffix_sq + "\n\n"
+            else:
+                s += "\t"+ doc_prefix_dq + doc + doc_suffix_dq + "\n\n"
 
     if n == 0:
         return  ''
```

I'll also add an example like this to the testing file.


---

Attachment

apply to scripts repo


---

Attachment

small Python file for testing purposes


---

Comment by burcin created at 2011-09-22 00:34:20

Changing status from needs_review to positive_review.


---

Comment by burcin created at 2011-09-22 00:34:20

Looks good to me. Thanks for looking into this John.


---

Comment by leif created at 2011-09-27 17:38:37

Changing status from positive_review to needs_work.


---

Comment by leif created at 2011-09-27 17:38:37

This needs to be rebased on #9739, and perhaps also #10952 (both merged into Sage 4.7.2.alpha3).


---

Comment by jhpalmieri created at 2011-09-27 18:52:57

Changing priority from minor to blocker.


---

Comment by jhpalmieri created at 2011-09-27 18:52:57

We missed an or two issue in #9739: with non-library files, first we just had a bug, using "source" instead of "file_name" or "root_name" or something.  Second, in the import statement added to the file,

```
s += "from %s import *\n\n" % target_name
```

we need to replace `target_name` with `os.path.basename(target_name)`.

In the new patch, I've made these two changes and also rebased.  Given that there is actually new content, this needs a new review.  Without the new content, doctesting .py non-library files completely fails, so I'm marking this as a blocker.  Feel free to downgrade if you think it's appropriate.

Oh, I also realized that the attached file for testing purposes has a bad name: replace the hyphen with an underscore.

The part needing review:

```diff
diff --git a/sage-doctest b/sage-doctest
--- a/sage-doctest
+++ b/sage-doctest
`@``@` -510,7 +510,7 `@``@` def check_with_tolerance(expected, actua
 
         elif ext in ['.py', '.sage']:
 
-            target_name = "%s_%d" % (file_name, os.getpid()) # like 'name', but
+            target_name = "%s_%d" % (root_name, os.getpid()) # like 'name', but
             target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'base'
 
             if ext == '.sage':
`@``@` -528,9 +528,9 `@``@` def check_with_tolerance(expected, actua
                 # TODO: instead of copying the file, add its source
                 # directory to PYTHONPATH.  We would also have to
                 # import from 'name' instead of 'target_name'.
-                os.system("cp '%s' %s.py" % (source, target_base))
+                os.system("cp '%s' %s.py" % (file_name, target_base))
 
-            s += "from %s import *\n\n" % target_name
+            s += "from %s import *\n\n" % os.path.basename(target_name)
 
             tmpfiles.append(target_base + ".py") # preparsed or copied original
             tmpfiles.append(target_base + ".pyc") # compiled version of it
```



---

Comment by jhpalmieri created at 2011-09-27 18:52:57

Changing status from needs_work to needs_review.


---

Comment by jhpalmieri created at 2011-09-27 19:03:19

Sorry, here's a new version.  The relevant changes:

```diff
diff --git a/sage-doctest b/sage-doctest
--- a/sage-doctest
+++ b/sage-doctest
`@``@` -510,8 +510,9 `@``@` def check_with_tolerance(expected, actua
 
         elif ext in ['.py', '.sage']:
 
-            target_name = "%s_%d" % (file_name, os.getpid()) # like 'name', but unique
-            target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'base', also unique
+            root_name = os.path.basename(root_name)
+            target_name = "%s_%d" % (root_name, os.getpid()) # like 'root_name', but unique
+            target_base = os.path.join(SAGE_TESTDIR, target_name) # like 'target_name' but with full path
 
             if ext == '.sage':
                 # TODO: preparse "<file>.sage" with a Sage library call
`@``@` -528,7 +529,7 `@``@` def check_with_tolerance(expected, actua
                 # TODO: instead of copying the file, add its source
                 # directory to PYTHONPATH.  We would also have to
                 # import from 'name' instead of 'target_name'.
-                os.system("cp '%s' %s.py" % (source, target_base))
+                os.system("cp '%s' %s.py" % (file_name, target_base))
 
             s += "from %s import *\n\n" % target_name
```

Changing "source" to "file_name" is necessary: doctesting non-library py files fails otherwise.  The other change is to avoid failures if you specify a path name for the file to be tested: `sage -t ./test.py` will fail without this, as compared to `sage -t test.py`.


---

Comment by leif created at 2011-09-27 19:32:50

Well, at _some point_ in the evolution of #9739 it worked (or was correct)... ;-)

Can anybody [else] review this [quickly]?


Sorry, I don't have the time, and I'm actually also not in the mood right now.


---

Comment by jhpalmieri created at 2011-09-27 19:54:17

Some things to test:

 - First apply the patches from #9739 and #10952.
 - Create a file "test.py" (not a Sage library file) and test it with "sage -t test.py", and also with "sage -t /path/to/test.py".  Try before and after applying [attachment:trac_8708-jhp.v2.patch].  You could just use [attachment:trac_8708-testing.py], but rename it so the name doesn't have any hyphens.  This file is supposed to have 3 failures.
 - Do the same with a file "test.sage".  (Just renaming your Python file to "test.sage" should be good enough.)


---

Comment by leif created at 2011-09-28 00:13:40

Changing status from needs_review to needs_work.


---

Comment by leif created at 2011-09-28 00:13:40

I now get the following doctest failures, certainly due to the triple single quote patch / modification:

```
The following tests failed:

	sage -t  -long -force_lib devel/sagenb-main/sagenb/notebook/worksheet.py # Exception from doctest framework
	sage -t  -long -force_lib devel/sage/sage/interacts/library_cython.pyx # 1 doctests failed
	sage -t  -long -force_lib devel/sage/sage/misc/sageinspect.py # Exception from doctest framework
```


With `-verbose`:

```sh
$ ./sage -t -long -verbose devel/sagenb-main/sagenb/notebook/worksheet.py
sage -t -long -verbose "devel/sagenb-main/sagenb/notebook/worksheet.py"
Traceback (most recent call last):
  File "/home/leif/.sage//tmp/worksheet_15100.py", line 3046, in <module>
    runner=runner)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/sagedoctest.py", line 54, in testmod_returning_runner
    runner=runner)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 1819, in testmod_returning_runner
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 893, in _find
    globs, seen)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 965, in _get_test
    filename, lineno)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 640, in _parse_example
    lineno + len(source_lines))
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 726, in _check_prefix
    (lineno+i+1, name, line))
ValueError: line 11 of the docstring for __main__.example_109 has inconsistent leading whitespace: '    "'
Exception raised by doctesting framework. Use -verbose for details.
```



```sh
$ ./sage -t -long -verbose devel/sage/sage/misc/sageinspect.py
sage -t -long -verbose "devel/sage/sage/misc/sageinspect.py"
Traceback (most recent call last):
  File "/home/leif/.sage//tmp/sageinspect_15131.py", line 1327, in <module>
    runner=runner)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/sagedoctest.py", line 54, in testmod_returning_runner
    runner=runner)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 1819, in testmod_returning_runner
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 893, in _find
    globs, seen)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 965, in _get_test
    filename, lineno)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 640, in _parse_example
    lineno + len(source_lines))
  File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/local/bin/ncadoctest.py", line 726, in _check_prefix
    (lineno+i+1, name, line))
ValueError: line 53 of the docstring for __main__.example_28 has inconsistent leading whitespace: '    """'
Exception raised by doctesting framework. Use -verbose for details.
```



```sh
$ ./sage -t -long -verbose devel/sage/sage/interacts/library_cython.pyxsage -t -long -verbose "devel/sage/sage/interacts/library_cython.pyx"

...

Trying:
    from sage.interacts.library_cython import cellular###line 91:_sage_    >>> from sage.interacts.library_cython import cellular
Expecting nothing
ok
Trying:
    rule = [Integer(1), Integer(0), Integer(1), Integer(0), Integer(0), Integer(1), Integer(1), Integer(0)]###line 92:_sage_    >>> rule = [1, 0, 1, 0, 0, 1, 1, 0]
Expecting nothing
ok
Trying:
    N = Integer(3)###line 93:_sage_    >>> N = 3
Expecting nothing
ok
Trying:
    print cellular(rule, Integer(3))###line 94:_sage_    >>> print cellular(rule, 3)
Expecting nothing
**********************************************************************
File "/home/leif/Sage/sage-4.7.2.alpha3-prerelease3/devel/sage/sage/interacts/library_cython.pyx", line ?, in __main__.example_3
Failed example:
    print cellular(rule, Integer(3))###line 94:_sage_    >>> print cellular(rule, 3)
Expected nothing
Got:
    [[0 0 0 1 0 0 0]
     [0 0 0 1 0 0 0]
     [0 1 0 1 0 1 0]]
Trying:
    sig_on_count()
Expecting:
    0
ok
4 items had no tests:
    __main__
    __main__.change_warning_output
    __main__.check_with_tolerance
    __main__.warning_function
3 items passed all tests:
   3 tests in __main__.example_0
   9 tests in __main__.example_1
   8 tests in __main__.example_2
**********************************************************************
1 items had failures:
   1 of   7 in __main__.example_3
27 tests in 8 items.
26 passed and 1 failed.
***Test Failed*** 1 failures.
```



---

Comment by leif created at 2011-09-28 00:18:07

P.S.:

John, could you perhaps separate the fix concerning doctesting non-library files, and attach it to #9739 (not modifying the other patches there, i.e., as a patch to be applied on top of the others)?


---

Comment by jhpalmieri created at 2011-09-28 00:36:39

Okay, I've done that now.  I'm also downgrading the priority of this ticket.  (We could also open a new ticket just for the issue now added on to #9739, if you think that would be cleaner.  #9739 is still marked as closed, by the way.  I didn't reopen it.)


---

Comment by jhpalmieri created at 2011-09-28 00:36:39

Changing priority from blocker to minor.


---

Comment by jhpalmieri created at 2011-09-28 00:39:28

apply to scripts repo


---

Attachment

Replying to [comment:15 jhpalmieri]:
> Okay, I've done that now.

Thanks; just the commit message there refers to this ticket (and its subject), i.e., is unrelated.

> #9739 is still marked as closed, by the way.  I didn't reopen it.

Unless nobody else reopens or closes tickets, or attaches files to / updates files on tickets I've already closed (and I didn't ask him to) I don't really care.

Reopening tickets IMHO only makes sense if I'm going to actually back it out.


---

Comment by leif created at 2011-09-28 01:10:42

s/nobody/somebody/ or s/unless/as long as/

It's getting late...


---

Comment by jhpalmieri created at 2011-09-28 04:13:28

The test failure in interacts/libary_cython.pyx is because of a doctest which would have failed in the past, but it was enclosed in triple single quotes, and so was skipped by the doctesting framework.  (There is a line saying `sage: print cellular(rule, 3)` with no output after it.)  We can certainly just stick in the output, but I have no idea if it's right.

I have a fix for sageinspect.py, but I'm not sure about worksheet.py.  I can work on it some more, but we should check whether there are failures in the flask notebook before working too hard on this one: if the file is going to go away soon, it's not worth working too hard fixing it.

I'm attaching a patch for the Sage library fixing the two files there; I'll try to get information about whether the patch to library_cython.pyx is actually the right thing to do.


---

Comment by jhpalmieri created at 2011-09-28 04:13:28

Changing status from needs_work to needs_info.


---

Comment by jhpalmieri created at 2011-09-28 05:37:45

For the sagenb problem, this patch seems to fix things:

```diff

diff --git a/sagenb/notebook/worksheet.py b/sagenb/notebook/worksheet.py
--- a/sagenb/notebook/worksheet.py
+++ b/sagenb/notebook/worksheet.py
`@``@` -3881,15 +3881,7 `@``@` except (KeyError, IOError):
             C.delete_output()
 
 
-__internal_test1 = '''
-def foo(x):
-    "
-    EXAMPLES:
-        sage: 2+2
-        4
-    "
-    return x
-'''.lstrip()
+__internal_test1 = '\ndef foo(x):\n    "\n    EXAMPLES:\n        sage: 2+2\n        4\n    "\n    return x'.lstrip()
 
 __internal_test2 = '''
 sage: 2 + 2
```

I don't know if it's the best approach.  Why does this use single double quotes, anyway?  Shouldn't the EXAMPLES block be surrounded by `"""`?  Modifying the patch here to use `"""` still passes doctests.


---

Comment by jhpalmieri created at 2011-09-29 18:55:02

The problem with library_cython.pyx should be dealt with at #11871, so I'm making that a dependency.  I'll remove that part of the doctest patch.


---

Attachment

Sage repository


---

Comment by jhpalmieri created at 2012-06-12 23:10:27

I've submitted a patch for the flask notebook to deal with the issue with notebook/worksheet, and that should be merged soon. There is a patch at #11871 for interacts/library_cython.pyx. So I think this is now ready to go.


---

Comment by jhpalmieri created at 2012-06-12 23:10:27

Changing status from needs_info to needs_review.


---

Comment by jhpalmieri created at 2012-06-15 23:12:53

Changing keywords from "" to "sd41".


---

Comment by jdemeyer created at 2013-02-28 16:03:10

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-02-28 16:03:10

Fixed by #12415.


---

Comment by jdemeyer created at 2013-03-07 08:17:01

Resolution: duplicate
