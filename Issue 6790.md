# Issue 6790: 12 doctest failures in devel/sage/sage/server/simple/twist.py

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-08-20 22:28:19

Assignee: boothby

On Solaris 10 update 7 (SPARC), the following test failed. Both ECL and Maxima were updated - ECL version 9.8.4, Maxima version 5.19.1. Sage was built with gcc 4.4.1

```
----------------------------------------------------------------------
----------------------------------------------------------------------
Thu Aug 20 20:02:37 BST 2009
dsage-trial tmp directory doesn't exist - creating ...
This script will run the unit tests for DSage
```

<SNIP>
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |

```
sage -t  "devel/sage/sage/server/simple/twist.py"
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 26:
    sage: nb = test_notebook(passwd, secure=False, address='localhost', port=port, verbose=True) #doctest: +ELLIPSIS
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[6]>", line 1, in <module>
        nb = test_notebook(passwd, secure=False, address='localhost', port=port, verbose=True) #doctest: +ELLIPSIS###line 26:
    sage: nb = test_notebook(passwd, secure=False, address='localhost', port=port, verbose=True) #doctest: +ELLIPSIS
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/sage/server/notebook/notebook_object.py", line 214, in test_notebook        p.expect("Starting factory")
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 912, in expect
        return self.expect_list(compiled_pattern_list, timeout, searchwindowsize)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python/site-packages/pexpect.py", line 989, in expect_list
        raise TIMEOUT (str(e) + '\n' + str(self))
    TIMEOUT: Timeout exceeded in read_nonblocking().
    <pexpect.spawn instance at 0x3b83dc8>
    version: 2.0 ($Revision: 1.151 $)
    command: /export/home/drkirkby/sage/sage-4.1.1/sage
    args: ['/export/home/drkirkby/sage/sage-4.1.1/sage', '-twistd', '--pidfile=tmpcsoWuM/twistd.pid', '-ny', 'tmpcsoWuM/twistedconf.tac']
    patterns:
        Starting factory
    buffer (last 100 chars):
    before (last 100 chars): y:12: DeprecationWarning: the md5 module is deprecated; use hashlib instead
      import os, md5, sys

    after: <class 'pexpect.TIMEOUT'>
    match: None
    match_index: None
    exitstatus: None
    flag_eof: 0
    pid: 12091
    child_fd: 3
    timeout: 30
    delimiter: <class 'pexpect.EOF'>
    logfile: None
    maxread: 2000
    searchwindowsize: None
    delaybeforesend: 0.1
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 40:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[10]>", line 1, in <module>
        login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))###line 40:
    sage: login_page = get_url('http://localhost:%s/simple/login?username=admin&password=%s' % (port, passwd))
      File "<doctest __main__.example_0[8]>", line 1, in get_url
        def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data###line 35:
    sage: def get_url(url): h = urllib.urlopen(url); data = h.read(); h.close(); return data
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/urllib.py", line 87, in urlopen
        return opener.open(url)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/urllib.py", line 203, in open
        return getattr(self, name)(url)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/urllib.py", line 342, in open_http
        h.endheaders()
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/httplib.py", line 868, in endheaders
        self._send_output()
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/httplib.py", line 740, in _send_output
        self.send(msg)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/httplib.py", line 699, in send
        self.connect()
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/httplib.py", line 683, in connect
        self.timeout)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/lib/python2.6/socket.py", line 514, in create_connection
        raise error, msg
    IOError: [Errno socket error] [Errno 128] Network is unreachable
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 41:
    sage: print "ignore this";  print login_page # random session id
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[11]>", line 1, in <module>
        print "ignore this";  print login_page # random session id###line 41:
    sage: print "ignore this";  print login_page # random session id
    NameError: name 'login_page' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 46:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[12]>", line 1, in <module>
        session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[Integer(0)]###line 46:
    sage: session = re.match(r'.*"session": "([^"]*)"', login_page, re.DOTALL).groups()[0]
    NameError: name 'login_page' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[14]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))###line 51:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=2*2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 69:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[16]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))###line 69:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=factor(%s)&timeout=0.1' % (port, session, n))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 79:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[17]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))###line 79:
    sage: print get_url('http://localhost:%s/simple/status?session=%s&cell=2' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 89:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[18]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))###line 89:
    sage: _ = get_url('http://localhost:%s/simple/interrupt?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[20]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))###line 95:
    sage: print get_url('http://localhost:%s/simple/compute?session=%s&code=%s' % (port, session, urllib.quote(code)))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[21]>", line 1, in <module>
        print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))###line 103:
    sage: print get_url('http://localhost:%s/simple/file?session=%s&cell=3&file=a.txt' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 108:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[22]>", line 1, in <module>
        _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))###line 108:
    sage: _ = get_url('http://localhost:%s/simple/logout?session=%s' % (port, session))
    NameError: name 'session' is not defined
**********************************************************************
File "/export/home/drkirkby/sage/sage-4.1.1/devel/sage/sage/server/simple/twist.py", line 109:
    sage: nb.dispose()
Exception raised:
    Traceback (most recent call last):
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1231, in run_one_test
        self.run_one_example(test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/sagedoctest.py", line 38, in run_one_example
        OrigDocTestRunner.run_one_example(self, test, example, filename, compileflags)
      File "/export/home/drkirkby/sage/sage-4.1.1/local/bin/ncadoctest.py", line 1172, in run_one_example
        compileflags, 1) in test.globs
      File "<doctest __main__.example_0[23]>", line 1, in <module>
        nb.dispose()###line 109:
    sage: nb.dispose()
    NameError: name 'nb' is not defined
**********************************************************************
1 items had failures:
  12 of  24 in __main__.example_0
***Test Failed*** 12 failures.
For whitespace errors, see the file /export/home/drkirkby/sage/sage-4.1.1/tmp/.doctest_twist.py
         [52.9 s]
sage -t  "devel/sage/sage/server/notebook/jquery.py"
         [20.3 s]
```



---

Comment by AlexGhitza created at 2009-08-20 23:58:30

This has 0% chance of being related to either the ECL or the Maxima upgrades.


---

Comment by mpatel created at 2010-08-20 01:36:25

This should no longer be a problem.  David, could you confirm this?


---

Comment by drkirkby created at 2010-08-20 11:06:19

Replying to [comment:2 mpatel]:
> This should no longer be a problem.  David, could you confirm this?
Yes, this can be closed. I've no idea when it was fixed, but it was a long time ago. 

Dave


---

Comment by mpatel created at 2010-08-20 12:31:26

Resolution: worksforme
