# Issue 9489: doctest doc/en/thematic_tutorials/group_theory.rst failure on 't2.math' (Solaris 10 SPARC)

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-07-13 14:09:19

Assignee: mvngu

CC:  jhpalmieri

## Hardware + software
 * Sun T5240 with two T2+ UltraSPARC processors
 * 2 CPUS = 16 cores = 128 hardware threads 
 * 1167 MHz
 * 32 GB RAM
 * Solaris 10 update 7 (5/09)
 * sage-4.5.rc0 with:
  * A library patch from #7379
  * An ECL patch from #9187


John Palmieri run the long doctests. On using John's build, I find the following test fails, even if run from the command line, and with SAGE_TIMEOUT_LONG increased to 10,000 seconds, which ensure there are no timeouts (around 3600 seconds should be sufficient on 't2.math' for SAGE_TIMEOUT_LONG)


```
sage -t -long "devel/sage/doc/en/thematic_tutorials/group_theory.rst"
**********************************************************************
File "/scratch/palmieri/sage-4.5.rc0/devel/sage/doc/en/thematic_tutorials/group_theory.rst", line 904:
    sage: map(order, subgroups)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/palmieri/sage-4.5.rc0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/palmieri/sage-4.5.rc0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/palmieri/sage-4.5.rc0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_42[4]>", line 1, in <module>
        map(order, subgroups)###line 904:
    sage: map(order, subgroups)
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/misc/functional.py", line 1231, in order
        return x.order()
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/groups/perm_gps/permgroup.py", line 1105, in order
        return Integer(self._gap_().Size())
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 1408, in __call__
        return self._obj.parent().function_call(self._name, [self._obj] + list(args), kwds)
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/interfaces/gap.py", line 619, in function_call
        ['%s=%s'%(key,value.name()) for key, value in kwds.items()])))
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/interfaces/gap.py", line 354, in eval
        result = Expect.eval(self, input_line, **kwds)
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/palmieri/sage-4.5.rc0/local/lib/python/site-packages/sage/interfaces/gap.py", line 492, in _eval_line
        raise RuntimeError, message
    RuntimeError: Unexpected EOF from Gap executing Size($sage58);
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_42
***Test Failed*** 1 failures.
For whitespace errors, see the file /rootpool2/local/kirkby/.sage//tmp/.doctest_group_theory.py
	 [108.3 s]
 
----------------------------------------------------------------------
The following tests failed:


	sage -t -long "devel/sage/doc/en/thematic_tutorials/group_theory.rst"
Total time for all tests: 108.3 seconds
```



---

Comment by jhpalmieri created at 2010-07-13 15:35:53

Changing priority from major to minor.


---

Comment by jhpalmieri created at 2010-07-13 15:35:53

I'm downgrading this to minor because when I rerun the test, it passes.  It might have failed originally because of running in parallel: memory issues or clashes in the .sage directory or something like that.  Since it's not repeatable, it will likely be harder to debug.


---

Comment by drkirkby created at 2010-07-13 15:51:37

Replying to [comment:2 jhpalmieri]:
> I'm downgrading this to minor because when I rerun the test, it passes.  It might have failed originally because of running in parallel: memory issues or clashes in the .sage directory or something like that.  Since it's not repeatable, it will likely be harder to debug.

Strange, as it was absolutely repeatable for me. I tried it several times. Now it works ok for me too! So it seems the only real failure on Solaris is #9490, which is also a failure (though a different one) on OS X - see #9445. 

As far as I could tell, all the other failures in your `ptestlong.log` can be explained by a timeout, or pass if I run it from the command line. If you have the patience, it might be worth you checking that too. 

Dave


---

Comment by jhpalmieri created at 2010-07-13 15:59:17

I checked the short ones, and they all passed.  I haven't retried the ones which timed out, although they look familiar from builds of earlier versions on t2, when I did have the patience to rerun them with large values for the TIMEOUT variables.

I'll see if I can rerun them today.


---

Comment by jhpalmieri created at 2010-07-15 22:34:57

With 4.5.rc1 and a large value for SAGE_TIMEOUT_LONG, all long tests pass except for `devel/sage/sage/parallel/decorate.py` which sometimes fails with a message `OSError: [Errno 12] Not enough space`.  That looks like an issue with disk space (?) rather than a Sage issue.

In particular, the test which is the subject of this ticket (group_theory.rst) passed when I ran "make ptestlong" and continues to pass when I run it from the command line.  So should we close it?  Dave, are you still seeing this?


---

Comment by drkirkby created at 2010-08-16 00:48:46

Resolution: invalid


---

Comment by drkirkby created at 2010-08-16 00:48:46

Replying to [comment:5 jhpalmieri]:
> In particular, the test which is the subject of this ticket (group_theory.rst) passed when I ran "make ptestlong" and continues to pass when I run it from the command line.  So should we close it?  Dave, are you still seeing this?

Sorry, I missed this until now. I agree, it should be closed. Lets make it invalid. 

Dave
