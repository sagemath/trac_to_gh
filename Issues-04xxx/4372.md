# Issue 4372: Repair to totallyreal_dsage

archive/issues_004372.json:
```json
{
    "body": "Assignee: @williamstein\n\nTwo changes/updates to get totallyreal_dsage to work:\n\n(1) Craig improved the totally real field enumeration, but changed the public incr() to increment().\n\n(2) dsage had some update where wall_time of a job is returned as a datetime object.\n\ntotallyreal_dsage is still at a nodoctest status, so shouldn't require any (meaningful) review if the patch works (it's against 3.1.4).\n\nJV\n\nIssue created by migration from https://trac.sagemath.org/ticket/4372\n\n",
    "closed_at": "2010-02-02T06:37:28Z",
    "created_at": "2008-10-26T16:45:38Z",
    "labels": [
        "component: number theory",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Repair to totallyreal_dsage",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/4372",
    "user": "https://github.com/jvoight"
}
```
Assignee: @williamstein

Two changes/updates to get totallyreal_dsage to work:

(1) Craig improved the totally real field enumeration, but changed the public incr() to increment().

(2) dsage had some update where wall_time of a job is returned as a datetime object.

totallyreal_dsage is still at a nodoctest status, so shouldn't require any (meaningful) review if the patch works (it's against 3.1.4).

JV

Issue created by migration from https://trac.sagemath.org/ticket/4372





---

archive/issue_comments_032081.json:
```json
{
    "body": "Attachment [10735.patch](tarball://root/attachments/some-uuid/ticket4372/10735.patch) by @jvoight created at 2008-10-26 16:45:56",
    "created_at": "2008-10-26T16:45:56Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32081",
    "user": "https://github.com/jvoight"
}
```

Attachment [10735.patch](tarball://root/attachments/some-uuid/ticket4372/10735.patch) by @jvoight created at 2008-10-26 16:45:56



---

archive/issue_comments_032082.json:
```json
{
    "body": "> totallyreal_dsage is still at a nodoctest status, so shouldn't require any (meaningful) review if the patch works (it's against 3.1.4). \n\n\nAny patch should be reviewed in detail regardless of nodoctest status or not. Is there a specific reason we shouldn't remove the nodoctest on that file now?\n\nCheers,\n\nMichael",
    "created_at": "2008-10-27T01:03:23Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32082",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

> totallyreal_dsage is still at a nodoctest status, so shouldn't require any (meaningful) review if the patch works (it's against 3.1.4). 


Any patch should be reviewed in detail regardless of nodoctest status or not. Is there a specific reason we shouldn't remove the nodoctest on that file now?

Cheers,

Michael



---

archive/issue_comments_032083.json:
```json
{
    "body": "Attachment [10737.patch](tarball://root/attachments/some-uuid/ticket4372/10737.patch) by @jvoight created at 2008-10-27 14:12:09",
    "created_at": "2008-10-27T14:12:09Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32083",
    "user": "https://github.com/jvoight"
}
```

Attachment [10737.patch](tarball://root/attachments/some-uuid/ticket4372/10737.patch) by @jvoight created at 2008-10-27 14:12:09



---

archive/issue_comments_032084.json:
```json
{
    "body": "> Any patch should be reviewed in detail regardless of nodoctest status or not. \n> Is there a specific reason we shouldn't remove the nodoctest on that file now?\n\n\nAgreed.  I'd say the code is still 'experimental'; it only most of the time works for me without extra effort, though this is probably because dsage itself keeps getting upgraded.  What is the sage philosophy here?  The code will never be used as a component in some thing else, but I thought I should still share it.  \n\nJV",
    "created_at": "2008-10-27T14:15:14Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32084",
    "user": "https://github.com/jvoight"
}
```

> Any patch should be reviewed in detail regardless of nodoctest status or not. 
> Is there a specific reason we shouldn't remove the nodoctest on that file now?


Agreed.  I'd say the code is still 'experimental'; it only most of the time works for me without extra effort, though this is probably because dsage itself keeps getting upgraded.  What is the sage philosophy here?  The code will never be used as a component in some thing else, but I thought I should still share it.  

JV



---

archive/issue_comments_032085.json:
```json
{
    "body": "> Agreed. I'd say the code is still 'experimental'; it only most of the time works \n> for me without extra effort, though this is probably because dsage itself \n> keeps getting upgraded.\n\n\nWell that will happen at most one more time, since dsage development stopped.",
    "created_at": "2008-11-28T22:34:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32085",
    "user": "https://github.com/williamstein"
}
```

> Agreed. I'd say the code is still 'experimental'; it only most of the time works 
> for me without extra effort, though this is probably because dsage itself 
> keeps getting upgraded.


Well that will happen at most one more time, since dsage development stopped.



---

archive/issue_comments_032086.json:
```json
{
    "body": "REFEREE:\n\nI applied the first two patches no problem to 3.2.1.alpha2.  The third patch fails to apply:\n\n```\nsage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4372/10737.patch')\nAttempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4372/10737.patch?format=raw\nLoading: [.]\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg status\ncd \"/home/was/build/sage-3.2.1.alpha1/devel/sage\" && hg import   \"/home/was/.sage/temp/sage/25372/tmp_2.patch\"\napplying /home/was/.sage/temp/sage/25372/tmp_2.patch\npatching file sage/rings/number_field/totallyreal_dsage.py\nHunk #1 FAILED at 296\n1 out of 1 hunk FAILED -- saving rejects to file sage/rings/number_field/totallyreal_dsage.py.rej\nabort: patch failed to apply\n---\n\nwas@sage:~/build/sage-3.2.1.alpha1$ more devel/sage/sage/rings/number_field/totallyreal_dsage.py.rej \n--- totallyreal_dsage.py\n+++ totallyreal_dsage.py\n@@ -297,7 +297,7 @@\n\n                     # Add the timings.\n                     self.cputime += job[1].cpu_time\n-                    self.walltime += job[1].wall_time\n+                    self.walltime += job[1].wall_time.seconds\n\n                     if write_result:\n                         fsock = open(filename_start + str(job[0]).replace(' ','') + '.out', 'w')\n```\n\nLooks easy to fix... so I fix it.  No problem.\n\nI then enable doctesting and try the tests, but they totally hang in line 60:\n\n```\nTrying:\n    dsage.worker()###line 60:_sage_    >>> dsage.worker()\nExpecting:\n    [...]\n2008-11-28 17:54:57-0800 [-] Log opened.\n2008-11-28 17:54:57-0800 [-] Log opened.\n2008-11-28 17:54:57-0800 [-] Logging to file:  /home/was/.sage/dsage/worker.log\n2008-11-28 17:54:57-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n2008-11-28 17:54:57-0800 [-] ==================================================\n2008-11-28 17:54:57-0800 [-] DSAGE Worker\n2008-11-28 17:54:57-0800 [-] Started with PID: 25788\n2008-11-28 17:54:57-0800 [-] Connecting to localhost:8081\n2008-11-28 17:54:57-0800 [-] Using SSL: True\n2008-11-28 17:54:57-0800 [-] ==================================================\n2008-11-28 17:54:57-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 2 seconds\n2008-11-28 17:54:57-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n2008-11-28 17:55:00-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n2008-11-28 17:55:00-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 7 seconds\n2008-11-28 17:55:00-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n2008-11-28 17:55:07-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n2008-11-28 17:55:07-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 22 seconds\n2008-11-28 17:55:07-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>\n[waited 20 minutes and it is stuck hard]\n```\n\nI delete ~/.sage/dsage and try again.  Doctesting finishes with some errors:\n\n```\nwas@sage:~/build/sage-3.2.1.alpha1$ ./sage -t devel/sage/sage/rings/number_field/totallyreal_dsage.py\nsage -t  devel/sage/sage/rings/number_field/totallyreal_dsage.pyGoing into testing mode...\nAdding testing client...\n2008-11-28 18:12:33-0800 [-] Log opened.\n2008-11-28 18:12:33-0800 [-] Log opened.\n2008-11-28 18:12:33-0800 [-] Logging to file:  /home/was/.sage/dsage/worker.log\n2008-11-28 18:12:33-0800 [-] Traceback (most recent call last):\n2008-11-28 18:12:33-0800 [-]   File \"/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py\", line 1039, in <module>\n2008-11-28 18:12:33-0800 [-]     main()\n2008-11-28 18:12:33-0800 [-]   File \"/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py\", line 1026, in main\n2008-11-28 18:12:33-0800 [-]     privkey_file=options.privkey_file)\n2008-11-28 18:12:33-0800 [-]   File \"/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py\", line 734, in __init__\n2008-11-28 18:12:33-0800 [-]     self.pubkey = keys.Key.fromFile(self.pubkey_file)\n2008-11-28 18:12:33-0800 [-]   File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/conch/ssh/keys.py\", line 60, in fromFile\n2008-11-28 18:12:33-0800 [-]     return Class.fromString(file(filename, 'rb').read(), type, passphrase)\n2008-11-28 18:12:33-0800 [-] IOError: [Errno 2] No such file or directory: '/home/was/.sage/dsage/dsage_key.pub'\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 51:\n    sage: dsage.setup_all()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[2]>\", line 1, in <module>\n        dsage.setup_all()###line 51:\n    sage: dsage.setup_all()\n    AttributeError: 'DistributedSage' object has no attribute 'setup_all'\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 53:\n    sage: dsage.server()\nExpected:\n    [...]\nGot:\n    Going into testing mode...\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 58:\n    sage: dsage.setup_worker()\nExpected:\n    [...]\nGot:\n    Worker configuration finished.\n    <BLANKLINE>\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 60:\n    sage: dsage.worker()\nExpected:\n    [...]\nGot nothing\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 65:\n    sage: Dtr = totallyreal_dsage()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_1[6]>\", line 1, in <module>\n        Dtr = totallyreal_dsage()###line 65:\n    sage: Dtr = totallyreal_dsage()\n      File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal_dsage.py\", line 69, in __init__\n        self.D = DSage()\n    NameError: global name 'DSage' is not defined\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 94:\n    sage: Dtr.enumerate(6, 15^6, 4)\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[2]>\", line 1, in <module>\n        Dtr.enumerate(Integer(6), Integer(15)**Integer(6), Integer(4))###line 94:\n    sage: Dtr.enumerate(6, 15^6, 4)\n    NameError: name 'Dtr' is not defined\n**********************************************************************\nFile \"/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py\", line 96:\n    sage: Dtr.compile_fields()\nException raised:\n    Traceback (most recent call last):\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1231, in run_one_test\n        self.run_one_example(test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py\", line 38, in run_one_example\n        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)\n      File \"/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py\", line 1172, in run_one_example\n        compileflags, 1) in test.globs\n      File \"<doctest __main__.example_2[3]>\", line 1, in <module>\n        Dtr.compile_fields()###line 96:\n    sage: Dtr.compile_fields()\n    NameError: name 'Dtr' is not defined\n**********************************************************************\n2 items had failures:\n   5 of   7 in __main__.example_1\n   2 of   4 in __main__.example_2\n***Test Failed*** 7 failures.\nFor whitespace errors, see the file /home/was/build/sage-3.2.1.alpha1/tmp/.doctest_totallyreal_dsage.pyTraceback (most recent call last):\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py\", line 614, in run\n    runApp(config)\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/scripts/twistd.py\", line 23, in runApp\n    _SomeApplicationRunner(config).run()\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py\", line 330, in run\n    self.application = self.createOrGetApplication()\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py\", line 416, in createOrGetApplication\n    application = getApplication(self.config, passphrase)\n--- <exception caught here> ---\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py\", line 427, in getApplication\n    application = service.loadApplication(filename, style, passphrase)\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/service.py\", line 368, in loadApplication\n    application = sob.loadValueFromFile(filename, 'application', passphrase)\n  File \"/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/persisted/sob.py\", line 214, in loadValueFromFile\n    exec fileObj in d, d\n  File \"dsage_server.tac\", line 130, in <module>\n    dsage_server, dsage_server_port, ssl = start_dsage_server(dsage_service)\n  File \"dsage_server.tac\", line 93, in start_dsage_server\n    cert = X509Certificate(open(SSL_CERT).read())\nexceptions.IOError: [Errno 2] No such file or directory: '/home/was/.sage/dsage/pubcert.pem'\n\nFailed to load application: [Errno 2] No such file or directory: '/home/was/.sage/dsage/pubcert.pem'\n\n\n\t [3.6 s]\nexit code: 1024\n \n----------------------------------------------------------------------\nThe following tests failed:\n\n\n\tsage -t  devel/sage/sage/rings/number_field/totallyreal_dsage.py\nTotal time for all tests: 3.6 seconds\n\n```\n\n\n... so I try\n\n```\nsage: dsage.setup()\n```\n\nand try doctesting again and it hangs.\n\n\nAny thoughts?",
    "created_at": "2008-11-29T02:16:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32086",
    "user": "https://github.com/williamstein"
}
```

REFEREE:

I applied the first two patches no problem to 3.2.1.alpha2.  The third patch fails to apply:

```
sage: hg_sage.apply('http://trac.sagemath.org/sage_trac/attachment/ticket/4372/10737.patch')
Attempting to load remote file: http://trac.sagemath.org/sage_trac/attachment/ticket/4372/10737.patch?format=raw
Loading: [.]
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg status
cd "/home/was/build/sage-3.2.1.alpha1/devel/sage" && hg import   "/home/was/.sage/temp/sage/25372/tmp_2.patch"
applying /home/was/.sage/temp/sage/25372/tmp_2.patch
patching file sage/rings/number_field/totallyreal_dsage.py
Hunk #1 FAILED at 296
1 out of 1 hunk FAILED -- saving rejects to file sage/rings/number_field/totallyreal_dsage.py.rej
abort: patch failed to apply
---

was@sage:~/build/sage-3.2.1.alpha1$ more devel/sage/sage/rings/number_field/totallyreal_dsage.py.rej 
--- totallyreal_dsage.py
+++ totallyreal_dsage.py
@@ -297,7 +297,7 @@

                     # Add the timings.
                     self.cputime += job[1].cpu_time
-                    self.walltime += job[1].wall_time
+                    self.walltime += job[1].wall_time.seconds

                     if write_result:
                         fsock = open(filename_start + str(job[0]).replace(' ','') + '.out', 'w')
```

Looks easy to fix... so I fix it.  No problem.

I then enable doctesting and try the tests, but they totally hang in line 60:

```
Trying:
    dsage.worker()###line 60:_sage_    >>> dsage.worker()
Expecting:
    [...]
2008-11-28 17:54:57-0800 [-] Log opened.
2008-11-28 17:54:57-0800 [-] Log opened.
2008-11-28 17:54:57-0800 [-] Logging to file:  /home/was/.sage/dsage/worker.log
2008-11-28 17:54:57-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
2008-11-28 17:54:57-0800 [-] ==================================================
2008-11-28 17:54:57-0800 [-] DSAGE Worker
2008-11-28 17:54:57-0800 [-] Started with PID: 25788
2008-11-28 17:54:57-0800 [-] Connecting to localhost:8081
2008-11-28 17:54:57-0800 [-] Using SSL: True
2008-11-28 17:54:57-0800 [-] ==================================================
2008-11-28 17:54:57-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 2 seconds
2008-11-28 17:54:57-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
2008-11-28 17:55:00-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
2008-11-28 17:55:00-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 7 seconds
2008-11-28 17:55:00-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
2008-11-28 17:55:07-0800 [-] Starting factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
2008-11-28 17:55:07-0800 [Uninitialized] <gnutls.interfaces.twisted.TLSConnector instance at 0x2aab35eaa830> will retry in 22 seconds
2008-11-28 17:55:07-0800 [Uninitialized] Stopping factory <sage.dsage.twisted.pb.ClientFactory instance at 0x2aab35eaa710>
[waited 20 minutes and it is stuck hard]
```

I delete ~/.sage/dsage and try again.  Doctesting finishes with some errors:

```
was@sage:~/build/sage-3.2.1.alpha1$ ./sage -t devel/sage/sage/rings/number_field/totallyreal_dsage.py
sage -t  devel/sage/sage/rings/number_field/totallyreal_dsage.pyGoing into testing mode...
Adding testing client...
2008-11-28 18:12:33-0800 [-] Log opened.
2008-11-28 18:12:33-0800 [-] Log opened.
2008-11-28 18:12:33-0800 [-] Logging to file:  /home/was/.sage/dsage/worker.log
2008-11-28 18:12:33-0800 [-] Traceback (most recent call last):
2008-11-28 18:12:33-0800 [-]   File "/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py", line 1039, in <module>
2008-11-28 18:12:33-0800 [-]     main()
2008-11-28 18:12:33-0800 [-]   File "/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py", line 1026, in main
2008-11-28 18:12:33-0800 [-]     privkey_file=options.privkey_file)
2008-11-28 18:12:33-0800 [-]   File "/home/was/build/sage-3.2.1.alpha1/local/bin/dsage_worker.py", line 734, in __init__
2008-11-28 18:12:33-0800 [-]     self.pubkey = keys.Key.fromFile(self.pubkey_file)
2008-11-28 18:12:33-0800 [-]   File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/conch/ssh/keys.py", line 60, in fromFile
2008-11-28 18:12:33-0800 [-]     return Class.fromString(file(filename, 'rb').read(), type, passphrase)
2008-11-28 18:12:33-0800 [-] IOError: [Errno 2] No such file or directory: '/home/was/.sage/dsage/dsage_key.pub'
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 51:
    sage: dsage.setup_all()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[2]>", line 1, in <module>
        dsage.setup_all()###line 51:
    sage: dsage.setup_all()
    AttributeError: 'DistributedSage' object has no attribute 'setup_all'
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 53:
    sage: dsage.server()
Expected:
    [...]
Got:
    Going into testing mode...
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 58:
    sage: dsage.setup_worker()
Expected:
    [...]
Got:
    Worker configuration finished.
    <BLANKLINE>
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 60:
    sage: dsage.worker()
Expected:
    [...]
Got nothing
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 65:
    sage: Dtr = totallyreal_dsage()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_1[6]>", line 1, in <module>
        Dtr = totallyreal_dsage()###line 65:
    sage: Dtr = totallyreal_dsage()
      File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/sage/rings/number_field/totallyreal_dsage.py", line 69, in __init__
        self.D = DSage()
    NameError: global name 'DSage' is not defined
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 94:
    sage: Dtr.enumerate(6, 15^6, 4)
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[2]>", line 1, in <module>
        Dtr.enumerate(Integer(6), Integer(15)**Integer(6), Integer(4))###line 94:
    sage: Dtr.enumerate(6, 15^6, 4)
    NameError: name 'Dtr' is not defined
**********************************************************************
File "/home/was/build/sage-3.2.1.alpha1/devel/sage/sage/rings/number_field/totallyreal_dsage.py", line 96:
    sage: Dtr.compile_fields()
Exception raised:
    Traceback (most recent call last):
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/home/was/build/sage-3.2.1.alpha1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_2[3]>", line 1, in <module>
        Dtr.compile_fields()###line 96:
    sage: Dtr.compile_fields()
    NameError: name 'Dtr' is not defined
**********************************************************************
2 items had failures:
   5 of   7 in __main__.example_1
   2 of   4 in __main__.example_2
***Test Failed*** 7 failures.
For whitespace errors, see the file /home/was/build/sage-3.2.1.alpha1/tmp/.doctest_totallyreal_dsage.pyTraceback (most recent call last):
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py", line 614, in run
    runApp(config)
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/scripts/twistd.py", line 23, in runApp
    _SomeApplicationRunner(config).run()
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py", line 330, in run
    self.application = self.createOrGetApplication()
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py", line 416, in createOrGetApplication
    application = getApplication(self.config, passphrase)
--- <exception caught here> ---
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/app.py", line 427, in getApplication
    application = service.loadApplication(filename, style, passphrase)
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/application/service.py", line 368, in loadApplication
    application = sob.loadValueFromFile(filename, 'application', passphrase)
  File "/home/was/build/sage-3.2.1.alpha1/local/lib/python2.5/site-packages/Twisted-8.1.0-py2.5-linux-x86_64.egg/twisted/persisted/sob.py", line 214, in loadValueFromFile
    exec fileObj in d, d
  File "dsage_server.tac", line 130, in <module>
    dsage_server, dsage_server_port, ssl = start_dsage_server(dsage_service)
  File "dsage_server.tac", line 93, in start_dsage_server
    cert = X509Certificate(open(SSL_CERT).read())
exceptions.IOError: [Errno 2] No such file or directory: '/home/was/.sage/dsage/pubcert.pem'

Failed to load application: [Errno 2] No such file or directory: '/home/was/.sage/dsage/pubcert.pem'


	 [3.6 s]
exit code: 1024
 
----------------------------------------------------------------------
The following tests failed:


	sage -t  devel/sage/sage/rings/number_field/totallyreal_dsage.py
Total time for all tests: 3.6 seconds

```


... so I try

```
sage: dsage.setup()
```

and try doctesting again and it hangs.


Any thoughts?



---

archive/issue_comments_032087.json:
```json
{
    "body": "Replying to [comment:4 was]:\n\nI'm not sure totallyreal_dsage has ever had its doctests pass.  I see some error messages are because dsage has even changed since the doctests were written.\n\nI'd like to keep this as nodoctest; it will be nontrivial to make the code easily usable to others, and yet I'd like to keep the code updated with my changes.\n\nJV",
    "created_at": "2008-11-30T02:46:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32087",
    "user": "https://github.com/jvoight"
}
```

Replying to [comment:4 was]:

I'm not sure totallyreal_dsage has ever had its doctests pass.  I see some error messages are because dsage has even changed since the doctests were written.

I'd like to keep this as nodoctest; it will be nontrivial to make the code easily usable to others, and yet I'd like to keep the code updated with my changes.

JV



---

archive/issue_comments_032088.json:
```json
{
    "body": "As of Sage 4.3.1, ticket #7975 removed dsage from the standard spkg repository. I'm closing this ticket as wontfix. If there's a need for using dsage, one could make dsage an optional package with doctests marked as optional.",
    "created_at": "2010-02-02T06:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32088",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

As of Sage 4.3.1, ticket #7975 removed dsage from the standard spkg repository. I'm closing this ticket as wontfix. If there's a need for using dsage, one could make dsage an optional package with doctests marked as optional.



---

archive/issue_comments_032089.json:
```json
{
    "body": "Resolution: wontfix",
    "created_at": "2010-02-02T06:37:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/4372#issuecomment-32089",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: wontfix



---

archive/issue_events_009890.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-02T06:37:28Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4372#event-9890"
}
```



---

archive/issue_events_009891.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2010-02-02T06:37:28Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/4372",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/4372#event-9891"
}
```
