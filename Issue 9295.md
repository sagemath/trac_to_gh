# Issue 9295: Add an spkg-check file for Python

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-06-21 11:01:52

Assignee: tbd

CC:  jsp

Despite the pivotal roles Python plays in Sage, the Python package is not tested by running "make test" even if the variable SAGE_CHECK is set to yes. This patch ensures it does get checked in such cases, by adding the file spkg-check, which gets run if and only if SAGE_CHECK is set to yes. 

The ticket is based on that at #9041, which has already received positive review, and includes some other python fixes. Since that is not merged, I've just left the patch level unchanged at .p9, but added another entry to the SPKG.txt file under .p9

Thank you to François Bissey who bought to my attention that 'make test' would test the python package. 

Dave 


---

Comment by drkirkby created at 2010-06-21 11:10:59

Mercurial patch to add an spkg-check file for Python


---

Attachment

Here's the revised package. 


http://boxen.math.washington.edu/home/kirkby/revised-patches/python-2.6.4.p9.spkg

With those changes, and SAGE_CHECK exported to "yes", so the test suite is run: 


```
Sleeping for three seconds before testing python
math module OK
hashlib module imported

real	1m30.977s
user	1m13.338s
sys	0m11.943s
Successfully installed python-2.6.4.p9
Running the test suite.
Testing the Python package
running build
running build_ext
<snip>
test_grammar
test_opcodes
test_dict
test_builtin
test_exceptions
test_types
test_unittest
test_doctest
test_doctest2
test_MimeWriter
test_SimpleHTTPServer
```


On my Sun Ultra 27 (OpenSolaris 06/2009), there are a few failures


```
322 tests OK.
5 tests failed:
    test_distutils test_float test_hotshot test_multiprocessing
    test_sunaudiodev
38 tests skipped:
    test_aepack test_al test_applesingle test_bsddb test_bsddb185
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_epoll test_gdbm test_gl test_imgfile test_kqueue
    test_linuxaudiodev test_macos test_macostools test_normalization
    test_ossaudiodev test_pep277 test_py3kwarn test_scriptpackages
    test_smtpnet test_socketserver test_ssl test_startfile test_tcl
    test_timeout test_urllib2net test_urllibnet test_winreg
    test_winsound test_zipfile64
2 skips unexpected on sunos5:
    test_tcl test_ssl
make[2]: *** [test] Error 1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.4.4.alpha1/spkg/build/python-2.6.4.p9/src'
An error occured whilst testing Python
*************************************
```


so it was useful to know about these. 

*Note, failures detected by the test routine do NOT stop stage building unless SAGE_CHECK is set to yes, so the fact the test suite finds failures has no detrimental effect on Sage, but should highlight areas where we should be concerned*

Dave


---

Comment by jhpalmieri created at 2010-06-21 17:49:58

Is this ready for review?

Given the positive review for #9041, this basically looks good to me.  On my mac, I get test failures also:

```
5 tests failed:
    test_asynchat test_ctypes test_distutils test_locale test_smtplib
39 tests skipped:
    test__locale test_aepack test_al test_applesingle test_bsddb
    test_bsddb3 test_cd test_cl test_codecmaps_cn test_codecmaps_hk
    test_codecmaps_jp test_codecmaps_kr test_codecmaps_tw test_curses
    test_dl test_epoll test_gdbm test_gl test_imageop test_imgfile
    test_largefile test_linuxaudiodev test_macos test_macostools
    test_normalization test_ossaudiodev test_pep277 test_py3kwarn
    test_scriptpackages test_smtpnet test_socketserver test_startfile
    test_sunaudiodev test_timeout test_urllib2net test_urllibnet
    test_winreg test_winsound test_zipfile64
5 skips unexpected on darwin:
    test_macos test_applesingle test_dl test_aepack
    test_scriptpackages
```

Two comments: if I set SAGE_CHECK to "yes" and run "sage -i python...", then it tells me that an error occurred, but then I get

```
$ echo ?$
0
```

I think this is a problem with how the script sage-sage is written, not this patch.

Also, "occurred" is misspelled in sage-check: it's missing an "r". Please fix this. The use of "whilst" looks a little strange to me, since it is followed a few lines later with "while" (from the script sage-spkg):

```
An error occured whilst testing Python
*************************************
Error testing package ** python-2.6.4.p9 **
*************************************
sage: An error occurred while testing python-2.6.4.p9
```

But that doesn't need to be changed.


---

Comment by drkirkby created at 2010-06-21 18:39:04

Changing status from new to needs_review.


---

Comment by drkirkby created at 2010-06-21 18:39:04

Yes, it is ready for review - I should have marked it as such. 

I'll sort out the spelling error and repost. 

Dave


---

Comment by drkirkby created at 2010-06-21 18:46:12

Correction of grammer and spelling.


---

Attachment

I've corrected the spelling error, and the grammar too. 

I've tried on two systems and 5 test failures on each. You get 5 too, though they are not all the same. However, we all get ' test_distutils' fail. I've seen some references in trac tickets, and/or .spkg files alluding to the fact distuils is not very good. 

Dave


---

Comment by drkirkby created at 2010-06-21 18:49:33

Changing assignee from tbd to drkirkby.


---

Comment by jhpalmieri created at 2010-06-21 18:51:55

I don't know if "whilst" is a grammar issue or just an issue of which side of the Atlantic you're from.

Anyway, positive review.


---

Comment by jhpalmieri created at 2010-06-21 18:51:55

Changing status from needs_review to positive_review.


---

Comment by drkirkby created at 2010-06-21 21:01:36

Just to make it clear, the package is still at 

http://boxen.math.washington.edu/home/kirkby/revised-patches/python-2.6.4.p9.spkg


---

Comment by rlm created at 2010-06-25 15:52:24

Resolution: fixed
