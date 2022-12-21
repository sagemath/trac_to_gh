# Issue 8978: Sage doesn't build on (64bit) OpenSuse 11.2

Issue created by migration from Trac.

Original creator: GeorgSWeber

Original creation time: 2010-05-16 13:09:09

Assignee: drkirkby

CC:  leif dimpase

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


---

Comment by GeorgSWeber created at 2010-05-20 21:27:30

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

Comment by leif created at 2010-05-21 01:49:18

Replying to [comment:1 GeorgSWeber]:
> {{{
> ... move the math library link option "-lm" somewhere *after*
> the object file "nb.o", but before (I did it *right* before) the last
> "-o test"". ...
> }}}

Just for the record, the position of `-o foo` is irrelevant; it's usually safe to put libraries (in the right order if appropriate, perhaps interspersed with `-L`s) just at the end of the line.


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Outdated spkg or build system ticket, should be closed


---

Comment by mkoeppe created at 2020-08-17 16:38:58

Changing status from new to needs_review.


---

Comment by chapoton created at 2020-09-13 07:27:24

Resolution: invalid
