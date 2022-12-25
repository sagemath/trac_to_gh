# Issue 6612: sage-update selects a suiteable mirror

archive/issues_006612.json:
```json
{
    "body": "Assignee: tbd\n\nThis is an enhancement to sage-update, that's triggerd by `sage -upgrade`. It downloads a list of available and up-to-date Sage mirrors, uses some heuristics to select a new one, and uses that instead of the default. This should further distribute the server load across the mirror network and speed up downloads. [>> see sage-devel discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/5fb0ea3a8b396982#)\n\nThings to test:\n\n* script works and selects a mirror, there is a fallback to the current mode, so, it should not make things worse.\n* the actual upgrade process works with the content that is actually mirrored. I've tested this and worked (4.0.2 > 4.1) but maybe someone else should give it a try, too.\n\nIssue created by migration from https://trac.sagemath.org/ticket/6612\n\n",
    "created_at": "2009-07-24T13:31:13Z",
    "labels": [
        "component: distribution"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-4.1.2",
    "title": "sage-update selects a suiteable mirror",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6612",
    "user": "https://github.com/haraldschilly"
}
```
Assignee: tbd

This is an enhancement to sage-update, that's triggerd by `sage -upgrade`. It downloads a list of available and up-to-date Sage mirrors, uses some heuristics to select a new one, and uses that instead of the default. This should further distribute the server load across the mirror network and speed up downloads. [>> see sage-devel discussion](http://groups.google.com/group/sage-devel/browse_thread/thread/5fb0ea3a8b396982#)

Things to test:

* script works and selects a mirror, there is a fallback to the current mode, so, it should not make things worse.
* the actual upgrade process works with the content that is actually mirrored. I've tested this and worked (4.0.2 > 4.1) but maybe someone else should give it a try, too.

Issue created by migration from https://trac.sagemath.org/ticket/6612





---

archive/issue_comments_054016.json:
```json
{
    "body": "sidenote to all spkg maintainers for clarification:\n\nmirroring the spkgs means that the current main repository of spkgs is essentially no longer used once this patch goes in. you have to push changes to any (standard) spkgs to the mirrors. that's the same procedure as with a new release and should be done in sync! testing is still possible by providing the url to the sagemath.org website, but it *does not automatically* work as it did until now! optional packages are not mirrored and also not covered by this patch, they are still located at the master server and this patch shouldn't mess around with them.",
    "created_at": "2009-07-24T16:43:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54016",
    "user": "https://github.com/haraldschilly"
}
```

sidenote to all spkg maintainers for clarification:

mirroring the spkgs means that the current main repository of spkgs is essentially no longer used once this patch goes in. you have to push changes to any (standard) spkgs to the mirrors. that's the same procedure as with a new release and should be done in sync! testing is still possible by providing the url to the sagemath.org website, but it *does not automatically* work as it did until now! optional packages are not mirrored and also not covered by this patch, they are still located at the master server and this patch shouldn't mess around with them.



---

archive/issue_comments_054017.json:
```json
{
    "body": "The patch should contain your username and a sensible commit message.",
    "created_at": "2009-08-04T10:42:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54017",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

The patch should contain your username and a sensible commit message.



---

archive/issue_comments_054018.json:
```json
{
    "body": "enables sage -update to select a suiteable mirror from the sage mirror network",
    "created_at": "2009-08-04T11:12:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54018",
    "user": "https://github.com/haraldschilly"
}
```

enables sage -update to select a suiteable mirror from the sage mirror network



---

archive/issue_comments_054019.json:
```json
{
    "body": "Attachment [6612-sage-update-mirror-network-r0.diff](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r0.diff) by mvngu created at 2009-08-14 07:14:46\n\nI received the following errors after patching `SAGE_ROOT/local/bin/sage-update` and doing an upgrade. Maybe this ticket would have to wait for Sage 4.1.2 :-(\n\n```\n[mvngu@darkstar sage-4.0]$ ./sage -upgrade\nTesting mirrors ...\nException in thread Thread-3:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-7:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-8:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-6:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-14:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-10:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-12:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-4:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-13:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-9:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-5:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-2:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-1:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-11:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nDownloading packages from http://www.sagemath.org//spkg\nhttp://www.sagemath.org//spkg/standard\nReading package lists...\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 304, in <module>\n    do_update()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 251, in do_update\n    packages = spkg_list('standard')\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 217, in spkg_list\n    urllib.urlretrieve(web_url, file, reporthook)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 89, in urlretrieve\n    return _urlopener.retrieve(url, filename, reporthook, data)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 222, in retrieve\n    fp = self.open(url, data)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 190, in open\n    return getattr(self, name)(url)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 338, in open_http\n    return self.http_error(url, fp, errcode, errmsg, headers)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 351, in http_error\n    result = method(url, fp, errcode, errmsg, headers)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 649, in http_error_301\n    return self.http_error_302(url, fp, errcode, errmsg, headers, data)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 630, in http_error_302\n    data)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 645, in redirect_internal\n    return self.open(newurl)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 190, in open\n    return getattr(self, name)(url)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/urllib.py\", line 325, in open_http\n    h.endheaders()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py\", line 860, in endheaders\n    self._send_output()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py\", line 732, in _send_output\n    self.send(msg)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py\", line 699, in send\n    self.connect()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/httplib.py\", line 667, in connect\n    socket.SOCK_STREAM):\nIOError: [Errno socket error] (-2, 'Name or service not known')\nError getting new packages!\nDouble checking that all packages have been installed.\nTesting mirrors ...\nException in thread Thread-7:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-8:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-3:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-11:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-14:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-10:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-12:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-9:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-13:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-6:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-5:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-4:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-1:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nException in thread Thread-2:\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 486, in __bootstrap_inner\n    self.run()\n  File \"/home/mvngu/usr/bin/sage-4.0/local/lib/python2.5/threading.py\", line 446, in run\n    self.__target(*self.__args, **self.__kwargs)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 92, in task\n    delay = pinger_urllib(m)\n  File \"/home/mvngu/usr/bin/sage-4.0/local/bin/sage-update\", line 78, in pinger_urllib\n    if u.getcode() is not 200:\nAttributeError: addinfourl instance has no attribute 'getcode'\n\nDownloading packages from http://www.sagemath.org//spkg\nhttp://www.sagemath.org//spkg/standard\nReading package lists...\n....Done\nThe following packages will be upgraded:\n  atlas-3.8.3.p5 cvxopt-0.9.p8 cython-0.11.1.p1 docutils-0.5.p0 dsage-1.0.1.p0 examples-4.1 extcode-4.1 flint-1.3.0.p1 freetype-2.3.5.p1 gap-4.4.10.p12 gd-2.0.35.p2 gdmodule-0.56.p6 gnutls-2.2.1.p2 ipython-0.9.1.p0 jinja-1.2.p0 libgcrypt-1.4.3.p1 libgpg_error-1.6.p1 libm4ri-20090617 linbox-1.1.6.p0 matplotlib-0.98.5.3rc0-svn6910.p4 mercurial-1.1.2.p0 moin-1.5.7.p3 mpir-1.2.p4 mpmath-0.12 networkx-0.99.p1-fake_really-0.36.p0 ntl-5.4.2.p8 numpy-1.3.0.p0 pexpect-2.0.p4 polybori-0.5rc.p8 pycrypto-2.0.1.p4 pygments-0.11.1.p0 pynac-0.1.8.p1 pyprocessing-0.52.p0 python-2.6.2.p1 python_gnutls-1.1.4.p5 r-2.6.1.p23 ratpoints-2.1.2.p2 readline-5.2.p7 rubiks-20070912.p9 sage-4.1 sage_scripts-4.1 scipy-0.7.p2 scipy_sandbox-20071020.p4 scons-1.2.0 setuptools-0.6c9.p0 singular-3-1-0-2-20090620 sphinx-0.5.1.p0 sqlalchemy-0.4.6.p1 sqlite-3.5.3.p4 sympy-0.6.4.p0 tachyon-0.98beta.p9 twisted-8.2.0 weave-0.4.9.p0 zodb3-3.7.0.p2\n* WARNING: This is a source-based upgrade, which could take hours, fail and render your Sage install useless!!\nDo you want to continue [y/N]? N\nAbort.\n```",
    "created_at": "2009-08-14T07:14:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54019",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [6612-sage-update-mirror-network-r0.diff](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r0.diff) by mvngu created at 2009-08-14 07:14:46

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

archive/issue_comments_054020.json:
```json
{
    "body": "This error is just the same for all threads, that's why it looks scary. The problem is, that you are running python 2.5 and it doesn't have a method to get the return code for a url request in \"urllib\". (addinfourl instance has no attribute 'getcode') ... e.g. getcode should not be \"404\" (indicating a missing webpage) and so on!\n\nDoes anyone know how to circumvent this? I'm using python 2.6, that's why it works for me. Additionally, even through there are exceptions, the whole process works fine as you can see at the bottom. Those exceptions are just ignored and upgrading would work as usual.",
    "created_at": "2009-08-14T07:25:42Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54020",
    "user": "https://github.com/haraldschilly"
}
```

This error is just the same for all threads, that's why it looks scary. The problem is, that you are running python 2.5 and it doesn't have a method to get the return code for a url request in "urllib". (addinfourl instance has no attribute 'getcode') ... e.g. getcode should not be "404" (indicating a missing webpage) and so on!

Does anyone know how to circumvent this? I'm using python 2.6, that's why it works for me. Additionally, even through there are exceptions, the whole process works fine as you can see at the bottom. Those exceptions are just ignored and upgrading would work as usual.



---

archive/issue_comments_054021.json:
```json
{
    "body": "more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... `",
    "created_at": "2009-08-14T07:26:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54021",
    "user": "https://github.com/haraldschilly"
}
```

more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... `



---

archive/issue_comments_054022.json:
```json
{
    "body": "Replying to [comment:6 schilly]:\n> more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... ` \n\nOK that worked.\n\n\n\nHmm... The coding style in the patch doesn't conform to coding conventions mentioned in the Developers' Guide. In particular, use 4 spaces for indentation. This ticket will have to wait for Sage 4.1.2.",
    "created_at": "2009-08-14T12:02:37Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54022",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:6 schilly]:
> more importantly, could you try to upgrade using a manually specified mirror? i.e. `./sage -upgrade http://...aarnet.../... ` 

OK that worked.



Hmm... The coding style in the patch doesn't conform to coding conventions mentioned in the Developers' Guide. In particular, use 4 spaces for indentation. This ticket will have to wait for Sage 4.1.2.



---

archive/issue_events_015612.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-08-14T12:02:37Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "milestone": "sage-4.1.2",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6612#event-15612"
}
```



---

archive/issue_comments_054023.json:
```json
{
    "body": "I got the following errors when upgrading from Sage 4.1.1.alpha0 to Sage 4.1.1:\n\n```\nsphinx-build -b html -d /home/mvngu/usr/bin/sage/devel/sage/doc/output/doctrees/en/numerical_sage   .  /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/numerical_sage\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage/local/bin/sphinx-build\", line 6, in <module>\n    import sage.all\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py\", line 64, in <module>\n    from sage.misc.all       import *         # takes a while\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py\", line 1, in <module>\n    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py\", line 30, in <module>\n    from banner import version, banner\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 20, in <module>\n    import sage.version\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py\", line 2\n    <<<<<<< local\n     ^\nSyntaxError: invalid syntax\nBuild finished.  The built documents can be found in /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/numerical_sage\nsphinx-build -b html -d /home/mvngu/usr/bin/sage/devel/sage/doc/output/doctrees/en/constructions   .  /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/constructions\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage/local/bin/sphinx-build\", line 6, in <module>\n    import sage.all\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py\", line 64, in <module>\n    from sage.misc.all       import *         # takes a while\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py\", line 1, in <module>\n    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py\", line 30, in <module>\n    from banner import version, banner\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 20, in <module>\n    import sage.version\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py\", line 2\n    <<<<<<< local\n     ^\nSyntaxError: invalid syntax\nBuild finished.  The built documents can be found in /home/mvngu/usr/bin/sage/devel/sage/doc/output/html/en/constructions\nTraceback (most recent call last):\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 667, in <module>\n    getattr(get_builder(name), type)()\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 258, in _wrapper\n    getattr(get_builder(document), name)(*args, **kwds)\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 345, in _wrapper\n    self.write_auto_rest_file(module_name)\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 528, in write_auto_rest_file\n    title = self.get_module_docstring_title(module_name)\n  File \"/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py\", line 497, in get_module_docstring_title\n    import sage.all\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/all.py\", line 64, in <module>\n    from sage.misc.all       import *         # takes a while\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/all.py\", line 1, in <module>\n    from misc import (alarm, ellipsis_range, ellipsis_iter, srange, xsrange, sxrange, getitem,\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py\", line 30, in <module>\n    from banner import version, banner\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py\", line 20, in <module>\n    import sage.version\n  File \"/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py\", line 2\n    <<<<<<< local\n     ^\nSyntaxError: invalid syntax\n```\nThe upgraded version doesn't even start properly:\n\n```\n[mvngu@darkstar sage]$ ./sage -br main\n\n----------------------------------------------------------\nsage: Building and installing modified Sage library files.\n\n\nInstalling c_lib\nscons: `install' is up to date.\nUpdating Cython code....\nTime to execute 0 commands: 2.71797180176e-05 seconds\nFinished compiling Cython code (time = 5.56926393509 seconds)\nrunning install\nrunning build\nrunning build_py\nrunning build_ext\nTotal time spent compiling C/C++ extensions:  1.11849784851 seconds.\nrunning install_lib\nbyte-compiling /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py to version.pyc\nSyntaxError: ('invalid syntax', ('/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/version.py', 2, 2, '<<<<<<< local\\n'))\n\nrunning install_egg_info\nRemoving /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\nWriting /home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage-0.0.0-py2.6.egg-info\n----------------------------------------------------------------------\n<<<<<<< local\n=======\n>>>>>>> other\n----------------------------------------------------------------------\n---------------------------------------------------------------------------\nSyntaxError                               Traceback (most recent call last)\n| Sage Version 4.1.1.alpha0, Release Date: 2009-07-20                |\n| Sage Version 4.1.1, Release Date: 2009-08-14                       |\n| Type notebook() for the GUI, and license() for information.        |\n/home/mvngu/usr/bin/sage/local/bin/<string> in <module>()\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/preparser_ipython.py in <module>()\n      6 ###########################################################################\n\n      7 \n----> 8 import sage.misc.interpreter\n      9 \n     10 import preparser\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/interpreter.py in <module>()\n    100 \n    101 import os\n--> 102 import log\n    103 \n    104 import remote_file\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/log.py in <module>()\n     63 \n     64 import interpreter\n---> 65 import latex\n     66 import misc\n     67 \n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/latex.py in <module>()\n     40 import random\n     41 \n---> 42 from misc import tmp_dir, graphics_filename\n     43 import sage_eval\n     44 from sage.misc.misc import SAGE_DOC\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py in <module>()\n     28 import sage.misc.prandom as random\n     29 \n---> 30 from banner import version, banner\n     31 \n     32 SAGE_ROOT = os.environ[\"SAGE_ROOT\"]\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py in <module>()\n     18 #*****************************************************************************\n\n     19 \n---> 20 import sage.version\n     21 \n     22 def version(clone = False):\n\nSyntaxError: invalid syntax (version.py, line 2)\nWARNING: Failure executing code: 'import sage.misc.preparser_ipython;  sage.misc.preparser_ipython.magma_colon_equals=True'\n---------------------------------------------------------------------------\nSyntaxError                               Traceback (most recent call last)\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/IPython/ipmaker.pyc in force_import(modname)\n     64         reload(sys.modules[modname])\n     65     else:\n---> 66         __import__(modname)\n     67 \n     68 \n\n/home/mvngu/usr/bin/sage/local/bin/ipy_profile_sage.py in <module>()\n      1 import os\n      2 if 'SAGE_CLEAN' not in os.environ:\n----> 3     import sage.misc.misc\n      4     from sage.misc.interpreter import preparser, _ip\n      5     preparser(True)\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/misc.py in <module>()\n     28 import sage.misc.prandom as random\n     29 \n---> 30 from banner import version, banner\n     31 \n     32 SAGE_ROOT = os.environ[\"SAGE_ROOT\"]\n\n/home/mvngu/usr/bin/sage/local/lib/python2.6/site-packages/sage/misc/banner.py in <module>()\n     18 #*****************************************************************************\n\n     19 \n---> 20 import sage.version\n     21 \n     22 def version(clone = False):\n\nSyntaxError: invalid syntax (version.py, line 2)\nError importing ipy_profile_sage - perhaps you should run %upgrade?\nWARNING: Loading of ipy_profile_sage failed.\n\n<ERROR: name 'sage_prompt' is not defined>\n<ERROR: name 'sage_prompt' is not defined>exit\nType exit() to exit.\n<ERROR: name 'sage_prompt' is not defined>exit()\n```",
    "created_at": "2009-08-16T09:28:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54023",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

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

archive/issue_comments_054024.json:
```json
{
    "body": "Replying to [comment:8 mvngu]:\n> I got the following errors when upgrading from Sage 4.1.1.alpha0 to Sage 4.1.1:\n\n{{{\n> \n> ---\n> <<<<<<< local\n> | Sage Version 4.1.1.alpha0, Release Date: 2009-07-20                |\n> =======\n> | Sage Version 4.1.1, Release Date: 2009-08-14                       |\n> >>>>>>> other\n\n> | Type notebook() for the GUI, and license() for information.        |\n> \n> ---\n\n}}}\n\nYour version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. \n\nI just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!",
    "created_at": "2009-08-18T13:38:33Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54024",
    "user": "https://github.com/haraldschilly"
}
```

Replying to [comment:8 mvngu]:
> I got the following errors when upgrading from Sage 4.1.1.alpha0 to Sage 4.1.1:

{{{
> 
> ---
> <<<<<<< local
> | Sage Version 4.1.1.alpha0, Release Date: 2009-07-20                |
> =======
> | Sage Version 4.1.1, Release Date: 2009-08-14                       |
> >>>>>>> other

> | Type notebook() for the GUI, and license() for information.        |
> 
> ---

}}}

Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. 

I just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!



---

archive/issue_comments_054025.json:
```json
{
    "body": "Replying to [comment:9 schilly]:\n> Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. \nHmm... I guess we need to document that in the update script. Essentially, the update script is for updating from one previous stable release to another new stable release.\n\n\n\n\n> I just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!\n\nIt worked fine for me too. I upgraded Sage 4.1 under Gentoo (running within VirtualBox) to Sage 4.1.1 using your patch. It went OK. Before I went home, I started the doctest suite and started to upgrade 4.1 under the Ubuntu host. Seems like I need to wait another few hours before I can check up on those updates/doctests on the computer in my office.\n\n\n\nOne of my pet peeves at the moment is that the patch doesn't conform to coding conventions. Another thing is that, when I use that patch to upgrade from my office computer, the patch would randomly choose a mirror from a list of the top three mirrors. That is OK as far as I'm concerned. An enhancement would be to allow the user to choose a mirror from one of the top three. My reason is that, say I upgrade from my office computer. That computer is located within a university network. At least over here in Australia, it is usually faster for me to upgrade from one of the Australian mirrors (preferably the Sydney Uni mirror) than from another any other mirrors.\n\n\n\nApart from the above rantings, I need to spend some quality time investigating each line of the patch.",
    "created_at": "2009-08-18T13:51:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54025",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Replying to [comment:9 schilly]:
> Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. 
Hmm... I guess we need to document that in the update script. Essentially, the update script is for updating from one previous stable release to another new stable release.




> I just upgraded from 4.1 to 4.1.1 using the czech cvut.cz mirror. It worked fine!

It worked fine for me too. I upgraded Sage 4.1 under Gentoo (running within VirtualBox) to Sage 4.1.1 using your patch. It went OK. Before I went home, I started the doctest suite and started to upgrade 4.1 under the Ubuntu host. Seems like I need to wait another few hours before I can check up on those updates/doctests on the computer in my office.



One of my pet peeves at the moment is that the patch doesn't conform to coding conventions. Another thing is that, when I use that patch to upgrade from my office computer, the patch would randomly choose a mirror from a list of the top three mirrors. That is OK as far as I'm concerned. An enhancement would be to allow the user to choose a mirror from one of the top three. My reason is that, say I upgrade from my office computer. That computer is located within a university network. At least over here in Australia, it is usually faster for me to upgrade from one of the Australian mirrors (preferably the Sydney Uni mirror) than from another any other mirrors.



Apart from the above rantings, I need to spend some quality time investigating each line of the patch.



---

archive/issue_comments_054026.json:
```json
{
    "body": "Replying to [comment:10 mvngu]:\n> Replying to [comment:9 schilly]:\n> > Your version info banner is corrupted and i guess you cannot upgrade from a pre release to a release due to such collissions. you have to resolve all of them first. \n\n> Hmm... I guess we need to document that in the update script. Essentially, the update script is for updating from one previous stable release to another new stable release.\n\nThe history behind that is, that `-upgrade` was only intended to be used by developers who know what it does. It's not so intelligent. Especially merge/patch rejections with that message banner are very common to me. But it's outside of the scope of this ticket ;) \n\n> One of my pet peeves at the moment is that the patch doesn't conform to coding conventions.\n\n\nyes, i'll change that, no problem.\n\n> An enhancement would be to allow the user to choose a mirror from one of the top three. \n\n\nThat's a good point for your situation. I can enhance it by a litte menu, where you either hit \"return\" and you get the random-top-3 or you enter a number to select one from all of the mirrors. That shouldn't be too hard.",
    "created_at": "2009-08-18T14:03:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54026",
    "user": "https://github.com/haraldschilly"
}
```

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

archive/issue_comments_054027.json:
```json
{
    "body": "Attachment [6612-sage-update-mirror-network-r1.patch](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r1.patch) by @haraldschilly created at 2009-08-24 22:41:13\n\nenables sage -update to select a suiteable mirror from the sage mirror network,updated patch",
    "created_at": "2009-08-24T22:41:13Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54027",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [6612-sage-update-mirror-network-r1.patch](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r1.patch) by @haraldschilly created at 2009-08-24 22:41:13

enables sage -update to select a suiteable mirror from the sage mirror network,updated patch



---

archive/issue_comments_054028.json:
```json
{
    "body": "first patch can be deleted, \"*-r1*\" contains everything including the optional manual mirror selection. My tests show that it asks two times, but the second one is only an assurance and well, shouldn't be a problem.",
    "created_at": "2009-08-29T08:44:58Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54028",
    "user": "https://github.com/haraldschilly"
}
```

first patch can be deleted, "*-r1*" contains everything including the optional manual mirror selection. My tests show that it asks two times, but the second one is only an assurance and well, shouldn't be a problem.



---

archive/issue_comments_054029.json:
```json
{
    "body": "complete patch",
    "created_at": "2009-09-07T10:16:28Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54029",
    "user": "https://github.com/haraldschilly"
}
```

complete patch



---

archive/issue_comments_054030.json:
```json
{
    "body": "Attachment [6612-sage-update-mirror-network-r2.patch](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r2.patch) by @haraldschilly created at 2009-09-07 10:18:45\n\npatches besides \"-r2\" can be deleted. now, it selects the \"best\" mirror automatically, uses the given one if there is any and asks the user which one to use if given url is \"ask\". additionally, this is documented in \"sage-sage\".\n\nand i know, line indentations are wrong, but the file has \"5\" by default but sage policy is 4.",
    "created_at": "2009-09-07T10:18:45Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54030",
    "user": "https://github.com/haraldschilly"
}
```

Attachment [6612-sage-update-mirror-network-r2.patch](tarball://root/attachments/some-uuid/ticket6612/6612-sage-update-mirror-network-r2.patch) by @haraldschilly created at 2009-09-07 10:18:45

patches besides "-r2" can be deleted. now, it selects the "best" mirror automatically, uses the given one if there is any and asks the user which one to use if given url is "ask". additionally, this is documented in "sage-sage".

and i know, line indentations are wrong, but the file has "5" by default but sage policy is 4.



---

archive/issue_comments_054031.json:
```json
{
    "body": "reviewer patch",
    "created_at": "2009-09-29T15:21:48Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54031",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

reviewer patch



---

archive/issue_comments_054032.json:
```json
{
    "body": "Attachment [trac_6612-reviewer.patch](tarball://root/attachments/some-uuid/ticket6612/trac_6612-reviewer.patch) by mvngu created at 2009-09-29 15:25:59\n\nThe two patches `6612-sage-update-mirror-network-r1.patch` and `6612-sage-update-mirror-network-r2.patch` look good to me. I have attached a reviewer patch `trac_6612-reviewer.patch` that include the following changes:\n\n* Some formatting fixes to `sage-sage`.\n* Remove the re-import of `urllib` and `socket`.\n* Remove the unused import of `subprocess`.\n* Remove multiple imports on one line.\n* Use three double quotation marks `\"` instead of three single quotation marks `'`.\n* Use 4 space indentation.\n* Spell checking.\n\nIf my patch gets some thumbs up, then the whole ticket can be merged for Sage 4.1.2.",
    "created_at": "2009-09-29T15:25:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54032",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Attachment [trac_6612-reviewer.patch](tarball://root/attachments/some-uuid/ticket6612/trac_6612-reviewer.patch) by mvngu created at 2009-09-29 15:25:59

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

archive/issue_comments_054033.json:
```json
{
    "body": "ok, thank's for fixing this and the reviewer patch looks good for me. also checking spelling in other parts of that file. ... and i once again forgot to combine my patches, so, only r0 is to ignore, it's r1 and r2 as you have noted.",
    "created_at": "2009-09-29T15:32:59Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54033",
    "user": "https://github.com/haraldschilly"
}
```

ok, thank's for fixing this and the reviewer patch looks good for me. also checking spelling in other parts of that file. ... and i once again forgot to combine my patches, so, only r0 is to ignore, it's r1 and r2 as you have noted.



---

archive/issue_comments_054034.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2009-09-30T04:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54034",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Resolution: fixed



---

archive/issue_comments_054035.json:
```json
{
    "body": "Merged patches in the script repository in this order:\n\n1. `6612-sage-update-mirror-network-r1.patch`\n2. `6612-sage-update-mirror-network-r2.patch`\n3. `trac_6612-reviewer.patch`",
    "created_at": "2009-09-30T04:05:47Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6612#issuecomment-54035",
    "user": "https://trac.sagemath.org/admin/accounts/users/mvngu"
}
```

Merged patches in the script repository in this order:

1. `6612-sage-update-mirror-network-r1.patch`
2. `6612-sage-update-mirror-network-r2.patch`
3. `trac_6612-reviewer.patch`



---

archive/issue_events_015613.json:
```json
{
    "actor": "https://trac.sagemath.org/admin/accounts/users/mvngu",
    "created_at": "2009-09-30T04:05:47Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6612",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6612#event-15613"
}
```
