# Issue 3586: twist.py -- doctest doesn't work on some machines due to ports not being open-able

Issue created by migration from https://trac.sagemath.org/ticket/3586

Original creator: was

Original creation time: 2008-07-07 15:29:56

Assignee: failure

On sagemath.org (ubuntu 64-bit opteron)


```

         [7.2 s]
sage -t  devel/sage/sage/server/simple/twist.py             **********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 27:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))###line 27:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
      File "<doctest __main__.example_0[7]>", line 1, in get_url
        def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data###line 23:
    sage: def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/urllib.py", line 82, in urlopen
        return opener.open(url)
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/urllib.py", line 190, in open
        return getattr(self, name)(url)
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/urllib.py", line 325, in open_http
        h.endheaders()
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/httplib.py", line 860, in endheaders
        self._send_output()
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/httplib.py", line 732, in _send_output
        self.send(msg)
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/httplib.py", line 699, in send
        self.connect()
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/httplib.py", line 683, in connect
        raise socket.error, msg
    IOError: [Errno socket error] (111, 'Connection refused')
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 28:
    sage: print "ignore this";  print login_page # random session id
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        print "ignore this";  print login_page # random session id###line 28:
    sage: print "ignore this";  print login_page # random session id
    NameError: name 'login_page' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 33:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[Integer(0)]###line 33:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
    NameError: name 'login_page' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 37:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))###line 37:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 48:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[14]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))###line 48:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 57:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[15]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))###line 57:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 66:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))###line 66:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 70:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))###line 70:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 78:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[19]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))###line 78:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/home2/sage/build/sage-3.0.4.alpha2/tmp/twist.py", line 82:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/home2/sage/build/sage-3.0.4.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[20]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))###line 82:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
1 items had failures:
  10 of  22 in __main__.example_0

```



---

Comment by wjp created at 2008-07-07 17:09:48

It seems that on the machine where this fails for me, this is probably a race condition between the notebook starting and the first connection being made. At least, when I add a sleep(1) after the test_notebook() call, I can no longer reproduce this.

Maybe we should make the notebook server print a small log message when it is ready to receive connections, and make run_notebook wait for that (through pexpect) when fork=True ?


---

Comment by was created at 2008-07-07 18:52:57

wjp is exactly right -- it's a race condition.

I've attached a patch that does what he suggested and it worked 10 times in a row, whereas before the doctest would fail every other time on sagemath.org. 

His suggestion about watching the server log sounds pretty painful to implement, but would be possible. That should be another ticket.


---

Attachment


---

Comment by was created at 2008-07-07 21:46:40

Resolution: fixed


---

Comment by mabshoff created at 2008-07-07 21:51:42

Merged in Sage 3.0.4.rc0
