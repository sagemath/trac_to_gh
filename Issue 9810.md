# Issue 9810: sage exits with 0, even if it is unable to install a package.

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2010-08-26 21:32:46

Assignee: GeorgSWeber

CC:  leif mpatel jhpalmieri

I wanted to do some testing of Sage in a loop and would check the return code to see if what I used worked or not. But this is impossible, as Sage appears to exit with 0, even if it should not have. In the example below, I try to install a non-existent package using Sage. The return code in a case like this should be non-zero, but it is not. 


```
drkirkby`@`hawk:~/sage-4.5.2$ ./sage -f some-non-existant-package
Force installing some-non-existant-package
Calling sage-spkg on some-non-existant-package
Warning: Attempted to overwrite SAGE_ROOT environment variable
Building Sage on Solaris in 64-bit mode
Creating SAGE_LOCAL/lib/sage-64.txt since it does not exist
Detected SAGE64 flag
Building Sage on Solaris in 64-bit mode
some-non-existant-package
Machine:
SunOS hawk 5.11 snv_134 i86pc i386 i86pc
Deleting directories from past builds of previous/current versions of some-non-existant-package
/export/home/drkirkby/sage-4.5.2/local/bin/sage-spkg: file some-non-existant-package does not exist
Attempting to download it.
http://www.sagemath.org//packages/optional/some-non-existant-package.spkg --> some-non-existant-package.spkg
[ ]
http://www.sagemath.org//packages/standard/some-non-existant-package.spkg --> some-non-existant-package.spkg
[ ]
http://www.sagemath.org//packages/experimental/some-non-existant-package.spkg --> some-non-existant-package.spkg
[ ]
http://www.sagemath.org//packages/archive/some-non-existant-package.spkg --> some-non-existant-package.spkg
[ ]
**********************************************************************
* Unable to download some-non-existant-package
* Please see http://www.sagemath.org//packages for a list of valid
* packages or check the package name.
**********************************************************************
sage: Failed to download package some-non-existant-package from http://www.sagemath.org/
drkirkby`@`hawk:~/sage-4.5.2$ $?
bash: 0: command not found
drkirkby`@`hawk:~/sage-4.5.2$ 
```


In contrast, if I try this with a well written command like `ls`


```
drkirkby`@`hawk:~/sage-4.5.2$ ls some-non-existant-package
some-non-existant-package: No such file or directory
drkirkby`@`hawk:~/sage-4.5.2$ $?
bash: 2: command not found
```


the exit code is non-zero - in this case 2. 

Also on a similar theme is #9799, showing that `make` can exit with the wrong code too.


---

Comment by leif created at 2010-08-26 23:35:07

Replying to [ticket:9811 drkirkby]:
> 

```
drkirkby`@`hawk:~/sage-4.5.2$ ./sage -f some-non-existant-package
...
drkirkby`@`hawk:~/sage-4.5.2$ $?
bash: 0: command not found
drkirkby`@`hawk:~/sage-4.5.2$ 
```



> In contrast, if I try this with a well written command like `ls`
> [...] the exit code is non-zero - in this case 2.

Well, you did `sage -f ...` ...

A well written command like `rm` exits with a zero status if you use `-f`:

```sh
leif`@`quadriga:~/Sage/spkgs/mpir-2.1.1$ rm -f non-existent-package ; echo $?
0
```


I wonder what Sage returns if you do `sage -i ...` instead... ;-)

Btw, `sage-spkg` has lots of other flaws. I'm considering writing (and using) my own version, since I doubt the bunch of changes I aim at would get merged soon... (Same for the top-level Makefile, which by the way was named `makefile`, I guess by some DOS programmer.)

Hopefully not too many people read our tickets... :D


---

Comment by drkirkby created at 2010-08-26 23:56:46

Replying to [comment:1 leif]:


> Well, you did `sage -f ...` ...
> I wonder what Sage returns if you do `sage -i ...` instead... ;-)

The Sage. It still exits with an exit code of zero. 
 
> Btw, `sage-spkg` has lots of other flaws. I'm considering writing (and using) my own version, since I doubt the bunch of changes I aim at would get merged soon... (Same for the top-level Makefile, which by the way was named `makefile`, I guess by some DOS programmer.)
> 
> Hopefully not too many people read our tickets... :D
  
More, should I think. 

Dave


---

Comment by leif created at 2010-10-19 11:34:09

From `sage-sage`:

```sh
...
install() {
   cd "$SAGE_ROOT/spkg"
   if [ $# -lt 2 ]; then
       sage-spkg
       exit $?
   fi
   OPT="$1"
   shift
   if [ "$1" = '-m' -o "$1" = '-s' ]; then
       OPT=$OPT" "$1
       shift
   fi
   SAGE_LOGS="$SAGE_ROOT/spkg/logs"
   if [ ! -d "$SAGE_LOGS" ]; then
       mkdir -p "$SAGE_LOGS"
   fi
   for PKG in "$`@`"
   do
       echo "Calling sage-spkg on $PKG"
       PKG_NAME=`echo "$PKG" | sed -e "s/\.spkg$//"`
       PKG_NAME=`basename "$PKG_NAME"`
       case $PKG in
       /*)
           sage-spkg $OPT "$PKG" 2>&1 | (trap "" SIGINT; tee -a ../install.log "$SAGE_LOGS/$PKG_NAME".log)
       ;;
       *)
           sage-spkg $OPT "$CUR/$PKG" 2>&1 | (trap "" SIGINT; tee -a ../install.log "$SAGE_LOGS/$PKG_NAME".log)
       ;;
       esac

       if [ $? -ne 0 ]; then
          exit 1
       fi
       shift
   done
   exit $?
}
...
if [ "$1" = '-i' ]; then
   shift
   echo "Installing $`@`"
   install " " "$`@`"
fi

if [ "$1" = '-f' ]; then
   shift
   echo "Force installing $`@`"
   install -f "$`@`"
fi
...
```


So once again, we get the exit status of `tee` rather than that of `sage-spkg`.


---

Comment by leif created at 2010-10-23 13:40:33

Using `pipestatus` there, too (i.e. in `sage-sage`) most probably requires #10157.


---

Comment by leif created at 2010-10-23 13:46:06

I intend to move the logging (`tee` / `pipestatus`) to `sage-spkg` anyway, s.t. we only pass the name of the logfile(s), and some option(s) on how much to log [where]; cf. also #10040 and #9799.


---

Comment by leif created at 2011-10-13 14:25:42

Changing status from new to needs_review.


---

Comment by leif created at 2011-10-13 14:25:42

Changing component from build to scripts.


---

Comment by leif created at 2011-10-13 14:25:42

Changing keywords from "" to "sage-sage return code status pipestatus tee".


---

Comment by leif created at 2011-10-13 14:25:42

Attached patch fixes the exit code (by using `pipestatus`) and a few minor things in that area of `sage-sage`.

(I haven't changed more since there are other tickets already touching `sage-sage` especially there, which may need _slight_ rebasing on the patch here though.)


---

Comment by leif created at 2011-10-13 14:30:57

CC'ing a potential reviewer... :P


---

Comment by leif created at 2011-10-13 14:34:57

SCRIPTS repo. Based on Sage 4.7.2.alpha4.


---

Attachment

Fixed a typo in a comment.

Sorry, patch (diff) doesn't look very nice, as I've changed the indentation (and replaced spaces by tabs).


---

Comment by jhpalmieri created at 2011-10-14 22:20:55

Looks okay to me.


---

Comment by jhpalmieri created at 2011-10-14 22:20:55

Changing status from needs_review to positive_review.


---

Comment by jdemeyer created at 2011-10-17 07:59:23

Resolution: fixed
