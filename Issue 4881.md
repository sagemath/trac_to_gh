# Issue 4881: [with spkgs, needs review] Experimental spkg for ETS-3.1.1 (including Chaco and Mayavi2)

Issue created by migration from Trac.

Original creator: jsp

Original creation time: 2008-12-26 15:52:24

Assignee: mabshoff

Keywords: 2D and 3D plotting

The Enthought Tool Suite [http://code.enthought.com/projects/](http://code.enthought.com/projects/)
has a lot of external dependencies,

The easiest way to install ets-3.1.1.spkg is

* download the spkgs from [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/) into
a $SAGE_ROOT of a reasonable recent sage

* download the shell script [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/install_ets.sh](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/install_ets.sh) and run it in $SAGE_ROOT

* wait a long time :)

After installation do a ./sage -sh and type mayavi2 to test the installation of
mayavi.

You can use mayavi mlab from within sage by starting with ./sage -wthread

See some screenshots: [http://picasaweb.google.com/j.spies88/ScreenshotsMlabMayavi210#](http://picasaweb.google.com/j.spies88/ScreenshotsMlabMayavi210#)

The user guide of Mayavi2 is Sphinxyfied: [http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/](http://code.enthought.com/projects/mayavi/docs/development/html/mayavi/)

Cheers,

Jaap


---

Comment by jsp created at 2008-12-26 17:04:47

Some screenshots from Chaco:

[http://code.enthought.com/projects/chaco/gallery.php](http://code.enthought.com/projects/chaco/gallery.php)

Jaap


---

Comment by was created at 2008-12-29 06:31:21

AT an absolutely bare minimum I would like to see this actually work on sage.math before it gets a positive review.  I just tried and even vtk wouldn't compile:

```
-- Looking for glXGetProcAddress - not found
-- Could not find extension loader.  Extensions disabled.
CMake Error: This project requires some variables to be set,
and cmake can not find them.
Please set the following variables:
OPENGL_INCLUDE_DIR (ADVANCED)

-- Configuring done
Error configuring VTK

real    0m19.176s
user    0m13.070s
sys     0m4.960s
sage: An error occurred while installing vtk-5.2
```


I then installed the libgl1-mesa-dev deb.

I do wish there could be a short quick sample .C program or autoconf script or something, that is very very unlikely to work unless opengl dev libraries, and all other obvious non-standard dependencies for building ETS are available.  Then this could be run first before the rest. 


Buildling takes a long time, so I'll comment further on this ticket as information becomes available.   I fully expect this to all work; it's just a matter of building the right dependencies.


---

Comment by was created at 2008-12-29 08:34:49

After doing this:

```
apt-get install libgl1-mesa-dev libglu1-mesa-dev
```

on sage.math, I was able to install all spkg's on the system-wide sage.


---

Comment by jsp created at 2008-12-29 12:32:35

Using vtk and wxPython we need an OpenGL (mesa is a good candidate).

We can test the installation of OpenGL at the start of spkg-install:


```
# Test OpenGL
glxinfo
if [ $? -ne 0 ]; then
    echo "Failed to find an OpenGL. Install mesa!"
    exit 1
fi

```


I tested this by putting away /usr/bin/glxinfo. Works for me.

I'll put up a changed vtk-5.2.skpg.

Same for wxPython.

Jaap


---

Comment by jsp created at 2008-12-29 13:40:43

On sage.math:



```
jsp`@`sage:~/sage/sage$ glxinfo
The program 'glxinfo' is currently not installed.  To run 'glxinfo' please ask your administrator to install the package 'mesa-utils'
-bash: glxinfo: command not found
jsp`@`sage:~/sage/sage$ 

```


Jaap


---

Comment by was created at 2008-12-30 01:20:14

Yeah, glxinfo is evidently separate from `libgl1-mesa-dev libglu1-mesa-dev` which are the devel libraries related to opengl that have to be installed.   I think it might be better to make a small minimal C program that tests for the presence of those libraries.


---

Comment by jsp created at 2008-12-30 02:11:17

Building is one thing. Using the package is another!

I can't imagine a mesa (OpenGL) install under linux without glxinfo, but ...

So I think glxinfo -h is a good test.

If not available, we suggest installation of all mesa.

In Fedora: sudo yum install "mesa*"

Testing the libraries is not enough!


---

Comment by was created at 2008-12-30 18:01:57

> "Testing the libraries is not enough!"

I tried to test whether or not this is the case, since right now sage.math is the un-imaginable opengl without glxinfo.  But when I tried I get that mayavi2 doesn't work at all even installed even after successfully installing all the spkg's in your distro.  But it doesn't look like this has anything to do with glxinfo:

```
wstein`@`sage:~/tmp/ETS$ ls -l /usr/local/sage/spkg/installed/*ets*
-rw-r--r-- 1 root root 260 2008-12-28 22:51 /usr/local/sage/spkg/installed/ets-3.1.1
wstein`@`sage:~/tmp/ETS$ ls -l /usr/local/sage/spkg/installed/*vtk*
-rw-r--r-- 1 root root 258 2008-12-28 22:28 /usr/local/sage/spkg/installed/vtk-5.2
wstein`@`sage:~/tmp/ETS$ sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

wstein`@`sage:~/tmp/ETS$ !which mayavi2
which sage mayavi2
/usr/local/sage/sage
/usr/local/sage/local/bin/mayavi2
wstein`@`sage:~/tmp/ETS$ !mayavi2
mayavi2
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/mayavi2", line 5, in <module>
    from pkg_resources import load_entry_point
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 2561, in <module>
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 626, in require
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 524, in resolve
pkg_resources.DistributionNotFound: EnthoughtBase>=3.0.2.dev
```


I'm not giving this a positive review until it works on sage.math. Do you have an account on sage.math?  If so, I think you should get it to work there, so I can give it a positive review.


---

Comment by was created at 2008-12-30 18:08:28

> I'm not giving this a positive review until it works on sage.math. Do you have an account 
> on sage.math? If so, I think you should get it to work there, so I can give it a positive 
> review.

I just want to add that I'm fully willing to install any standard ubuntu packages to get this to work.


---

Comment by jsp created at 2008-12-30 18:30:45

Does wxPython work?



```
To test do ./sage -sh
cd to local/share/wxPython/demo
Than try python demo.py
```


If not the OpenGL install is not working.

Yes, I do have an account, but don't know how to test and run X applications through ssh.

Is mesa-utils a standard ubuntu package? 

Jaap


---

Comment by jsp created at 2008-12-30 22:41:05

I need a proper X display:



```
jsp`@`sage:~/sage/sage$ ./sage -wthread
----------------------------------------------------------------------
----------------------------------------------------------------------
sage: Unable to access the X Display, is $DISPLAY set properly?
jsp`@`sage:~/sage/sage$ 
| Sage Version 3.2.1, Release Date: 2008-12-01                       |
| Type notebook() for the GUI, and license() for information.        |
```


Cheers,

Jaap


---

Comment by mabshoff created at 2008-12-30 22:42:07

Replying to [comment:11 jsp]:
> I need a proper X display:

Log into sage.math via "ssh -X"

Cheers,

Michael


---

Comment by jsp created at 2008-12-31 11:41:46

Replying to [comment:12 mabshoff]:
> Replying to [comment:11 jsp]:
> > I need a proper X display:
> 
> Log into sage.math via "ssh -X"
> 
> Cheers,
> 
> Michael


Did you test that?


```
/usr/bin/X11/xauth:  creating new authority file /home/jsp/.Xauthority
jsp`@`sage:~$ startx

X: cannot stat /etc/X11/X (No such file or directory), aborting.
giving up.
xinit:  No such file or directory (errno 2):  unable to connect to X server
xinit:  No such process (errno 3):  Server error.
Couldnt get a file descriptor referring to the console
jsp`@`sage:~$ 


Jaap


```



---

Comment by jsp created at 2008-12-31 14:22:23

Replying to [comment:9 was]:

> I just want to add that I'm fully willing to install any standard ubuntu packages to get this to work.  

Let us be realistic. How can we test and run X programs without an X-server?

This packages should be run and tested on a local PC with a good configured /etc/xorg.conf, etcetera.

Jaap


---

Comment by jsp created at 2008-12-31 14:49:35

Maybe the following will work:


```
The use of ssh enables a secure connection from a local X server to a remote application server.

    * Set X11Forwarding and AllowTcpForwarding entries to yes in /etc/ssh/sshd_config of the remote host, if you want to avoid corresponding command-line options.

    * Start the X server on the local host. (running)

    * Open an xterm in the local host. (done)

    * Run ssh to establish a connection with the remote site.

           localname `@` localhost $ ssh -q -X -l loginname remotehost.domain
           Password:
           .....

    * Run X application commands on the remote site.

           loginname `@` remotehost $ ./sage -wthread &

This method allows the display of the remote X client output as if it were locally connected through a local UNIX domain socket. 
```



Jaap


---

Comment by jsp created at 2008-12-31 15:32:16

Replying to [comment:15 jsp]:
> Maybe the following will work:
> 

> This method allows the display of the remote X client output as if it were locally connected through a local UNIX domain socket. 



This works on my local network.

Jaap


---

Comment by jsp created at 2009-01-18 19:51:25

Testing this over the net is mission impossible!

I now know what ETS means! Extra Terrestial Software.

I installed Ubuntu on an old laptop. Installed mesa, and more. It works like a charm!

sage.math is not the right platform to build, run and debug X11/OpenGL based software
based on interaction!

Jaap


---

Comment by jsp created at 2009-01-19 00:00:49

Among others I installed the following (most as dependencies):


```
libice-dev (version 2:1.0.4-1) will be installed
libpthread-stubs0 (version 0.1-2) will be installed
libpthread-stubs0-dev (version 0.1-2) will be installed
libsm-dev (version 2:1.0.3-2) will be installed
libx11-dev (version 2:1.1.5-2ubuntu1.1) will be installed
libxau-dev (version 1:1.0.3-3) will be installed
libxcb-xlib0-dev (version 1.1-1.1) will be installed
libxcb1-dev (version 1.1-1.1) will be installed
libxdmcp-dev (version 1:1.0.2-3) will be installed
libxext-dev (version 2:1.0.4-1) will be installed
libxi-dev (version 2:1.1.3-2build1) will be installed
libxt-dev (version 1:1.0.5-3) will be installed
tcl8.4-dev (version 8.4.19-2) will be installed
tk8.4-dev (version 8.4.19-1) will be installed
x11proto-core-dev (version 7.0.12-1ubuntu0.1) will be installed
x11proto-input-dev (version 1.4.3-2ubuntu6) will be installed
x11proto-kb-dev (version 1.0.3-3ubuntu1) will be installed
x11proto-xext-dev (version 7.0.2-6build1) will be installed
xtrans-dev (version 1.2-2) will be installed



build-essential (version 11.4) will be installed
debhelper (version 7.0.13ubuntu1) will be installed
dpkg-dev (version 1.14.20ubuntu6) will be installed
freeglut3-dev (version 2.4.0-6.1) will be installed
gettext (version 0.17-3ubuntu2) will be installed
html2text (version 1.3.2a-5) will be installed
intltool-debian (version 0.35.0+20060710.1) will be installed
lesstif2 (version 1:0.95.0-2.1ubuntu1) will be installed
libatk1.0-dev (version 1.24.0-0ubuntu1) will be installed
libcairo2-dev (version 1.8.0-0ubuntu1.1) will be installed
libexpat1-dev (version 2.0.1-4) will be installed
libfontconfig1-dev (version 2.6.0-1ubuntu4) will be installed
libfreetype6-dev (version 2.3.7-2ubuntu1) will be installed
libgl1-mesa-dev (version 7.2-1ubuntu2) will be installed
libglib2.0-dev (version 2.18.2-0ubuntu2) will be installed
libglu1-mesa-dev (version 7.2-1ubuntu2) will be installed
libglw1-mesa (version 7.0.3-0ubuntu1) will be installed
libgtk2.0-dev (version 2.14.4-0ubuntu1) will be installed
libgtkgl2.0-1 (version 2.0.0-1) will be installed
libgtkgl2.0-dev (version 2.0.0-1) will be installed
libgtkglext1-dev (version 1.2.0-1ubuntu1) will be installed
libgtkglextmm-x11-1.2 (version 1.2.0-0ubuntu1) will be installed
libmail-sendmail-perl (version 0.79-5) will be installed
libpango1.0-dev (version 1.22.2-0ubuntu1) will be installed
libpixman-1-dev (version 0.12.0-1) will be installed
libpng12-dev (version 1.2.27-1) will be installed
libsys-hostname-long-perl (version 1.4-2) will be installed
libxcb-render-util0-dev (version 0.2+git36-1) will be installed
libxcb-render0-dev (version 1.1-1.1) will be installed
libxcomposite-dev (version 1:0.4.0-3) will be installed
libxcursor-dev (version 1:1.1.9-1) will be installed
libxdamage-dev (version 1:1.1.1-4) will be installed
libxfixes-dev (version 1:4.0.3-2) will be installed
libxft-dev (version 2.1.12-3ubuntu1) will be installed
libxinerama-dev (version 2:1.0.3-2) will be installed
libxmu-dev (version 2:1.0.4-1) will be installed
libxmu-headers (version 2:1.0.4-1) will be installed
libxrandr-dev (version 2:1.2.3-1) will be installed
libxrender-dev (version 1:0.9.4-2) will be installed
mesa-common-dev (version 7.2-1ubuntu2) will be installed
mesademos (version 6.2.1-1) will be installed
po-debconf (version 1.0.15ubuntu1) will be installed
python-opengl (version 3.0.0~b3-1ubuntu2) will be installed
x11proto-composite-dev (version 1:0.4-2) will be installed
x11proto-damage-dev (version 1:1.1.0-2build1) will be installed
x11proto-fixes-dev (version 1:4.0-3) will be installed
x11proto-gl-dev (version 1.4.9-1) will be installed
x11proto-randr-dev (version 1.2.2-1) will be installed
x11proto-render-dev (version 2:0.9.3-2) will be installed
x11proto-xinerama-dev (version 1.1.2-5ubuntu1) will be installed
zlib1g-dev (version 1:1.2.3.3.dfsg-12ubuntu1) will be installed

```


and xorg-dev: libXtst, etc,

Jaap


---

Comment by jason created at 2009-01-30 17:06:57

I hope that it would be possible to use from sage.math via X11 forwarding, but the OpenGL may be problematic.  As it is, I get:


```
jason`@`sage:~$ sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

jason`@`sage:~$ mayavi2 
Traceback (most recent call last):
  File "/usr/local/sage/local/bin/mayavi2", line 5, in <module>
    from pkg_resources import load_entry_point
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 2561, in <module>
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 626, in require
  File "build/bdist.linux-x86_64/egg/pkg_resources.py", line 524, in resolve
pkg_resources.DistributionNotFound: EnthoughtBase>=3.0.2.dev
```


X11 Forwarding works for me (via ssh -X sage.math.washington.edu).

I'll try installing these packages locally.


---

Comment by cwitty created at 2009-02-04 05:53:46

I ran into some very annoying problems with this package, where it appeared to build successfully but then failed to work.  I can't recommend this spkg (even for experimental) until something is done.

There were two separate issues.  Both allowed an apparently successful build which then failed to run.  The first is that some X libraries were not installed on my machine; when I tried to run mayavi2, I got the 

```
pkg_resources.DistributionNotFound: EnthoughtBase>=3.0.2.dev
```

error described above.

Once that was fixed, mayavi2 still would not run; this time I got this error:

```
ImportError: cannot import name cached_property
```

This time the problem was that I had installs of previous versions of these spkgs in site-python.  Once I removed those, I was able to successfully install and run this spkg.

IMHO, the current status is not acceptable even for experimental.  At least, the package should detect at build time that it did not build successfully (that mayavi2 cannot be run successfully), and fail the build in this case; and also print out some useful text (Something along the lines of "Try installing xorg-dev and removing old versions of this package from site-python", but a bit more detailed and acknowledging the existence of systems other than Debian/Ubuntu).


---

Comment by jsp created at 2009-02-06 22:57:43

Replying to [comment:20 cwitty]:
> I ran into some very annoying problems with this package, where it appeared to build successfully but then failed to work.  I can't recommend this spkg (even for experimental) until something is done.
> 

I added some tests.

> There were two separate issues.  Both allowed an apparently successful build which then failed to run.  The first is that some X libraries were not installed on my machine; when I tried to run mayavi2, I got the 
> {{{
> pkg_resources.DistributionNotFound: EnthoughtBase>=3.0.2.dev
> }}}
> error described above.
> 
> Once that was fixed, mayavi2 still would not run; this time I got this error:
> {{{
> ImportError: cannot import name cached_property
> }}}
> This time the problem was that I had installs of previous versions of these spkgs in site-python.  Once I removed those, I was able to successfully install and run this spkg.
> 

spkg-install now removes mayavi_2.x.y installs.

> IMHO, the current status is not acceptable even for experimental.  At least, the package should detect at build time that it did not build successfully (that mayavi2 cannot be run successfully), and fail the build in this case; and also print out some useful text (Something along the lines of "Try installing xorg-dev and removing old versions of this package from site-python", but a bit more detailed and acknowledging the existence of systems other than Debian/Ubuntu).

The first installs were on Fedora 9 and 10! Ubuntu/Debian came along recently.

I put in some more tests in spkg-install. Maybe this helps. I could build this package on sage.math (there are some runtime problems).

At the end I give some advice how to check the install.

See sage.math.washington.edu/home/jsp/sage/sage-3.2.3/

Try ./sage -sh

mayavi2

there

Cheers,

Jaap


---

Comment by jsp created at 2009-02-26 22:43:57

OK, let me state once more: this is taking way to long! Remember this is experimental!!

Some guys have installed this with success, among them Carl Witty, Jason Grout and Ondrej Certik on various hardware.

I resign on having this run on sage.math. There are to much problems with building and debugging this on a remote server!

So I propose the wstein criterium: 'this should run on sage.math' will go away. If not, I'm off and propose this ticket to be closed. And I'll open a new ticket, more up to date: ets-3.1.1.rev23061.spkg

[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/ets-3.1.1.rev23061.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/ets-3.1.1.rev23061.spkg)

to be found with dependencies in:

[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/)

Anyway time flies, so we better go for the latest.

Jaap


---

Comment by mabshoff created at 2009-02-26 23:02:52

Replying to [comment:22 jsp]:

Hi Jaap,

> OK, let me state once more: this is taking way to long! Remember this is experimental!!

See my comments on #4880.

> Some guys have installed this with success, among them Carl Witty, Jason Grout and Ondrej Certik on various hardware.

Yes, but after updating the spkg you did not change the summary, hence if you look for things to review this ticket falls off my list since its status is "needs work".


> I resign on having this run on sage.math. There are to much problems with building and debugging this on a remote server!
> 
> So I propose the wstein criterium: 'this should run on sage.math' will go away.

It is only for optional spkgs, not experimental. Experimental can be broken badly, there is no guarantees. It would generally be nice if experimental spkgs worked on sage.math, but given the missing X and all that it is hard to make things like this spkg work.

> If not, I'm off and propose this ticket to be closed. And I'll open a new ticket, more up to date: ets-3.1.1.rev23061.spkg
> 
> [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/ets-3.1.1.rev23061.spkg](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/ets-3.1.1.rev23061.spkg)
> 
> to be found with dependencies in:
> 
> [http://sage.math.washington.edu/home/jsp/SPKGS/ETS/](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/)
> 
> Anyway time flies, so we better go for the latest.
> 
> Jaap


I have updated the summary to reflect the updated spkg. Generally there is no point in closing this and opening another ticket if you updated the spkg in the admittedly too long review time.

Cheers,

Michael


---

Comment by jsp created at 2009-02-26 23:24:25

Replying to [comment:23 mabshoff]:

> > So I propose the wstein criterium: 'this should run on sage.math' will go away.
> 
> It is only for optional spkgs, not experimental. Experimental can be broken badly, there is no guarantees. It would generally be nice if experimental spkgs worked on sage.math, but given the missing X and all that it is hard to make things like this spkg work.
> 

Citing from a comment from wstein above: 

I'm not giving this a positive review until it works on sage.math. Do you have an account on sage.math? If so, I think you should get it to work there, so I can give it a positive review.

So, I was confused in some way! Let us have some clear criteria on experimental :).

Jaap


---

Comment by jsp created at 2009-02-27 19:44:26

An animation, see:

[http://sage.math.washington.edu/home/jsp/animations/anim_surf.mov](http://sage.math.washington.edu/home/jsp/animations/anim_surf.mov)

Cheers,

Jaap


---

Comment by was created at 2009-03-16 18:06:37


```
    So... do you want us to

    [ ] drop all the spkg's in experimental, or


Drop them in experimental. I think that will give them some exposure
and who knows there are people around who can help porting to OSX
and Windows. I would like to see comments in the second column of
http://www.sagemath.org/packages/experimental/

```


Since these are experimental and our standards for that are "we know where to find you if you sneak 'rm -rf *' in", but not much else, and based on Jaap's wishes above, I give this a positive review.


---

Comment by jsp created at 2009-03-17 18:16:26

For the latest spks see:

[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/?C=M;O=D](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/?C=M;O=D)

For instructions see the REAME.txt

Jaap


---

Comment by mabshoff created at 2009-04-01 05:39:53

Resolution: fixed


---

Comment by mabshoff created at 2009-04-01 05:39:53

Closed in the Sage 3.4.1 time frame by merging ets-3.1.1.rev23241.spkg into the experimental spkg repo.

Jaap: Is there anything else that needed uploading? In case there is just comment on the ticket and I will take care of it - no need to reopen this ticket or open another one.

Cheers,

Michael


---

Comment by jsp created at 2009-04-01 08:55:15

Replying to [comment:28 mabshoff]:

> Jaap: Is there anything else that needed uploading? In case there is just comment on the ticket and I will take care of it - no need to reopen this ticket or open another one.
> 

Needed to build ets:


```
configobj-4.5.3.spkg
reportlab-2.2.spkg
setupdocs.spkg
swig-1.3.31.spkg
vtk-5.2.1.spkg
wxPython-2.8.9.1.spkg
```


All can be found here:
[http://sage.math.washington.edu/home/jsp/SPKGS/ETS/](http://sage.math.washington.edu/home/jsp/SPKGS/ETS/)
