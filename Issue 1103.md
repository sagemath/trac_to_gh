# Issue 1103: 2.8.12.alpha1: doctest failure in schemes/elliptic_curves/lseries_ell.py

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-05 00:39:57

Assignee: failure


```
sage -t  devel/sage-main/sage/schemes/elliptic_curves/lseries_ell.py********************************************************
**************
File "lseries_ell.py", line 112:
    sage: L = e.Lseries().dokchitser(15)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError:   *** vector: impossible assignment I-->S
    Unable to create L-series, due to precision or other limits in PARI.
Got:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        L = e.Lseries().dokchitser(Integer(15))###line 112:
    sage: L = e.Lseries().dokchitser(15)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/schemes/elliptic_curves/lseries_ell
.py", line 141, in dokchitser
        max_asymp_coeffs=max_asymp_coeffs)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py", line 269
, in init_coeffs
        self._gp_eval('initLdata("%s", %s)'%(v, cutoff))
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py", line 208
, in _gp_eval
        t = self.gp().eval(s)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 707, in
 eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 208, in _ev
al_line
        return self._eval_line(line)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 208, in _ev
al_line
        return self._eval_line(line)
<SNIP>
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 204, in _ev
al_line
        wait_for_prompt=wait_for_prompt)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 629, in
 _eval_line
        E.expect(self._prompt)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 911, in expect
        compiled_pattern_list = self.compile_pattern_list(pattern)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/site-packages/pexpect.py", line 843, in compile_patter
n_list
        compiled_pattern_list.append(re.compile(p, re.DOTALL))
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/re.py", line 180, in compile
        return _compile(pattern, flags)
      File "/tmp/Work-mabshoff/sage-2.8.12.alpha1/local/lib/python2.5/re.py", line 222, in _compile
        p = _cache.get(cachekey)
    RuntimeError: maximum recursion depth exceeded in cmp
**********************************************************************
```



---

Comment by was created at 2007-11-05 13:19:29

Changing status from new to assigned.


---

Comment by was created at 2007-11-05 13:19:29

This was caused by me fixing another trac bug on osx, then putting in a doctest to expose it.  Evidently I only fixed the bug on osx, since it's still evident in 64-bit linux.


---

Comment by was created at 2007-11-05 13:19:29

Changing assignee from failure to was.


---

Comment by cwitty created at 2007-11-06 02:58:17

The stack overflow message is caused by a bug in the gp interface (#1109).  However, fixing that does not make this doctest pass.

When I turn on logging (by changing "logfile=None" to "logfile='/tmp/dklog'" on line 194 of dokchitser.py), I can see that gp behaves quite differently on 32-bit linux and 64-bit linux.

On 64-bit linux, the logfile includes this chunk:

```
? initLdata("a(k)", 1.000)\q
\q

ata("a(k)", 1.000)

  *** vector: the PARI stack overflows !

  current stack size: 10000000 (9.537 Mbytes)

  [hint] you can increase GP stack with allocatemem()

```

(after this, the interface then keeps doubling the available memory, and gp keeps saying out of memory, until gp refuses to double the memory any more at 4.8 GB).

The corresponding section in the 32-bit linux logfile looks like this:

```
? initLdata("a(k)", 1.000)
initLdata("a(k)", 1.000)
\q
\q

vector: impossible assignment I-->S

? \q
\q

```

followed by a whole bunch of NUL characters.

Having NUL characters show up in the logfile seems like a bad sign; it makes me wonder if something is going wrong inside gp on 32-bit linux, and maybe the 64-bit linux result is actually the correct one.

I'm not planning to continue looking at this; it seems like a job for somebody familiar with gp and the dokchitser code.


---

Comment by cwitty created at 2007-11-06 03:58:56

After applying the second patch in #1109, the doctest failure on 64-bit linux changes to this:

```
sage -t  devel/sage-sage-test/sage/schemes/elliptic_curves/lseries_ell.py**********************************************************************
File "lseries_ell.py", line 112:
    sage: L = e.Lseries().dokchitser(15)
Expected:
    Traceback (most recent call last):
    ...
    RuntimeError:   *** vector: impossible assignment I-->S
    Unable to create L-series, due to precision or other limits in PARI.
Got:
    Traceback (most recent call last):
      File "/home/cwitty/sage/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_6[4]>", line 1, in <module>
        L = e.Lseries().dokchitser(Integer(15))###line 112:
    sage: L = e.Lseries().dokchitser(15)
      File "/home/cwitty/sage/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 141, in dokchitser
        max_asymp_coeffs=max_asymp_coeffs)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py", line 269, in init_coeffs
        self._gp_eval('initLdata("%s", %s)'%(v, cutoff))
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/lfunctions/dokchitser.py", line 208, in _gp_eval
        t = self.gp().eval(s)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/expect.py", line 710, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 210, in _eval_line
        return self._eval_line(line)
      File "/home/cwitty/sage/local/lib/python2.5/site-packages/sage/interfaces/gp.py", line 209, in _eval_line
        raise RuntimeError, a
    RuntimeError:   *** vector: the PARI stack overflows !
      current stack size: 2560000000 (2441.406 Mbytes)
      [hint] you can increase GP stack with allocatemem()
    <BLANKLINE>
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_6
***Test Failed*** 1 failures.
For whitespace errors, see the file .doctest_lseries_ell.py
         [7.7 s]
exit code: 256
 
----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage-sage-test/sage/schemes/elliptic_curves/lseries_ell.py
Total time for all tests: 7.7 seconds
```



---

Comment by was created at 2007-11-07 05:18:19

Resolution: fixed
