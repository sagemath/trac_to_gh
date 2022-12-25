# Issue 9536: python setup.py picks prefix from ~/.pydistutils.cfg

archive/issues_009536.json:
```json
{
    "body": "Assignee: @aghitza\n\nCC:  @jdemeyer @embray @nexttime @kiwifb @vbraun\n\nHi,\nseveral packages do use `python setup.py`. This picks up the customized settings from ~/.pydistutils.cfg. This is bad, because it overrides the prefix setting. \n\nFor sage-main, I'll attach a patch: `setup.cfg` in the corresponding directory overrides the usere settings. Maybe there's a global solution.\n\nRegards,\n  Alexander Dreyer\n\nIssue created by migration from https://trac.sagemath.org/ticket/9536\n\n",
    "created_at": "2010-07-18T14:07:14Z",
    "labels": [
        "component: algebra",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-7.6",
    "title": "python setup.py picks prefix from ~/.pydistutils.cfg",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/9536",
    "user": "https://github.com/alexanderdreyer"
}
```
Assignee: @aghitza

CC:  @jdemeyer @embray @nexttime @kiwifb @vbraun

Hi,
several packages do use `python setup.py`. This picks up the customized settings from ~/.pydistutils.cfg. This is bad, because it overrides the prefix setting. 

For sage-main, I'll attach a patch: `setup.cfg` in the corresponding directory overrides the usere settings. Maybe there's a global solution.

Regards,
  Alexander Dreyer

Issue created by migration from https://trac.sagemath.org/ticket/9536





---

archive/issue_comments_091692.json:
```json
{
    "body": "Patch for sage-main",
    "created_at": "2010-07-18T14:09:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91692",
    "user": "https://github.com/alexanderdreyer"
}
```

Patch for sage-main



---

archive/issue_comments_091693.json:
```json
{
    "body": "Changing assignee from @aghitza to @alexanderdreyer.",
    "created_at": "2010-07-18T14:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91693",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing assignee from @aghitza to @alexanderdreyer.



---

archive/issue_comments_091694.json:
```json
{
    "body": "Attachment [setup_py_issue.patch](tarball://root/attachments/some-uuid/ticket9536/setup_py_issue.patch) by @alexanderdreyer created at 2010-07-18 14:46:44",
    "created_at": "2010-07-18T14:46:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91694",
    "user": "https://github.com/alexanderdreyer"
}
```

Attachment [setup_py_issue.patch](tarball://root/attachments/some-uuid/ticket9536/setup_py_issue.patch) by @alexanderdreyer created at 2010-07-18 14:46:44



---

archive/issue_comments_091695.json:
```json
{
    "body": "The following packages from the distribution use setup.py and may be affected:\n\n```\nzodb3-3.7.0.p4\nscipy_sandbox-20071020.p5\npexpect-2.0.p4\nsqlalchemy-0.5.8\nglpk-4.44\nmpmath-0.15\npil-1.1.6.p2\nmercurial-1.3.1.p2\npycrypto-2.0.1.p5\nmpir-1.2.2.p1\nweave-0.4.9.p0\nsympy-0.6.4.p0\nscons-1.2.0\nnumpy-1.3.0.p3\ngdmodule-0.56.p7\nsagetex-2.2.5\nsage-4.5\nmatplotlib-0.99.3\nsage_scripts-4.5\nsetuptools-0.6c9.p0\npython-2.6.4.p9\npython_gnutls-1.1.4.p7\nsagenb-0.8.1\nnetworkx-1.0.1\njinja-1.2.p0\ncython-0.12.1\npygments-0.11.1.p0\nscipy-0.7.p5\ncvxopt-0.9.p8\njinja2-2.1.1.p0\nsphinx-0.6.3.p4\ndocutils-0.5.p0\ntwisted-9.0.p2\nipython-0.9.1.p0\nmoin-1.9.1.p1\n```\n\n\nThe following already have setup.cfg, but it may not have the prefix definition:\n\n```\nzodb3-3.7.0.p4\nsqlalchemy-0.5.8\nscons-1.2.0\nmatplotlib-0.99.3\nsetuptools-0.6c9.p0\nsagenb-0.8.1\nnetworkx-1.0.1\njinja-1.2.p0\npygments-0.11.1.p0\njinja2-2.1.1.p0\nsphinx-0.6.3.p4\ntwisted-9.0.p2\nmoin-1.9.1.p1\n```\n",
    "created_at": "2010-07-18T15:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91695",
    "user": "https://github.com/alexanderdreyer"
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

archive/issue_comments_091696.json:
```json
{
    "body": "Hi!\nI am not an export for that for that, but did you read\nhttp://docs.python.org/install/#location-and-names-of-config-files\nThere seems to be some options:\n\u2013no-user-cfg\n\nCheers,\nMichael",
    "created_at": "2010-07-19T10:07:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91696",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
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

archive/issue_comments_091697.json:
```json
{
    "body": "Hi Michael,\nindeed, that's a better solution. But both have the problem, that 30+ packages would have to be fixed, and it might be forgotten in the future. (Maybe there some monkey patch for distutils, that all of it can be overwritten by the environment.)\n\nBest regards,\n  Alexander",
    "created_at": "2010-07-19T10:13:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91697",
    "user": "https://github.com/alexanderdreyer"
}
```

Hi Michael,
indeed, that's a better solution. But both have the problem, that 30+ packages would have to be fixed, and it might be forgotten in the future. (Maybe there some monkey patch for distutils, that all of it can be overwritten by the environment.)

Best regards,
  Alexander



---

archive/issue_comments_091698.json:
```json
{
    "body": "maybe, I did not try (just read the docs):\nhttp://docs.python.org/install/#inst-config-files\n\ncreate system distutils.cfg\n\n\n```\n[global]\nno-user-cfg=1\n```\n",
    "created_at": "2010-07-19T10:23:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91698",
    "user": "https://trac.sagemath.org/admin/accounts/users/PolyBoRi"
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

archive/issue_comments_091699.json:
```json
{
    "body": "Hi,\nunfortunately, this is a Python 2.7 feature and it does not support no-user-cfg in distutils.cfg :-(\n\nRegards,\n  Alexander",
    "created_at": "2010-07-19T15:11:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91699",
    "user": "https://github.com/alexanderdreyer"
}
```

Hi,
unfortunately, this is a Python 2.7 feature and it does not support no-user-cfg in distutils.cfg :-(

Regards,
  Alexander



---

archive/issue_comments_091700.json:
```json
{
    "body": "patch for sage/spkg/base/sage-env sage/local/bin/sage-env (needs python 2.6.4.p10)",
    "created_at": "2010-07-19T20:46:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91700",
    "user": "https://github.com/alexanderdreyer"
}
```

patch for sage/spkg/base/sage-env sage/local/bin/sage-env (needs python 2.6.4.p10)



---

archive/issue_comments_091701.json:
```json
{
    "body": "Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket9536/sage-env.patch) by @alexanderdreyer created at 2010-07-19 20:50:41\n\nHi,\nI backported the handling of setup.py --no-user-cfg from  Python 2.7 to Python 2.6.4 and also added the handling of the environment variable `DISTUTILS_NO_USER_CFG` to python's distutils. \n\nThe new spkg can be found here: \nhttp://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg\n\nThe last patch adds this variable to `sage-env`.\n\nRegards,\n  Alexander",
    "created_at": "2010-07-19T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91701",
    "user": "https://github.com/alexanderdreyer"
}
```

Attachment [sage-env.patch](tarball://root/attachments/some-uuid/ticket9536/sage-env.patch) by @alexanderdreyer created at 2010-07-19 20:50:41

Hi,
I backported the handling of setup.py --no-user-cfg from  Python 2.7 to Python 2.6.4 and also added the handling of the environment variable `DISTUTILS_NO_USER_CFG` to python's distutils. 

The new spkg can be found here: 
http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg

The last patch adds this variable to `sage-env`.

Regards,
  Alexander



---

archive/issue_comments_091702.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-07-19T20:50:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91702",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091703.json:
```json
{
    "body": "Reported upstream:\nhttp://bugs.python.org/issue9309",
    "created_at": "2010-07-19T21:16:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91703",
    "user": "https://github.com/alexanderdreyer"
}
```

Reported upstream:
http://bugs.python.org/issue9309



---

archive/issue_comments_091704.json:
```json
{
    "body": "Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)",
    "created_at": "2010-07-20T09:41:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91704",
    "user": "https://github.com/alexanderdreyer"
}
```

Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)



---

archive/issue_comments_091705.json:
```json
{
    "body": "Replying to [comment:9 AlexanderDreyer]:\n> Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)\nYou should also create patches/ACKS.txt.diff as a unified diff file. Although its fairly obvious you can recreate that now, that will not be the case if Python source code is updated. \n\nWould a simpler solution not be for sage-env to set this variable and export it? I don't know much about python, so can't review this myself. \n\nDave",
    "created_at": "2010-07-21T11:49:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91705",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Replying to [comment:9 AlexanderDreyer]:
> Minor update: http://sage.math.washington.edu/home/dreyer/suse101/python-2.6.4.p10.spkg (useful, if the `sage-env` patch is not used)
You should also create patches/ACKS.txt.diff as a unified diff file. Although its fairly obvious you can recreate that now, that will not be the case if Python source code is updated. 

Would a simpler solution not be for sage-env to set this variable and export it? I don't know much about python, so can't review this myself. 

Dave



---

archive/issue_comments_091706.json:
```json
{
    "body": "Maybe a misunderstanding: the patch of python is necessary  to fix that issue anyway. (This first variant didn't work, if the environment variable was *not* set.)",
    "created_at": "2010-07-21T15:45:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91706",
    "user": "https://github.com/alexanderdreyer"
}
```

Maybe a misunderstanding: the patch of python is necessary  to fix that issue anyway. (This first variant didn't work, if the environment variable was *not* set.)



---

archive/issue_comments_091707.json:
```json
{
    "body": "Attachment [python-2.6.4.p10.patch](tarball://root/attachments/some-uuid/ticket9536/python-2.6.4.p10.patch) by @alexanderdreyer created at 2010-07-21 15:58:15\n\nAdding handling of environment variable DISTUTILS_NO_USER_CFG to python's distutils",
    "created_at": "2010-07-21T15:58:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91707",
    "user": "https://github.com/alexanderdreyer"
}
```

Attachment [python-2.6.4.p10.patch](tarball://root/attachments/some-uuid/ticket9536/python-2.6.4.p10.patch) by @alexanderdreyer created at 2010-07-21 15:58:15

Adding handling of environment variable DISTUTILS_NO_USER_CFG to python's distutils



---

archive/issue_comments_091708.json:
```json
{
    "body": "I've added ACKS.txt.patch to the spkg.",
    "created_at": "2010-07-21T16:03:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91708",
    "user": "https://github.com/alexanderdreyer"
}
```

I've added ACKS.txt.patch to the spkg.



---

archive/issue_comments_091709.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2010-07-29T14:02:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91709",
    "user": "https://github.com/alexanderdreyer"
}
```

Changing component from algebra to build.



---

archive/issue_comments_091710.json:
```json
{
    "body": "The python community does not like the idea of adding an environment variable, see:\nhttp://bugs.python.org/issue9309",
    "created_at": "2010-09-30T07:23:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91710",
    "user": "https://github.com/alexanderdreyer"
}
```

The python community does not like the idea of adding an environment variable, see:
http://bugs.python.org/issue9309



---

archive/issue_comments_091711.json:
```json
{
    "body": "Please fill in your real name as Author.",
    "created_at": "2012-07-27T20:42:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91711",
    "user": "https://github.com/jdemeyer"
}
```

Please fill in your real name as Author.



---

archive/issue_comments_091712.json:
```json
{
    "body": "Changing status from needs_review to needs_work.",
    "created_at": "2015-05-29T02:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91712",
    "user": "https://github.com/kcrisman"
}
```

Changing status from needs_review to needs_work.



---

archive/issue_comments_091713.json:
```json
{
    "body": "Needs a branch.  And we have updated Python.  And probably other reasons it isn't ready yet.  (Or conceivably has been solved in the meantime?)",
    "created_at": "2015-05-29T02:20:07Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91713",
    "user": "https://github.com/kcrisman"
}
```

Needs a branch.  And we have updated Python.  And probably other reasons it isn't ready yet.  (Or conceivably has been solved in the meantime?)



---

archive/issue_comments_091714.json:
```json
{
    "body": "New commits:",
    "created_at": "2016-10-31T06:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91714",
    "user": "https://github.com/mkoeppe"
}
```

New commits:



---

archive/issue_comments_091715.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2016-10-31T06:33:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91715",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_091716.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2016-11-07T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91716",
    "user": "https://github.com/embray"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_091717.json:
```json
{
    "body": "This looks like the right approach, thanks.",
    "created_at": "2016-11-07T13:29:40Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91717",
    "user": "https://github.com/embray"
}
```

This looks like the right approach, thanks.



---

archive/issue_events_009686.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-11-08T23:42:27Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9536#event-9686"
}
```



---

archive/issue_comments_091718.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2016-11-08T23:42:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91718",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed



---

archive/issue_comments_091719.json:
```json
{
    "body": "Resolution changed from fixed to ",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91719",
    "user": "https://github.com/vbraun"
}
```

Resolution changed from fixed to 



---

archive/issue_comments_091720.json:
```json
{
    "body": "Changing status from closed to new.",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91720",
    "user": "https://github.com/vbraun"
}
```

Changing status from closed to new.



---

archive/issue_events_009687.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2016-11-09T20:47:14Z",
    "event": "reopened",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9536#event-9687"
}
```



---

archive/issue_comments_091721.json:
```json
{
    "body": "Prevents pyzmq from building...",
    "created_at": "2016-11-09T20:47:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91721",
    "user": "https://github.com/vbraun"
}
```

Prevents pyzmq from building...



---

archive/issue_comments_091722.json:
```json
{
    "body": "\n```\n  Source in /tmp/pip-mTg5Xg-build has version 16.0.0, which satisfies requirement pyzmq==16.0.0 from file:///mnt/disk/home/release/Sage/local/var/tmp/sage/build/pyzmq-16.0.0/src\nInstalling collected packages: pyzmq\n  Running setup.py install for pyzmq: started\n    Running command /mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\n    running configure\n    error: error in command line: command 'Configure' has no such option 'no_user_cfg'\n    Running setup.py install for pyzmq: finished with status 'error'\nCleaning up...\n  Removing source in /tmp/pip-mTg5Xg-build\nCommand \"/mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\" failed with error code 1 in /tmp/pip-mTg5Xg-build/\nException information:\nTraceback (most recent call last):\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/basecommand.py\", line 215, in main\n    status = self.run(options, args)\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/commands/install.py\", line 317, in run\n    prefix=options.prefix_path,\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_set.py\", line 742, in install\n    **kwargs\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/req/req_install.py\", line 880, in install\n    spinner=spinner,\n  File \"/mnt/disk/home/release/Sage/local/lib/python2.7/site-packages/pip/utils/__init__.py\", line 718, in call_subprocess\n    % (command_desc, proc.returncode, cwd))\nInstallationError: Command \"/mnt/disk/home/release/Sage/local/bin/python -u -c \"import setuptools, tokenize;__file__='/tmp/pip-mTg5Xg-build/setup.py';exec(compile(getattr(tokenize, 'open', open)(__file__).read().replace('\\r\\n', '\\n'), __file__, 'exec'))\" configure --zmq=/mnt/disk/home/release/Sage/local --no-user-cfg install --record /tmp/pip-o79sR3-record/install-record.txt --single-version-externally-managed --compile\" failed with error code 1 in /tmp/pip-mTg5Xg-build/\n```\n",
    "created_at": "2016-11-09T20:48:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91722",
    "user": "https://github.com/vbraun"
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

archive/issue_comments_091723.json:
```json
{
    "body": "I've created an upstream issue for this:\n https://github.com/zeromq/pyzmq/issues/937",
    "created_at": "2016-11-09T21:55:17Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91723",
    "user": "https://github.com/mkoeppe"
}
```

I've created an upstream issue for this:
 https://github.com/zeromq/pyzmq/issues/937



---

archive/issue_comments_091724.json:
```json
{
    "body": "That's annoying.  For now we should probably remove pip install from pyzmq.",
    "created_at": "2016-11-10T11:42:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91724",
    "user": "https://github.com/embray"
}
```

That's annoying.  For now we should probably remove pip install from pyzmq.



---

archive/issue_comments_091725.json:
```json
{
    "body": "Upstream pyzmq reports that it works with pip 9.0.1, setuptools 28.8.0.\n\nLet's try with upgrading these packages. #21835 does the upgrade of pip to 9.0.0...",
    "created_at": "2016-11-10T18:11:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91725",
    "user": "https://github.com/mkoeppe"
}
```

Upstream pyzmq reports that it works with pip 9.0.1, setuptools 28.8.0.

Let's try with upgrading these packages. #21835 does the upgrade of pip to 9.0.0...



---

archive/issue_comments_091726.json:
```json
{
    "body": "Upgrading setuptools to 28.8.0 does not fix the pyzmq install.\n\nI'll wait for the pip upgrade.",
    "created_at": "2016-11-10T18:56:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91726",
    "user": "https://github.com/mkoeppe"
}
```

Upgrading setuptools to 28.8.0 does not fix the pyzmq install.

I'll wait for the pip upgrade.



---

archive/issue_comments_091727.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-11-10T22:04:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91727",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_091728.json:
```json
{
    "body": "Here's a fix for our `pyzmq` `spkg-install`, with help from upstream.",
    "created_at": "2016-11-11T03:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91728",
    "user": "https://github.com/mkoeppe"
}
```

Here's a fix for our `pyzmq` `spkg-install`, with help from upstream.



---

archive/issue_comments_091729.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2016-11-11T03:06:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91729",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_091730.json:
```json
{
    "body": "Just a comment: it would make sense to use `$PIP_INSTALL` for a few more packages where no extra options are needed: `fpylll`, `gambit`, `sagenb`, `sagetex`.",
    "created_at": "2016-11-11T16:39:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91730",
    "user": "https://github.com/jdemeyer"
}
```

Just a comment: it would make sense to use `$PIP_INSTALL` for a few more packages where no extra options are needed: `fpylll`, `gambit`, `sagenb`, `sagetex`.



---

archive/issue_comments_091731.json:
```json
{
    "body": "I agree, but that should be on a different ticket. I've created #21864 for this.",
    "created_at": "2016-11-11T19:53:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91731",
    "user": "https://github.com/mkoeppe"
}
```

I agree, but that should be on a different ticket. I've created #21864 for this.



---

archive/issue_comments_091732.json:
```json
{
    "body": "Needs review.",
    "created_at": "2016-11-15T01:54:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91732",
    "user": "https://github.com/mkoeppe"
}
```

Needs review.



---

archive/issue_comments_091733.json:
```json
{
    "body": "Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:",
    "created_at": "2016-12-29T01:07:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91733",
    "user": "https://trac.sagemath.org/admin/accounts/users/git"
}
```

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:



---

archive/issue_comments_091734.json:
```json
{
    "body": "Rebased, needs review.",
    "created_at": "2016-12-29T01:08:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91734",
    "user": "https://github.com/mkoeppe"
}
```

Rebased, needs review.



---

archive/issue_comments_091735.json:
```json
{
    "body": "ping?",
    "created_at": "2017-01-16T18:35:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91735",
    "user": "https://github.com/mkoeppe"
}
```

ping?



---

archive/issue_comments_091736.json:
```json
{
    "body": "The issue with `--global-option` and `--no-user-cfg` still seems odd to me. I think that should be considered a bug in pip.  But I guess there's nothing to be done for now.",
    "created_at": "2017-01-17T12:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91736",
    "user": "https://github.com/embray"
}
```

The issue with `--global-option` and `--no-user-cfg` still seems odd to me. I think that should be considered a bug in pip.  But I guess there's nothing to be done for now.



---

archive/issue_comments_091737.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2017-01-17T12:06:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91737",
    "user": "https://github.com/embray"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_events_009688.json:
```json
{
    "actor": "https://github.com/vbraun",
    "created_at": "2017-01-21T16:35:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/9536#event-9688"
}
```



---

archive/issue_comments_091738.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2017-01-21T16:35:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/9536",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/9536#issuecomment-91738",
    "user": "https://github.com/vbraun"
}
```

Resolution: fixed
