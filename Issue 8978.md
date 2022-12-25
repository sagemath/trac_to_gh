# Issue 8978: Sage doesn't build on (64bit) OpenSuse 11.2

archive/issues_008978.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  @nexttime @dimpase\n\nThere has been a recent report about Sage not building on (64bit) OpenSuse 11., see \n\nhttp://groups.google.com/group/sage-devel/browse_thread/thread/6947016a2d3f664e#\n\nOne issue is readline, and if one looks at the following snippet from the readline-6.0.p1 spkg-install:\n\n```\nif [ -f /etc/SuSE-release ]; then\n    if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then\n        echo \"OpenSUSE 11.1 detected\"\n        if [ -d /usr/include/readline/ ]; then\n            echo \"The development version of libreadline is installed -> copying\"\n            if [ `uname -p` = \"x86_64\" ]; then\n                cp /lib64/libreadline.so.* \"$SAGE_LOCAL\"/lib\n            else\n                cp /lib/libreadline.so.* \"$SAGE_LOCAL\"/lib\n            fi\n            cp -r /usr/include/readline  \"$SAGE_LOCAL\"/include\n            exit 0\n```\n\nit seems clear why this did work for OpenSuse 11.1 --- but not OpenSuse 11.2.\nThe user report mentioned also a problem with building Symmetrica (probably $SAGE64 is not set, but should).\nMaybe there are even more problems lurking.\n\nCan someone confirm these issues (I don't have access to a 64bit OpenSuse 11.2 installation myself)?\n\nIssue created by migration from https://trac.sagemath.org/ticket/8978\n\n",
    "created_at": "2010-05-16T13:09:09Z",
    "labels": [
        "component: porting",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Sage doesn't build on (64bit) OpenSuse 11.2",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8978",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```
Assignee: drkirkby

CC:  @nexttime @dimpase

There has been a recent report about Sage not building on (64bit) OpenSuse 11., see 

http://groups.google.com/group/sage-devel/browse_thread/thread/6947016a2d3f664e#

One issue is readline, and if one looks at the following snippet from the readline-6.0.p1 spkg-install:

```
if [ -f /etc/SuSE-release ]; then
    if [ `grep 11.1 /etc/SuSE-release > /dev/null; echo $?` -eq 0 ]; then
        echo "OpenSUSE 11.1 detected"
        if [ -d /usr/include/readline/ ]; then
            echo "The development version of libreadline is installed -> copying"
            if [ `uname -p` = "x86_64" ]; then
                cp /lib64/libreadline.so.* "$SAGE_LOCAL"/lib
            else
                cp /lib/libreadline.so.* "$SAGE_LOCAL"/lib
            fi
            cp -r /usr/include/readline  "$SAGE_LOCAL"/include
            exit 0
```

it seems clear why this did work for OpenSuse 11.1 --- but not OpenSuse 11.2.
The user report mentioned also a problem with building Symmetrica (probably $SAGE64 is not set, but should).
Maybe there are even more problems lurking.

Can someone confirm these issues (I don't have access to a 64bit OpenSuse 11.2 installation myself)?

Issue created by migration from https://trac.sagemath.org/ticket/8978





---

archive/issue_comments_082701.json:
```json
{
    "body": "Update:\n\nIt turned out (see the above thread) the Symmetrica spkg needed a change to its makefile:\n\n```\n... move the math library link option \"-lm\" somewhere *after*\nthe object file \"nb.o\", but before (I did it *right* before) the last\n\"-o test\"\". ...\n```\n\nand also applying #8844 was necessary. With these three changes (new readline.spkg, new symmetrica.spkg, patched module_list.py), Sage seems to build and start up the Sage interpreter OK. Starting the Sage notebook seems to have one more issue left:\n\n```\nI am now seeing an error message when starting the sage notebook - see below.\n\nIf I display http://localhost:8000 instead of\nhttp://localhost:8000/?startup_token=ae62addaf110060a2765c595ea17d16\nthe notebook works OK.\nBest, Paul\n\n> ./sage -notebook\n\n----------------------------------------------------------------------\n----------------------------------------------------------------------\n| Sage Version 4.4.1, Release Date: 2010-05-02                       |\n| Type notebook() for the GUI, and license() for information.        |\nPlease wait while the Sage Notebook server starts...\n...\nThe notebook files are stored in: sage_notebook.sagenb\n**************************************************\n*                                                *\n* Open your web browser to http://localhost:8000 *\n*                                                *\n**************************************************\n2010-05-21 01:03:09+1000 [-] Log opened.\n2010-05-21 01:03:09+1000 [-] twistd 9.0.0\n(/home/leopardi/src/Sage/sage-4.4.1/local/bin/python 2.6.4) starting up.\n2010-05-21 01:03:09+1000 [-] reactor class:\ntwisted.internet.selectreactor.SelectReactor.\n2010-05-21 01:03:09+1000 [-] twisted.web2.channel.http.HTTPFactory starting on\n8000\n2010-05-21 01:03:09+1000 [-] Starting factory\n<twisted.web2.channel.http.HTTPFactory instance at 0x3e25ab8>\n<unknown program name>(24368)/ ClientApp::doIt: Creating ClientApp\nkioclient(24368) ClientApp::kde_open:\nKUrl(\"http://localhost:8000/?startup_token=ae62addaf110060a2765c595ea17d16\")\nkioclient(24368)/kdecore (KSycoca): Trying to open ksycoca from  \n\"/var/tmp/kdecache-leopardi/ksycoca4\"\nkioclient(24368) KSharedUiServerProxy::KSharedUiServerProxy: kuiserver\nregistered\n2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1]\n/home/leopardi/src/Sage/sage-4.4.1/local/lib/python2.6/site-\npackages/twisted/internet/defer.py:262: exceptions.DeprecationWarning: Don't\npass strings (like 'Bad token') to failure.Failure (replacing with a\nDefaultException).\n2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1] Exception rendering:\n2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1] Unhandled Error\n        Traceback (most recent call last):\n        Failure: twisted.python.failure.DefaultException: Bad token \n```\n",
    "created_at": "2010-05-20T21:27:30Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8978#issuecomment-82701",
    "user": "https://trac.sagemath.org/admin/accounts/users/GeorgSWeber"
}
```

Update:

It turned out (see the above thread) the Symmetrica spkg needed a change to its makefile:

```
... move the math library link option "-lm" somewhere *after*
the object file "nb.o", but before (I did it *right* before) the last
"-o test"". ...
```

and also applying #8844 was necessary. With these three changes (new readline.spkg, new symmetrica.spkg, patched module_list.py), Sage seems to build and start up the Sage interpreter OK. Starting the Sage notebook seems to have one more issue left:

```
I am now seeing an error message when starting the sage notebook - see below.

If I display http://localhost:8000 instead of
http://localhost:8000/?startup_token=ae62addaf110060a2765c595ea17d16
the notebook works OK.
Best, Paul

> ./sage -notebook

----------------------------------------------------------------------
----------------------------------------------------------------------
| Sage Version 4.4.1, Release Date: 2010-05-02                       |
| Type notebook() for the GUI, and license() for information.        |
Please wait while the Sage Notebook server starts...
...
The notebook files are stored in: sage_notebook.sagenb
**************************************************
*                                                *
* Open your web browser to http://localhost:8000 *
*                                                *
**************************************************
2010-05-21 01:03:09+1000 [-] Log opened.
2010-05-21 01:03:09+1000 [-] twistd 9.0.0
(/home/leopardi/src/Sage/sage-4.4.1/local/bin/python 2.6.4) starting up.
2010-05-21 01:03:09+1000 [-] reactor class:
twisted.internet.selectreactor.SelectReactor.
2010-05-21 01:03:09+1000 [-] twisted.web2.channel.http.HTTPFactory starting on
8000
2010-05-21 01:03:09+1000 [-] Starting factory
<twisted.web2.channel.http.HTTPFactory instance at 0x3e25ab8>
<unknown program name>(24368)/ ClientApp::doIt: Creating ClientApp
kioclient(24368) ClientApp::kde_open:
KUrl("http://localhost:8000/?startup_token=ae62addaf110060a2765c595ea17d16")
kioclient(24368)/kdecore (KSycoca): Trying to open ksycoca from  
"/var/tmp/kdecache-leopardi/ksycoca4"
kioclient(24368) KSharedUiServerProxy::KSharedUiServerProxy: kuiserver
registered
2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1]
/home/leopardi/src/Sage/sage-4.4.1/local/lib/python2.6/site-
packages/twisted/internet/defer.py:262: exceptions.DeprecationWarning: Don't
pass strings (like 'Bad token') to failure.Failure (replacing with a
DefaultException).
2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1] Exception rendering:
2010-05-21 01:03:16+1000 [HTTPChannel,1,127.0.0.1] Unhandled Error
        Traceback (most recent call last):
        Failure: twisted.python.failure.DefaultException: Bad token 
```




---

archive/issue_comments_082702.json:
```json
{
    "body": "Replying to [comment:1 GeorgSWeber]:\n> {{{\n> ... move the math library link option \"-lm\" somewhere *after*\n> the object file \"nb.o\", but before (I did it *right* before) the last\n> \"-o test\"\". ...\n> }}}\n\nJust for the record, the position of `-o foo` is irrelevant; it's usually safe to put libraries (in the right order if appropriate, perhaps interspersed with `-L`s) just at the end of the line.",
    "created_at": "2010-05-21T01:49:18Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8978#issuecomment-82702",
    "user": "https://github.com/nexttime"
}
```

Replying to [comment:1 GeorgSWeber]:
> {{{
> ... move the math library link option "-lm" somewhere *after*
> the object file "nb.o", but before (I did it *right* before) the last
> "-o test"". ...
> }}}

Just for the record, the position of `-o foo` is irrelevant; it's usually safe to put libraries (in the right order if appropriate, perhaps interspersed with `-L`s) just at the end of the line.



---

archive/issue_events_021949.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-08-13T15:35:53Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21949"
}
```



---

archive/issue_events_021950.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-5.12",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21950"
}
```



---

archive/issue_events_021951.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-01-30T21:20:52Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21951"
}
```



---

archive/issue_events_021952.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21952"
}
```



---

archive/issue_events_021953.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-05-06T15:20:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21953"
}
```



---

archive/issue_events_021954.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.3",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21954"
}
```



---

archive/issue_events_021955.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/vbraun_spam",
    "created_at": "2014-08-10T16:51:03Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21955"
}
```



---

archive/issue_comments_082703.json:
```json
{
    "body": "Outdated spkg or build system ticket, should be closed",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8978#issuecomment-82703",
    "user": "https://github.com/mkoeppe"
}
```

Outdated spkg or build system ticket, should be closed



---

archive/issue_events_021956.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-17T16:38:58Z",
    "event": "demilestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-6.4",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21956"
}
```



---

archive/issue_events_021957.json:
```json
{
    "actor": "https://github.com/mkoeppe",
    "created_at": "2020-08-17T16:38:58Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21957"
}
```



---

archive/issue_comments_082704.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2020-08-17T16:38:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8978#issuecomment-82704",
    "user": "https://github.com/mkoeppe"
}
```

Changing status from new to needs_review.



---

archive/issue_events_021958.json:
```json
{
    "actor": "https://github.com/fchapoton",
    "created_at": "2020-09-13T07:27:24Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/8978#event-21958"
}
```



---

archive/issue_comments_082705.json:
```json
{
    "body": "Resolution: invalid",
    "created_at": "2020-09-13T07:27:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8978",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8978#issuecomment-82705",
    "user": "https://github.com/fchapoton"
}
```

Resolution: invalid
