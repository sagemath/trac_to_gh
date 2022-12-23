# Issue 1871: wiki -- pressing control-c just starts another copy running

Issue created by migration from https://trac.sagemath.org/ticket/1871

Original creator: was

Original creation time: 2008-01-20 22:15:06

Assignee: was

The wiki() command on OSX is broken.  On Linux (at least on sage.math), hitting control-c after starting the wiki just starts it again on the next port.  Very bad:

```
was@sage:~/tmp$ sage
----------------------------------------------------------------------
----------------------------------------------------------------------
| SAGE Version 2.10, Release Date: 2008-01-18                        |
| Type notebook() for the GUI, and license() for information.        |
wiki(sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
2008/01/20 15:09 -0700 [-] Log opened.
2008/01/20 15:09 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up
2008/01/20 15:09 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/01/20 15:09 -0700 [-] Loading twistedconf.py...
2008/01/20 15:09 -0700 [-] Loaded.
2008/01/20 15:09 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2008/01/20 15:09 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2ab6a72409e0>
2008/01/20 15:09 -0700 [-] set uid/gid 1000/1000
2008/01/20 15:11 -0700 [-] Received SIGINT, shutting down.
2008/01/20 15:11 -0700 [-] (Port 9000 Closed)
2008/01/20 15:11 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2ab6a72409e0>
2008/01/20 15:11 -0700 [-] Main loop terminated.
2008/01/20 15:11 -0700 [-] Server Shut Down.
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9001 *
*                                                *
**************************************************
2008/01/20 15:11 -0700 [-] Log opened.
2008/01/20 15:11 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up
2008/01/20 15:11 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/01/20 15:11 -0700 [-] Loading twistedconf.py...
2008/01/20 15:11 -0700 [-] Loaded.
2008/01/20 15:11 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9001
2008/01/20 15:11 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2b019cbb59e0>
2008/01/20 15:11 -0700 [-] set uid/gid 1000/1000
2008/01/20 15:11 -0700 [-] Received SIGINT, shutting down.
2008/01/20 15:11 -0700 [-] (Port 9001 Closed)
2008/01/20 15:11 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2b019cbb59e0>
2008/01/20 15:11 -0700 [-] Main loop terminated.
2008/01/20 15:11 -0700 [-] Server Shut Down.
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9002 *
*                                                *
**************************************************
2008/01/20 15:11 -0700 [-] Log opened.
2008/01/20 15:11 -0700 [-] twistd 2.5.0 (/home/was/s/local/bin/python 2.5.1) starting up
2008/01/20 15:11 -0700 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2008/01/20 15:11 -0700 [-] Loading twistedconf.py...
2008/01/20 15:11 -0700 [-] Loaded.
2008/01/20 15:11 -0700 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9002
2008/01/20 15:11 -0700 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2b578a4b49e0>
2008/01/20 15:11 -0700 [-] set uid/gid 1000/1000
2008/01/20 15:12 -0700 [-] Received SIGINT, shutting down.
2008/01/20 15:12 -0700 [-] (Port 9002 Closed)
2008/01/20 15:12 -0700 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x2b578a4b49e0>
2008/01/20 15:12 -0700 [-] Main loop terminated.
2008/01/20 15:12 -0700 [-] Server Shut Down.
Port 9000 is already in use.  Trying next port...
**************************************************
*                                                *
* Open your web browser to http://localhost:9003 *
*                                                *
**************************************************
...

```



---

Comment by was created at 2008-02-05 14:57:25

Also, we should upgrade to the newest version of the wiki software:


```
Greetings Sages!

Was wondering if I might put in a request to have the moin wiki that
is bundled with sage upgraded to version 1.6.1?   Among all other
other features/bugfixes introduced since version 1.5.7p2 is
WikiSynchronization, which I think is extremely cool!

Thanks very much.  I truly appreciate all of the wonderful work the
sage team is doing.

Regards,

--gordon
```



---

Comment by rlm created at 2008-02-10 03:17:28

See also the details in #596 - a duplicate of this ticket.


---

Comment by rlm created at 2009-03-07 00:02:09

These both depend on #3693.


---

Comment by wdj created at 2009-06-19 22:21:15

Using an intel macbook running 10.4, I cannot get both patches to apply, nor can I get only the 2nd patch to apply. The first patch fixes the problem (that once you start wiki() running, ctl-c kills the wiki server running on localhost:9000 but also starts it running on localhost:9001.) However, ctl-c also causes an error:


```
sage: wiki()
**************************************************
*                                                *
* Open your web browser to http://localhost:9000 *
*                                                *
**************************************************
2009-06-19 18:06:30-0400 [-] Log opened.
2009-06-19 18:06:30-0400 [-] twistd 8.1.0 (/Users/davidjoyner/sagefiles/sage-4.0.2.rc3/local/bin/python 2.5.4) starting up
2009-06-19 18:06:30-0400 [-] reactor class: <class 'twisted.internet.selectreactor.SelectReactor'>
2009-06-19 18:06:30-0400 [-] MoinMoin.server.twistedmoin.MoinSite starting on 9000
2009-06-19 18:06:30-0400 [-] Starting factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1632210>
2009-06-19 18:06:30-0400 [-] set uid/gid 501/501
2009-06-19 18:07:06-0400 [HTTPChannel,0,127.0.0.1] /Users/davidjoyner/sagefiles/sage-4.0.2.rc3/local/lib/python2.5/site-packages/MoinMoin/request.py:1485: exceptions.DeprecationWarning: IPv4Address.__getitem__ is deprecated.  Use attributes instead.
2009-06-19 18:07:06-0400 [-] 127.0.0.1 - - [19/Jun/2009:22:07:05 +0000] "GET / HTTP/1.1" 404 7613 "-" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:06-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:05 +0000] "GET /wiki/common/js/common.js HTTP/1.1" 200 3892 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:06-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:05 +0000] "GET /wiki/modern/css/common.css HTTP/1.1" 200 7048 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:06-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:05 +0000] "GET /wiki/modern/css/screen.css HTTP/1.1" 200 7558 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:06-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:05 +0000] "GET /wiki/modern/css/print.css HTTP/1.1" 200 775 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:07-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:06 +0000] "GET /wiki/modern/css/projection.css HTTP/1.1" 200 587 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:07-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:06 +0000] "GET /wiki/common/moinmoin.png HTTP/1.1" 200 6190 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
2009-06-19 18:07:09-0400 [HTTPChannel,0,127.0.0.1] 127.0.0.1 - - [19/Jun/2009:22:07:08 +0000] "GET /favicon.ico HTTP/1.1" 200 1718 "http://localhost:9000/" "Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_11; en) AppleWebKit/530.17 (KHTML, like Gecko) Version/4.0 Safari/530.17"
^C2009-06-19 18:07:21-0400 [-] Received SIGINT, shutting down.
2009-06-19 18:07:21-0400 [-] (Port 9000 Closed)
2009-06-19 18:07:21-0400 [-] Stopping factory <MoinMoin.server.twistedmoin.MoinSite instance at 0x1632210>
2009-06-19 18:07:21-0400 [-] Main loop terminated.
2009-06-19 18:07:21-0400 [-] Server Shut Down.
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)

/Users/davidjoyner/.sage/temp/zeus.home/618/_Users_davidjoyner__sage_init_sage_0.py in <module>()

/Users/davidjoyner/sagefiles/sage-4.0.2.rc3/local/lib/python2.5/site-packages/sage/server/wiki/moin.pyc in wiki(directory, port, address, threads)
     98             break
     99     
--> 100     os.chdir(original_path)
    101     return True
    102 

NameError: global name 'original_path' is not defined
sage: 
```


Is this the intended behavior?

change "needs review" -> "needs work" since it seems that the second patch should apply and I suspect that Robert Miller did not intend this behavior.


---

Attachment

Apply only this patch


---

Comment by rlm created at 2009-06-19 22:58:26

Hopefully this patch won't rot for another 3 months! :)


---

Comment by wdj created at 2009-06-20 01:25:51

Applies okay to 4.0.2.rc3 and passes sage -testall on an intel macbook running 10.4. Corrects the bug, as advertised, and exits without raising an error.


---

Comment by rlm created at 2009-06-24 09:48:27

Resolution: fixed
