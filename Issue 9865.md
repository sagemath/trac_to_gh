# Issue 9865: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed

Issue created by migration from https://trac.sagemath.org/ticket/9866

Original creator: mpatel

Original creation time: 2010-09-07 07:27:15

Assignee: mvngu

CC:  mvngu

Minh Nguyen gets this error on a [GCC compile farm](http://gcc.gnu.org/wiki/CompileFarm) Debian 5.0 machine (gcc100.fsffrance.org, AMD Opteron(tm) Processor 252 `@` 2647.708 MHz) with a trial "final" 4.5.3 (essentially the same as 4.5.3.rc0):

```python
sage -t  -long "devel/sage/sage/schemes/elliptic_curves/heegner.py"
Exception RuntimeError: RuntimeError("Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.\n",) in <bound method Dokchitser.__del__ of Dokchitser L-series of conduct
or 389 and weight 2> ignored
**********************************************************************
File "/home/mvngu/sage-4.5.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6831:
    sage: E.heegner_sha_an(-7)                                  # long
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_234[12]>", line 1, in <module>
        E.heegner_sha_an(-Integer(7))                                  # long###line 6831:
    sage: E.heegner_sha_an(-7)                                  # long
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py", line 6878, in heegner_sha_an
        L_E = E.lseries().dokchitser(prec).derivative(1, rE)
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 135, in dokchitser
        gp = L.gp()
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/lfunctions/dokchitser.py", line 226, in gp
        g.read('computel.gp')
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 607, in read
        self.eval(self._read_in_file_command(filename))
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/gp.py", line 315, in _eval_line
        wait_for_prompt=wait_for_prompt)
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
        self._start()
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 458, in _start
        self.__name, cmd, self._install_hints())
    RuntimeError: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.

**********************************************************************
File "/home/mvngu/sage-4.5.3/devel/sage/sage/schemes/elliptic_curves/heegner.py", line 6839:
    sage: E.heegner_sha_an(-56)                                 # long
Exception raised:
    Traceback (most recent call last):
      File "/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/mvngu/sage-4.5.3/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_234[14]>", line 1, in <module>
        E.heegner_sha_an(-Integer(56))                                 # long###line 6839:
    sage: E.heegner_sha_an(-56)                                 # long
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py", line 6878, in heegner_sha_an
        L_E = E.lseries().dokchitser(prec).derivative(1, rE)
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py", line 135, in dokchitser
        gp = L.gp()
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/lfunctions/dokchitser.py", line 226, in gp
        g.read('computel.gp')
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 607, in read
        self.eval(self._read_in_file_command(filename))
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 983, in eval
        return '\n'.join([self._eval_line(L, **kwds) for L in code.split('\n') if L != ''])
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/gp.py", line 315, in _eval_line
        wait_for_prompt=wait_for_prompt)
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 637, in _eval_line
        self._start()
      File "/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py", line 458, in _start
        self.__name, cmd, self._install_hints())
    RuntimeError: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.

**********************************************************************
1 items had failures:
   2 of  18 in __main__.example_234
***Test Failed*** 2 failures.
Exception RuntimeError: RuntimeError('Unable to start pari',) in <bound method Dokchitser.__del__ of Dokchitser L-series of conductor 65 and weight 2> ignored
For whitespace errors, see the file /tmp/mvngu/dot_sage//tmp/.doctest_heegner.py
         [143.5 s]
```

[Here](http://wiki.sagemath.org/devel/BuildFarm/sage-4.5.3?action=AttachFile&do=get&target=gcc100.fsffrance.log.bz2) is the test log.

[Here](http://groups.google.com/group/sage-devel/browse_thread/thread/555cc03211ed9069/f98a20047d65261e#f98a20047d65261e) is the only mention I found of a similar message on sage-devel.


---

Comment by jdemeyer created at 2010-09-07 08:31:25

Is this error reproducible, does it happen every time?  What happens if you run `sage -gp` on that machine?


---

Comment by mpatel created at 2010-09-07 22:29:35

Changing priority from major to blocker.


---

Comment by mpatel created at 2010-09-19 06:54:56

Changing priority from blocker to major.


---

Comment by jdemeyer created at 2010-09-19 08:34:09

Changing status from new to needs_info.


---

Comment by jdemeyer created at 2011-04-06 08:01:32

Resolution: invalid


---

Comment by jdemeyer created at 2011-04-06 08:01:32

Nobody seems to care very much, so I'm closing this as invalid.


---

Comment by drkirkby created at 2011-04-07 21:12:12

I have had this result in a doctest failure onOpenSolaris on more than one occasion. But it's not every reproducible. The test fails, then passes when rerun. 

Sorry I did not comment earlier. 

Dave


---

Comment by jdemeyer created at 2011-04-08 08:22:39

One "solution" to track down further this problem is to change the exception handling code in `sage/interfaces/expect.py`.  This is the relevant code:

```
        try:
            if self.__remote_cleaner and self._server:
                c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
                os.system(c)
            self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
            if self._do_cleaner():
                cleaner.cleaner(self._expect.pid, cmd)

        except (ExceptionPexpect, pexpect.EOF, IndexError):
            self._expect = None
            self._session_number = BAD_SESSION
            failed_to_start.append(self.__name)
            raise RuntimeError, "Unable to start %s because the command '%s' failed.\n%s"%(
                self.__name, cmd, self._install_hints())
```

The problem is that we probably lose information by catching the exception and re-raising a different exception.  We only know that `gp` failed, but not for which reason.  I'm guessing something OS-related like not enough memory, but we don't know for sure.


---

Comment by drkirkby created at 2011-04-08 22:16:03

Replying to [comment:7 jdemeyer]:
> One "solution" to track down further this problem is to change the exception handling code in `sage/interfaces/expect.py`.  This is the relevant code:
> {{{
>         try:
>             if self.__remote_cleaner and self._server:
>                 c = 'sage-native-execute  ssh %s "nohup sage -cleaner"  &'%self._server
>                 os.system(c)
>             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)
>             if self._do_cleaner():
>                 cleaner.cleaner(self._expect.pid, cmd)
> 
>         except (ExceptionPexpect, pexpect.EOF, IndexError):
>             self._expect = None
>             self._session_number = BAD_SESSION
>             failed_to_start.append(self.__name)
>             raise RuntimeError, "Unable to start %s because the command '%s' failed.\n%s"%(
>                 self.__name, cmd, self._install_hints())
> }}}
> The problem is that we probably lose information by catching the exception and re-raising a different exception.  We only know that `gp` failed, but not for which reason.  I'm guessing something OS-related like not enough memory, but we don't know for sure.

I doubt it's a lack of memory. My machine has 12 GB RAM and I suspect 50-100 GB or so of swap. That said, others do use the machine, but I usually do check logs when I get doctest failures - that's why I wish the date+time of the doctests were recorded. 

I know it's not normal to reopen tickets, but since this one was closed only a few hours ago, with no releases of Sage since, would it be sensible to reopen this? The problem does still exist and on more than one platform

Dave


---

Comment by jdemeyer created at 2011-04-11 08:27:25

Resolution changed from invalid to 


---

Comment by jdemeyer created at 2011-04-11 08:27:25

Changing status from closed to new.


---

Comment by roed created at 2013-03-28 23:02:38

Changing assignee from mvngu to was.


---

Comment by roed created at 2013-03-28 23:02:38

Changing component from doctest to interfaces.
