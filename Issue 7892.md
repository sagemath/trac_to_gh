# Issue 7892: Python fails to build hashlib module on Solaris 8

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-01-11 00:22:44

Assignee: drkirkby

CC:  jsp dimpase

Although Solaris 8 is not supported, I thought I'd try a build of Sage 4.3 on a Sun Blade 1000 running Solaris 8 10/2001 - the first release of Solaris 8 I believe. 

This was useful, as it highlighted a failure in Python's spkg-install. The spkg-install exited with no useful error message - it did not give a clue where the failure was, due to incorrect usage of 'set -e'.  

However, after correcting the spkg-install issue (#7761), the reason for the failure become apparent - a failure to build the Python haslib module. This is exactly the same failure which caused myself and Jaap Spies a lot of grief - see #7761. 

It would appear that either the wrong version of OpenSSL or a mixture of OpenSSL versions can easily cause Python to fail to build the haslib module. Finding a suitable version can be tricky, and there is no obvious way to specify which version of OpenSSL python should use if there are more than one version present. In this case, I believe there was only one version, so I'm unsure why Python would not build haslib with it. Perhaps this version is too new for the version of Python in Solaris

For this Solaris 8 build, I purposely used oldish versions of tools when I built from source, but used whatever I found first on Sunfreeware for the binaries, which tend to be a lot newer than 2001 when this version of Solaris was released. The basic build process was:

 * Install Solaris 8 Solaris 8 10/01 (an old i.e. October 2001 release)
 * Download wget 1.12, which needed OpenSSL. The version of OpenSSL installed was 0.9.8l, which is the latest release.
 * Download a binary of gcc 3.4.6 from Sunfreeware.com, as this version of Solaris 8 came with no gcc. 
 * Download necessary libraries for gcc.
 * Install gcc 4.0.4 from source, as gcc 3.4.6 is too old to build Sage. 
 * Download a binary of perl v5.8.8 from Sunfreeware, as the perl 5.005_03 in Solaris 8 is too old to build Sage (or at least 'prereq' exits with a version this old. I doubt anyone has actually tested all versions to find the absolute minimum necessary). 
 
*It would appear we need to address exactly the issue of OpenSSL with Solaris, as it is problematic.*


```
changing mode of /export/home/drkirkby/sage-4.3/local/lib/python2.6/lib-dynload/_multiprocessing_failed.so to 755
changing mode of /export/home/drkirkby/sage-4.3/local/lib/python2.6/lib-dynload/_ctypes.so to 755
changing mode of /export/home/drkirkby/sage-4.3/local/lib/python2.6/lib-dynload/ to 755
running install_scripts
copying build/scripts-2.6/pydoc -> /export/home/drkirkby/sage-4.3/local/bin
copying build/scripts-2.6/idle -> /export/home/drkirkby/sage-4.3/local/bin
copying build/scripts-2.6/2to3 -> /export/home/drkirkby/sage-4.3/local/bin
copying build/scripts-2.6/smtpd.py -> /export/home/drkirkby/sage-4.3/local/bin
changing mode of /export/home/drkirkby/sage-4.3/local/bin/pydoc to 755
changing mode of /export/home/drkirkby/sage-4.3/local/bin/idle to 755
changing mode of /export/home/drkirkby/sage-4.3/local/bin/2to3 to 755
changing mode of /export/home/drkirkby/sage-4.3/local/bin/smtpd.py to 755
running install_egg_info
Writing /export/home/drkirkby/sage-4.3/local/lib/python2.6/lib-dynload/Python-2.6.2-py2.6.egg-info
if test -f /export/home/drkirkby/sage-4.3/local/bin/python -o -h /export/home/drkirkby/sage-4.3/local/bin/python; \
        then rm -f /export/home/drkirkby/sage-4.3/local/bin/python; \
        else true; \
        fi
(cd /export/home/drkirkby/sage-4.3/local/bin; ln python2.6 python)
rm -f /export/home/drkirkby/sage-4.3/local/bin/python-config
(cd /export/home/drkirkby/sage-4.3/local/bin; ln -s python2.6-config python-config)
./install-sh -c -m 644 ./Misc/python.man \
                /export/home/drkirkby/sage-4.3/local/share/man/man1/python.1
make[2]: Leaving directory `/export/home/drkirkby/sage-4.3/spkg/build/python-2.6.2.p5/src'
Sleeping for three seconds before testing python
Traceback (most recent call last):
  File "<string>", line 1, in <module>
  File "/export/home/drkirkby/sage-4.3/local/lib/python2.6/hashlib.py", line 136, in <module>
    md5 = __get_builtin_constructor('md5')
  File "/export/home/drkirkby/sage-4.3/local/lib/python2.6/hashlib.py", line 63, in __get_builtin_constructor
    import _md5
ImportError: No module named _md5
hashlib module failed to import

real    10m31.767s
user    8m6.410s
sys     1m51.870s
sage: An error occurred while installing python-2.6.2.p5
```





---

Comment by drkirkby created at 2010-01-15 21:52:05

Changing priority from major to minor.


---

Comment by drkirkby created at 2010-01-15 21:52:05

I'm drooping the priority of this, as Solaris 8 is not supported.


---

Comment by mkoeppe created at 2020-04-25 02:56:36

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-04-25 02:56:36

outdated, should be closed


---

Comment by dimpase created at 2020-04-25 04:11:39

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-04-25 06:23:43

Resolution: invalid
