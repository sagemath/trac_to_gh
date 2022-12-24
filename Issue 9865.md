# Issue 9865: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed

archive/issues_009865.json:
```json
{
    "body": "Assignee: mvngu\n\nCC:  mvngu\n\nMinh Nguyen gets this error on a [GCC compile farm](http://gcc.gnu.org/wiki/CompileFarm) Debian 5.0 machine (gcc100.fsffrance.org, AMD Opteron(tm) Processor 252 `@` 2647.708 MHz) with a trial \"final\" 4.5.3 (essentially the same as 4.5.3.rc0):\n\n```python\nsage -t  -long \"devel/sage/sage/schemes/elliptic_curves/heegner.py\"\nException RuntimeError: RuntimeError(\"Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.\\n\",) in <bound method Dokchitser.__del__ of Dokchitser L-series of conduct\nor 389 and weight 2> ignored\n**********************************************************************\nFile \"/home/mvngu/sage-4.5.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6831:\n    sage: E.heegner_sha_an(-7)                                  # long\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_234[12]>\", line 1, in <module>\n        E.heegner_sha_an(-Integer(7))                                  # long###line 6831:\n    sage: E.heegner_sha_an(-7)                                  # long\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py\", line 6878, in heegner_sha_an\n        L_E = E.lseries().dokchitser(prec).derivative(1, rE)\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py\", line 135, in dokchitser\n        gp = L.gp()\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/lfunctions/dokchitser.py\", line 226, in gp\n        g.read('computel.gp')\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 607, in read\n        self.eval(self._read_in_file_command(filename))\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 983, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/gp.py\", line 315, in _eval_line\n        wait_for_prompt=wait_for_prompt)\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 637, in _eval_line\n        self._start()\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 458, in _start\n        self.__name, cmd, self._install_hints())\n    RuntimeError: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.\n\n**********************************************************************\nFile \"/home/mvngu/sage-4.5.3/devel/sage/sage/schemes/elliptic_curves/heegner.py\", line 6839:\n    sage: E.heegner_sha_an(-56)                                 # long\nException raised:\n    Traceback (most recent call last):\n      File \"/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/mvngu/sage-4.5.3/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/mvngu/sage-4.5.3/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_234[14]>\", line 1, in <module>\n        E.heegner_sha_an(-Integer(56))                                 # long###line 6839:\n    sage: E.heegner_sha_an(-56)                                 # long\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/heegner.py\", line 6878, in heegner_sha_an\n        L_E = E.lseries().dokchitser(prec).derivative(1, rE)\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/schemes/elliptic_curves/lseries_ell.py\", line 135, in dokchitser\n        gp = L.gp()\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/lfunctions/dokchitser.py\", line 226, in gp\n        g.read('computel.gp')\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 607, in read\n        self.eval(self._read_in_file_command(filename))\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 983, in eval\n        return '\\n'.join([self._eval_line(L, **kwds) for L in code.split('\\n') if L != ''])\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/gp.py\", line 315, in _eval_line\n        wait_for_prompt=wait_for_prompt)\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 637, in _eval_line\n        self._start()\n      File \"/home/mvngu/sage-4.5.3/local/lib/python/site-packages/sage/interfaces/expect.py\", line 458, in _start\n        self.__name, cmd, self._install_hints())\n    RuntimeError: Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed.\n\n**********************************************************************\n1 items had failures:\n   2 of  18 in __main__.example_234\n***Test Failed*** 2 failures.\nException RuntimeError: RuntimeError('Unable to start pari',) in <bound method Dokchitser.__del__ of Dokchitser L-series of conductor 65 and weight 2> ignored\nFor whitespace errors, see the file /tmp/mvngu/dot_sage//tmp/.doctest_heegner.py\n         [143.5 s]\n```\n\n[Here](http://wiki.sagemath.org/devel/BuildFarm/sage-4.5.3?action=AttachFile&do=get&target=gcc100.fsffrance.log.bz2) is the test log.\n\n[Here](http://groups.google.com/group/sage-devel/browse_thread/thread/555cc03211ed9069/f98a20047d65261e#f98a20047d65261e) is the only mention I found of a similar message on sage-devel.\n\nIssue created by migration from https://trac.sagemath.org/ticket/9866\n\n",
    "created_at": "2010-09-07T07:27:15Z",
    "labels": [
        "doctest",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Unable to start pari because the command 'gp --emacs --fast --quiet --stacksize 10000000' failed",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9865",
    "user": "mpatel"
}
```
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

Issue created by migration from https://trac.sagemath.org/ticket/9866





---

archive/issue_comments_097468.json:
```json
{
    "body": "Is this error reproducible, does it happen every time?  What happens if you run `sage -gp` on that machine?",
    "created_at": "2010-09-07T08:31:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97468",
    "user": "jdemeyer"
}
```

Is this error reproducible, does it happen every time?  What happens if you run `sage -gp` on that machine?



---

archive/issue_comments_097469.json:
```json
{
    "body": "Changing priority from major to blocker.",
    "created_at": "2010-09-07T22:29:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97469",
    "user": "mpatel"
}
```

Changing priority from major to blocker.



---

archive/issue_comments_097470.json:
```json
{
    "body": "Changing priority from blocker to major.",
    "created_at": "2010-09-19T06:54:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97470",
    "user": "mpatel"
}
```

Changing priority from blocker to major.



---

archive/issue_comments_097471.json:
```json
{
    "body": "Changing status from new to needs_info.",
    "created_at": "2010-09-19T08:34:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97471",
    "user": "jdemeyer"
}
```

Changing status from new to needs_info.



---

archive/issue_comments_097472.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2011-04-06T08:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97472",
    "user": "jdemeyer"
}
```

Resolution: invalid



---

archive/issue_comments_097473.json:
```json
{
    "body": "Nobody seems to care very much, so I'm closing this as invalid.",
    "created_at": "2011-04-06T08:01:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97473",
    "user": "jdemeyer"
}
```

Nobody seems to care very much, so I'm closing this as invalid.



---

archive/issue_comments_097474.json:
```json
{
    "body": "I have had this result in a doctest failure onOpenSolaris on more than one occasion. But it's not every reproducible. The test fails, then passes when rerun. \n\nSorry I did not comment earlier. \n\nDave",
    "created_at": "2011-04-07T21:12:12Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97474",
    "user": "drkirkby"
}
```

I have had this result in a doctest failure onOpenSolaris on more than one occasion. But it's not every reproducible. The test fails, then passes when rerun. 

Sorry I did not comment earlier. 

Dave



---

archive/issue_comments_097475.json:
```json
{
    "body": "One \"solution\" to track down further this problem is to change the exception handling code in `sage/interfaces/expect.py`.  This is the relevant code:\n\n```\n        try:\n            if self.__remote_cleaner and self._server:\n                c = 'sage-native-execute  ssh %s \"nohup sage -cleaner\"  &'%self._server\n                os.system(c)\n            self._expect = pexpect.spawn(cmd, logfile=self.__logfile)\n            if self._do_cleaner():\n                cleaner.cleaner(self._expect.pid, cmd)\n\n        except (ExceptionPexpect, pexpect.EOF, IndexError):\n            self._expect = None\n            self._session_number = BAD_SESSION\n            failed_to_start.append(self.__name)\n            raise RuntimeError, \"Unable to start %s because the command '%s' failed.\\n%s\"%(\n                self.__name, cmd, self._install_hints())\n```\n\nThe problem is that we probably lose information by catching the exception and re-raising a different exception.  We only know that `gp` failed, but not for which reason.  I'm guessing something OS-related like not enough memory, but we don't know for sure.",
    "created_at": "2011-04-08T08:22:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97475",
    "user": "jdemeyer"
}
```

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

archive/issue_comments_097476.json:
```json
{
    "body": "Replying to [comment:7 jdemeyer]:\n> One \"solution\" to track down further this problem is to change the exception handling code in `sage/interfaces/expect.py`.  This is the relevant code:\n> {{{\n>         try:\n>             if self.__remote_cleaner and self._server:\n>                 c = 'sage-native-execute  ssh %s \"nohup sage -cleaner\"  &'%self._server\n>                 os.system(c)\n>             self._expect = pexpect.spawn(cmd, logfile=self.__logfile)\n>             if self._do_cleaner():\n>                 cleaner.cleaner(self._expect.pid, cmd)\n> \n>         except (ExceptionPexpect, pexpect.EOF, IndexError):\n>             self._expect = None\n>             self._session_number = BAD_SESSION\n>             failed_to_start.append(self.__name)\n>             raise RuntimeError, \"Unable to start %s because the command '%s' failed.\\n%s\"%(\n>                 self.__name, cmd, self._install_hints())\n> }}}\n> The problem is that we probably lose information by catching the exception and re-raising a different exception.  We only know that `gp` failed, but not for which reason.  I'm guessing something OS-related like not enough memory, but we don't know for sure.\n\nI doubt it's a lack of memory. My machine has 12 GB RAM and I suspect 50-100 GB or so of swap. That said, others do use the machine, but I usually do check logs when I get doctest failures - that's why I wish the date+time of the doctests were recorded. \n\nI know it's not normal to reopen tickets, but since this one was closed only a few hours ago, with no releases of Sage since, would it be sensible to reopen this? The problem does still exist and on more than one platform\n\nDave",
    "created_at": "2011-04-08T22:16:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97476",
    "user": "drkirkby"
}
```

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

archive/issue_comments_097477.json:
```json
{
    "body": "Resolution changed from invalid to ",
    "created_at": "2011-04-11T08:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97477",
    "user": "jdemeyer"
}
```

Resolution changed from invalid to 



---

archive/issue_comments_097478.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2011-04-11T08:27:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97478",
    "user": "jdemeyer"
}
```

Changing status from closed to new.



---

archive/issue_comments_097479.json:
```json
{
    "body": "Changing assignee from mvngu to was.",
    "created_at": "2013-03-28T23:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97479",
    "user": "roed"
}
```

Changing assignee from mvngu to was.



---

archive/issue_comments_097480.json:
```json
{
    "body": "Changing component from doctest to interfaces.",
    "created_at": "2013-03-28T23:02:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9865",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9865#issuecomment-97480",
    "user": "roed"
}
```

Changing component from doctest to interfaces.
