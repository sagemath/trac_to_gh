# Issue 4564: [with patch, needs review] implement long long -> mpz_t

Issue created by migration from https://trac.sagemath.org/ticket/4564

Original creator: robertwb

Original creation time: 2008-11-20 13:02:49

Assignee: somebody

For some reason, there is no function to do this shipped with gmp...


---

Attachment

So the code here looks good. I even pulled out my old G4 and tested it on a big-endian machine, and everything worked fine.

I do have one question, though: doesn't the `mpz_set_longlong` belong somewhere more generic than `integer.pyx`? I would have put it somewhere in libcsage. Of course, then it wouldn't be so easy to raise the exception ...


---

Comment by robertwb created at 2008-11-20 23:11:29

Yeah, probably does belong in libcsage... I'm going to be moving stuff around when I split up cdefs anyways. I was just concentrating more on divisors at that point ;).


---

Comment by craigcitro created at 2008-11-20 23:12:40

That works. Let's merge this now, then, and worry about it later. Maybe open a ticket for the cdefs cleanup and mention this, so we don't forget?


---

Comment by robertwb created at 2008-11-20 23:15:19

See #846. I'm planning on doing that today.


---

Comment by mabshoff created at 2008-11-21 05:47:22

I am seeing a doctest failure here:

```
sage -t -long devel/sage/sage/rings/integer.pyx             
**********************************************************************
File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/devel/sage/sage/rings/integer.pyx", line 199:
    sage: sage: _test_mpz_set_longlong(100000000000)
Exception raised:
    Traceback (most recent call last):
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/scratch/mabshoff/release-cycle/sage-3.2.1.alpha0/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[6]>", line 1
         sage: _test_mpz_set_longlong(Integer(100000000000))###line 199:
    sage: sage: _test_mpz_set_longlong(100000000000)
          ^
     SyntaxError: invalid syntax
**********************************************************************
1 items had failures:
```


I guess this is caused by an extra "sage: " in that line. I am editing the patch to fix this.

Cheers,

Michael


---

Comment by mabshoff created at 2008-11-21 05:54:24

Merged in Sage 3.2.1.alpha0


---

Comment by mabshoff created at 2008-11-21 05:54:24

Resolution: fixed
