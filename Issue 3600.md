# Issue 3600: [with patch, needs review] implement process pool for dsage workers

archive/issues_003600.json:
```json
{
    "body": "Assignee: yi\n\nKeywords: dsage\n\nThis patch gets rid of the old dsage worker behavior. Specifically, it does the following things:\n\n1. Workers no longer poll the server for new jobs.\n2. Workers no longer poll sage for when the job finishes.\n3. Doctests run much more reliably now, and in much less time (no need for # long time now)\n4. The worker, as well as the server use twistd now, this make things like running them under a profile\n    trivial.\n\nIt's a rather big patch so right now I'd like people to apply it and run the doc/unittests. To run the unittests, do\n\n```\nsage: !trial sage.dsage\n```\n\n\nRun doctests as normal. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/3600\n\n",
    "created_at": "2008-07-08T01:29:03Z",
    "labels": [
        "dsage",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "[with patch, needs review] implement process pool for dsage workers",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/3600",
    "user": "yi"
}
```
Assignee: yi

Keywords: dsage

This patch gets rid of the old dsage worker behavior. Specifically, it does the following things:

1. Workers no longer poll the server for new jobs.
2. Workers no longer poll sage for when the job finishes.
3. Doctests run much more reliably now, and in much less time (no need for # long time now)
4. The worker, as well as the server use twistd now, this make things like running them under a profile
    trivial.

It's a rather big patch so right now I'd like people to apply it and run the doc/unittests. To run the unittests, do

```
sage: !trial sage.dsage
```


Run doctests as normal. 



Issue created by migration from https://trac.sagemath.org/ticket/3600





---

archive/issue_comments_025435.json:
```json
{
    "body": "Attachment [dsage_process_pool.patch](tarball://root/attachments/some-uuid/ticket3600/dsage_process_pool.patch) by yi created at 2008-07-08 01:29:25",
    "created_at": "2008-07-08T01:29:25Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25435",
    "user": "yi"
}
```

Attachment [dsage_process_pool.patch](tarball://root/attachments/some-uuid/ticket3600/dsage_process_pool.patch) by yi created at 2008-07-08 01:29:25



---

archive/issue_comments_025436.json:
```json
{
    "body": "all the patches split up and whitespace only patches are in the whitespace sub directory",
    "created_at": "2008-07-08T06:23:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25436",
    "user": "yi"
}
```

all the patches split up and whitespace only patches are in the whitespace sub directory



---

archive/issue_comments_025437.json:
```json
{
    "body": "Attachment [dsage_process_pool_patches.tar.2.gz](tarball://root/attachments/some-uuid/ticket3600/dsage_process_pool_patches.tar.2.gz) by yi created at 2008-07-08 06:23:34\n\nall the patches split up and whitespace only patches are in the whitespace sub directory",
    "created_at": "2008-07-08T06:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25437",
    "user": "yi"
}
```

Attachment [dsage_process_pool_patches.tar.2.gz](tarball://root/attachments/some-uuid/ticket3600/dsage_process_pool_patches.tar.2.gz) by yi created at 2008-07-08 06:23:34

all the patches split up and whitespace only patches are in the whitespace sub directory



---

archive/issue_comments_025438.json:
```json
{
    "body": "Tarball here:\nhttp://sage.math.washington.edu/home/yqiang/Patches/dsage_process_pool_patches.tar.gz",
    "created_at": "2008-07-08T06:33:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25438",
    "user": "yi"
}
```

Tarball here:
http://sage.math.washington.edu/home/yqiang/Patches/dsage_process_pool_patches.tar.gz



---

archive/issue_comments_025439.json:
```json
{
    "body": "This should be a very high priority to get reviewed -- it gives orders of magnitude performance improvements.",
    "created_at": "2008-07-08T18:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25439",
    "user": "gfurnish"
}
```

This should be a very high priority to get reviewed -- it gives orders of magnitude performance improvements.



---

archive/issue_comments_025440.json:
```json
{
    "body": "Changing keywords from \"dsage\" to \"dsage, editor_gfurnish\".",
    "created_at": "2008-07-08T18:01:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25440",
    "user": "gfurnish"
}
```

Changing keywords from "dsage" to "dsage, editor_gfurnish".



---

archive/issue_comments_025441.json:
```json
{
    "body": "On Sage.math against 3.0.4\n\n```\nsage -t  devel/sage-main/sage/dsage/dist_functions/dist_factor.pysh: line 1:  4406 Segmentation fault      /home/gfurnish/sage-3.0.4-x86_64-Linux/local/bin/python /home/gfurnish/sage-3.0.4-x86_64-Linux/tmp/.doctest_dist_factor.py >/tmp/tmpofG7O8 2>/tmp/tmpIYRdmR\n\nA mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.\n\nsage.dsage.database.tests.test_client\n  ClientTestCase\n    testGetPublicKey ...                                                   [OK]\n    testGetUsername ...                                                    [OK]\n    testInitClient ...                                                     [OK]\n    testSetConnected ...                                                   [OK]\n    testSetEnabled ...                                                     [OK]\n                                                 [ERROR]\nsage.dsage.database.tests.test_job\n  JobTestCase\n    testcreate_job ...                                                     [OK]\n    testjobCreationTime ...                                                [OK]\n    testjobFailures ...                                                    [OK]\n    testjobFile ...                                                        [OK]\n    testjobFinishTime ...                                                  [OK]\n    testjobKilled ...                                                      [OK]\n    testjobResult ...                                                      [OK]\n    testjobStatus ...                                                      [OK]\n    testjobUpdateTime ...                                                  [OK]\n    testjob_id ...                                                         [OK]\n                                                     [ERROR]\n                                                     [ERROR]\n                                                     [ERROR]\n                                                     [ERROR]\n                                                     [ERROR]\n\n===============================================================================\n[ERROR]: sage.dsage.database.tests.test_clientdb\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_clientdb.py\", line 25, in <module>\n    from sage.dsage.database.db_config import init_db\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/db_config.py\", line 5, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n===============================================================================\n[ERROR]: sage.dsage.database.tests.test_jobdb\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_jobdb.py\", line 24, in <module>\n    from sage.dsage.database.jobdb import JobDatabaseSQLite, JobDatabaseSA\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py\", line 21, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n===============================================================================\n[ERROR]: sage.dsage.database.tests.test_workerdb\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_workerdb.py\", line 7, in <module>\n    from sage.dsage.database.db_config import init_db_sa as init_db\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/db_config.py\", line 5, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n===============================================================================\n[ERROR]: sage.dsage.server.tests.test_server\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/server/tests/test_server.py\", line 25, in <module>\n    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py\", line 21, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_pubkeyauth\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/twisted/tests/test_pubkeyauth.py\", line 38, in <module>\n    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py\", line 21, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n===============================================================================\n[ERROR]: sage.dsage.twisted.tests.test_remote\n\nTraceback (most recent call last):\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py\", line 546, in loadPackage\n    module = modinfo.load()\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 380, in load\n    return self.pathEntry.pythonPath.moduleLoader(self.name)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py\", line 618, in moduleLoader\n    return self._moduleLoader(modname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 426, in namedAny\n    topLevelPackage = _importAndCheckStack(trialname)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py\", line 377, in _importAndCheckStack\n    return __import__(importName)\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/twisted/tests/test_remote.py\", line 35, in <module>\n    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py\", line 21, in <module>\n    from sqlalchemy import *\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py\", line 8, in <module>\n    from sqlalchemy.types import \\\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py\", line 28, in <module>\n    from sqlalchemy.util import pickle, Decimal as _python_Decimal\n  File \"/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py\", line 21, in <module>\n    set_types = set, sets.Set\nexceptions.AttributeError: 'module' object has no attribute 'Set'\n-------------------------------------------------------------------------------\nRan 15 tests in 0.017s\n```\n\nWe discussed this patch pretty much in depth, so once it works properly (and I test it on some more architectures), I'll give it a positive review.",
    "created_at": "2008-07-10T12:23:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25441",
    "user": "gfurnish"
}
```

On Sage.math against 3.0.4

```
sage -t  devel/sage-main/sage/dsage/dist_functions/dist_factor.pysh: line 1:  4406 Segmentation fault      /home/gfurnish/sage-3.0.4-x86_64-Linux/local/bin/python /home/gfurnish/sage-3.0.4-x86_64-Linux/tmp/.doctest_dist_factor.py >/tmp/tmpofG7O8 2>/tmp/tmpIYRdmR

A mysterious error (perphaps a memory error?) occurred, which may have crashed doctest.

sage.dsage.database.tests.test_client
  ClientTestCase
    testGetPublicKey ...                                                   [OK]
    testGetUsername ...                                                    [OK]
    testInitClient ...                                                     [OK]
    testSetConnected ...                                                   [OK]
    testSetEnabled ...                                                     [OK]
                                                 [ERROR]
sage.dsage.database.tests.test_job
  JobTestCase
    testcreate_job ...                                                     [OK]
    testjobCreationTime ...                                                [OK]
    testjobFailures ...                                                    [OK]
    testjobFile ...                                                        [OK]
    testjobFinishTime ...                                                  [OK]
    testjobKilled ...                                                      [OK]
    testjobResult ...                                                      [OK]
    testjobStatus ...                                                      [OK]
    testjobUpdateTime ...                                                  [OK]
    testjob_id ...                                                         [OK]
                                                     [ERROR]
                                                     [ERROR]
                                                     [ERROR]
                                                     [ERROR]
                                                     [ERROR]

===============================================================================
[ERROR]: sage.dsage.database.tests.test_clientdb

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_clientdb.py", line 25, in <module>
    from sage.dsage.database.db_config import init_db
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/db_config.py", line 5, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
===============================================================================
[ERROR]: sage.dsage.database.tests.test_jobdb

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_jobdb.py", line 24, in <module>
    from sage.dsage.database.jobdb import JobDatabaseSQLite, JobDatabaseSA
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py", line 21, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
===============================================================================
[ERROR]: sage.dsage.database.tests.test_workerdb

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/tests/test_workerdb.py", line 7, in <module>
    from sage.dsage.database.db_config import init_db_sa as init_db
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/db_config.py", line 5, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
===============================================================================
[ERROR]: sage.dsage.server.tests.test_server

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/server/tests/test_server.py", line 25, in <module>
    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py", line 21, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_pubkeyauth

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/twisted/tests/test_pubkeyauth.py", line 38, in <module>
    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py", line 21, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
===============================================================================
[ERROR]: sage.dsage.twisted.tests.test_remote

Traceback (most recent call last):
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/trial/runner.py", line 546, in loadPackage
    module = modinfo.load()
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 380, in load
    return self.pathEntry.pythonPath.moduleLoader(self.name)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/modules.py", line 618, in moduleLoader
    return self._moduleLoader(modname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 426, in namedAny
    topLevelPackage = _importAndCheckStack(trialname)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/twisted/python/reflect.py", line 377, in _importAndCheckStack
    return __import__(importName)
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/twisted/tests/test_remote.py", line 35, in <module>
    from sage.dsage.database.jobdb import JobDatabaseSA as JobDatabase
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/sage/dsage/database/jobdb.py", line 21, in <module>
    from sqlalchemy import *
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/__init__.py", line 8, in <module>
    from sqlalchemy.types import \
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/types.py", line 28, in <module>
    from sqlalchemy.util import pickle, Decimal as _python_Decimal
  File "/home/gfurnish/sage-3.0.4-x86_64-Linux/local/lib/python2.5/site-packages/SQLAlchemy-0.4.6-py2.5.egg/sqlalchemy/util.py", line 21, in <module>
    set_types = set, sets.Set
exceptions.AttributeError: 'module' object has no attribute 'Set'
-------------------------------------------------------------------------------
Ran 15 tests in 0.017s
```

We discussed this patch pretty much in depth, so once it works properly (and I test it on some more architectures), I'll give it a positive review.



---

archive/issue_comments_025442.json:
```json
{
    "body": "The distfactor thing segfaulting is a known issue. \nI can't reproduce the unittest failures on sage.math, using 3.0.4. Can you try it on some other architecture and see if you get the same thing?",
    "created_at": "2008-07-10T15:25:36Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25442",
    "user": "yi"
}
```

The distfactor thing segfaulting is a known issue. 
I can't reproduce the unittest failures on sage.math, using 3.0.4. Can you try it on some other architecture and see if you get the same thing?



---

archive/issue_comments_025443.json:
```json
{
    "body": "Another note:\nYou will see some errors about the reactor being left in an unclean state. This is OK for now and is expected. The unit tests should still all pass.",
    "created_at": "2008-07-10T21:56:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25443",
    "user": "yi"
}
```

Another note:
You will see some errors about the reactor being left in an unclean state. This is OK for now and is expected. The unit tests should still all pass.



---

archive/issue_comments_025444.json:
```json
{
    "body": "New version which fixes the reactor left in an unclean state errors.",
    "created_at": "2008-07-10T22:48:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25444",
    "user": "yi"
}
```

New version which fixes the reactor left in an unclean state errors.



---

archive/issue_comments_025445.json:
```json
{
    "body": "Attachment [ppool_unit_tests.patch](tarball://root/attachments/some-uuid/ticket3600/ppool_unit_tests.patch) by yi created at 2008-07-13 18:40:42\n\nbundle to be applied against 3.0.4",
    "created_at": "2008-07-13T18:40:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25445",
    "user": "yi"
}
```

Attachment [ppool_unit_tests.patch](tarball://root/attachments/some-uuid/ticket3600/ppool_unit_tests.patch) by yi created at 2008-07-13 18:40:42

bundle to be applied against 3.0.4



---

archive/issue_comments_025446.json:
```json
{
    "body": "Attachment [dsage_ppool.2.hg](tarball://root/attachments/some-uuid/ticket3600/dsage_ppool.2.hg) by yi created at 2008-07-13 18:40:45\n\nbundle to be applied against 3.0.4",
    "created_at": "2008-07-13T18:40:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25446",
    "user": "yi"
}
```

Attachment [dsage_ppool.2.hg](tarball://root/attachments/some-uuid/ticket3600/dsage_ppool.2.hg) by yi created at 2008-07-13 18:40:45

bundle to be applied against 3.0.4



---

archive/issue_comments_025447.json:
```json
{
    "body": "Please apply dsage_pool.hg and run the unit tests and doctests. The doctests say that they are failing on dsage_interface.py and testdoc.py but that seems to be a problem with the doctest framework since all the tests actually pass (on sage.math, running 3.0.4)",
    "created_at": "2008-07-13T18:41:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25447",
    "user": "yi"
}
```

Please apply dsage_pool.hg and run the unit tests and doctests. The doctests say that they are failing on dsage_interface.py and testdoc.py but that seems to be a problem with the doctest framework since all the tests actually pass (on sage.math, running 3.0.4)



---

archive/issue_comments_025448.json:
```json
{
    "body": "Could someone go through the patches and post something that applies against the current tree and then delete all the old crap?\n\nI know Mike Hansen is working on getting these patches cleaned up and finally into Sage.\n\nCheers,\n\nMichael",
    "created_at": "2008-12-07T07:24:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25448",
    "user": "mabshoff"
}
```

Could someone go through the patches and post something that applies against the current tree and then delete all the old crap?

I know Mike Hansen is working on getting these patches cleaned up and finally into Sage.

Cheers,

Michael



---

archive/issue_comments_025449.json:
```json
{
    "body": "Notes:\nIn worker/monitor.py the ConnectTLS seems to need a factory argument.\n\nAfter fixing this authentication seems broken.",
    "created_at": "2008-12-09T00:10:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25449",
    "user": "gfurnish"
}
```

Notes:
In worker/monitor.py the ConnectTLS seems to need a factory argument.

After fixing this authentication seems broken.



---

archive/issue_comments_025450.json:
```json
{
    "body": "I think we are going to have trouble getting this rebased and merged, given it doesn't seem to work very well (at all).  I went ahead and started working on organically modifying dsage over at #4745 to solve many (most) of the same problems as this ticket.",
    "created_at": "2008-12-09T07:27:27Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25450",
    "user": "gfurnish"
}
```

I think we are going to have trouble getting this rebased and merged, given it doesn't seem to work very well (at all).  I went ahead and started working on organically modifying dsage over at #4745 to solve many (most) of the same problems as this ticket.



---

archive/issue_comments_025451.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2008-12-11T14:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25451",
    "user": "mhansen"
}
```

Resolution: invalid



---

archive/issue_comments_025452.json:
```json
{
    "body": "Based on the code at #4745, I think we can close this as invalid.  There are a few things that might be worth pulling out of here.",
    "created_at": "2008-12-11T14:54:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/3600",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/3600#issuecomment-25452",
    "user": "mhansen"
}
```

Based on the code at #4745, I think we can close this as invalid.  There are a few things that might be worth pulling out of here.
