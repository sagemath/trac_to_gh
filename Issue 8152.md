# Issue 8152: Python needs to search /usr/sfw/lib on Solaris for OpenSSL libraries.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-02-02 11:15:01

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


---

Comment by robertwb created at 2010-02-03 05:24:57

> Sage currently depends on OpenSSL to build the haslib module in Python. 

As I mentioned on the list, are we sure about this ?


---

Comment by drkirkby created at 2010-02-03 06:44:55

Let us discuss this on the list for now at least, then put some comments on the ticket when we have a more definate understanding of this.


---

Comment by robertwb created at 2010-02-03 06:49:00

+1

For the record, here's a link to the discussion: http://groups.google.com/group/sage-devel/browse_thread/thread/df54a7a71b7aea65 (though I seem to recall a couple of other threads having relevant information as well).


---

Attachment

Install.log showing the failure for python to install properly.


---

Comment by drkirkby created at 2010-02-12 02:50:39

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

Comment by jdemeyer created at 2015-04-09 10:17:53

Changing status from new to needs_review.


---

Comment by jdemeyer created at 2015-04-09 10:18:05

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2015-04-09 10:18:05

Obsolete I guess...


---

Comment by vbraun created at 2015-04-09 12:12:24

Resolution: fixed
