# Issue 9166: cygwin: sympow does not work on cygwin

Issue created by migration from Trac.

Original creator: was

Original creation time: 2010-06-07 04:22:20

Assignee: tbd

CC:  mhansen

Basically, Mark Watkins program Sympow is completely broken on Microsoft Windows (Cygwin):


```

sage -t  "devel/sage/sage/lfunctions/sympow.py"             
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/lfunctions/sympow.py", line 213:
    sage: sympow.modular_degree(EllipticCurve('11a'))
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[2]>", line 1, in <module>
        sympow.modular_degree(EllipticCurve('11a'))###line 213:
    sage: sympow.modular_degree(EllipticCurve('11a'))
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree

... etc.
```



---

Comment by was created at 2010-06-07 04:38:21

Another failure that is caused by sympow not working:

```

sage -t  "devel/sage/sage/modular/abvar/abvar.py"           
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/modular/abvar/abvar.py", line 3305:
    sage: E.modular_degree()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_84[8]>", line 1, in <module>
        E.modular_degree()###line 3305:
    sage: E.modular_degree()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3311, in modular_degree
        m = sympow.modular_degree(self)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree
```



---

Comment by was created at 2010-06-07 04:39:11

Another failure:

```

sage -t  "devel/sage/sage/modular/hecke/submodule.py"       
**********************************************************************
File "/home/wstein/sage-4.4.3/devel/sage/sage/modular/hecke/submodule.py", line 497:
    sage: EllipticCurve('128a').congruence_number()
Exception raised:
    Traceback (most recent call last):
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/wstein/sage-4.4.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_16[19]>", line 1, in <module>
        EllipticCurve('128a').congruence_number()###line 497:
    sage: EllipticCurve('128a').congruence_number()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3404, in congruence_number
        m = self.modular_degree()
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/ell_rational_field.py", line 3311, in modular_degree
        m = sympow.modular_degree(self)
      File "/home/wstein/sage-4.4.3/local/lib/python/site-packages/sage/lfunctions/sympow.py", line 229, in modular_degree
        raise RuntimeError, "failed to compute modular degree"
    RuntimeError: failed to compute modular degree

```



---

Comment by retry created at 2010-07-20 10:28:15

Sympow doesn't work for me on Arch Linux, GCC 4.5.0

These doctests fail for me:

        sage -t  "devel/sage/sage/modular/hecke/submodule.py"

        sage -t  "devel/sage/sage/modular/abvar/abvar.py"

        sage -t  "devel/sage/sage/lfunctions/sympow.py"

        sage -t  "devel/sage/sage/schemes/elliptic_curves/ell_rational_field.py"


---

Comment by retry created at 2010-07-20 10:28:59

test.log with failures


---

Attachment

Replying to [comment:3 retry]:
> Sympow doesn't work for me on Arch Linux, GCC 4.5.0

That's now
 * Cygwin
 * Arch Linux
 * Solaris 10 on x86 #9703.
 * OpenSolaris on x86 

The pseudo C code is not valid C. It tried to return functions from those declared as void, so its not clear to me what the intended behaviour. 

I've tried to build this with the Sun C compiler, but it refuses to compile it. 

Dave


---

Comment by mpatel created at 2010-08-23 23:25:36

Ticket #9703, which I'll merge into 4.5.3.alpha2, should fix the problems here.  If someone can confirm that they do, I'll close this ticket.


---

Comment by mpatel created at 2010-08-25 21:22:03

Resolution: duplicate
