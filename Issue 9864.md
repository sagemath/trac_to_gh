# Issue 9864: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed

archive/issues_009864.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  @dandrake mvngu alexanderdreyer\n\nReported by Dan Drake on [sage-devel](http://groups.google.com/group/sage-devel/browse_thread/thread/23fd468a4d406389/56ad02c448380af9?#56ad02c448380af9) and [sage-release](http://groups.google.com/group/sage-release/browse_thread/thread/a865f2fa728335c0/2fbf4ba1859e76bb#2fbf4ba1859e76bb):\n\n```\nTwo builds of 4.3.4 are not doctesting properly for me; both are failing\nthe doctest for free_module.py because Singular won't start. The\nfailures always end with \"TypeError: Unable to start singular because\nthe command 'Singular -t --ticks-per-sec 1000' failed.\"\n\nThis happens on two virtual machines: one running Ubuntu Hardy, the\nother running Ubuntu Lucid. I've tried rebuilding Singular, but it\ndidn't work in either case. I tried a couple of the doctests manually,\nand they seemed to work, and I can start Singular using the above\ncommand with no troubles.\n\nI've built 4.3.4 on two different machines (not virtual machines) and\neverything works fine. I'm attaching a log of the failed doctest. Any\nideas? \n```\n\nTracebacks:\n\n```\nsage -t  \"devel/sage/sage/modules/free_module.py\"           \n**********************************************************************\nFile \"/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py\", line 2533:\n    sage: W = M.submodule([x*B[0], 2*B[1]- x*B[2]]); W\nException raised:\n    Traceback (most recent call last):\n      File \"/home/alex/sage-4.3.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/alex/sage-4.3.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/alex/sage-4.3.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_69[11]>\", line 1, in <module>\n        W = M.submodule([x*B[Integer(0)], Integer(2)*B[Integer(1)]- x*B[Integer(2)]]); W###line 2533:\n    sage: W = M.submodule([x*B[0], 2*B[1]- x*B[2]]); W\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 2545, in submodule\n        V = self.span(gens, check=check, already_echelonized=already_echelonized)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 2461, in span\n        self.ambient_module(), gens, check=check, already_echelonized=already_echelonized)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 5446, in __init__\n        echelonize=True, already_echelonized=already_echelonized)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4553, in __init__\n        basis = self._echelonized_basis(ambient, basis)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4666, in _echelonized_basis\n        d = self._denominator(basis)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4774, in _denominator\n        d = sage.rings.integer.Integer(B[0].denominator())\n      File \"free_module_element.pyx\", line 958, in sage.modules.free_module_element.FreeModuleElement.denominator (sage/modules/free_module_element.c:8071)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 343, in lcm\n        return lcm_func(self, singular, have_ring)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 451, in lcm_func\n        lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 339, in _singular_\n        return _singular_func(self, singular, have_ring)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 383, in _singular_func\n        self.parent()._singular_(singular).set_ring() #this is expensive\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 196, in _singular_\n        return self._singular_init_(singular)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 241, in _singular_init_\n        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 897, in ring\n        R = self('%s,%s,%s'%(char, vars, order), 'ring')\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 660, in __call__\n        return SingularElement(self, type, x, False)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 1109, in __init__\n        raise TypeError, x\n    TypeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.\n\n**********************************************************************\nFile \"/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py\", line 2538:\n    sage: W.ambient_module()\nExpected:\n    Ambient free module of rank 3 over the principal ideal domain Univariate Polynomial Ring in x over Rational Field\nGot:\n    Ambient free module of rank 3 over the principal ideal domain Integer Ring\n**********************************************************************\nFile \"/home/alex/sage-4.3.4/devel/sage/sage/modules/free_module.py\", line 2681:\n    sage: W = M.submodule_with_basis([x*B[0], 2*B[0]- x*B[2]]); W\nException raised:\n    Traceback (most recent call last):\n      File \"/home/alex/sage-4.3.4/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/alex/sage-4.3.4/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/alex/sage-4.3.4/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_71[15]>\", line 1, in <module>\n        W = M.submodule_with_basis([x*B[Integer(0)], Integer(2)*B[Integer(0)]- x*B[Integer(2)]]); W###line 2681:\n    sage: W = M.submodule_with_basis([x*B[0], 2*B[0]- x*B[2]]); W\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 2687, in submodule_with_basis\n        V = self.span_of_basis(basis=basis, check=check, already_echelonized=already_echelonized)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 2602, in span_of_basis\n        already_echelonized=already_echelonized)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4577, in __init__\n        w = self._echelonized_basis(ambient, basis)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4666, in _echelonized_basis\n        d = self._denominator(basis)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/modules/free_module.py\", line 4774, in _denominator\n        d = sage.rings.integer.Integer(B[0].denominator())\n      File \"free_module_element.pyx\", line 958, in sage.modules.free_module_element.FreeModuleElement.denominator (sage/modules/free_module_element.c:8071)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 343, in lcm\n        return lcm_func(self, singular, have_ring)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 451, in lcm_func\n        lcm = self._singular_(have_ring=have_ring).lcm(right._singular_(have_ring=have_ring))\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 339, in _singular_\n        return _singular_func(self, singular, have_ring)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 383, in _singular_func\n        self.parent()._singular_(singular).set_ring() #this is expensive\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 196, in _singular_\n        return self._singular_init_(singular)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 241, in _singular_init_\n        self.__singular = singular.ring(self.characteristic(), _vars, order=order, check=False)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 897, in ring\n        R = self('%s,%s,%s'%(char, vars, order), 'ring')\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 660, in __call__\n        return SingularElement(self, type, x, False)\n      File \"/home/alex/sage-4.3.4/local/lib/python/site-packages/sage/interfaces/singular.py\", line 1109, in __init__\n        raise TypeError, x\n    TypeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.\n\n**********************************************************************\n2 items had failures:\n   2 of  13 in __main__.example_69\n   1 of  16 in __main__.example_71\n***Test Failed*** 3 failures.\nFor whitespace errors, see the file /home/alex/.sage//tmp/.doctest_free_module.py\n\t [13.0 s]\n```\n\n\nMinh Nguyen reports seeing the same error a Debian 5.0 machine (gcc100.fsffrance.org, AMD Opteron(tm) Processor 252 `@` 2647.708 MHz).  [Here](http://wiki.sagemath.org/devel/BuildFarm/sage-4.5.3?action=AttachFile&do=get&target=gcc100.fsffrance.log.bz2) is the test log.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9865\n\n",
    "created_at": "2010-09-07T07:08:54Z",
    "labels": [
        "component: doctest",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9864",
    "user": "https://github.com/qed777"
}
```
Assignee: mvngu

CC:  @dandrake mvngu alexanderdreyer

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

Issue created by migration from https://trac.sagemath.org/ticket/9865





---

archive/issue_comments_097291.json:
```json
{
    "body": "I've just seen this error while testing the trial \"final\" 4.5.3 on t2:\n\n```python\nsage -t -long  devel/sage/sage/crypto/mq/sr.py\n**********************************************************************\nFile \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/devel/sage-main/sage/crypto/mq/sr.py\", line 118:\n    sage: for V in I.variety():\n       for k,v in sorted(V.iteritems()):\n          print k,v\n       print\nException raised:\n    Traceback (most recent call last):\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_0[20]>\", line 1, in <module>\n        for V in I.variety():###line 118:\n    sage: for V in I.variety():\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 407, in __call__\n        return self.f(self._instance, *args, **kwds)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 2092, in variety\n        d = self.dimension()\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 407, in __call__\n        return self.f(self._instance, *args, **kwds)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1010, in dimension\n        v = self._groebner_basis_singular_raw()\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 1175, in _groebner_basis_singular_raw\n        S = self._singular_().groebner()\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_ideal.py\", line 517, in _singular_\n        self.ring()._singular_(singular).set_ring()\n      File \"sage_object.pyx\", line 583, in sage.structure.sage_object.SageObject._singular_ (sage/structure/sage_object.c:6315)\n      File \"sage_object.pyx\", line 379, in sage.structure.sage_object.SageObject._interface_ (sage/structure/sage_object.c:3374)\n      File \"pbori.pyx\", line 1190, in sage.rings.polynomial.pbori.BooleanPolynomialRing._singular_init_ (sage/rings/polynomial/pbori.cpp:10968)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/rings/quotient_ring.py\", line 756, in _singular_init_\n        self.__R._singular_().set_ring()\n      File \"multi_polynomial_libsingular.pyx\", line 994, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:9038)\n      File \"multi_polynomial_libsingular.pyx\", line 1135, in sage.rings.polynomial.multi_polynomial_libsingular.MPolynomialRing_libsingular._singular_init_ (sage/rings/polynomial/multi_polynomial_libsingular.cpp:9607)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 890, in ring\n        self.eval(s)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 546, in eval\n        s = Expect.eval(self, x, **kwds)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 983, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 634, in _eval_line\n        return self._eval_line_using_file(line)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 621, in _eval_line_using_file\n        s = self._eval_line(self._read_in_file_command(tmp_to_use), allow_use_file=False)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 637, in _eval_line\n        self._start()\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 375, in _start\n        Expect._start(self, alt_message)\n      File \"/scratch/mpatel/tmp/bb/slave/t2_scratch/build/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 458, in _start\n        self.__name, cmd, self._install_hints())\n    RuntimeError: Unable to start singular because the command 'Singular -t --ticks-per-sec 1000' failed.\n\n**********************************************************************\n1 items had failures:\n   1 of  28 in __main__.example_0\n***Test Failed*** 1 failures.\nFor whitespace errors, see the file /scratch/mpatel/.sage/tmp/.doctest_sr.py\n```\n",
    "created_at": "2010-09-07T07:11:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97291",
    "user": "https://github.com/qed777"
}
```

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

archive/issue_comments_097292.json:
```json
{
    "body": "In [comment:1 my case], the test passed when I ran it again.  I could not reproduce it.",
    "created_at": "2010-09-07T07:12:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97292",
    "user": "https://github.com/qed777"
}
```

In [comment:1 my case], the test passed when I ran it again.  I could not reproduce it.



---

archive/issue_comments_097293.json:
```json
{
    "body": "I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.\n\nAlso, rebooting and running the test again made the test pass back then.",
    "created_at": "2010-09-07T07:26:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97293",
    "user": "https://trac.sagemath.org/admin/accounts/users/cschwan"
}
```

I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.

Also, rebooting and running the test again made the test pass back then.



---

archive/issue_comments_097294.json:
```json
{
    "body": "Replying to [comment:4 cschwan]:\n> I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.\n\nInteresting. On the Arch VM where I was seeing the same problem, increasing the RAM allocated to the VM from 1152 MB up to 1768 MB seems to fix the problem. (Using 4.5.3.alpha2.) But there are still questions: why do the tests pass when run in Sage normally? Does the doctest framework really take 600+ MB of memory? And why exactly does Singular fail to start -- is it just unable to allocate enough memory? If so, can we get a better error message? These tests seem to work on non-VMs with less memory -- or do they? Why is that?",
    "created_at": "2010-09-07T08:40:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97294",
    "user": "https://github.com/dandrake"
}
```

Replying to [comment:4 cschwan]:
> I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.

Interesting. On the Arch VM where I was seeing the same problem, increasing the RAM allocated to the VM from 1152 MB up to 1768 MB seems to fix the problem. (Using 4.5.3.alpha2.) But there are still questions: why do the tests pass when run in Sage normally? Does the doctest framework really take 600+ MB of memory? And why exactly does Singular fail to start -- is it just unable to allocate enough memory? If so, can we get a better error message? These tests seem to work on non-VMs with less memory -- or do they? Why is that?



---

archive/issue_comments_097295.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-09-07T22:29:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97295",
    "user": "https://github.com/qed777"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_097296.json:
```json
{
    "body": "Replying to [comment:5 ddrake]:\n> Replying to [comment:4 cschwan]:\n> > I remember having the same failure in free_module.py and I think its most likely caused by having not sufficient memory - everytime I run free_module.py's my system (i686 + 1GB RAM + 512 MB swap) is heavily using swap.\n> \n> Interesting. On the Arch VM where I was seeing the same problem, increasing the RAM allocated to the VM from 1152 MB up to 1768 MB seems to fix the problem. (Using 4.5.3.alpha2.) But there are still questions: why do the tests pass when run in Sage normally? Does the doctest framework really take 600+ MB of memory? And why exactly does Singular fail to start -- is it just unable to allocate enough memory? If so, can we get a better error message? These tests seem to work on non-VMs with less memory -- or do they? Why is that?\n\nI've successfully built and `p`test`long`ed recent versions of Sage on e.g.:\n* Single-core (no HT either) with only 768 MB (and GUI running), and I believe half of that would not cause swapping. (IIRC built with 2 jobs, tested with only one thread.)\n* Quad-core (no HT) with 8 GB: Built with 32 jobs, `ptestlong` with 64(!) threads without swapping. (I then only further tried `ptestlong` with 128 threads, which as expected caused massive swapping s.t. almost all tests timed out.)\n\nI recently examined the memory consumption of testing files in `sage/schemes/elliptic_curves` since these were said to be the record holders. The \"winner\" of these was `sha_tate.py` with a peak usage (just that process) of 226 MB.",
    "created_at": "2010-09-08T00:17:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97296",
    "user": "https://github.com/nexttime"
}
```

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

archive/issue_comments_097297.json:
```json
{
    "body": "lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...\n\nMore to come; the test is still running.",
    "created_at": "2010-09-08T13:55:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97297",
    "user": "https://github.com/nexttime"
}
```

lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...

More to come; the test is still running.



---

archive/issue_comments_097298.json:
```json
{
    "body": "Changing keywords from \"\" to \"pexpect EOF crash exception\".",
    "created_at": "2010-09-09T01:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97298",
    "user": "https://github.com/nexttime"
}
```

Changing keywords from "" to "pexpect EOF crash exception".



---

archive/issue_comments_097299.json:
```json
{
    "body": "Replying to [comment:8 leif]:\n> lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...\n> \n> More to come; the test is still running.\n\n2 threads were perhaps too much for that old machine (CPU, not RAM), though *the build* went fine with three jobs.\n\nAs reported by me on sage-release, `ptestlong` gave one timeout and two doctest failures due to Singular having \"crashed\" (plus two `NameError`s as a result of that):\n\n```\nsage -t  -long devel/sage/sage/rings/polynomial/multi_polynomial_element.py\n**********************************************************************\nFile \"/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py\", line 1513:\n    sage: M = f.lift(I)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[5]>\", line 1, in <module>\n        M = f.lift(I)###line 1513:\n    sage: M = f.lift(I)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/multi_polynomial_element.py\", line 1519, in lift\n        fs = self._singular_()\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 347, in _singular_\n        return _singular_func(self, singular, have_ring)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 391, in _singular_func\n        self.parent()._singular_(singular).set_ring() #this is expensive\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 195, in _singular_\n        return self._singular_init_(singular)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/rings/polynomial/polynomial_singular_interface.py\", line 236, in _singular_init_\n        self.__singular = singular.ring(\"(complex,%d,0,I)\"%digits, _vars,  order=order, check=False)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 890, in ring\n        self.eval(s)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 546, in eval\n        s = Expect.eval(self, x, **kwds)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 983, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 637, in _eval_line\n        self._start()\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 377, in _start\n        self.lib('general')   # assumed loaded by misc/constants.py\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 703, in lib\n        self.eval('LIB \"%s\"'%lib)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/singular.py\", line 546, in eval\n        s = Expect.eval(self, x, **kwds)\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 983, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/home/leif/Sage/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 668, in _eval_line\n        raise RuntimeError, \"%s\\n%s crashed executing %s\"%(msg,self, line)\n    RuntimeError: End Of File (EOF) in read_nonblocking(). Exception style platform.\n    <pexpect.spawn instance at 0xaf32c0c>\n    version: 2.0 ($Revision: 1.151 $)\n    command: /home/leif/Sage/sage-4.5.3/local/bin/Singular\n    args: ['/home/leif/Sage/sage-4.5.3/local/bin/Singular', '-t', '--ticks-per-sec', '1000']\n    patterns:\n        \n    > \n    buffer (last 100 chars): \n    before (last 100 chars): mmand(a), continue(c) or quit Singular(q) ?fatal flex scanner internal error--end of buffer missed\n\n\n    after: <class 'pexpect.EOF'>\n    match: None\n    match_index: None\n    exitstatus: None\n    flag_eof: 1\n    pid: 26203\n    child_fd: 4\n    timeout: None\n    delimiter: <class 'pexpect.EOF'>\n    logfile: None\n    maxread: 1000\n    searchwindowsize: None\n    delaybeforesend: 0\n    Singular crashed executing LIB \"general.lib\";\n**********************************************************************\nFile \"/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py\", line 1514:\n    sage: M\nException raised:\n    Traceback (most recent call last):\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[6]>\", line 1, in <module>\n        M###line 1514:\n    sage: M\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py\", line 1516:\n    sage: sum( map( mul , zip( M, I.gens() ) ) ) == f\nException raised:\n    Traceback (most recent call last):\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/leif/Sage/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_49[7]>\", line 1, in <module>\n        sum( map( mul , zip( M, I.gens() ) ) ) == f###line 1516:\n    sage: sum( map( mul , zip( M, I.gens() ) ) ) == f\n    NameError: name 'M' is not defined\n**********************************************************************\nFile \"/home/leif/Sage/sage-4.5.3/devel/sage-main/sage/rings/polynomial/multi_polynomial_element.py\", line 1570:\n    sage: f.quo_rem(x)\nExpected:\n    (x*y + 1.00000000000000, 1.00000000000000)\nGot:\n    Singular crashed -- automatically restarting.\n    (x*y + 1.00000000000000, 1.00000000000000)\n**********************************************************************\n2 items had failures:\n   3 of   8 in __main__.example_49\n   1 of   5 in __main__.example_51\n***Test Failed*** 4 failures.\nFor whitespace errors, see the file /home/leif/.sage//tmp/.doctest_multi_polynomial_element.py\n     [45.9 s]\n```\n\n\nIt's not that clear if the error is caused by Singular, pexpect or Sage's Singular interface (or even the operating system, Ubuntu 7.10, kernel 2.6.22-16-generic).",
    "created_at": "2010-09-09T01:41:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97299",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:8 leif]:
> lol, I've just built Sage 4.5.3 on the (single-core) Pentium 4 with 768 MB RAM, and it seems I now get doctest errors due to Singular crashing while running `ptestlong` with two threads...
> 
> More to come; the test is still running.

2 threads were perhaps too much for that old machine (CPU, not RAM), though *the build* went fine with three jobs.

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

archive/issue_comments_097300.json:
```json
{
    "body": "P.S.: Both doctesting just these files and also `make testlong` passed without errors.\n\nI wonder if `read_nonblocking()` is the right thing to do... (One can use signals to implement timeouts if that's the reason. I haven't looked at the code.)",
    "created_at": "2010-09-09T01:57:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97300",
    "user": "https://github.com/nexttime"
}
```

P.S.: Both doctesting just these files and also `make testlong` passed without errors.

I wonder if `read_nonblocking()` is the right thing to do... (One can use signals to implement timeouts if that's the reason. I haven't looked at the code.)



---

archive/issue_comments_097301.json:
```json
{
    "body": "Changing component from doctest to interfaces.",
    "created_at": "2013-03-28T23:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97301",
    "user": "https://github.com/roed314"
}
```

Changing component from doctest to interfaces.



---

archive/issue_comments_097302.json:
```json
{
    "body": "Changing assignee from mvngu to @williamstein.",
    "created_at": "2013-03-28T23:01:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97302",
    "user": "https://github.com/roed314"
}
```

Changing assignee from mvngu to @williamstein.



---

archive/issue_comments_097303.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-09-07T18:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97303",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_097304.json:
```json
{
    "body": "I think this should be fixed in the mean time.",
    "created_at": "2015-09-07T18:55:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97304",
    "user": "https://github.com/jdemeyer"
}
```

I think this should be fixed in the mean time.



---

archive/issue_comments_097305.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-09-07T18:55:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97305",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009994.json:
```json
{
    "actor": "@vbraun",
    "created_at": "2015-09-12T13:59:48Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9864#event-9994"
}
```



---

archive/issue_comments_097306.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-09-12T13:59:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9864",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9864#issuecomment-97306",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
