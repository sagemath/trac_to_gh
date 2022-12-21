# Issue 6626: can't upgrade to cliquer-1.2.p0 since package name is missing from file deps

Issue created by migration from Trac.

Original creator: mvngu

Original creation time: 2009-07-26 08:26:02

Assignee: mabshoff

CC:  ncohen rlm

Keywords: cliquer

As the subject says. This is a follow up to #6355.


---

Comment by mvngu created at 2009-07-26 08:26:57

The SPKG installs OK if doing so from source. But there is a problem when it comes to upgrading from 4.1.1.alpha0 to 4.1.1.alpha1. Here's a relevant snippet:

```
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: dsage-1.0.1.p0 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable

real	58m23.858s
user	52m19.696s
sys	4m53.842s
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 259, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
Double checking that all packages have been installed.
Downloading packages from http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard
Reading package lists...
Done
The following packages will be upgraded:
  cliquer-1.2.p0
* WARNING: This is a source-based upgrade, which could take hours, fail and render your Sage install useless!!
Do you want to continue [y/N]? y
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/cliquer-1.2.p0.spkg --> cliquer-1.2.p0.spkg
[..........]
Deleting old spkg cliquer-1.2.p0.spkg
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/install --> install
[.]
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/deps --> deps
[..]
http://sage.math.washington.edu/home/mvngu/release/sage-4.1.1.alpha1//spkg/standard/newest_version --> newest_version
[.]
sage-spkg sage-4.1.1.alpha1 
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
sage-4.1.1.alpha1
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: sage-4.1.1.alpha1 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable
sage-spkg gap-4.4.10.p12 2>&1
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
gap-4.4.10.p12
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: gap-4.4.10.p12 is already installed
sage-spkg dsage-1.0.1.p0 2>&1
You must set the SAGE_ROOT environment variable or
run this script from the SAGE_ROOT or 
SAGE_ROOT/local/bin/ directory.
dsage-1.0.1.p0
Machine:
Linux darkstar 2.6.28-13-generic #45-Ubuntu SMP Tue Jun 30 19:49:51 UTC 2009 i686 GNU/Linux
sage: dsage-1.0.1.p0 is already installed
cd /home/mvngu/usr/bin/sage && . local/bin/sage-env && cd local/bin/ && ./sage-make_relative
Making script relocatable

real	0m0.414s
user	0m0.156s
sys	0m0.184s
Traceback (most recent call last):
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 673, in <module>
    getattr(get_builder(name), type)()
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 259, in _wrapper
    getattr(get_builder(document), name)(*args, **kwds)
  File "/home/mvngu/usr/bin/sage/devel/sage/doc/common/builder.py", line 616, in get_builder
    elif name in get_documents() or name in AllBuilder().get_all_documents():
NameError: global name 'get_documents' is not defined
```

Apparently, the package name should have been added to the file

```
SAGE_ROOT/spkg/standard/deps
```



---

Comment by rlm created at 2009-07-27 15:55:54

Replying to [comment:1 mvngu]:
> Apparently, the package name should have been added to the file
> {{{
> SAGE_ROOT/spkg/standard/deps
> }}}

This has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.


---

Comment by mvngu created at 2009-07-28 03:17:12

Replying to [comment:2 rlm]:
> Replying to [comment:1 mvngu]:
> > Apparently, the package name should have been added to the file
> > {{{
> > SAGE_ROOT/spkg/standard/deps
> > }}}
> 
> This has always been the release manager's job. For example, when I added ratpoints to sage-4.1, I just put the relevant lines into `deps` myself, since I was managing the release.
Ah... I didn't know about this. The release management wiki page should have some information about updating the `deps` file, if it's not there already. Looks like this ticket is now invalid, right?


---

Comment by rlm created at 2009-07-30 15:15:57

Resolution: invalid
