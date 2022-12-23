# Issue 3600: [with patch, needs review] implement process pool for dsage workers

Issue created by migration from https://trac.sagemath.org/ticket/3600

Original creator: yi

Original creation time: 2008-07-08 01:29:03

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




---

Attachment


---

Comment by yi created at 2008-07-08 06:23:24

all the patches split up and whitespace only patches are in the whitespace sub directory


---

Attachment

all the patches split up and whitespace only patches are in the whitespace sub directory


---

Comment by yi created at 2008-07-08 06:33:32

Tarball here:
http://sage.math.washington.edu/home/yqiang/Patches/dsage_process_pool_patches.tar.gz


---

Comment by gfurnish created at 2008-07-08 18:01:58

This should be a very high priority to get reviewed -- it gives orders of magnitude performance improvements.


---

Comment by gfurnish created at 2008-07-08 18:01:58

Changing keywords from "dsage" to "dsage, editor_gfurnish".


---

Comment by gfurnish created at 2008-07-10 12:23:11

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

Comment by yi created at 2008-07-10 15:25:36

The distfactor thing segfaulting is a known issue. 
I can't reproduce the unittest failures on sage.math, using 3.0.4. Can you try it on some other architecture and see if you get the same thing?


---

Comment by yi created at 2008-07-10 21:56:31

Another note:
You will see some errors about the reactor being left in an unclean state. This is OK for now and is expected. The unit tests should still all pass.


---

Comment by yi created at 2008-07-10 22:48:57

New version which fixes the reactor left in an unclean state errors.


---

Attachment

bundle to be applied against 3.0.4


---

Attachment

bundle to be applied against 3.0.4


---

Comment by yi created at 2008-07-13 18:41:58

Please apply dsage_pool.hg and run the unit tests and doctests. The doctests say that they are failing on dsage_interface.py and testdoc.py but that seems to be a problem with the doctest framework since all the tests actually pass (on sage.math, running 3.0.4)


---

Comment by mabshoff created at 2008-12-07 07:24:54

Could someone go through the patches and post something that applies against the current tree and then delete all the old crap?

I know Mike Hansen is working on getting these patches cleaned up and finally into Sage.

Cheers,

Michael


---

Comment by gfurnish created at 2008-12-09 00:10:06

Notes:
In worker/monitor.py the ConnectTLS seems to need a factory argument.

After fixing this authentication seems broken.


---

Comment by gfurnish created at 2008-12-09 07:27:27

I think we are going to have trouble getting this rebased and merged, given it doesn't seem to work very well (at all).  I went ahead and started working on organically modifying dsage over at #4745 to solve many (most) of the same problems as this ticket.


---

Comment by mhansen created at 2008-12-11 14:54:14

Resolution: invalid


---

Comment by mhansen created at 2008-12-11 14:54:14

Based on the code at #4745, I think we can close this as invalid.  There are a few things that might be worth pulling out of here.
