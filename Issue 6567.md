# Issue 6567: function to test whether or not some integer is a primitive root modulo n

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-20 12:11:43

Assignee: was

CC:  kcrisman

Keywords: primitive roots

Currently, the function `primitive_root()` finds a primitive root modulo n. Ticket #6467 proposes to find all primitive roots modulo a fixed n. We should also implement a function to determine whether or not some integer is a primitive root modulo n. A good way is to do this without first having to generate all primitive roots mod n.


---

Comment by roed created at 2012-10-17 08:24:49

Review anyone?


---

Comment by roed created at 2012-10-17 08:24:49

Changing status from new to needs_review.


---

Comment by saraedum created at 2012-11-18 20:35:21

There is a problem in the docstring:


```
Traceback (most recent call last):
  File "/dev/shm/sage_testdir/integer_mod_10415.py", line 3096, in <module>
    runner=runner)
  File "/dev/shm/sage/local/bin/sagedoctest.py", line 54, in testmod_returning_runner
    runner=runner)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 1819, in testmod_returning_runner
    for test in finder.find(m, name, globs=globs, extraglobs=extraglobs):
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 839, in find
    self._find(tests, obj, name, module, source_lines, globs, {})
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 893, in _find
    globs, seen)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 881, in _find
    test = self._get_test(obj, name, module, globs, source_lines)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 965, in _get_test
    filename, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 594, in get_doctest
    return DocTest(self.get_examples(string, name), globs,
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 608, in get_examples
    return [x for x in self.parse(string, name)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 570, in parse
    self._parse_example(m, name, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 628, in _parse_example
    self._check_prompt_blank(source_lines, indent, name, lineno)
  File "/dev/shm/sage/local/bin/ncadoctest.py", line 715, in _check_prompt_blank
    line[indent:indent+3], line))
ValueError: line 27 of the docstring for __main__.example_32 lacks blank after ...: '            ....:     for k in range(Integer(1),Integer(4)):'
```



---

Comment by saraedum created at 2012-11-18 20:35:21

Changing status from needs_review to needs_work.


---

Comment by roed created at 2013-02-27 01:05:00

The doctesting error was due to depending on syntax only valid after #12415.  Since I don't want to wait on that, I've updated the doctest (and also marked the dependency correctly).


---

Comment by roed created at 2013-02-27 01:05:00

Changing status from needs_work to needs_review.


---

Comment by kcrisman created at 2013-02-27 04:26:36


```
# self**(p**k*(p-1)//q) = 1 for some q 
```

Should that be `k-1`?  I'd also put it "# now self..." just to make it clear

Everything else looks nice.  I feel like I want to check the logic for numbers divisible by 2, 3, or 5 but where start > 5 a little more closely (getting late here) but if someone else does that first that is fine.


---

Attachment


---

Comment by roed created at 2013-02-27 11:38:01

I'm not quite sure what you meant by the "# now self..." but I made some change along those lines.  I'm also not sure why patchbot was giving me a failure in applying.  Hopefully the new patch won't have the same problem.


---

Attachment

Fixes single line in self.is_primitive_root() to make compatible with new 12116.patch


---

Comment by spice created at 2013-02-28 23:42:31

Patch applies, but with the (proposed) change to #12116 - swapping the order integers returned by `perfect_power()` so that `(a^b).perfect_power()` returns `(a,b)` and not `(b,a)` - the code breaks on perfect powers or twice perfect powers. A simple single line change fixes this; I've uploaded a new patch with this fix. Line 1485 goes from

```
k, p = odd.perfect_power() 
```

to

```
p, k = odd.perfect_power() 
```

Everything else is good.


---

Comment by roed created at 2013-03-01 01:16:01

Fine with me.


---

Comment by roed created at 2013-03-01 01:16:01

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2013-03-04 07:43:14

Please clarify which patch(es) must be applied.


---

Comment by jdemeyer created at 2013-03-06 10:26:19

Resolution: fixed
