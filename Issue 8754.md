# Issue 8754: sagenb -- add "how to test" directions to the sagenb README.txt

archive/issues_008754.json:
```json
{
    "body": "Assignee: jason, was\n\nCC:  chapoton\n\n\n```\n1. Doctest: \n       sage -t -sagenb \n2. Run the Selenium test suite:\n       sage -python sagenb/testing/run_tests.py \n\nTo use Selenium, you must visit http://seleniumhq.org/download/ and:\n\n      * Download and extract Selenium RC (\"the Selenium Remote Control\")\n\n      * Run it as follows on Linux:\n             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3\n             $ java -jar selenium-server.jar\n             $ cd /path/to/sagenb-0.8/src/sagenb\n             $ sage  -python sagenb/testing/run_tests.py\n\n      * Run it as follows on OS X:\n             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3\n             $ cd /path/to/sagenb-0.8/src/sagenb\n             $ sage\n             sage: import sagenb.testing.run_tests as rt \n             sage: rt.setup_tests('localhost', False, '*firefox')\n             sage: rt.run_any()\n```\n\n\nThat the instructions for OS X are different is probably a bug. \n\n\n\nIssue created by migration from https://trac.sagemath.org/ticket/8754\n\n",
    "created_at": "2010-04-24T21:00:55Z",
    "labels": [
        "notebook",
        "minor",
        "enhancement"
    ],
    "title": "sagenb -- add \"how to test\" directions to the sagenb README.txt",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8754",
    "user": "was"
}
```
Assignee: jason, was

CC:  chapoton


```
1. Doctest: 
       sage -t -sagenb 
2. Run the Selenium test suite:
       sage -python sagenb/testing/run_tests.py 

To use Selenium, you must visit http://seleniumhq.org/download/ and:

      * Download and extract Selenium RC ("the Selenium Remote Control")

      * Run it as follows on Linux:
             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3
             $ java -jar selenium-server.jar
             $ cd /path/to/sagenb-0.8/src/sagenb
             $ sage  -python sagenb/testing/run_tests.py

      * Run it as follows on OS X:
             $ cd /path/to/selenium-remote-control-1.0.3/selenium-server-1.0.3
             $ cd /path/to/sagenb-0.8/src/sagenb
             $ sage
             sage: import sagenb.testing.run_tests as rt 
             sage: rt.setup_tests('localhost', False, '*firefox')
             sage: rt.run_any()
```


That the instructions for OS X are different is probably a bug. 



Issue created by migration from https://trac.sagemath.org/ticket/8754





---

archive/issue_comments_080081.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-04-25T00:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80081",
    "user": "was"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_080082.json:
```json
{
    "body": "Attachment [trac_8754-sagenb.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.patch) by was created at 2010-04-25 00:41:39",
    "created_at": "2010-04-25T00:41:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80082",
    "user": "was"
}
```

Attachment [trac_8754-sagenb.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.patch) by was created at 2010-04-25 00:41:39



---

archive/issue_comments_080083.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2010-04-25T00:56:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80083",
    "user": "was"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_080084.json:
```json
{
    "body": "Attachment [trac_8754-sagenb.2.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.2.patch) by acleone created at 2010-04-25 01:27:44\n\nAdded a development section.  Replaces the last patch",
    "created_at": "2010-04-25T01:27:44Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80084",
    "user": "acleone"
}
```

Attachment [trac_8754-sagenb.2.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.2.patch) by acleone created at 2010-04-25 01:27:44

Added a development section.  Replaces the last patch



---

archive/issue_comments_080085.json:
```json
{
    "body": "Attachment [trac_8754-sagenb.replaces2.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.replaces2.patch) by acleone created at 2010-05-29 22:29:00\n\nNewest Version.  Added a \"Reviewing Patches\" section.  Apply only this.",
    "created_at": "2010-05-29T22:29:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80085",
    "user": "acleone"
}
```

Attachment [trac_8754-sagenb.replaces2.patch](tarball://root/attachments/some-uuid/ticket8754/trac_8754-sagenb.replaces2.patch) by acleone created at 2010-05-29 22:29:00

Newest Version.  Added a "Reviewing Patches" section.  Apply only this.



---

archive/issue_comments_080086.json:
```json
{
    "body": "Changing status from positive_review to needs_work.",
    "created_at": "2010-07-23T06:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80086",
    "user": "mpatel"
}
```

Changing status from positive_review to needs_work.



---

archive/issue_comments_080087.json:
```json
{
    "body": "Should someone review the latest patch?  I noticed two minor problems:\n\n* `dwnload`\n* An extra `*` in `b) * Run it as follows:`\n\nAlso, should the reviewing section first refer in some way to steps 1,2,3, and/or 6 of the development section?",
    "created_at": "2010-07-23T06:44:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80087",
    "user": "mpatel"
}
```

Should someone review the latest patch?  I noticed two minor problems:

* `dwnload`
* An extra `*` in `b) * Run it as follows:`

Also, should the reviewing section first refer in some way to steps 1,2,3, and/or 6 of the development section?



---

archive/issue_comments_080088.json:
```json
{
    "body": "Reported \"upstream\" at https://github.com/sagemath/sagenb/issues/221",
    "created_at": "2014-09-16T21:34:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80088",
    "user": "kcrisman"
}
```

Reported "upstream" at https://github.com/sagemath/sagenb/issues/221



---

archive/issue_comments_080089.json:
```json
{
    "body": "Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80089",
    "user": "mkoeppe"
}
```

Proposing to close all sagenb tickets as outdated, so that all remaining open tickets in the notebook component are about the Jupyter notebook.



---

archive/issue_comments_080090.json:
```json
{
    "body": "Changing status from needs_work to needs_review.",
    "created_at": "2020-08-18T00:36:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80090",
    "user": "mkoeppe"
}
```

Changing status from needs_work to needs_review.



---

archive/issue_comments_080091.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-08-19T12:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8754",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8754#issuecomment-80091",
    "user": "chapoton"
}
```

Resolution: invalid
