# Issue 5500: add remark to tutorial to make defining functions at the command line much clearer

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-03-12 05:57:58

Assignee: tba


```
Folks,

I have one suggestion for the Sage Tutorial.

In Section 2.3, after the text

## sage: def is_even(n):
...       return n%2 == 0
## I suggest that you add an instruction to press [Enter/Return/Newline]
after the

...       return n%2 == 0

to conclude the definition.

When I followed the instruction exactly as it is given, without
inserting a blank line, I got an error like this:
### sage: def is_even(n):
....:     return n%2 == 0
....: sage: is_even(2)
------------------------------------------------------------
   File "<ipython console>", line 3
     sage: is_even(Integer(2))
        ^
SyntaxError: invalid syntax
### It was only after I emailed sage-support that I was told I needed to
insert a blank line to conclude the definition. Because I am new to
Python, this was not old hat to me. Hence my suggestion to append:
#### Insert a blank line here by pressing [Return or Enter]

(after the line

...       return n%2 == 0)
#### Many thanks.

Chandra
```



---

Attachment

I've incorporated the suggestions at 

http://groups.google.com/group/sage-devel/browse_thread/thread/5dd8364a8b069d6c/ebc01381136f476d

into a patch.


---

Comment by mvngu created at 2009-03-19 06:51:40

Fix doctest failure


---

Attachment

REFEREE REPORT



The patch *5500-tut.patch* mostly looks good: it applies OK against Sage 3.4, but with one doctest failure:

```
[mvngu`@`sage ~]$ sage -t -long scratch/sage-3.4/devel/sage-5500/doc/en/tutorial/tour_help.rst
sage -t -long "devel/sage-5500/doc/en/tutorial/tour_help.rst"
Traceback (most recent call last):
  File "/home/mvngu/scratch/sage-3.4/tmp/tour_help.py", line 296, in <module>
    runner=runner)
  File "/home/mvngu/scratch/sage-3.4/local/bin/sagedoctest.py", line 54, in testmod_returning_runner
    runner=runner)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 1819, in testmod_returning_runner
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 893, in _find
    globs, seen)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 965, in _get_test
    filename, lineno)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 628, in _parse_example
    self._check_prompt_blank(source_lines, indent, name, lineno)
  File "/home/mvngu/scratch/sage-3.4/local/bin/ncadoctest.py", line 715, in _check_prompt_blank
    line[indent:indent+3], line))
ValueError: line 9 of the docstring for __main__.example_0 lacks blank after ...: '    ...:      return n%Integer(2) == Integer(0)'

	 [3.3 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage-5500/doc/en/tutorial/tour_help.rst"
Total time for all tests: 3.3 seconds
```

This is caused by the following lines in the patch:

```
-    ...       return n%2 == 0
+    ...:      return n%2 == 0
+    ...:
```

The other patch *trac_5500-referee.patch* should fix the above doctest failure.


---

Comment by robertwb created at 2009-03-19 06:58:22

:( I was trying to make things more explicit. New patch coming up.


---

Comment by robertwb created at 2009-03-19 06:58:57

Nevermind, you already attached one. Looks good.


---

Comment by mabshoff created at 2009-03-23 20:34:52

Resolution: fixed


---

Comment by mabshoff created at 2009-03-23 20:34:52

Merged both patches in Sage 3.4.1.alpha0.

Cheers,

Michael
