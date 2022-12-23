# Issue 9536: python setup.py picks prefix from ~/.pydistutils.cfg

archive/issues_009536.json:
```json
{
    "body": "Assignee: AlexGhitza\n\nCC:  jdemeyer embray leif fbissey vbraun\n\nHi,\nseveral packages do use `python setup.py`. This picks up the customized settings from ~/.pydistutils.cfg. This is bad, because it overrides the prefix setting. \n\nFor sage-main, I'll attach a patch: `setup.cfg` in the corresponding directory overrides the usere settings. Maybe there's a global solution.\n\nRegards,\n  Alexander Dreyer\n\nIssue created by migration from https://trac.sagemath.org/ticket/9536\n\n",
    "created_at": "2010-07-18T14:07:14Z",
    "labels": [
        "algebra",
        "major",
        "bug"
    ],
    "title": "python setup.py picks prefix from ~/.pydistutils.cfg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9536",
    "user": "AlexanderDreyer"
}
```
Assignee: AlexGhitza

CC:  jdemeyer embray leif fbissey vbraun

Hi,
several packages do use `python setup.py`. This picks up the customized settings from ~/.pydistutils.cfg. This is bad, because it overrides the prefix setting. 

For sage-main, I'll attach a patch: `setup.cfg` in the corresponding directory overrides the usere settings. Maybe there's a global solution.

Regards,
  Alexander Dreyer

Issue created by migration from https://trac.sagemath.org/ticket/9536





---

archive/issue_comments_091846.json:
```json
{
    "body": "Patch for sage-main",
    "created_at": "2010-07-18T14:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91846",
    "user": "AlexanderDreyer"
}
```

Patch for sage-main



---

archive/issue_comments_091847.json:
```json
{
    "body": "Changing assignee from AlexGhitza to AlexanderDreyer.",
    "created_at": "2010-07-18T14:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91847",
    "user": "AlexanderDreyer"
}
```

Changing assignee from AlexGhitza to AlexanderDreyer.



---

archive/issue_comments_091848.json:
```json
{
    "body": "Attachment",
    "created_at": "2010-07-18T14:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91848",
    "user": "AlexanderDreyer"
}
```

Attachment



---

archive/issue_comments_091849.json:
```json
{
    "body": "The following packages from the distribution use setup.py and may be affected:\n\n```\nzodb3-3.7.0.p4\nscipy_sandbox-20071020.p5\npexpect-2.0.p4\nsqlalchemy-0.5.8\nglpk-4.44\nmpmath-0.15\npil-1.1.6.p2\nmercurial-1.3.1.p2\npycrypto-2.0.1.p5\nmpir-1.2.2.p1\nweave-0.4.9.p0\nsympy-0.6.4.p0\nscons-1.2.0\nnumpy-1.3.0.p3\ngdmodule-0.56.p7\nsagetex-2.2.5\nsage-4.5\nmatplotlib-0.99.3\nsage_scripts-4.5\nsetuptools-0.6c9.p0\npython-2.6.4.p9\npython_gnutls-1.1.4.p7\nsagenb-0.8.1\nnetworkx-1.0.1\njinja-1.2.p0\ncython-0.12.1\npygments-0.11.1.p0\nscipy-0.7.p5\ncvxopt-0.9.p8\njinja2-2.1.1.p0\nsphinx-0.6.3.p4\ndocutils-0.5.p0\ntwisted-9.0.p2\nipython-0.9.1.p0\nmoin-1.9.1.p1\n```\n\n\nThe following already have setup.cfg, but it may not have the prefix definition:\n\n```\nzodb3-3.7.0.p4\nsqlalchemy-0.5.8\nscons-1.2.0\nmatplotlib-0.99.3\nsetuptools-0.6c9.p0\nsagenb-0.8.1\nnetworkx-1.0.1\njinja-1.2.p0\npygments-0.11.1.p0\njinja2-2.1.1.p0\nsphinx-0.6.3.p4\ntwisted-9.0.p2\nmoin-1.9.1.p1\n```\n",
    "created_at": "2010-07-18T15:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91849",
    "user": "AlexanderDreyer"
}
```

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

archive/issue_comments_091850.json:
```json
{
    "body": "Hi!\nI am not an export for that for that, but did you read\nhttp://docs.python.org/install/#location-and-names-of-config-files\nThere seems to be some options:\n\u2013no-user-cfg\n\nCheers,\nMichael",
    "created_at": "2010-07-19T10:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91850",
    "user": "PolyBoRi"
}
```

Hi!
I am not an export for that for that, but did you read
http://docs.python.org/install/#location-and-names-of-config-files
There seems to be some options:
–no-user-cfg

Cheers,
Michael



---

archive/issue_comments_091851.json:
```json
{
    "body": "Hi Michael,\nindeed, that's a better solution. But both have the problem, that 30+ packages would have to be fixed, and it might be forgotten in the future. (Maybe there some monkey patch for distutils, that all of it can be overwritten by the environment.)\n\nBest regards,\n  Alexander",
    "created_at": "2010-07-19T10:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91851",
    "user": "AlexanderDreyer"
}
```

Hi Michael,
indeed, that's a better solution. But both have the problem, that 30+ packages would have to be fixed, and it might be forgotten in the future. (Maybe there some monkey patch for distutils, that all of it can be overwritten by the environment.)

Best regards,
  Alexander



---

archive/issue_comments_091852.json:
```json
{
    "body": "maybe, I did not try (just read the docs):\nhttp://docs.python.org/install/#inst-config-files\n\ncreate system distutils.cfg\n\n\n```\n[global]\nno-user-cfg=1\n```\n",
    "created_at": "2010-07-19T10:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91852",
    "user": "PolyBoRi"
}
```

maybe, I did not try (just read the docs):
http://docs.python.org/install/#inst-config-files

create system distutils.cfg


```
[global]
no-user-cfg=1
```




---

archive/issue_comments_091853.json:
```json
{
    "body": "Hi,\nunfortunately, this is a Python 2.7 feature and it does not support no-user-cfg in distutils.cfg :-(\n\nRegards,\n  Alexander",
    "created_at": "2010-07-19T15:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91853",
    "user": "AlexanderDreyer"
}
```

Hi,
unfortunately, this is a Python 2.7 feature and it does not support no-user-cfg in distutils.cfg :-(

Regards,
  Alexander



---

archive/issue_comments_091854.json:
```json
{
    "body": "patch for sage/spkg/base/sage-env sage/local/bin/sage-env (needs python 2.6.4.p10)",
    "created_at": "2010-07-19T20:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91854",
    "user": "AlexanderDreyer"
}
```

patch for sage/spkg/base/sage-env sage/local/bin/sage-env (needs python 2.6.4.p10)



---

archive/issue_comments_091855.json:
```json
{
    "body": "Attachment\n\nHi,\nI backported the handling of setup.py --no-user-cfg from  Python 2.7 to Python 2.6.4 and also added the handling of the environment variable `DISTUTILS_NO_USER_CFG` to python's distutils. \n\nThe new spkg can be found here: \nhttp://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg\n\nThe last patch adds this variable to `sage-env`.\n\nRegards,\n  Alexander",
    "created_at": "2010-07-19T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91855",
    "user": "AlexanderDreyer"
}
```

Attachment

Hi,
I backported the handling of setup.py --no-user-cfg from  Python 2.7 to Python 2.6.4 and also added the handling of the environment variable `DISTUTILS_NO_USER_CFG` to python's distutils. 

The new spkg can be found here: 
http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg

The last patch adds this variable to `sage-env`.

Regards,
  Alexander



---

archive/issue_comments_091856.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-19T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91856",
    "user": "AlexanderDreyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091857.json:
```json
{
    "body": "Reported upstream:\nhttp://bugs.python.org/issue9309",
    "created_at": "2010-07-19T21:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91857",
    "user": "AlexanderDreyer"
}
```

Reported upstream:
http://bugs.python.org/issue9309



---

archive/issue_comments_091858.json:
```json
{
    "body": "Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)",
    "created_at": "2010-07-20T09:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91858",
    "user": "AlexanderDreyer"
}
```

Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)



---

archive/issue_comments_091859.json:
```json
{
    "body": "Replying to [comment:9 AlexanderDreyer]:\n> Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)\nYou should also create patches/ACKS.txt.diff as a unified diff file. Although its fairly obvious you can recreate that now, that will not be the case if Python source code is updated. \n\nWould a simpler solution not be for sage-env to set this variable and export it? I don't know much about python, so can't review this myself. \n\nDave",
    "created_at": "2010-07-21T11:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91859",
    "user": "drkirkby"
}
```

Replying to [comment:9 AlexanderDreyer]:
> Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)
You should also create patches/ACKS.txt.diff as a unified diff file. Although its fairly obvious you can recreate that now, that will not be the case if Python source code is updated. 

Would a simpler solution not be for sage-env to set this variable and export it? I don't know much about python, so can't review this myself. 

Dave



---

archive/issue_comments_091860.json:
```json
{
    "body": "Maybe a misunderstanding: the patch of python is necessary  to fix that issue anyway. (This first variant didn't work, if the environment variable was *not* set.)",
    "created_at": "2010-07-21T15:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91860",
    "user": "AlexanderDreyer"
}
```

Maybe a misunderstanding: the patch of python is necessary  to fix that issue anyway. (This first variant didn't work, if the environment variable was *not* set.)



---

archive/issue_comments_091861.json:
```json
{
    "body": "Attachment\n\nAdding handling of environment variable DISTUTILS_NO_USER_CFG to python's distutils",
    "created_at": "2010-07-21T15:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91861",
    "user": "AlexanderDreyer"
}
```

Attachment

Adding handling of environment variable DISTUTILS_NO_USER_CFG to python's distutils



---

archive/issue_comments_091862.json:
```json
{
    "body": "I've added ACKS.txt.patch to the spkg.",
    "created_at": "2010-07-21T16:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91862",
    "user": "AlexanderDreyer"
}
```

I've added ACKS.txt.patch to the spkg.



---

archive/issue_comments_091863.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2010-07-29T14:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91863",
    "user": "AlexanderDreyer"
}
```

Changing component from algebra to build.



---

archive/issue_comments_091864.json:
```json
{
    "body": "The python community does not like the idea of adding an environment variable, see:\nhttp://bugs.python.org/issue9309",
    "created_at": "2010-09-30T07:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91864",
    "user": "AlexanderDreyer"
}
```

The python community does not like the idea of adding an environment variable, see:
http://bugs.python.org/issue9309



---

archive/issue_comments_091865.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91865",
    "user": "jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_091866.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-05-29T02:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91866",
    "user": "kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091867.json:
```json
{
    "body": "Needs a branch.  And we have updated Python.  And probably other reasons it isn't ready yet.  (Or conceivably has been solved in the meantime?)",
    "created_at": "2015-05-29T02:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91867",
    "user": "kcrisman"
}
```

Needs a branch.  And we have updated Python.  And probably other reasons it isn't ready yet.  (Or conceivably has been solved in the meantime?)



---

archive/issue_comments_091868.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-10-31T06:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91868",
    "user": "mkoeppe"
}
```

New commits:



---

archive/issue_comments_091869.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-10-31T06:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91869",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091870.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-07T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91870",
    "user": "embray"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091871.json:
```json
{
    "body": "This looks like the right approach, thanks.",
    "created_at": "2016-11-07T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91871",
    "user": "embray"
}
```

This looks like the right approach, thanks.



---

archive/issue_comments_091872.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-08T23:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91872",
    "user": "vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_091873.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91873",
    "user": "vbraun"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091874.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91874",
    "user": "vbraun"
}
```

Changing status from closed to new.



---

archive/issue_comments_091875.json:
```json
{
    "body": "Prevents pyzmq from building...",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91875",
    "user": "vbraun"
}
```

Prevents pyzmq from building...



---

archive/issue_comments_091876.json:
```json
{
    "body": "\n```\n  Source in /tmp/pip-mTg5Xg-build has version 16.0.0, which satisfies requirement pyzmq==16.0.0 from file:///mnt/disk/home/release/Sage/local/var/tmp/sage/build/pyzmq-16.0.0/src\nInstalling collected packages: pyzmq\n  Running setup.py install for pyzmq: started\n    Running command /mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\n    running configure\n    error: error in command line: command 'Configure' has no such option 'no_user_cfg'\n    Running setup.py install for pyzmq: finished with status 'error'\nCleaning up...\n  Removing source in /tmp/pip-mTg5Xg-build\nCommand \"/mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\" failed with error code 1 in /tmp/pip-mTg5Xg-build/\nException information:\nTraceback (most recent call last):\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/basecommand.py\", line 215, in main\n    status = self.run(options, args)\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/commands/install.py\", line 317, in run\n    prefix=options.prefix_path,\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_set.py\", line 742, in install\n    **kwargs\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_install.py\", line 880, in install\n    spinner=spinner,\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/utils/__init__.py\", line 718, in call_subprocess\n    % (command_desc, proc.returncode, cwd))\nInstallationError: Command \"/mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\" failed with error code 1 in /tmp/pip-mTg5Xg-build/\n```\n",
    "created_at": "2016-11-09T20:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91876",
    "user": "vbraun"
}
```


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

archive/issue_comments_091877.json:
```json
{
    "body": "I've created an upstream issue for this:\n https://github.com/zeromq/pyzmq/issues/937",
    "created_at": "2016-11-09T21:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91877",
    "user": "mkoeppe"
}
```

I've created an upstream issue for this:
 https://github.com/zeromq/pyzmq/issues/937



---

archive/issue_comments_091878.json:
```json
{
    "body": "That's annoying.  For now we should probably remove pip install from pyzmq.",
    "created_at": "2016-11-10T11:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91878",
    "user": "embray"
}
```

That's annoying.  For now we should probably remove pip install from pyzmq.



---

archive/issue_comments_091879.json:
```json
{
    "body": "Upstream pyzmq reports that it works with pip 9.0.1, setuptools 28.8.0.\n\nLet's try with upgrading these packages. #21835 does the upgrade of pip to 9.0.0...",
    "created_at": "2016-11-10T18:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91879",
    "user": "mkoeppe"
}
```

Upstream pyzmq reports that it works with pip 9.0.1, setuptools 28.8.0.

Let's try with upgrading these packages. #21835 does the upgrade of pip to 9.0.0...



---

archive/issue_comments_091880.json:
```json
{
    "body": "Upgrading setuptools to 28.8.0 does not fix the pyzmq install.\n\nI'll wait for the pip upgrade.",
    "created_at": "2016-11-10T18:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91880",
    "user": "mkoeppe"
}
```

Upgrading setuptools to 28.8.0 does not fix the pyzmq install.

I'll wait for the pip upgrade.



---

archive/issue_comments_091881.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-11-10T22:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91881",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_091882.json:
```json
{
    "body": "Here's a fix for our `pyzmq` `spkg-install`, with help from upstream.",
    "created_at": "2016-11-11T03:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91882",
    "user": "mkoeppe"
}
```

Here's a fix for our `pyzmq` `spkg-install`, with help from upstream.



---

archive/issue_comments_091883.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-11-11T03:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91883",
    "user": "mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091884.json:
```json
{
    "body": "Just a comment: it would make sense to use `$PIP_INSTALL` for a few more packages where no extra options are needed: `fpylll`, `gambit`, `sagenb`, `sagetex`.",
    "created_at": "2016-11-11T16:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91884",
    "user": "jdemeyer"
}
```

Just a comment: it would make sense to use `$PIP_INSTALL` for a few more packages where no extra options are needed: `fpylll`, `gambit`, `sagenb`, `sagetex`.



---

archive/issue_comments_091885.json:
```json
{
    "body": "I agree, but that should be on a different ticket. I've created #21864 for this.",
    "created_at": "2016-11-11T19:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91885",
    "user": "mkoeppe"
}
```

I agree, but that should be on a different ticket. I've created #21864 for this.



---

archive/issue_comments_091886.json:
```json
{
    "body": "Needs review.",
    "created_at": "2016-11-15T01:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91886",
    "user": "mkoeppe"
}
```

Needs review.



---

archive/issue_comments_091887.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-12-29T01:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91887",
    "user": "git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_091888.json:
```json
{
    "body": "Rebased, needs review.",
    "created_at": "2016-12-29T01:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91888",
    "user": "mkoeppe"
}
```

Rebased, needs review.



---

archive/issue_comments_091889.json:
```json
{
    "body": "ping?",
    "created_at": "2017-01-16T18:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91889",
    "user": "mkoeppe"
}
```

ping?



---

archive/issue_comments_091890.json:
```json
{
    "body": "The issue with `--global-option` and `--no-user-cfg` still seems odd to me. I think that should be considered a bug in pip.  But I guess there's nothing to be done for now.",
    "created_at": "2017-01-17T12:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91890",
    "user": "embray"
}
```

The issue with `--global-option` and `--no-user-cfg` still seems odd to me. I think that should be considered a bug in pip.  But I guess there's nothing to be done for now.



---

archive/issue_comments_091891.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-01-17T12:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91891",
    "user": "embray"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091892.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-01-21T16:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91892",
    "user": "vbraun"
}
```

Resolution: fixed
