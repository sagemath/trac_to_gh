# Issue 1204: 2.8.13.alpha0: libs/cremona/constructor.py doctest failures

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-18 23:12:55

Assignee: failure


```
sage -t  devel/sage-main/sage/libs/cremona/constructor.py   **********************************************************************
File "constructor.py", line 42:
    sage: M = CremonaModularSymbols(-1)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: the level (= -1) must be a positive integer
Got:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[4]>", line 1, in <module>
        M = CremonaModularSymbols(-Integer(1))###line 42:
    sage: M = CremonaModularSymbols(-1)
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py", line 64, in CremonaModularSymbols
        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)
      File "homspace.pyx", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__
        raise ValueError, "the level (= %s) must be at least 2"%level
    ValueError: the level (= -1) must be at least 2
**********************************************************************
File "constructor.py", line 46:
    sage: M = CremonaModularSymbols(0)
Expected:
    Traceback (most recent call last):
    ...
    ValueError: the level (= 0) must be a positive integer
Got:
    Traceback (most recent call last):
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/doctest.py", line 1212, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[5]>", line 1, in <module>
        M = CremonaModularSymbols(Integer(0))###line 46:
    sage: M = CremonaModularSymbols(0)
      File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13.alpha0/local/lib/python2.5/site-packages/sage/libs/cremona/constructor.py", line 64, in CremonaModularSymbols
        return ModularSymbols(level=level, sign=sign, cuspidal=cuspidal, verbose=verbose)
      File "homspace.pyx", line 25, in sage.libs.cremona.homspace.ModularSymbols.__init__
        raise ValueError, "the level (= %s) must be at least 2"%level
    ValueError: the level (= 0) must be at least 2
**********************************************************************
```



---

Comment by mabshoff created at 2007-11-19 00:49:52


```
[01:37] <was_> In fact, now that I think about it, I think I changed the value error slightly.  Oops.
[01:37] <mabshoff> :)
[01:37] <was_> Feel free to just change the doctests in your code.  My mistake.
[01:37] <mabshoff> Ok, it was "ValueError: the level (= -1) must be at least 2" but it is now 
[01:38] <mabshoff> "ValueError: the level (= -1) must be a positive integer"
[01:43] <mabshoff> Ok, when I changed the Valueerror the doctest in sage -t  devel/sage-main/sage/libs/cremona/constructor.py passes
[01:43] <mabshoff> Does it really have to be \geq 2 or just postive?
[01:43] <was_> In theory the level must be >= 1.
[01:44] <was_> In Cremona's program, he didn't do level 1 correctly (it crashes), so it must be >= 2 for Cremona.
[01:44] <mabshoff> ok
[01:44] <was_> Level 1 just gives the 0 space anyways, so no problem.
```


Michael


---

Comment by mabshoff created at 2007-11-19 00:49:52

Resolution: fixed
