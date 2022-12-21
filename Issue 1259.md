# Issue 1259: readline miscompiles on OSX 10.5.[1]

Issue created by migration from Trac.

Original creator: mabshoff

Original creation time: 2007-11-25 04:34:31

Assignee: mabshoff

Justin Walker reports:

```
The only problem with the build is this, with readline:

Configured with: /var/tmp/gcc/gcc-5465~16/src/configure --disable-
checking -enable-werror --prefix=/usr --mandir=/share/man --enable-
languages=c,objc,c++,obj-c++ --program-transform-name=/^[cg][^.-]*$/s/
$/-4.0/ --with-gxx-include-dir=/include/c++/4.0.0 --with-slibdir=/usr/
lib --build=i686-apple-darwin9 --with-arch=apple --with-tune=generic  
--host=i686-apple-darwin9 --target=i686-apple-darwin9
Thread model: posix
gcc version 4.0.1 (Apple Inc. build 5465)
i686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  
with -dynamiclib
i686-apple-darwin9-gcc-4.0.1: -compatibility_version only allowed  
with -dynamiclib
make[3]: *** [libreadline.5.2.dylib] Error 1
make[3]: *** Waiting for unfinished jobs....
make[3]: *** [libhistory.5.2.dylib] Error 1
make[2]: [install-shared] Error 2 (ignored)

FWIW, this same error crops up in a standalone build of readline, but  
it kills the build.  Sage seems to be unconcerned.
```



---

Comment by mabshoff created at 2007-11-25 04:34:41

Changing status from new to assigned.


---

Comment by mabshoff created at 2008-01-17 01:01:19

The same issue applies to termcap. On 10.5 we end up with only static libraries.


---

Comment by mabshoff created at 2008-01-28 05:14:48

Craig Citro says:

```
Since we're mentioning it, there's a known issue with the readline
build on certain platforms, which you can spot by looking at your
install.log at the section where readline gets installed. I don't know
why these would be related, and Michael Abshoff is suspicious -- which
probably means I'm wrong :) -- but if I were motivated to look, I'd
probably start there. This is trac ticket #1259. It's easy to get the
build problems to go away, but I'm not sure if it's the "right" way to
do so -- if you untar the readline package, go into src/support, and
look at shobj-conf. If you edit line 145 to say:

darwin[89]*)

and line 174 to start with

     darwin[789]*)

then it builds with no errors. However, if you look at what you're
doing, you're basically just telling the builder to use the same
options for 10.5 (which is what I assume Darwin9 is?) as it uses on
Darwin 8. I have absolutely no idea whether or not that's a wise idea.

Once one does this, you could try rebuilding all of Sage with the new
readline package, and seeing if you get the same troubles.
```


Cheers,

Michael


---

Comment by craigcitro created at 2008-02-24 01:09:07

Resolution: duplicate


---

Comment by craigcitro created at 2008-02-24 01:09:07

This is going to be fixed with #2282.
