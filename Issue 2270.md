# Issue 2270: glib spkg

Issue created by migration from Trac.

Original creator: gfurnish

Original creation time: 2008-02-22 23:17:14

Assignee: gfurnish

glib is a c library with algorithms for just about everything under the sun.  The documentation for the library is available at http://library.gnome.org/devel/glib/2.14/ and the spkg itself may be downloaded at http://www.indirectproof.net/sage/glib-2.14.0.spkg




---

Comment by mabshoff created at 2008-02-22 23:18:51

Changing priority from minor to major.


---

Comment by gfurnish created at 2008-02-22 23:23:43

Changing status from new to assigned.


---

Comment by malb created at 2008-02-25 11:23:15

My five cents (William asked me to comment):
 * `glib` is a pretty mature and well respected library, so I
   wouldn't expect any bad surprises here
 * I never worked with it but the API documentation reads really good
 * I also suspect that it is reasonably fast but I don't know. But it seems hard to screw this up (at least for stuff like linked lists). But do we really see a speed improvement if Python objects are thrown in these data structures?
 * It would be nice to have a 2-3 page tutorial on how to use it from Sage/Cython and how it interacts with Python objects.
 * If it builds everywhere and the size is manageable I say: include!


---

Comment by gfurnish created at 2008-03-01 05:14:35

Moved spkg to http://sage.math.washington.edu/home/gfurnish/glib-2.14.0.spkg


---

Comment by was created at 2008-03-01 05:39:30

REFEREE REPORT:

1. There is no .hg directory in the spkg.

2. The SPKG.txt is empty (and doesn't following the official format).

3. This code should all be completely deleted; it doesn't make any sense to include.

```
 #NOTE: Be sure to also update patches/gap*


# Indicate that glib has somehow been updated, which invalidates all workspaces.
touch "$SAGE_LOCAL/bin/glib_stamp"
```


That stamp stuff is *only* for Gap, and not for any other spkg.  See #527.

4. It's bad form and error prone to have the explicit version and package
number of the glib directory in the spkg-install.  In particularly, doing

```
TARGET="glib-2.14.0"  
INSTALL_DIR=$SAGE_LOCAL/lib/$TARGET
```

looks really suspicious to me.  Why install to glib-2.14.0?  

5. I think these two lines could delete a users Sage install if
there is a space in the install directory ($SAGE_LOCAL).  I haven't
tested this.  

```
    INSTALL_DIR=$SAGE_LOCAL/lib/$TARGET
    rm -rf $INSTALL_DIR
```

There *will* eventually be users with spaces in 
their install directory names -- we try hard to support this, and
should in fact start testing it.   Basically just do the above
but put quotes around things.   Also, is it really necessary
to remove the old install directory?  We do that in other spkg's
only when it turns out that not doing so leads to serious breakage
problems on upgrades. 

6. There is a set of quotes missing here:

```
    ./configure --prefix=$SAGE_LOCAL PREFIX="$SAGE_LOCAL" CC="$CC" CXX="$CXX"
```


7. Is it really necessary to do all these explicit copies
instead of `make install`?  Is make install broken for glibc?

```
    $CP ./glib/*.la .
    $CP ./gthread/*.la .
    $CP ./gobject/*.la .
    $CP ./gmodule/*.la .

    $MKDIR $INSTALL_DIR
    $CP -r * $INSTALL_DIR
```

Also, the above would break if $INSTALL_DIR had spaces in it. 

8. There's no really good test that make install actually worked.

[[I realized you probably made that spkg-install by just copying
something *I* did a long time ago, which was probably a mess.  I'm just
pointing out all the problems in it for the record.]]

9. OK, so I deleted everything that makes me nervous above and
came up with:

```/bin/sh
###########################################
## GLIB
###########################################

cd src
./configure --prefix="$SAGE_LOCAL" PREFIX="$SAGE_LOCAL" CC="$CC" CXX="$CXX"    
if [ $? -ne 0 ]; then
    echo "Configuration of glib failed."
    exit 1
fi
echo "Building and installing $TARGET"
$MAKE    
if [ $? -ne 0 ]; then
    echo "Error building glib."
    exit 1
fi
$MAKE install
if [ $? -ne 0 ]; then
    echo "Error installing glib."
    exit 1
fi
```

I made a new spkg like this and put it here:

http://sage.math.washington.edu/home/was/tmp/glib-2.14.0.p0.spkg

10. For the record, half of glib-2.14.0.spkg is the src/docs subdirectory.  This can probably go for the spkg.  

11. Build testing:

On OS X 10.5.1 intel *and* OS X 10.4 ppc:

```
...
checking for special C compiler options needed for large files... no
checking for _FILE_OFFSET_BITS value needed for large files... no
checking for _LARGE_FILES value needed for large files... no
checking for pkg-config... no
configure: error: *** pkg-config not found. See http://www.freedesktop.org/software/pkgconfig/
Configuration of glib failed.

real	0m8.123s
user	0m1.253s
sys	0m1.581s
sage: An error occurred while installing glib-2.14.0.p0
```


On Linux (sage.math):

```
checking for _LARGE_FILES value needed for large files... no
checking for pkg-config... no
configure: error: *** pkg-config not found. See http://www.freedesktop.org/software/pkgconfig/
Configuration of glib failed.

real    0m3.598s
user    0m0.824s
sys     0m1.120s
sage: An error occurred while installing glib-2.14.0.p0
```


OK, so I do:

```
was`@`sage:~/build/sage-2.10.3.alpha0$ sudo apt-get install pkg-config
```


The build completes successfuly on sage.math in 2m8.136s real time, which isn't bad. 
(This is with my simplified spkg-install.)  After doing that there are files such as `SAGE_ROOT/local/lib/libglib-2.0.so`, so all that explicit copying you were doing in spkg-install wasn't necessary. 

12. Thus glib depends on pkg-config.  I looked for a few minutes but couldn't find much about pkg-config.  What is it?  License?  Size?  Dependencies?  Sage would also have to include it if it includes glib. 

I'll need a pkg-config spkg in order to test further on OS X...


---

Comment by gfurnish created at 2008-03-01 07:23:19

http://sage.math.washington.edu/home/gfurnish/spkg/pkgconfig-0.18.spkg is the gpl pkg-config spkg.


---

Comment by was created at 2008-03-01 07:28:05

gfurnish posted an spkg for pkg-config here:

   http://sage.math.washington.edu/home/gfurnish/spkg/

It works. 

Unfortunately, that's not enough.   Now  on OSX we get libintl.h missing:

```
checking for LC_MESSAGES... yes
checking libintl.h usability... no
checking libintl.h presence... no
checking for libintl.h... no
configure: error:
*** You must have either have gettext support in your C library, or use the
*** GNU gettext library. (http://www.gnu.org/software/gettext/gettext.html

Configuration of glib failed.

real	0m8.201s
```



---

Comment by gfurnish created at 2008-03-01 18:41:42

New glib spkg for mac os.  It probably won't fully work, but it will get farther. http://sage.math.washington.edu/home/gfurnish/spkg/glib-2.14.0.p2.spkg


---

Comment by was created at 2008-03-01 18:59:23

You're right -- it doesn't work on OS X:

```
 gcc -DHAVE_CONFIG_H -I. -I. -I.. -I.. -DG_LOG_DOMAIN=\"GLib\" -DG_DISABLE_CAST_CHECKS -DG_DISABLE_DEPRECATED -DGLIB_COMPILATION -D_REENTRANT -g -O2 -Wall -MT gregex.lo -MD -MP -MF .deps/gregex.Tpo -c gregex.c  -fno-common -DPIC -o .libs/gregex.o
In file included from gregex.c:27:
../glib/gi18n.h:23:21: error: libintl.h: No such file or directory
gregex.c: In function 'match_error':
gregex.c:126: warning: implicit declaration of function 'gettext'
gregex.c:126: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:174: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c: In function 'g_match_info_next':
gregex.c:319: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c: In function 'g_regex_new':
gregex.c:884: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:893: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:936: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:958: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c: In function 'g_regex_match_all_full':
gregex.c:1354: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c: In function 'expand_escape':
gregex.c:1782: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1798: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1838: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1847: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1854: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1865: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1883: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1945: warning: incompatible implicit declaration of built-in function 'gettext'
gregex.c:1959: warning: incompatible implicit declaration of built-in function 'gettext'
make[4]: *** [gregex.lo] Error 1
make[3]: *** [all-recursive] Error 1
make[2]: *** [all] Error 2
make[1]: *** [all-recursive] Error 1
make: *** [all] Error 2
Error building glib.

real	1m9.648s
```



---

Comment by gfurnish created at 2008-03-01 23:50:06

New spkgs:
http://sage.math.washington.edu/home/gfurnish/spkg/pcre-7.6.spkg
http://sage.math.washington.edu/home/gfurnish/spkg/glib-2.14.5.spkg


---

Comment by was created at 2008-03-02 00:24:03

ISSUES:

1. One must also install

   http://sage.math.washington.edu/home/gfurnish/spkg/gettext-0.16.spkg

This is 5.8MB and take 6 minutes to compile on my 2.6Ghz laptop.  And it succeeds!

2. But, glib still fails to compile:

```
checking for LC_MESSAGES... yes
checking libintl.h usability... no
checking libintl.h presence... no
checking for libintl.h... no
configure: error:
*** You must have either have gettext support in your C library, or use the
*** GNU gettext library. (http://www.gnu.org/software/gettext/gettext.html

Configuration of glib failed.

real	0m5.354s
user	0m1.573s
sys	0m2.044s
```



---

Comment by gfurnish created at 2008-03-03 02:35:17

The new plan is to pull relevant source out of glib and roll our own lib to avoid problems with unnecessary dependencies and spkgs.


---

Comment by gfurnish created at 2008-03-09 05:39:39

Creating a glib spkg is too expensive in terms of dependencies for algorithms that are not useful.  Therefore we will integrate the c files for those algorithms that are useful and ignore the ones that are not. See #2436


---

Comment by gfurnish created at 2008-03-09 05:39:39

Resolution: invalid
