# Issue 9864: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed

Issue created by migration from Trac.

Original creator: mpatel

Original creation time: 2010-09-07 07:08:54

Assignee: mvngu

CC:  ddrake mvngu alexanderdreyer

Reported by Dan Drake on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/23fd468a4d406389/56ad02c448380af9?#56ad02c448380af9) and [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/a865f2fa728335c0/2fbf4ba1859e76bb#2fbf4ba1859e76bb):

```
Two builds of 4.3.4 are not doctesting properly for me; both are failing
the doctest for free_module.py because Singular won't start. The
failures always end with "TypeError: Unable to start singular because
the command 'Singular -t --ticks-per-sec 1000' failed."

This happens on two virtual machines: one running Ubuntu Hardy, the
other running Ubuntu Lucid. I've tried rebuilding Singular, but it
didn't work in either case. I tried a couple of the doctests manually,
and they seemed to work, and I can start Singular using the above
command with no troubles.

I've built 4.3.4 on two different machines (not virtual machines) and
everything works fine. I'm attaching a log of the failed doctest. Any
ideas? 
```

Tracebacks:

```
sage -t  "devel/sage/sage/modules/free_module.py"           
**********************************************************************
File "/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py", line 2533:
    sage: W = M.submodule([x*B[0], 2*B[1]- x*B[2]]); W
Exception raised:
    Traceback (most recent call last):
      File "/home/alex/sage-4.3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/alex/sage-4.3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/alex/sage-4.3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_69[11]>", line 1, in <module>
        W = M.submodule([x*B[Integer(0)], Integer(2)*B[Integer(1)]- x*B[Integer(2)]]); W###line 2533:
    sage: W = M.submodule([x*B[0], 2*B[1]- x*B[2]]); W
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 2545, in submodule
        V = self.span(gens, check=check, already_echelonized=already_echelonized)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 2461, in span
        self.ambient_module(), gens, check=check, already_echelonized=already_echelonized)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 5446, in __init__
        echelonize=True, already_echelonized=already_echelonized)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4553, in __init__
        basis = self._echelonized_basis(ambient, basis)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4666, in _echelonized_basis
        d = self._denominator(basis)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4774, in _denominator
        d = sage.rings.integer.Integer(B[0].denominator())
      File "free_module_element.pyx", line 958, in sage.modules.free_module_element.FreeModuleElement.denominator (sage/modules/free_module_element.c:8071)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 343, in lcm
        return lcm_func(self, singular, have_ring)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 451, in lcm_func
        lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 339, in _singular_
        return _singular_func(self, singular, have_ring)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 383, in _singular_func
        self.parent()._singular_(singular).set_ring() #this is expensive
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 196, in _singular_
        return self._singular_init_(singular)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 241, in _singular_init_
        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 897, in ring
        R = self('%s,%s,%s'%(char, vars, order), 'ring')
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 660, in __call__
        return SingularElement(self, type, x, False)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 1109, in __init__
        raise TypeError, x
    TypeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.

**********************************************************************
File "/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py", line 2538:
    sage: W.ambient_module()
Expected:
    Ambient free module of rank 3 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field
Got:
    Ambient free module of rank 3 over the principal ideal domain Integer Ring
**********************************************************************
File "/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py", line 2681:
    sage: W = M.submodule_with_basis([x*B[0], 2*B[0]- x*B[2]]); W
Exception raised:
    Traceback (most recent call last):
      File "/home/alex/sage-4.3.4/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/alex/sage-4.3.4/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/alex/sage-4.3.4/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_71[15]>", line 1, in <module>
        W = M.submodule_with_basis([x*B[Integer(0)], Integer(2)*B[Integer(0)]- x*B[Integer(2)]]); W###line 2681:
    sage: W = M.submodule_with_basis([x*B[0], 2*B[0]- x*B[2]]); W
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 2687, in submodule_with_basis
        V = self.span_of_basis(basis=basis, check=check, already_echelonized=already_echelonized)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 2602, in span_of_basis
        already_echelonized=already_echelonized)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4577, in __init__
        w = self._echelonized_basis(ambient, basis)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4666, in _echelonized_basis
        d = self._denominator(basis)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py", line 4774, in _denominator
        d = sage.rings.integer.Integer(B[0].denominator())
      File "free_module_element.pyx", line 958, in sage.modules.free_module_element.FreeModuleElement.denominator (sage/modules/free_module_element.c:8071)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 343, in lcm
        return lcm_func(self, singular, have_ring)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 451, in lcm_func
        lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 339, in _singular_
        return _singular_func(self, singular, have_ring)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 383, in _singular_func
        self.parent()._singular_(singular).set_ring() #this is expensive
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 196, in _singular_
        return self._singular_init_(singular)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 241, in _singular_init_
        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 897, in ring
        R = self('%s,%s,%s'%(char, vars, order), 'ring')
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 660, in __call__
        return SingularElement(self, type, x, False)
      File "/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py", line 1109, in __init__
        raise TypeError, x
    TypeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.

**********************************************************************
2 items had failures:
   2 of  13 in __main__.example_69
   1 of  16 in __main__.example_71
***Test Failed*** 3 failures.
For whitespace errors, see the file /home/alex/.sage//tmp/.doctest_free_module.py
	 [13.0 s]
```


Minh Nguyen reports seeing the same error a Debian 5.0 machine (gcc100.fsffrance.org, AMD Opteron(tm) Processor 252 `@` 2647.708 MHz).  [Here](http://wiki.sagemath.org/devel/BuildFarm/sage-4.5.3?action=AttachFile&do=get&target=gcc100.fsffrance.log.bz2) is the test log.


---

Comment by mpatel created at 2010-09-07 07:11:16

I've just seen this error while testing the trial "final" 4.5.3 on t2:

```python
sage -t -long  devel/sage/sage/crypto/mq/sr.py
**********************************************************************
File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/devel/sage-main/sage/crypto/mq/sr.py", line 118:
    sage: for V in I.variety():
       for k,v in sorted(V.iteritems()):
          print k,v
       print
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[20]>", line 1, in <module>
        for V in I.variety():###line 118:
    sage: for V in I.variety():
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 2092, in variety
        d = self.dimension()
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 407, in __call__
        return self.f(self._instance, *args, **kwds)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1010, in dimension
        v = self._groebner_basis_singular_raw()
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 1175, in _groebner_basis_singular_raw
        S = self._singular_().groebner()
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py", line 517, in _singular_
        self.ring()._singular_(singular).set_ring()
      File "sage_object.pyx", line 583, in sage.structure.sage_object.SageObject._singular_ (sage/structure/sage_object.c:6315)
      File "sage_object.pyx", line 379, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3374)
      File "pbori.pyx", line 1190, in sage.rings.polynomial.pbori.BooleanPolynomialRing._singular_init_ (sage/rings/polynomial/pbori.cpp:10968)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/quotient_ring.py", line 756, in _singular_init_
        self.__R._singular_().set_ring()
      File "multi_polynomial_libsingular.pyx", line 994, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:9038)
      File "multi_polynomial_libsingular.pyx", line 1135, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_init_ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:9607)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 890, in ring
        self.eval(s)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 546, in eval
        s = Expect.eval(self, x, **kwds)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 634, in _eval_line
        return self._eval_line_using_file(line)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 621, in _eval_line_using_file
        s = self._eval_line(self._read_in_file_command(tmp_to_use), allow_use_file=False)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
        self._start()
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 375, in _start
        Expect._start(self, alt_message)
      File "/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 458, in _start
        self.__name, cmd, self._install_hints())
    RuntimeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.

**********************************************************************
1 items had failures:
   1 of  28 in __main__.example_0
***Test Failed*** 1 failures.
For whitespace errors, see the file /scratch/mpatel/.sage/tmp/.doctest_sr.py
```



---

Comment by mpatel created at 2010-09-07 07:12:44

In [comment:1 my case], the test passed when I ran it again.  I could not reproduce it.


---

Comment by cschwan created at 2010-09-07 07:26:46

I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.

Also, rebooting and running the test again made the test pass back then.


---

Comment by ddrake created at 2010-09-07 08:40:14

Replying to [comment:4 cschwan]:
> I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.

Interesting. On the Arch VM where I was seeing the same problem, increasing the RAM allocated to the VM from 1152 MB up to 1768 MB seems to fix the problem. (Using 4.5.3.alpha2.) But there are still questions: why do the tests pass when run in Sage normally? Does the doctest framework really take 600+ MB of memory? And why exactly does Singular fail to start -- is it just unable to allocate enough memory? If so, can we get a better error message? These tests seem to work on non-VMs with less memory -- or do they? Why is that?


---

Comment by mpatel created at 2010-09-07 22:29:07

Changing priority from major to blocker.


---

Comment by leif created at 2010-09-08 00:17:01

Replying to [comment:5 ddrake]:
> Replying to [comment:4 cschwan]:
> > I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.
> 
> Interesting. On the Arch VM where I was seeing the same problem, increasing the RAM allocated to the VM from 1152 MB up to 1768 MB seems to fix the problem. (Using 4.5.3.alpha2.) But there are still questions: why do the tests pass when run in Sage normally? Does the doctest framework really take 600+ MB of memory? And why exactly does Singular fail to start -- is it just unable to allocate enough memory? If so, can we get a better error message? These tests seem to work on non-VMs with less memory -- or do they? Why is that?

I've successfully built and `p`test`long`ed recent versions of Sage on e.g.:
 * Single-core (no HT either) with only 768 MB (and GUI running), and I believe half of that would not cause swapping. (IIRC built with 2 jobs, tested with only one thread.)
 * Quad-core (no HT) with 8 GB: Built with 32 jobs, `ptestlong` with 64(!) threads without swapping. (I then only further tried `ptestlong` with 128 threads, which as expected caused massive swapping s.t. almost all tests timed out.)

I recently examined the memory consumption of testing files in `sage/schemes/elliptic_curves` since these were said to be the record holders. The "winner" of these was `sha_tate.py` with a peak usage (just that process) of 226 MB.


---

Comment by leif created at 2010-09-08 13:55:09

lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...

More to come; the test is still running.


---

Comment by leif created at 2010-09-09 01:41:04

Changing keywords from "" to "pexpect EOF crash exception".


---

Comment by leif created at 2010-09-09 01:41:04

Replying to [comment:8 leif]:
> lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...
> 
> More to come; the test is still running.

2 threads were perhaps too much for that old machine (CPU, not RAM), though _the build_ went fine with three jobs.

As reported by me on sage-release, `ptestlong` gave one timeout and two doctest failures due to Singular having "crashed" (plus two `NameError`s as a result of that):

```
sage -t  -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py
**********************************************************************
File "/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py", line 1513:
    sage: M = f.lift(I)
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[5]>", line 1, in <module>
        M = f.lift(I)###line 1513:
    sage: M = f.lift(I)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_element.py", line 1519, in lift
        fs = self._singular_()
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 347, in _singular_
        return _singular_func(self, singular, have_ring)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 391, in _singular_func
        self.parent()._singular_(singular).set_ring() #this is expensive
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 195, in _singular_
        return self._singular_init_(singular)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py", line 236, in _singular_init_
        self.__singular = singular.ring("(complex,%d,0,I)"%digits, _vars,  order=order, check=False)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 890, in ring
        self.eval(s)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 546, in eval
        s = Expect.eval(self, x, **kwds)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
        self._start()
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 377, in _start
        self.lib('general')   # assumed loaded by misc/constants.py
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 703, in lib
        self.eval('LIB "%s"'%lib)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py", line 546, in eval
        s = Expect.eval(self, x, **kwds)
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 668, in _eval_line
        raise RuntimeError, "%s\n%s crashed executing %s"%(msg,self, line)
    RuntimeError: End Of File (EOF) in read_nonblocking(). Exception style platform.
    <pexpect.spawn instance at 0xaf32c0c>
    version: 2.0 ($Revision: 1.151 $)
    command: /home/leif/Sage/sage-4.5.3/local/bin/Singular
    args: ['/home/leif/Sage/sage-4.5.3/local/bin/Singular', '-t', '--ticks-per-sec', '1000']
    patterns:
        
    > 
    buffer (last 100 chars): 
    before (last 100 chars): mmand(a), continue(c) or quit Singular(q) ?fatal flex scanner internal error--end of buffer missed


    after: <class 'pexpect.EOF'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 1
    pid: 26203
    child_fd: 4
    timeout: None
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 1000
    searchwindowsize: None
    delaybeforesend: 0
    Singular crashed executing LIB "general.lib";
**********************************************************************
File "/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py", line 1514:
    sage: M
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[6]>", line 1, in <module>
        M###line 1514:
    sage: M
    NameError: name 'M' is not defined
**********************************************************************
File "/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py", line 1516:
    sage: sum( map( mul , zip( M, I.gens() ) ) ) == f
Exception raised:
    Traceback (most recent call last):
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_49[7]>", line 1, in <module>
        sum( map( mul , zip( M, I.gens() ) ) ) == f###line 1516:
    sage: sum( map( mul , zip( M, I.gens() ) ) ) == f
    NameError: name 'M' is not defined
**********************************************************************
File "/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py", line 1570:
    sage: f.quo_rem(x)
Expected:
    (x*y + 1.00000000000000, 1.00000000000000)
Got:
    Singular crashed -- automatically restarting.
    (x*y + 1.00000000000000, 1.00000000000000)
**********************************************************************
2 items had failures:
   3 of   8 in __main__.example_49
   1 of   5 in __main__.example_51
***Test Failed*** 4 failures.
For whitespace errors, see the file /home/leif/.sage//tmp/.doctest_multi_polynomial_element.py
     [45.9 s]
```


It's not that clear if the error is caused by Singular, pexpect or Sage's Singular interface (or even the operating system, Ubuntu 7.10, kernel 2.6.22-16-generic).


---

Comment by leif created at 2010-09-09 01:57:28

P.S.: Both doctesting just these files and also `make testlong` passed without errors.

I wonder if `read_nonblocking()` is the right thing to do... (One can use signals to implement timeouts if that's the reason. I haven't looked at the code.)


---

Comment by mpatel created at 2010-10-07 12:12:00

Changing priority from blocker to major.


---

Comment by roed created at 2013-03-28 23:01:53

Changing component from doctest to interfaces.


---

Comment by roed created at 2013-03-28 23:01:53

Changing assignee from mvngu to was.


---

Comment by jdemeyer created at 2015-09-07 18:55:27

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-09-07 18:55:27

I think this should be fixed in the mean time.


---

Comment by jdemeyer created at 2015-09-07 18:55:32

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2015-09-12 13:59:48

Resolution: fixed
