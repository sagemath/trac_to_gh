# Issue 8836: sagenb doctest issue discovered on t2.

Issue created by migration from https://trac.sagemath.org/ticket/8836

Original creator: was

Original creation time: 2010-05-01 06:34:35

Assignee: jason, was

William to Mike Hansen:

```
Hi,

Is this caused by your cygwin fixed?

sage -t  -long "local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sagenb/misc/misc.py"
**********************************************************************
File "/scratch/wstein/build/sage-4.4.1.alpha2/local/lib/python2.6/site-packages/sagenb-0.8-py2.6.egg/sa
genb/misc/misc.py", line 109:
   sage: print "ignore this";
sage.server.misc.find_next_available_port('', 9000, verbose=False)   #
random output -- depends on network
Exception raised:
   Traceback (most recent call last):
     File "/scratch/wstein/build/sage-4.4.1.alpha2/local/bin/ncadoctest.py",
line 1231, in run_one_tes
t
       self.run_one_example(test, example, filename, compileflags)
     File "/scratch/wstein/build/sage-4.4.1.alpha2/local/bin/sagedoctest.py",
line 38, in run_one_exam
ple
       OrigDocTestRunner.run_one_example(self, test, example,
filename, compileflags)
     File "/scratch/wstein/build/sage-4.4.1.alpha2/local/bin/ncadoctest.py",
line 1172, in run_one_exa
mple
       compileflags, 1) in test.globs
     File "<doctest __main__.example_2[2]>", line 1, in <module>
       print "ignore this";
sage.server.misc.find_next_available_port('', Integer(9000),
verbose=Fals
e)   # random output -- depends on network###line 109:
   sage: print "ignore this";
sage.server.misc.find_next_available_port('', 9000, verbose=False)   #
random output -- depends on network
     File "/scratch/wstein/build/sage-4.4.1.alpha2/local/lib/python/site-packages/sage/server/misc.py"
, line 105, in find_next_available_port
       for port in range(start, start+max_tries+1):
     File "element.pyx", line 1271, in
sage.structure.element.RingElement.__add__ (sage/structure/elem
ent.c:10830)
     File "coerce.pyx", line 765, in
sage.structure.coerce.CoercionModel_cache_maps.bin_op (sage/struc
ture/coerce.c:6966)
   TypeError: unsupported operand parent(s) for '+': '<type 'str'>'
and 'Integer Ring'
**********************************************************************
1 items had failures:
  1 of   3 in __main__.example_2
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/wstein/sage//tmp/.doctest_misc.py
        [16.3 s]
```


Mike to William

```
> Is this caused by your cygwin fixed?

Yes.  The doctest is wrong:

> sage.server.misc.find_next_available_port('', 9000, verbose=False)   #

sage.server.misc.find_next_available_port was not changed --
sagenb.misc.misc.find_next_available_port was.

--Mike
```




---

Comment by mhansen created at 2010-05-01 06:42:06

Changing status from new to needs_review.


---

Attachment


---

Comment by was created at 2010-05-01 18:50:30

Resolution: fixed
