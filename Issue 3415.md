# Issue 3415: sage-3.0.3.alpha2 -- clean test of simple.py fails badly on osx ppc (fermat)

Issue created by migration from Trac.

Original creator: was

Original creation time: 2008-06-13 14:29:45

Assignee: boothby


```
fermat:sage-3.0.3.alpha2 was$ ./sage -t devel/sage/sage/server/simple/twist.py
sage -t  devel/sage/sage/server/simple/twist.py             **********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 26:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[8]>", line 1, in <module>
        login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))###line 26:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
      File "<doctest __main__.example_0[7]>", line 1, in get_url
        def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data###line 22:
    sage: def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/urllib.py", line 82, in urlopen
        return opener.open(url)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/urllib.py", line 190, in open
        return getattr(self, name)(url)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/urllib.py", line 325, in open_http
        h.endheaders()
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/httplib.py", line 860, in endheaders
        self._send_output()
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/httplib.py", line 732, in _send_output
        self.send(msg)
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/httplib.py", line 699, in send
        self.connect()
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/httplib.py", line 683, in connect
        raise socket.error, msg
    IOError: [Errno socket error] (60, 'Operation timed out')
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 27:
    sage: print "ignore this";  print login_page # random session id
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[9]>", line 1, in <module>
        print "ignore this";  print login_page # random session id###line 27:
    sage: print "ignore this";  print login_page # random session id
    NameError: name 'login_page' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 32:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[Integer(0)]###line 32:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
    NameError: name 'login_page' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 35:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))###line 35:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 46:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[13]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))###line 46:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 55:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[14]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))###line 55:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 64:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[15]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))###line 64:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 68:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))###line 68:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 76:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))###line 76:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/Users/was/build/sage-3.0.3.alpha2/tmp/twist.py", line 80:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/Users/was/build/sage-3.0.3.alpha2/local/lib/python2.5/doctest.py", line 1228, in __run
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[19]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))###line 80:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
1 items had failures:
  10 of  21 in __main__.example_0
***Test Failed*** 10 failures.
For whitespace errors, see the file /Users/was/build/sage-3.0.3.alpha2/tmp/.doctest_twist.py
         [89.2 s]
exit code: 1024

----------------------------------------------------------------------
The following tests failed:


        sage -t  devel/sage/sage/server/simple/twist.py
```



---

Comment by was created at 2008-06-13 14:29:56

Changing assignee from boothby to robertwb.


---

Attachment

I knew I was getting into trouble as soon as I tried to write doctests for a live notebook... 

The above patch may not fix the issue, but it will help debut what is going on. It looks like it was unable to open a port to start the notebook (firewall issue?).


---

Comment by was created at 2008-06-13 22:32:08

In retrospect I think the network on the given test machine (at Harvard) is very foobar'd. 
So apply this safe package and close this.


---

Comment by mabshoff created at 2008-06-15 18:39:31

Merged in Sage 3.0.3.rc0


---

Comment by mabshoff created at 2008-06-15 18:39:31

Resolution: fixed
