# Issue 9536: python setup.py picks prefix from ~/.pydistutils.cfg

Issue created by migration from https://trac.sagemath.org/ticket/9536

Original creator: AlexanderDreyer

Original creation time: 2010-07-18 14:07:14

Assignee: AlexGhitza

CC:  jdemeyer embray leif fbissey vbraun

Hi,
several packages do use `python setup.py`. This picks up the customized settings from ~/.pydistutils.cfg. This is bad, because it overrides the prefix setting. 

For sage-main, I'll attach a patch: `setup.cfg` in the corresponding directory overrides the usere settings. Maybe there's a global solution.

Regards,
  Alexander Dreyer


---

Comment by AlexanderDreyer created at 2010-07-18 14:09:00

Patch for sage-main


---

Comment by AlexanderDreyer created at 2010-07-18 14:46:44

Changing assignee from AlexGhitza to AlexanderDreyer.


---

Attachment


---

Comment by AlexanderDreyer created at 2010-07-18 15:08:26

The following packages from the distribution use setup.py and may be affected:

```
zodb3-3.7.0.p4
scipy_sandbox-20071020.p5
pexpect-2.0.p4
sqlalchemy-0.5.8
glpk-4.44
mpmath-0.15
pil-1.1.6.p2
mercurial-1.3.1.p2
pycrypto-2.0.1.p5
mpir-1.2.2.p1
weave-0.4.9.p0
sympy-0.6.4.p0
scons-1.2.0
numpy-1.3.0.p3
gdmodule-0.56.p7
sagetex-2.2.5
sage-4.5
matplotlib-0.99.3
sage_scripts-4.5
setuptools-0.6c9.p0
python-2.6.4.p9
python_gnutls-1.1.4.p7
sagenb-0.8.1
networkx-1.0.1
jinja-1.2.p0
cython-0.12.1
pygments-0.11.1.p0
scipy-0.7.p5
cvxopt-0.9.p8
jinja2-2.1.1.p0
sphinx-0.6.3.p4
docutils-0.5.p0
twisted-9.0.p2
ipython-0.9.1.p0
moin-1.9.1.p1
```


The following already have setup.cfg, but it may not have the prefix definition:

```
zodb3-3.7.0.p4
sqlalchemy-0.5.8
scons-1.2.0
matplotlib-0.99.3
setuptools-0.6c9.p0
sagenb-0.8.1
networkx-1.0.1
jinja-1.2.p0
pygments-0.11.1.p0
jinja2-2.1.1.p0
sphinx-0.6.3.p4
twisted-9.0.p2
moin-1.9.1.p1
```



---

Comment by PolyBoRi created at 2010-07-19 10:07:42

Hi!
I am not an export for that for that, but did you read
http://docs.python.org/install/#location-and-names-of-config-files
There seems to be some options:
–no-user-cfg

Cheers,
Michael


---

Comment by AlexanderDreyer created at 2010-07-19 10:13:22

Hi Michael,
indeed, that's a better solution. But both have the problem, that 30+ packages would have to be fixed, and it might be forgotten in the future. (Maybe there some monkey patch for distutils, that all of it can be overwritten by the environment.)

Best regards,
  Alexander


---

Comment by PolyBoRi created at 2010-07-19 10:23:03

maybe, I did not try (just read the docs):
http://docs.python.org/install/#inst-config-files

create system distutils.cfg


```
[global]
no-user-cfg=1
```



---

Comment by AlexanderDreyer created at 2010-07-19 15:11:54

Hi,
unfortunately, this is a Python 2.7 feature and it does not support no-user-cfg in distutils.cfg :-(

Regards,
  Alexander


---

Comment by AlexanderDreyer created at 2010-07-19 20:46:45

patch for sage/spkg/base/sage-env sage/local/bin/sage-env (needs python 2.6.4.p10)


---

Attachment

Hi,
I backported the handling of setup.py --no-user-cfg from  Python 2.7 to Python 2.6.4 and also added the handling of the environment variable `DISTUTILS_NO_USER_CFG` to python's distutils. 

The new spkg can be found here: 
http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg

The last patch adds this variable to `sage-env`.

Regards,
  Alexander


---

Comment by AlexanderDreyer created at 2010-07-19 20:50:41

Changing status from new to needs_review.


---

Comment by AlexanderDreyer created at 2010-07-19 21:16:27

Reported upstream:
http://bugs.python.org/issue9309


---

Comment by AlexanderDreyer created at 2010-07-20 09:41:42

Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)


---

Comment by drkirkby created at 2010-07-21 11:49:06

Replying to [comment:9 AlexanderDreyer]:
> Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)
You should also create patches/ACKS.txt.diff as a unified diff file. Although its fairly obvious you can recreate that now, that will not be the case if Python source code is updated. 

Would a simpler solution not be for sage-env to set this variable and export it? I don't know much about python, so can't review this myself. 

Dave


---

Comment by AlexanderDreyer created at 2010-07-21 15:45:42

Maybe a misunderstanding: the patch of python is necessary  to fix that issue anyway. (This first variant didn't work, if the environment variable was _not_ set.)


---

Attachment

Adding handling of environment variable DISTUTILS_NO_USER_CFG to python's distutils


---

Comment by AlexanderDreyer created at 2010-07-21 16:03:40

I've added ACKS.txt.patch to the spkg.


---

Comment by AlexanderDreyer created at 2010-07-29 14:02:15

Changing component from algebra to build.


---

Comment by AlexanderDreyer created at 2010-09-30 07:23:45

The python community does not like the idea of adding an environment variable, see:
http://bugs.python.org/issue9309


---

Comment by jdemeyer created at 2012-07-27 20:42:35

Please fill in your real name as Author.


---

Comment by kcrisman created at 2015-05-29 02:20:07

Changing status from needs_review to needs_work.


---

Comment by kcrisman created at 2015-05-29 02:20:07

Needs a branch.  And we have updated Python.  And probably other reasons it isn't ready yet.  (Or conceivably has been solved in the meantime?)


---

Comment by mkoeppe created at 2016-10-31 06:33:40

New commits:


---

Comment by mkoeppe created at 2016-10-31 06:33:40

Changing status from needs_work to needs_review.


---

Comment by embray created at 2016-11-07 13:29:40

Changing status from needs_review to positive_review.


---

Comment by embray created at 2016-11-07 13:29:40

This looks like the right approach, thanks.


---

Comment by vbraun created at 2016-11-08 23:42:27

Resolution: fixed


---

Comment by vbraun created at 2016-11-09 20:47:14

Resolution changed from fixed to 


---

Comment by vbraun created at 2016-11-09 20:47:14

Changing status from closed to new.


---

Comment by vbraun created at 2016-11-09 20:47:14

Prevents pyzmq from building...


---

Comment by vbraun created at 2016-11-09 20:48:05


```
  Source in /tmp/pip-mTg5Xg-build has version 16.0.0, which satisfies requirement pyzmq==16.0.0 from file:///mnt/disk/home/release/Sage/local/var/tmp/sage/build/pyzmq-16.0.0/src
Installing collected packages: pyzmq
  Running setup.py install for pyzmq: started
    Running command /mnt/disk/home/release/Sage/local/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile
    running configure
    error: error in command line: command 'Configure' has no such option 'no_user_cfg'
    Running setup.py install for pyzmq: finished with status 'error'
Cleaning up...
  Removing source in /tmp/pip-mTg5Xg-build
Command "/mnt/disk/home/release/Sage/local/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-mTg5Xg-build/
Exception information:
Traceback (most recent call last):
  File "/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/basecommand.py", line 215, in main
    status = self.run(options, args)
  File "/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/commands/install.py", line 317, in run
    prefix=options.prefix_path,
  File "/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_set.py", line 742, in install
    **kwargs
  File "/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_install.py", line 880, in install
    spinner=spinner,
  File "/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/utils/__init__.py", line 718, in call_subprocess
    % (command_desc, proc.returncode, cwd))
InstallationError: Command "/mnt/disk/home/release/Sage/local/bin/python -u -c "import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\r\n', '\n'), __file__, 'exec'))" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile" failed with error code 1 in /tmp/pip-mTg5Xg-build/
```



---

Comment by mkoeppe created at 2016-11-09 21:55:17

I've created an upstream issue for this:
 https://github.com/zeromq/pyzmq/issues/937


---

Comment by embray created at 2016-11-10 11:42:15

That's annoying.  For now we should probably remove pip install from pyzmq.


---

Comment by mkoeppe created at 2016-11-10 18:11:49

Upstream pyzmq reports that it works with pip 9.0.1, setuptools 28.8.0.

Let's try with upgrading these packages. #21835 does the upgrade of pip to 9.0.0...


---

Comment by mkoeppe created at 2016-11-10 18:56:35

Upgrading setuptools to 28.8.0 does not fix the pyzmq install.

I'll wait for the pip upgrade.


---

Comment by git created at 2016-11-10 22:04:36

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mkoeppe created at 2016-11-11 03:06:26

Here's a fix for our `pyzmq` `spkg-install`, with help from upstream.


---

Comment by mkoeppe created at 2016-11-11 03:06:26

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2016-11-11 16:39:05

Just a comment: it would make sense to use `$PIP_INSTALL` for a few more packages where no extra options are needed: `fpylll`, `gambit`, `sagenb`, `sagetex`.


---

Comment by mkoeppe created at 2016-11-11 19:53:18

I agree, but that should be on a different ticket. I've created #21864 for this.


---

Comment by mkoeppe created at 2016-11-15 01:54:41

Needs review.


---

Comment by git created at 2016-12-29 01:07:50

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by mkoeppe created at 2016-12-29 01:08:30

Rebased, needs review.


---

Comment by mkoeppe created at 2017-01-16 18:35:50

ping?


---

Comment by embray created at 2017-01-17 12:06:23

The issue with `--global-option` and `--no-user-cfg` still seems odd to me. I think that should be considered a bug in pip.  But I guess there's nothing to be done for now.


---

Comment by embray created at 2017-01-17 12:06:23

Changing status from needs_review to positive_review.


---

Comment by vbraun created at 2017-01-21 16:35:21

Resolution: fixed
