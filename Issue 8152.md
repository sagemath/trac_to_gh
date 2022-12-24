# Issue 8152: Python needs to search /usr/sfw/lib on Solaris for OpenSSL libraries.

archive/issues_008152.json:
```json
{
    "body": "Assignee: drkirkby\n\nCC:  was jsp\n\nSage currently depends on OpenSSL to build the haslib module in Python. OpenSSL is not distributed with Sage due to license issues. However, the GPL allows us to link to the libraries if they are part of the core operating system, such as the kernel or compilers. (Someone could argue OpenSSL is not part of the core operating system, so even if it comes with the operating system, we can't use it. However, that is another issue.)\n\nThe OpenSSL libraries are installed on Solaris 10 in /usr/sfw/lib.  The problem is, python does not currently look there for the libraries. I've submitted an enhancement request to the Python bug database. \n\nhttp://bugs.python.org/issue7836\n\nthat they add that directory to the list of directories searched. \n\nUntil this gets fixed, I believe we should add the directory /usr/sfw/lib to the top-level setup.py. Then Sage should build on Solaris 10 (but not OpenSolaris) without installation of any OpenSSL libraries. \n\nThere is no point making this patch operating system specific, as the code in python is only a search path: \n\n\n```\n       ssl_libs = find_library_file(self.compiler, 'ssl',lib_dirs,\n                                     ['/usr/local/ssl/lib',\n                                      '/usr/contrib/ssl/lib/'\n                                     ] )\n\n```\n\n\nI'm not sure if we need to know the location of the include directories, but they are in /usr/src/include/openssl. There is again similar code in setup.py to search for the include files:\n\n\n```\n        # Detect SSL support for the socket module (via _ssl)\n        search_for_ssl_incs_in = [\n                              '/usr/local/ssl/include',\n                              '/usr/contrib/ssl/include/'\n                             ]\n\n```\n\n\nAny comments, before I go to the trouble of making a patch, which just appends the search path for the OpenSSL directories?  Does this seem a reasonable thing to do? \n\nDave\n\nIssue created by migration from https://trac.sagemath.org/ticket/8152\n\n",
    "created_at": "2010-02-02T11:15:01Z",
    "labels": [
        "porting: Solaris",
        "major",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "Python needs to search /usr/sfw/lib on Solaris for OpenSSL libraries.",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/8152",
    "user": "drkirkby"
}
```
Assignee: drkirkby

CC:  was jsp

Sage currently depends on OpenSSL to build the haslib module in Python. OpenSSL is not distributed with Sage due to license issues. However, the GPL allows us to link to the libraries if they are part of the core operating system, such as the kernel or compilers. (Someone could argue OpenSSL is not part of the core operating system, so even if it comes with the operating system, we can't use it. However, that is another issue.)

The OpenSSL libraries are installed on Solaris 10 in /usr/sfw/lib.  The problem is, python does not currently look there for the libraries. I've submitted an enhancement request to the Python bug database. 

http://bugs.python.org/issue7836

that they add that directory to the list of directories searched. 

Until this gets fixed, I believe we should add the directory /usr/sfw/lib to the top-level setup.py. Then Sage should build on Solaris 10 (but not OpenSolaris) without installation of any OpenSSL libraries. 

There is no point making this patch operating system specific, as the code in python is only a search path: 


```
       ssl_libs = find_library_file(self.compiler, 'ssl',lib_dirs,
                                     ['/usr/local/ssl/lib',
                                      '/usr/contrib/ssl/lib/'
                                     ] )

```


I'm not sure if we need to know the location of the include directories, but they are in /usr/src/include/openssl. There is again similar code in setup.py to search for the include files:


```
        # Detect SSL support for the socket module (via _ssl)
        search_for_ssl_incs_in = [
                              '/usr/local/ssl/include',
                              '/usr/contrib/ssl/include/'
                             ]

```


Any comments, before I go to the trouble of making a patch, which just appends the search path for the OpenSSL directories?  Does this seem a reasonable thing to do? 

Dave

Issue created by migration from https://trac.sagemath.org/ticket/8152





---

archive/issue_comments_071671.json:
```json
{
    "body": "> Sage currently depends on OpenSSL to build the haslib module in Python. \n\nAs I mentioned on the list, are we sure about this ?",
    "created_at": "2010-02-03T05:24:57Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71671",
    "user": "robertwb"
}
```

> Sage currently depends on OpenSSL to build the haslib module in Python. 

As I mentioned on the list, are we sure about this ?



---

archive/issue_comments_071672.json:
```json
{
    "body": "Let us discuss this on the list for now at least, then put some comments on the ticket when we have a more definate understanding of this.",
    "created_at": "2010-02-03T06:44:55Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71672",
    "user": "drkirkby"
}
```

Let us discuss this on the list for now at least, then put some comments on the ticket when we have a more definate understanding of this.



---

archive/issue_comments_071673.json:
```json
{
    "body": "+1\n\nFor the record, here's a link to the discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/df54a7a71b7aea65 (though I seem to recall a couple of other threads having relevant information as well).",
    "created_at": "2010-02-03T06:49:00Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71673",
    "user": "robertwb"
}
```

+1

For the record, here's a link to the discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/df54a7a71b7aea65 (though I seem to recall a couple of other threads having relevant information as well).



---

archive/issue_comments_071674.json:
```json
{
    "body": "Attachment [install.log.gz](tarball://root/attachments/some-uuid/ticket8152/install.log.gz) by drkirkby created at 2010-02-12 02:44:32\n\nInstall.log showing the failure for python to install properly.",
    "created_at": "2010-02-12T02:44:32Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71674",
    "user": "drkirkby"
}
```

Attachment [install.log.gz](tarball://root/attachments/some-uuid/ticket8152/install.log.gz) by drkirkby created at 2010-02-12 02:44:32

Install.log showing the failure for python to install properly.



---

archive/issue_comments_071675.json:
```json
{
    "body": "Here's one example of this failing on Solaris 10 03/2005. I freshly installed Solaris 10 on this machine yesterday. All that has been added are \n\n* Sun patch 123647-04 to overcome a bug in the supplied gcc 3.4.3\n* Installed gmp-4.3.2\n* Installed mpfr-2.4.2\n* Built gcc 4.4.3\n\nClearly there are failures on Solaris 10, which can be remidied by to LD_LIBRARY_PATH a directory containing the OpenSSL libraries. \n\n\n```\nSleeping for three seconds before testing python\nTraceback (most recent call last):\n  File \"<string>\", line 1, in <module>\n  File \"/export/home/drkirkby/sage-4.3.2/local/lib/python2.6/hashlib.py\", line 136, in <module>\n    md5 = __get_builtin_constructor('md5')\n  File \"/export/home/drkirkby/sage-4.3.2/local/lib/python2.6/hashlib.py\", line 63, in __get_builtin_constructor\n    import _md5\nImportError: No module named _md5\nhashlib module failed to import\n\nreal\t19m24.520s\nuser\t16m14.347s\nsys\t2m57.845s\nsage: An error occurred while installing python-2.6.4.p5\n```\n",
    "created_at": "2010-02-12T02:50:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71675",
    "user": "drkirkby"
}
```

Here's one example of this failing on Solaris 10 03/2005. I freshly installed Solaris 10 on this machine yesterday. All that has been added are 

* Sun patch 123647-04 to overcome a bug in the supplied gcc 3.4.3
* Installed gmp-4.3.2
* Installed mpfr-2.4.2
* Built gcc 4.4.3

Clearly there are failures on Solaris 10, which can be remidied by to LD_LIBRARY_PATH a directory containing the OpenSSL libraries. 


```
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/drkirkby/sage-4.3.2/local/lib/python2.6/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/drkirkby/sage-4.3.2/local/lib/python2.6/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5
hashlib module failed to import

real	19m24.520s
user	16m14.347s
sys	2m57.845s
sage: An error occurred while installing python-2.6.4.p5
```




---

archive/issue_comments_071676.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2015-04-09T10:17:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71676",
    "user": "jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_071677.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2015-04-09T10:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71677",
    "user": "jdemeyer"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_071678.json:
```json
{
    "body": "Obsolete I guess...",
    "created_at": "2015-04-09T10:18:05Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71678",
    "user": "jdemeyer"
}
```

Obsolete I guess...



---

archive/issue_comments_071679.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2015-04-09T12:12:24Z",
    "issue": "https://github.com/sagemath/sagetest/issues/8152",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/8152#issuecomment-71679",
    "user": "vbraun"
}
```

Resolution: fixed
