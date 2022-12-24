# Issue 8435: SageNB 0.7.5.2

archive/issues_008435.json:
```json
{
    "body": "Assignee: was\n\nCC:  jhpalmieri mhansen mvngu robert.marik acleone\n\nCandidates: #5601, #7911, #8141, #8324, #8265, #8387.\n\nIssue created by migration from https://trac.sagemath.org/ticket/8435\n\n",
    "created_at": "2010-03-04T11:11:52Z",
    "labels": [
        "notebook",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.3.4",
    "title": "SageNB 0.7.5.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8435",
    "user": "mpatel"
}
```
Assignee: was

CC:  jhpalmieri mhansen mvngu robert.marik acleone

Candidates: #5601, #7911, #8141, #8324, #8265, #8387.

Issue created by migration from https://trac.sagemath.org/ticket/8435





---

archive/issue_comments_075709.json:
```json
{
    "body": "I'll make a new package after I wake up.",
    "created_at": "2010-03-04T11:12:22Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75709",
    "user": "mpatel"
}
```

I'll make a new package after I wake up.



---

archive/issue_comments_075710.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2010-03-04T22:44:31Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75710",
    "user": "mpatel"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_075711.json:
```json
{
    "body": "Attachment [sagenb-0.7.5.2_selenium_fails.log](tarball://root/attachments/some-uuid/ticket8435/sagenb-0.7.5.2_selenium_fails.log) by acleone created at 2010-03-05 17:28:11\n\nSelenium Failures",
    "created_at": "2010-03-05T17:28:11Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75711",
    "user": "acleone"
}
```

Attachment [sagenb-0.7.5.2_selenium_fails.log](tarball://root/attachments/some-uuid/ticket8435/sagenb-0.7.5.2_selenium_fails.log) by acleone created at 2010-03-05 17:28:11

Selenium Failures



---

archive/issue_comments_075712.json:
```json
{
    "body": "The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.",
    "created_at": "2010-03-06T23:54:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75712",
    "user": "mvngu"
}
```

The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.



---

archive/issue_comments_075713.json:
```json
{
    "body": "I have two other problems (after intallation and sage -t -sagenb)\n\n```\nsage -t  \"local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py\"\n**********************************************************************\nFile \"/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py\", line 688:\n    sage: sage_getsourcelines(matrix, True)[1]\nExpected:\n    34\nGot:\n    33\n**********************************************************************\n1 items had failures:\n   1 of   5 in __main__.example_13\n***Test Failed*** 1 failures.\n\nsage -t  \"local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py\"\n**********************************************************************\nFile \"/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py\", line 2720:\n    sage: color_selector('purple', widget = 'colorpicker')\nExpected:\n    Interact color selector labeled None, with default RGB color (0.50..., 0.0, 0.50...), widget 'colorpicker', and visible input box\nGot:\n    Interact color selector labeled None, with default RGB color (0.5, 0.0, 1.0), widget 'colorpicker', and visible input box\n**********************************************************************\n1 items had failures:\n   1 of   9 in __main__.example_109\n***Test Failed*** 1 failures.\n\n```\n\nto Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(.",
    "created_at": "2010-03-07T18:33:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75713",
    "user": "robert.marik"
}
```

I have two other problems (after intallation and sage -t -sagenb)

```
sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py"
**********************************************************************
File "/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/misc/sageinspect.py", line 688:
    sage: sage_getsourcelines(matrix, True)[1]
Expected:
    34
Got:
    33
**********************************************************************
1 items had failures:
   1 of   5 in __main__.example_13
***Test Failed*** 1 failures.

sage -t  "local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py"
**********************************************************************
File "/opt/sage-4.3.3/local/lib/python2.6/site-packages/sagenb-0.7.5.2-py2.6.egg/sagenb/notebook/interact.py", line 2720:
    sage: color_selector('purple', widget = 'colorpicker')
Expected:
    Interact color selector labeled None, with default RGB color (0.50..., 0.0, 0.50...), widget 'colorpicker', and visible input box
Got:
    Interact color selector labeled None, with default RGB color (0.5, 0.0, 1.0), widget 'colorpicker', and visible input box
**********************************************************************
1 items had failures:
   1 of   9 in __main__.example_109
***Test Failed*** 1 failures.

```

to Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(.



---

archive/issue_comments_075714.json:
```json
{
    "body": "Replying to [comment:6 robert.marik]:\n> to Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(. \n\nI don't think that's true.  I think that William, Tim Dumol, and myself are all pretty comfortable with the code.  I think it's more of any issue that other people haven't put time in trying to work on it.",
    "created_at": "2010-03-07T18:36:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75714",
    "user": "mhansen"
}
```

Replying to [comment:6 robert.marik]:
> to Minh: I think that allmost nobody else than mpatel has deep knowledges of SageNB code :(. 

I don't think that's true.  I think that William, Tim Dumol, and myself are all pretty comfortable with the code.  I think it's more of any issue that other people haven't put time in trying to work on it.



---

archive/issue_comments_075715.json:
```json
{
    "body": "Replying to [comment:6 robert.marik]:\n> I have two other problems (after intallation and sage -t -sagenb)\n\nWhich version of Sage is this?  Those doctest failures sound like consequences of patches to keep up with changes in Sage 4.3.4.alpha0, so you might get errors if you run this version of sagenb with an older version of Sage.",
    "created_at": "2010-03-07T18:41:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75715",
    "user": "jhpalmieri"
}
```

Replying to [comment:6 robert.marik]:
> I have two other problems (after intallation and sage -t -sagenb)

Which version of Sage is this?  Those doctest failures sound like consequences of patches to keep up with changes in Sage 4.3.4.alpha0, so you might get errors if you run this version of sagenb with an older version of Sage.



---

archive/issue_comments_075716.json:
```json
{
    "body": "Replying to [comment:7 mhansen]:\n> \n> I don't think that's true.  I think that William, Tim Dumol, and myself ....\n\nOh sorry, I forgot ...\n\nAnd yes, I tested on the last released Sage - Sage 4.3.3. So sorry for the noise.\n\nRobert",
    "created_at": "2010-03-07T20:28:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75716",
    "user": "robert.marik"
}
```

Replying to [comment:7 mhansen]:
> 
> I don't think that's true.  I think that William, Tim Dumol, and myself ....

Oh sorry, I forgot ...

And yes, I tested on the last released Sage - Sage 4.3.3. So sorry for the noise.

Robert



---

archive/issue_comments_075717.json:
```json
{
    "body": "Replying to [comment:5 mvngu]:\n> The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.\n\nI think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.  Opinions?  (Now sagenb-0.7.5.3 is available, so it should be tested.)",
    "created_at": "2010-03-09T05:54:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75717",
    "user": "jhpalmieri"
}
```

Replying to [comment:5 mvngu]:
> The upgraded package [sagenb-0.7.5.2.spkg](http://sage.math.washington.edu/home/mpatel/trac/8435/sagenb-0.7.5.2.spkg) works for me. All doctests passed. I'm not familiar with the SageNB package, so I invite someone more knowledgeable to review the code changes.

I think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.  Opinions?  (Now sagenb-0.7.5.3 is available, so it should be tested.)



---

archive/issue_comments_075718.json:
```json
{
    "body": "Replying to [comment:11 jhpalmieri]:\n> I think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.\n\nI think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release. Anyway, John's argument convinces me.",
    "created_at": "2010-03-09T05:59:15Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75718",
    "user": "mvngu"
}
```

Replying to [comment:11 jhpalmieri]:
> I think that if all of the relevant tickets have received positive reviews, then people have presumably reviewed the code changes.  So perhaps passing doctests should be good enough for this ticket to be given a positive review.

I think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release. Anyway, John's argument convinces me.



---

archive/issue_comments_075719.json:
```json
{
    "body": "Replying to [comment:12 mvngu]:\n> I think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release.\n\nThis sounds sensible.",
    "created_at": "2010-03-09T06:35:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75719",
    "user": "jhpalmieri"
}
```

Replying to [comment:12 mvngu]:
> I think that is reasonable. In most cases, it is safe for a new SageNB spkg to go into an alpha release. But I would refrain from putting a new SageNB spkg into an rc release.

This sounds sensible.



---

archive/issue_comments_075720.json:
```json
{
    "body": "The Selenium tests passed for me with Firefox 3.5.8 on Linux, but let me know.",
    "created_at": "2010-03-09T06:45:49Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75720",
    "user": "mpatel"
}
```

The Selenium tests passed for me with Firefox 3.5.8 on Linux, but let me know.



---

archive/issue_comments_075721.json:
```json
{
    "body": "Strange - I get the same Selenium failures on 0.7.5.3 as the ones listed above.\n\nMy setup:\n* FF 3.5.8 on Ubuntu 32-bit 9.10\n* Selenium Server 1.0.3 run with `java -jar selenium-server.jar`\n* `sagenb-0.7.5.3/src/sagenb/sagenb/testing$ sage -python run_tests.py`\n* sage version 4.3.4.alpha0\n* SAGENB_VERSION is '0.7.5.3'\n* All doctests pass (`sage -t -sagenb`).",
    "created_at": "2010-03-09T07:14:06Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75721",
    "user": "acleone"
}
```

Strange - I get the same Selenium failures on 0.7.5.3 as the ones listed above.

My setup:
* FF 3.5.8 on Ubuntu 32-bit 9.10
* Selenium Server 1.0.3 run with `java -jar selenium-server.jar`
* `sagenb-0.7.5.3/src/sagenb/sagenb/testing$ sage -python run_tests.py`
* sage version 4.3.4.alpha0
* SAGENB_VERSION is '0.7.5.3'
* All doctests pass (`sage -t -sagenb`).



---

archive/issue_comments_075722.json:
```json
{
    "body": "You're right. I just upgraded to Selenium 1.0.3 (from 1.0.1) and now they don't all pass.  I'll investigate.\n\nTo run the [Selenium](http://seleniumhq.org/) tests with Firefox, check that Java is installed and [download Selenium RC](http://seleniumhq.org/download/):\n\n```sh\nwget http://selenium.googlecode.com/files/selenium-remote-control-1.0.3.zip\nmkdir selenium\ncd selenium\nunzip selenium-remote-control-1.0.3.zip\ncd selenium-server-1.0.3\njava -jar selenium-server.jar\n```\n\nTo run the SageNB tests, I usually do the following, e.g., in a script:\n\n```python\nsage: import sagenb.testing.run_tests as rt\nsage: brow = '*firefox3 /usr/lib64/firefox-3.5.8/firefox'  \nsage: rt.setup_tests('localhost', False, brow)\nsage: rt.run_any()\n```\n\nThe `setup_tests` step may not be necessary, but I think it helps to give the path to the actual Firefox binary.  See docstrings for a few examples.",
    "created_at": "2010-03-09T07:19:04Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75722",
    "user": "mpatel"
}
```

You're right. I just upgraded to Selenium 1.0.3 (from 1.0.1) and now they don't all pass.  I'll investigate.

To run the [Selenium](http://seleniumhq.org/) tests with Firefox, check that Java is installed and [download Selenium RC](http://seleniumhq.org/download/):

```sh
wget http://selenium.googlecode.com/files/selenium-remote-control-1.0.3.zip
mkdir selenium
cd selenium
unzip selenium-remote-control-1.0.3.zip
cd selenium-server-1.0.3
java -jar selenium-server.jar
```

To run the SageNB tests, I usually do the following, e.g., in a script:

```python
sage: import sagenb.testing.run_tests as rt
sage: brow = '*firefox3 /usr/lib64/firefox-3.5.8/firefox'  
sage: rt.setup_tests('localhost', False, brow)
sage: rt.run_any()
```

The `setup_tests` step may not be necessary, but I think it helps to give the path to the actual Firefox binary.  See docstrings for a few examples.



---

archive/issue_comments_075723.json:
```json
{
    "body": "A possibly outdated [comment](http://trac.sagemath.org/sage_trac/ticket/6855#comment:12) about earlier tests with other browsers.",
    "created_at": "2010-03-09T07:23:34Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75723",
    "user": "mpatel"
}
```

A possibly outdated [comment](http://trac.sagemath.org/sage_trac/ticket/6855#comment:12) about earlier tests with other browsers.



---

archive/issue_comments_075724.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2010-03-09T08:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75724",
    "user": "mhansen"
}
```

Resolution: fixed



---

archive/issue_comments_075725.json:
```json
{
    "body": "I'm going to merge 0.7.5.3 into alpha1 since it seems like the issue is more with the Selenium code than the actual SageNB code.  A ticket can be opened for that.",
    "created_at": "2010-03-09T08:04:38Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75725",
    "user": "mhansen"
}
```

I'm going to merge 0.7.5.3 into alpha1 since it seems like the issue is more with the Selenium code than the actual SageNB code.  A ticket can be opened for that.



---

archive/issue_comments_075726.json:
```json
{
    "body": "I agree.  The tests fail because the new Se creates *two* worksheets when we call `selenium.open('/new_worksheet')`.  I don't know if this is a Se bug.",
    "created_at": "2010-03-09T08:53:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8435",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8435#issuecomment-75726",
    "user": "mpatel"
}
```

I agree.  The tests fail because the new Se creates *two* worksheets when we call `selenium.open('/new_worksheet')`.  I don't know if this is a Se bug.
