# Issue 6900: Sage pexpect problems - suggestion to use upstream release

Issue created by migration from https://trac.sagemath.org/ticket/6900

Original creator: pcpa

Original creation time: 2009-09-07 04:32:43

Assignee: boothby

Keywords: pexpect

Since pexpect is a very important package, I would like to point one problem that happens when DOT_SAGE is set to a long pathname, causing the SaveWorkspace("/path/to/$DOT_SAGE/gap/workspace-ext");
command in interfaces/gap.py fail (and possibly others).

  Sample test case to reproduce the problem:

% mkdir -p /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage
<<make sure DOT_SAGE will point to that directory>>
% sage
<<exit sage>>
% ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/
README.txt
<<change DOT_SAGE to something like just /tmp/0123456789/>>
% sage
<<exit sage>>
% ls /tmp/0123456789/.sage/gap
README.txt  workspace-1328071335

  The problem is due to the command having more then 80 characters.

  Currently sage uses pexpect-2.0 (patchlevel 4). And this is also one special case in my rpm packages of sage, because if using the latest upstream, in my case:
% rpm -q python-pexpect
python-pexpect-2.4-1mdv2010.0
it works correctly in the terminal interface, but doesn't work correctly in the notebook interface.

  A quick and dirty way to test a newer pexpect would be:
% mkdir $HOME/tmp/sage-pexpect
% mv $SAGE_ROOT/lib/python/site-packages/{ANSI,FSM,pexpect,pxssh,screen}.py $HOME/tmp/sage-pexpect
% cp newer-python-pexpect/{ANSI,FSM,pexpect,pxssh,screen}.py $SAGE_ROOT/lib/python/site-packages
% sage
sage: notebook()

  After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.
A screenshot of the problem, that happens the first time a background process is started is:
http://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg
but, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.

  Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)


---

Comment by pcpa created at 2009-09-08 14:17:39

Replying to [ticket:6900 pcpa]:
[Sorry for replying to myself]
>   After starting the notebook, and using a newer pexpect, try some command that causes a background processes to be created, like the first singular example in the tutorial.
> A screenshot of the problem, that happens the first time a background process is started is:
> http://img134.imageshack.us/img134/557/sagewithnewerpexpect1.jpg
> but, as also shown in the screenshot, in subsequent evaluations, it works correctly in the notebook.
> 
>   Since it always works correct in the terminal interface of sage, I suspect it is an issue in the notebook/worksheet code. And in that case, it actually may be a different way to debug problems in the sage pexpect interface (also a suggestion :-)

  For people familiar with the notebook code, I think what may be also a good hint as to what may be wrong is that the extra noise in the output is not "really noise", but the "dancing" / and \ characters that go to the browser titlebar.


---

Comment by aapitzsch created at 2014-08-18 19:11:53

Changing status from new to needs_review.


---

Comment by aapitzsch created at 2014-08-18 19:11:53

I cannot reproduce the problem.


---

Comment by kcrisman created at 2014-09-18 03:05:21

You've got to do something with GAP, of course... but I agree that this seems to not be an issue now.

```
$ ls /tmp/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/0123456789/.sage/gap/
README.txt                     workspace-8276014924322680366

$ ls /tmp/0123456789/.sage/gap/
README.txt			workspace-8276014924322680366
```



---

Comment by kcrisman created at 2014-09-18 03:05:21

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2014-09-18 17:58:35

Resolution: worksforme
