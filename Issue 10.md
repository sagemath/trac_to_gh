# Issue 10: Error building M2 under Linux without readline

Issue created by migration from Trac.

Original creator: was

Original creation time: 2006-09-12 18:04:56

Assignee: somebody

This is on a minimal Ubuntu install without the system-wide readline-dev package.
SAGE's M2 build script should use SAGE's readline, but it isn't. 


```
configure: error: missing library: readline
{'_': './spkg-install', 'CPPFLAGS': '-I/home/was/s/local/include  ', 'SAGE_LOCAL': '/home/was/s/local', '__sage__': '', 'PYTHONHOME': '/home/was/s/local', 'SSH_CLIENT': '192.168.3.1 51123 22', 'LOGNAME': 'was', 'USER': 'was', 'HOME': '/home/was', 'PATH': '/home/was/s/spkg/build/macaulay2-2006-08-26:/home/was/s:/home/was/s/local/bin:/home/was/s:/home/was/s/local/bin:/home/was/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/usr/bin/X11:/usr/games', 'LD_LIBRARY_PATH': '/home/was/s/local/lib:/home/was/s/local/lib:', 'LANG': 'en_US.UTF-8', 'TERM': 'xterm-color', 'SHELL': '/bin/bash', 'LIBRARY_PATH': '/home/was/s/local/lib:/home/was/s/local/lib:', 'LANGUAGE': 'en', 'LN': 'ln', 'SAGE_STARTUP_FILE': '/home/was/.sage//init.sage', 'UNAME': 'Linux', 'EDITOR': 'vi', 'LDFLAGS': '-L/home/was/s/local/lib/ ', 'GP_DATA_DIR': '/home/was/s/local/share/pari', 'TOUCH': 'touch', 'RM': 'rm', 'LESSOPEN': '| /usr/bin/lesspipe %s', 'SAGE_STARTUP_COMMAND': '\nfrom sage.all import *;import os; os.chdir("/home/was/s");import sage.misc.interpreter;from sage.misc.interpreter import attached_files;_=sage.misc.interpreter.load_startup_file("/home/was/.sage//init.sage");\n', 'CUR': '/home/was/s/spkg/build', 'CC': 'gcc', 'PYTHONPATH': ':/home/was/s/local/lib/python2.4', 'MKDIR': 'mkdir', 'LD': 'ld', 'SAGE_DATA': '/home/was/s/data', 'DYLD_LIBRARY_PATH': '/home/was/s/local/lib:/home/was/s/local/lib::/home/was/s/local/lib::', 'SAGE64': 'no', 'AS': 'as', 'AR': 'ar', 'RANLIB': 'ranlib', 'CP': 'cp', 'SAGE_ROOT': '/home/was/s', 'SSH_CONNECTION': '192.168.3.1 51123 192.168.3.3 22', 'LESSCLOSE': '/usr/bin/lesspipe %s %s', 'CXX': 'g++', 'SSH_TTY': '/dev/pts/0', 'OLDPWD': '/home/was/s/spkg/build', 'SAGE_SERVER': 'http://modular.math.washington.edu/sage/packages', 'CHMOD': 'chmod', 'HISTCONTROL': 'ignoredups', 'SHLVL': '4', 'PWD': '/home/was/s/spkg/build/macaulay2-2006-08-26', 'MV': 'mv', 'SHAREDFLAGS': '-fPIC', 'DOT_SAGE': '/home/was/.sage/', 'MAIL': '/var/mail/was', 'LS_COLORS': 'no=00:fi=00:di=01;34:ln=01;36:pi=40;33:so=01;35:do=01;35:bd=40;33;01:cd=40;33;01:or=40;31;01:su=37;41:sg=30;43:tw=30;42:ow=34;42:st=37;44:ex=01;32:*.tar=01;31:*.tgz=01;31:*.arj=01;31:*.taz=01;31:*.lzh=01;31:*.zip=01;31:*.z=01;31:*.Z=01;31:*.gz=01;31:*.bz2=01;31:*.deb=01;31:*.rpm=01;31:*.jar=01;31:*.jpg=01;35:*.jpeg=01;35:*.gif=01;35:*.bmp=01;35:*.pbm=01;35:*.pgm=01;35:*.ppm=01;35:*.tga=01;35:*.xbm=01;35:*.xpm=01;35:*.tif=01;35:*.tiff=01;35:*.png=01;35:*.mov=01;35:*.mpg=01;35:*.mpeg=01;35:*.avi=01;35:*.fli=01;35:*.gl=01;35:*.dl=01;35:*.xcf=01;35:*.xwd=01;35:*.flac=01;35:*.mp3=01;35:*.mpc=01;35:*.ogg=01;35:*.wav=01;35:', 'MAKE': 'make', 'SAGE_PACKAGES': '/home/was/s/spkg'}
Error configuring M2

real    16m57.258s
user    0m31.322s
sys     2m51.991s
sage: An error occured while installing macaulay2-2006-08-26
Please email William Stein <wstein`@`gmail.com> explaining the
problem and send him /home/was/s/install.log
If you want to try to fix the problem, *don't* just cd to
/home/was/s/spkg/build/macaulay2-2006-08-26 and type 'make'.
Instead (using bash) type "source local/bin/sage-env" from the directory
/home/was/s
in order to set all environment variables correctly, then cd to
/home/was/s/spkg/build/macaulay2-2006-08-26
```



---

Comment by was created at 2006-09-12 18:05:05

Changing priority from major to minor.


---

Comment by was created at 2006-10-18 20:55:40

NOTE: If you just install readline-dev (for ubuntu say), then the M2 build works.


---

Comment by mabshoff created at 2007-08-23 11:03:05

Changing component from basic arithmetic to packages.


---

Comment by mabshoff created at 2007-08-23 11:03:05

Changing assignee from somebody to was.


---

Comment by mabshoff created at 2007-09-05 21:17:01

There is a new Macaulay 2 release coming in a week or two. It is likely that an experimental package will appear before that.

Cheers,

Michael


---

Comment by mabshoff created at 2007-09-05 21:17:20

Changing assignee from was to mabshoff.


---

Comment by mabshoff created at 2007-09-07 21:49:49

Changing priority from minor to major.


---

Comment by mabshoff created at 2007-09-09 06:07:00

Changing status from new to assigned.


---

Comment by mabshoff created at 2007-09-13 03:56:22

There are too many problems at the moment, i.e. mostly that the configure script only picks up NTL from $SAGE_LOCAL, but not factory, libcf, BLAS & Lapack, so postpone this until 2.9.

Cheers,

Michael


---

Comment by was created at 2007-09-14 02:55:45

Changing type from defect to enhancement.


---

Comment by mabshoff created at 2008-01-30 16:35:28


```
Dear Macaulay 2 users,

We've released, as a test release, version 1.0.9test of M2.  Feel free to
download it from http://www.math.uiuc.edu/Macaulay2/Downloads/TestReleases/ and
try it out.  

We hope to release 1.1 within a week, based on this test.

The corresponding subversion (svn) URL is
svn://macaulay2.math.uiuc.edu/Macaulay2/release-branches/1.1, and after release
of 1.1 there will be "stable" URL corresponding to it.

This version fixes a recently detected bug (there since 0.9.95) in computations
with rings where the variables don't all have multi-degree vectors whose first
component is strictly positive.  Answers for total Ext (it computes Ext^n(M,N)
for all n at the same time) came out wrong, because it (necessarily) makes use
of such degree vectors.

This version also introduces good support for arbitrary precision real and
complex numbers.

Dan and Mike
```



---

Comment by mhansen created at 2008-02-27 12:25:28

Bump.  What is the status of the 1.1 spkg?  Is there anything I can do to help?


---

Comment by mabshoff created at 2008-02-27 21:48:54

Replying to [comment:14 mhansen]:
> Bump.  What is the status of the 1.1 spkg?  Is there anything I can do to help?

Hi mhansen: Lack of time. I have some notes that do 99.5% of the work for 1.1. We need to package various bits like boehm's gc either within the optional spkg or add some additional optional spkgs that get automatically installed. I am not sure what I will do during SD8, but maybe I will get to this.

Cheers,

Michael


---

Comment by gfurnish created at 2008-07-01 04:23:10

SPKG for 1.1 on OSX and Linux available at http://sage.math.washington.edu/home/gfurnish/spkg/macaulay2-1.1.spkg

Credit to Gary Furnish and Daniel Grayson.


---

Comment by gfurnish created at 2008-07-01 04:24:55

This depends on the gdbm and boehm_gc spkgs at #3531 and #3532.


---

Comment by gfurnish created at 2008-07-01 04:24:55

Changing status from assigned to new.


---

Comment by gfurnish created at 2008-07-01 04:24:55

Changing assignee from mabshoff to gfurnish.


---

Comment by was created at 2008-07-01 06:55:31

After installing the spkgs at #3531 and #3532 successfully, I get this:

```
...
configure: creating ./config.status
config.status: error: cannot find input file: GNUmakefile.in

real	0m20.569s
user	0m10.182s
sys	0m6.901s
sage: An error occurred while installing macaulay2-1.1
```



---

Comment by was created at 2008-07-01 06:59:27

Never mind -- my download was corrupted (by me).


---

Comment by mhansen created at 2008-07-01 07:28:19

The new spkg builds without errors on my Ubuntu 8.04 Core 2 Duo machine.


---

Comment by gfurnish created at 2008-07-01 17:19:46

This builds successfully on bsd.sage


---

Comment by gfurnish created at 2008-07-01 17:36:53

We are still making some changes to clean this up even more on other OS's.


---

Comment by mhansen created at 2008-07-06 18:12:30

The latest spkg built and installed fine for me on Linux.


---

Comment by mabshoff created at 2008-07-21 20:27:02

The spkg Gary provided has been uploaded to the experimental spkg repo replacing the previous spkg.

Cheers,

Michael


---

Comment by mabshoff created at 2008-07-21 20:27:25

Changing component from packages to experimental package.


---

Comment by mabshoff created at 2008-07-21 20:27:25

Finally merged in Sage 3.0.6.rc0 :)


---

Comment by mabshoff created at 2008-07-21 20:28:44

Finally merged in Sage 3.0.6.rc0 :)


---

Comment by mabshoff created at 2008-07-21 20:28:44

Resolution: fixed
