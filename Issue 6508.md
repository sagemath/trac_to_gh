# Issue 6508: make installing extcode depend on mercurial

Issue created by migration from Trac.

Original creator: was

Original creation time: 2009-07-10 17:44:39

Assignee: mabshoff


```


On Fri, Jul 10, 2009 at 8:08 AM, Jan Groenewald<jan`@`aims.ac.za> wrote:
>
> Hi
>
> sage -upgrade 4.0 to 4.1:
>
>
> Finished extraction
> ****************************************************
> Host system
> uname -a:
> Linux hamerkop 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 22:12:12 UTC 2009 x86_64 GNU/Linux
> ****************************************************
> ****************************************************
> GCC Version
> gcc -v
> Using built-in specs.
> Target: x86_64-linux-gnu
> Configured with: ../src/configure -v --with-pkgversion='Ubuntu 4.3.3-5ubuntu4' --with-bugurl=file:///usr/share/doc/gcc-4.3/README.Bugs --enable-languages=c,c++,fortran,objc,obj-c++ --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --with-gxx-include-dir=/usr/include/c++/4.3 --program-suffix=-4.3 --enable-clocale=gnu --enable-libstdcxx-debug --enable-objc-gc --enable-mpfr --with-tune=generic --enable-checking=release --build=x86_64-linux-gnu --host=x86_64-linux-gnu --target=x86_64-linux-gnu
> Thread model: posix
> gcc version 4.3.3 (Ubuntu 4.3.3-5ubuntu4)
> ****************************************************
> Traceback (most recent call last):
>  File "/usr/local/src/sage-4.0/local/bin/hg", line 11, in <module>
>    from mercurial import demandimport; demandimport.enable()
> ImportError: No module named mercurial
> Traceback (most recent call last):
>  File "/usr/local/src/sage-4.0/local/bin/hg", line 11, in <module>
>    from mercurial import demandimport; demandimport.enable()
> ImportError: No module named mercurial
> Traceback (most recent call last):
>  File "/usr/local/src/sage-4.0/local/bin/hg", line 11, in <module>
>    from mercurial import demandimport; demandimport.enable()
> ImportError: No module named mercurial
> Traceback (most recent call last):
>  File "/usr/local/src/sage-4.0/local/bin/hg", line 11, in <module>
>    from mercurial import demandimport; demandimport.enable()
> ImportError: No module named mercurial
> Traceback (most recent call last):
>  File "/usr/local/src/sage-4.0/local/bin/hg", line 11, in <module>
>    from mercurial import demandimport; demandimport.enable()
> ImportError: No module named mercurial
>
> real    0m0.049s
> user    0m0.020s
> sys     0m0.028s
> sage: An error occurred while installing extcode-4.1
> Please email sage-devel http://groups.google.com/group/sage-devel
> explaining the problem and send the relevant part of
> of /usr/local/src/sage-4.0/install.log.  Describe your computer, operating system, etc.
> If you want to try to fix the problem, yourself *don't* just cd to
> /usr/local/src/sage-4.0/spkg/build/extcode-4.1 and type 'make'.
> Instead type "/usr/local/src/sage-4.0/sage -sh"
> in order to set all environment variables correctly, then cd to
> /usr/local/src/sage-4.0/spkg/build/extcode-4.1
> (When you are done debugging, you can type "exit" to leave the
> subshell.)
> make: *** [installed/extcode-4.1] Error 1
>
> real    0m2.154s
> user    0m1.992s
> sys     0m0.112s
> Error building Sage.
> Error installing Sage!
> 1 root`@`hamerkop:/usr/local/src/sage-4.0#
>
>
> I guess this means only half my installation is upgraded and it is a bit b0rked now?

Just manually force mercurial to install via 

   sage -f mercurial-1.1.2.p0

then type "make" (or "sage -upgrade") after that finishes to continue the upgrade.

I think this caused by a mistake in the spkg/standard/deps file.  These lines are wrong:

$(INST)/$(EXTCODE): $(BASE)
        $(SAGE_SPKG) $(EXTCODE) 2>&1

since clealry installing the EXTCODE package depends on mercurial.  It should be:

$(INST)/$(EXTCODE): $(BASE)  $(INST)/$(MERCURIAL)
        $(SAGE_SPKG) $(EXTCODE) 2>&1

```



---

Comment by mvngu created at 2009-08-03 07:06:05

The file `SAGE_ROOT/spkg/standard/deps` has been changed so that now the lines for extcode are:

```
# Mercurial must be built before building extcode. See trac ticket #6508.
$(INST)/$(EXTCODE): $(BASE) $(INST)/$(MERCURIAL)
        $(SAGE_SPKG) $(EXTCODE) 2>&1
```

I'm building Sage 4.0 from source on sage.math so that I can test upgrading from that version to the latest rc release of Sage 4.1.1. This should take a while to test.


---

Comment by mvngu created at 2009-08-05 00:07:53

The above changes seem to be working fine for me. I'm releasing these changes with Sage 4.1.1.rc1 so others can test upgrading from Sage 4.0 to 4.1.1.rc1. If all goes well, this ticket would be closed as being merged in Sage 4.1.1.rc1.


---

Comment by mvngu created at 2009-08-07 09:33:28

This has been fixed in Sage 4.1.1.rc2. So I'm closing this ticket as fixed.


---

Comment by mvngu created at 2009-08-07 09:33:28

Resolution: fixed
