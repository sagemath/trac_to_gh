# Issue 6612: sage-update selects a suiteable mirror

Issue created by migration from https://trac.sagemath.org/ticket/6612

Original creator: schilly

Original creation time: 2009-07-24 13:31:13

Assignee: tbd

This is an enhancement to sage-update, that's triggerd by `sage -upgrade`. It downloads a list of available and up-to-date Sage mirrors, uses some heuristics to select a new one, and uses that instead of the default. This should further distribute the server load across the mirror network and speed up downloads. [>> see sage-devel discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/5fb0ea3a8b396982#)

Things to test:

 * script works and selects a mirror, there is a fallback to the current mode, so, it should not make things worse.
 * the actual upgrade process works with the content that is actually mirrored. I've tested this and worked (4.0.2 > 4.1) but maybe someone else should give it a try, too.


---

Comment by schilly created at 2009-07-24 16:43:39

sidenote to all spkg maintainers for clarification:

mirroring the spkgs means that the current main repository of spkgs is essentially no longer used once this patch goes in. you have to push changes to any (standard) spkgs to the mirrors. that's the same procedure as with a new release and should be done in sync! testing is still possible by providing the url to the sagemath.org website, but it *does not automatically* work as it did until now! optional packages are not mirrored and also not covered by this patch, they are still located at the master server and this patch shouldn't mess around with them.


---

Comment by mvngu created at 2009-08-04 10:42:45

The patch should contain your username and a sensible commit message.


---

Comment by schilly created at 2009-08-04 11:12:21

enables sage -update to select a suiteable mirror from the sage mirror network


---

Attachment

I received the following errors after patching `SAGE_ROOT/local/bin/sage-update` and doing an upgrade. Maybe this ticket would have to wait for Sage 4.1.2 :-(

```
[mvngu@darkstar sage-4.0]$ ./sage -upgrade
Testing mirrors ...
Exception in thread Thread-3:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-7:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-8:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-6:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-14:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-10:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-12:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-4:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-13:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-9:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-5:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-2:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-1:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-11:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Downloading packages from http://www.sagemath.org//spkg
http://www.sagemath.org//spkg/standard
Reading package lists...
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 304, in <module>
    do_update()
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 251, in do_update
    packages = spkg_list('standard')
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 217, in spkg_list
    urllib.urlretrieve(web_url, file, reporthook)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 89, in urlretrieve
    return _urlopener.retrieve(url, filename, reporthook, data)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 222, in retrieve
    fp = self.open(url, data)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 190, in open
    return getattr(self, name)(url)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 338, in open_http
    return self.http_error(url, fp, errcode, errmsg, headers)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 351, in http_error
    result = method(url, fp, errcode, errmsg, headers)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 649, in http_error_301
    return self.http_error_302(url, fp, errcode, errmsg, headers, data)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 630, in http_error_302
    data)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 645, in redirect_internal
    return self.open(newurl)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 190, in open
    return getattr(self, name)(url)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py", line 325, in open_http
    h.endheaders()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py", line 860, in endheaders
    self._send_output()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py", line 732, in _send_output
    self.send(msg)
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py", line 699, in send
    self.connect()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py", line 667, in connect
    socket.SOCK_STREAM):
IOError: [Errno socket error] (-2, 'Name or service not known')
Error getting new packages!
Double checking that all packages have been installed.
Testing mirrors ...
Exception in thread Thread-7:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-8:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-3:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-11:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-14:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-10:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-12:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-9:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-13:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-6:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-5:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-4:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-1:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Exception in thread Thread-2:
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 486, in __bootstrap_inner
    self.run()
  File "/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py", line 446, in run
    self.__target(*self.__args, **self.__kwargs)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 92, in task
    delay = pinger_urllib(m)
  File "/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update", line 78, in pinger_urllib
    if u.getcode() is not 200:
AttributeError: addinfourl instance has no attribute 'getcode'

Downloading packages from http://www.sagemath.org//spkg
http://www.sagemath.org//spkg/standard
Reading package lists...
....Done
The following packages will be upgraded:
  atlas-3.8.3.p5 cvxopt-0.9.p8 cython-0.11.1.p1 docutils-0.5.p0 dsage-1.0.1.p0 examples-4.1 extcode-4.1 flint-1.3.0.p1 freetype-2.3.5.p1 gap-4.4.10.p12 gd-2.0.35.p2 gdmodule-0.56.p6 gnutls-2.2.1.p2 ipython-0.9.1.p0 jinja-1.2.p0 libgcrypt-1.4.3.p1 libgpg_error-1.6.p1 libm4ri-20090617 linbox-1.1.6.p0 matplotlib-0.98.5.3rc0-svn6910.p4 mercurial-1.1.2.p0 moin-1.5.7.p3 mpir-1.2.p4 mpmath-0.12 networkx-0.99.p1-fake_really-0.36.p0 ntl-5.4.2.p8 numpy-1.3.0.p0 pexpect-2.0.p4 polybori-0.5rc.p8 pycrypto-2.0.1.p4 pygments-0.11.1.p0 pynac-0.1.8.p1 pyprocessing-0.52.p0 python-2.6.2.p1 python_gnutls-1.1.4.p5 r-2.6.1.p23 ratpoints-2.1.2.p2 readline-5.2.p7 rubiks-20070912.p9 sage-4.1 sage_scripts-4.1 scipy-0.7.p2 scipy_sandbox-20071020.p4 scons-1.2.0 setuptools-0.6c9.p0 singular-3-1-0-2-20090620 sphinx-0.5.1.p0 sqlalchemy-0.4.6.p1 sqlite-3.5.3.p4 sympy-0.6.4.p0 tachyon-0.98beta.p9 twisted-8.2.0 weave-0.4.9.p0 zodb3-3.7.0.p2
* WARNING: This is a source-based upgrade, which could take hours, fail and render your Sage install useless!!
Do you want to continue [y/N]? N
Abort.
```



---

Comment by schilly created at 2009-08-14 07:25:42

This error is just the same for all threads, that's why it looks scary. The problem is, that you are running python 2.5 and it doesn't have a method to get the return code for a url request in "urllib". (addinfourl instance has no attribute 'getcode') ... e.g. getcode should not be "404" (indicating a missing webpage) and so on!

Does anyone know how to circumvent this? I'm using python 2.6, that's why it works for me. Additionally, even through there are exceptions, the whole process works fine as you can see at the bottom. Those exceptions are just ignored and upgrading would work as usual.


---

Comment by schilly created at 2009-08-14 07:26:52

more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... `


---

Comment by mvngu created at 2009-08-14 12:02:37

Replying to [comment:6 schilly]:
> more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... ` 
OK that worked.



Hmm... The coding style in the patch doesn't conform to coding conventions mentioned in the Developers' Guide. In particular, use 4 spaces for indentation. This ticket will have to wait for Sage 4.1.2.


---

Comment by mvngu created at 2009-08-16 09:28:54

I got the following errors when upgrading from Sage 4.1.1.alpha0 to Sage 4.1.1:

```
sphinx-build -b html -d /home/mvngu/usr/bin/sage/devel/sage/doc/output/doctrees/en/numerical_sage   .  /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/numerical_sage
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/local/bin/sphinx-build", line 6, in <module>
    import sage.all
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py", line 1, in <module>
    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py", line 30, in <module>
    from banner import version, banner
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py", line 20, in <module>
    import sage.version
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py", line 2
    <<<<<<< local
     ^
SyntaxError: invalid syntax
Build finished.  The built documents can be found in /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/numerical_sage
sphinx-build -b html -d /home/mvngu/usr/bin/sage/devel/sage/doc/output/doctrees/en/constructions   .  /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/constructions
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/local/bin/sphinx-build", line 6, in <module>
    import sage.all
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py", line 1, in <module>
    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py", line 30, in <module>
    from banner import version, banner
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py", line 20, in <module>
    import sage.version
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py", line 2
    <<<<<<< local
     ^
SyntaxError: invalid syntax
Build finished.  The built documents can be found in /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/constructions
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 667, in <module>
    getattr(get_builder(name), type)()
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 258, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 345, in _wrapper
    self.write_auto_rest_file(module_name)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 528, in write_auto_rest_file
    title = self.get_module_docstring_title(module_name)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 497, in get_module_docstring_title
    import sage.all
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py", line 64, in <module>
    from sage.misc.all       import *         # takes a while
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py", line 1, in <module>
    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py", line 30, in <module>
    from banner import version, banner
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py", line 20, in <module>
    import sage.version
  File "/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py", line 2
    <<<<<<< local
     ^
SyntaxError: invalid syntax
```

The upgraded version doesn't even start properly:

```
[mvngu@darkstar sage]$ ./sage -br main

----------------------------------------------------------
sage: Building and installing modified Sage library files.


Installing c_lib
scons: `install' is up to date.
Updating Cython code....
Time to execute 0 commands: 2.71797180176e-05 seconds
Finished compiling Cython code (time = 5.56926393509 seconds)
running install
running build
running build_py
running build_ext
Total time spent compiling C/C++ extensions:  1.11849784851 seconds.
running install_lib
byte-compiling /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py to version.pyc
SyntaxError: ('invalid syntax', ('/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py', 2, 2, '<<<<<<< local\n'))

running install_egg_info
Removing /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
Writing /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info
----------------------------------------------------------------------
<<<<<<< local
=======
>>>>>>> other
----------------------------------------------------------------------
---------------------------------------------------------------------------
SyntaxError                               Traceback (most recent call last)
| Sage Version 4.1.1.alpha0, Release Date: 2009-07-20                |
| Sage Version 4.1.1, Release Date: 2009-08-14                       |
| Type notebook() for the GUI, and license() for information.        |
/home/mvngu/usr/bin/sage/local/bin/<string> in <module>()

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/preparser_ipython.py in <module>()
      6 ###########################################################################

      7 
----> 8 import sage.misc.interpreter
      9 
     10 import preparser

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/interpreter.py in <module>()
    100 
    101 import os
--> 102 import log
    103 
    104 import remote_file

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/log.py in <module>()
     63 
     64 import interpreter
---> 65 import latex
     66 import misc
     67 

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/latex.py in <module>()
     40 import random
     41 
---> 42 from misc import tmp_dir, graphics_filename
     43 import sage_eval
     44 from sage.misc.misc import SAGE_DOC

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py in <module>()
     28 import sage.misc.prandom as random
     29 
---> 30 from banner import version, banner
     31 
     32 SAGE_ROOT = os.environ["SAGE_ROOT"]

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py in <module>()
     18 #*****************************************************************************

     19 
---> 20 import sage.version
     21 
     22 def version(clone = False):

SyntaxError: invalid syntax (version.py, line 2)
WARNING: Failure executing code: 'import sage.misc.preparser_ipython;  sage.misc.preparser_ipython.magma_colon_equals=True'
---------------------------------------------------------------------------
SyntaxError                               Traceback (most recent call last)

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)
     64         reload(sys.modules[modname])
     65     else:
---> 66         __import__(modname)
     67 
     68 

/home/mvngu/usr/bin/sage/local/bin/ipy_profile_sage.py in <module>()
      1 import os
      2 if 'SAGE_CLEAN' not in os.environ:
----> 3     import sage.misc.misc
      4     from sage.misc.interpreter import preparser, _ip
      5     preparser(True)

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py in <module>()
     28 import sage.misc.prandom as random
     29 
---> 30 from banner import version, banner
     31 
     32 SAGE_ROOT = os.environ["SAGE_ROOT"]

/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py in <module>()
     18 #*****************************************************************************

     19 
---> 20 import sage.version
     21 
     22 def version(clone = False):

SyntaxError: invalid syntax (version.py, line 2)
Error importing ipy_profile_sage - perhaps you should run %upgrade?
WARNING: Loading of ipy_profile_sage failed.

<ERROR: name 'sage_prompt' is not defined>
<ERROR: name 'sage_prompt' is not defined>exit
Type exit() to exit.
<ERROR: name 'sage_prompt' is not defined>exit()
```



---

Comment by schilly created at 2009-08-18 13:38:33

Replying to [comment:8 mvngu]:
> I got the following errors when upgrading from Sage 4.1.1.alpha0 to Sage 4.1.1:

```
> ----------------------------------------------------------------------
> <<<<<<< local
> | Sage Version 4.1.1.alpha0, Release Date: 2009-07-20                |
> =======
> | Sage Version 4.1.1, Release Date: 2009-08-14                       |
> >>>>>>> other
> | Type notebook() for the GUI, and license() for information.        |
> ----------------------------------------------------------------------
```


Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. 

I just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!


---

Comment by mvngu created at 2009-08-18 13:51:41

Replying to [comment:9 schilly]:
> Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. 
Hmm... I guess we need to document that in the update script. Essentially, the update script is for updating from one previous stable release to another new stable release.




> I just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!
It worked fine for me too. I upgraded Sage 4.1 under Gentoo (running within VirtualBox) to Sage 4.1.1 using your patch. It went OK. Before I went home, I started the doctest suite and started to upgrade 4.1 under the Ubuntu host. Seems like I need to wait another few hours before I can check up on those updates/doctests on the computer in my office.



One of my pet peeves at the moment is that the patch doesn't conform to coding conventions. Another thing is that, when I use that patch to upgrade from my office computer, the patch would randomly choose a mirror from a list of the top three mirrors. That is OK as far as I'm concerned. An enhancement would be to allow the user to choose a mirror from one of the top three. My reason is that, say I upgrade from my office computer. That computer is located within a university network. At least over here in Australia, it is usually faster for me to upgrade from one of the Australian mirrors (preferably the Sydney Uni mirror) than from another any other mirrors.



Apart from the above rantings, I need to spend some quality time investigating each line of the patch.


---

Comment by schilly created at 2009-08-18 14:03:24

Replying to [comment:10 mvngu]:
> Replying to [comment:9 schilly]:
> > Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. 
> Hmm... I guess we need to document that in the update script. Essentially, the update script is for updating from one previous stable release to another new stable release.

The history behind that is, that `-upgrade` was only intended to be used by developers who know what it does. It's not so intelligent. Especially merge/patch rejections with that message banner are very common to me. But it's outside of the scope of this ticket ;) 

> One of my pet peeves at the moment is that the patch doesn't conform to coding conventions.

yes, i'll change that, no problem.

> An enhancement would be to allow the user to choose a mirror from one of the top three. 

That's a good point for your situation. I can enhance it by a litte menu, where you either hit "return" and you get the random-top-3 or you enter a number to select one from all of the mirrors. That shouldn't be too hard.


---

Attachment

enables sage -update to select a suiteable mirror from the sage mirror network,updated patch


---

Comment by schilly created at 2009-08-29 08:44:58

first patch can be deleted, "*-r1*" contains everything including the optional manual mirror selection. My tests show that it asks two times, but the second one is only an assurance and well, shouldn't be a problem.


---

Comment by schilly created at 2009-09-07 10:16:28

complete patch


---

Attachment

patches besides "-r2" can be deleted. now, it selects the "best" mirror automatically, uses the given one if there is any and asks the user which one to use if given url is "ask". additionally, this is documented in "sage-sage".

and i know, line indentations are wrong, but the file has "5" by default but sage policy is 4.


---

Comment by mvngu created at 2009-09-29 15:21:48

reviewer patch


---

Attachment

The two patches `6612-sage-update-mirror-network-r1.patch` and `6612-sage-update-mirror-network-r2.patch` look good to me. I have attached a reviewer patch `trac_6612-reviewer.patch` that include the following changes:

 * Some formatting fixes to `sage-sage`.
 * Remove the re-import of `urllib` and `socket`.
 * Remove the unused import of `subprocess`.
 * Remove multiple imports on one line.
 * Use three double quotation marks `"` instead of three single quotation marks `'`.
 * Use 4 space indentation.
 * Spell checking.

If my patch gets some thumbs up, then the whole ticket can be merged for Sage 4.1.2.


---

Comment by schilly created at 2009-09-29 15:32:59

ok, thank's for fixing this and the reviewer patch looks good for me. also checking spelling in other parts of that file. ... and i once again forgot to combine my patches, so, only r0 is to ignore, it's r1 and r2 as you have noted.


---

Comment by mvngu created at 2009-09-30 04:05:47

Resolution: fixed


---

Comment by mvngu created at 2009-09-30 04:05:47

Merged patches in the script repository in this order:

 1. `6612-sage-update-mirror-network-r1.patch`
 1. `6612-sage-update-mirror-network-r2.patch`
 1. `trac_6612-reviewer.patch`
