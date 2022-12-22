# Issue 6550: We need to be able to save itermediate files - particulary for ATLAS

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-07-17 18:01:54

Assignee: tbd

CC:  leif mpatel

When ATLAS builds, it goes through a lengthly tuning process (taking 8.5 hours on 't2'). That could be shorted, by saving architectural defaults, but that needs the temporary files. 
 
Setting 


```
DELETE_TMP=0
```


on line 76 of $SAGE_ROOT/local/bin/sage-spkg causes a syntax error. 

We need way to do this. Preferably from an environment variable. 

In theory, if the line is changed to:


```
DELETE_TMP="${REMOVE_TMP:-1}"
```


then setting the environment variable REMOVE_TMP to 0 would make DELETE_TMP change from 1 to 0. Otherwise, it would default to 1.

But all I get are syntax errors. 

To me, this is an important enhancement if we want to reduce the build time of Sage on 't2'

Dave 


---

Comment by wjp created at 2009-07-17 18:30:52

Which syntax errors do you get exactly?

Setting DELETE_TMP=0 and then running `./sage -f zlib-1.2.3.p4` works fine for me here (linux, bash 3.2.39) and leaves the build directory intact.

-Willem Jan


---

Comment by drkirkby created at 2009-07-17 23:03:41

I'll run this later today (its one minute past midnight here), but I understood that if DELETE_TMP was changed on line 76, to 0, then all intermediate files would be retained. Changing that line 76 causes a syntax error report. I'll run it later and shoe you the output. 

Dave


---

Comment by drkirkby created at 2009-07-17 23:04:03

Changing assignee from tbd to drkirkby.


---

Comment by drkirkby created at 2009-07-17 23:04:03

Changing component from algebra to build.


---

Comment by drkirkby created at 2009-07-19 15:09:50

It seems if I only change DELETE_TMP to 0, then it does work. But any attempt I have made to get the code to behave in the way an environment variable is set, just fails miserably. This is despite the fact that a bit of code that changes the value of DELETE_TMP outwide of Sage works fine. 

Also, I note from that script that the -m option is supposed to be used to save temp files, which is what william told me. But it only works for one file. 

I wrote a small script (see below) which sets the variable DELETE_TMP to 0 or 1 in exactly the same way as in the script inside $SAGE_ROOT/local/bin/sage-spkg However, the setting is done depending on the value of an environment variable.  (I've tried simpler version too, but whatever I try, I can't seem to get something that allows an environment variable to decide if temporary files are kept or not. 

```
kirkby`@`t2:[~] $ ./testprog
TMPVAR=1
DELETE_TMP=1
DELETE_TMP is one
kirkby`@`t2:[~] $ export DELETE_TMP_FILES=0
kirkby`@`t2:[~] $ ./testprog
TMPVAR=0
DELETE_TMP=0
DELETE_TMP is zero
kirkby`@`t2:[~] $ export DELETE_TMP_FILES=1
kirkby`@`t2:[~] $ ./testprog
TMPVAR=1
DELETE_TMP=1
DELETE_TMP is one
kirkby`@`t2:[~] $ unset DELETE_TMP_FILES
kirkby`@`t2:[~] $ ./testprog
TMPVAR=1
DELETE_TMP=1
DELETE_TMP is one
```

Here's the code which generates this. 


```/bin/sh
TMPVAR="${DELETE_TMP_FILES-1}"
echo "TMPVAR=$TMPVAR"

if [ "x$TMPVAR" = "x0" ] ; then
   DELETE_TMP=0
elif [ "x$TMPVAR" = "x1" ] ; then
   DELETE_TMP=1
else
   echo "Error in enviroment variable DELETE_TMP_FILES."
   echo "The enviroment variable DELETE_TMP_FILES should be set to 0 to keep the temporary files, or 1 to delete them. By default they are deleted"
   exit
fi
echo "DELETE_TMP=$DELETE_TMP"

if [ $DELETE_TMP -eq  1 ] ; then
  echo "DELETE_TMP is one"
fi


if [ $DELETE_TMP -eq 0  ] ; then
  echo "DELETE_TMP is zero"
fi

```



---

Comment by drkirkby created at 2010-08-03 02:44:01

I'm wondering if either of you guys have a clue how to solve this. It seems a trivial problem, but I just can't get it to work. 

I can see it is going to be needed soon for debugging on Solaris, as deleting all the source files makes debugging much harder, as the debugger does not have the source code.


---

Comment by mpatel created at 2010-08-03 04:19:16

What happens with

```diff
diff --git a/sage-spkg b/sage-spkg
--- a/sage-spkg
+++ b/sage-spkg
`@``@` -84,6 +84,9 `@``@` if [ $1 = '-s' -o $1 = '-m' ]; then
     DELETE_TMP=0
     shift
 fi
+if [ "$SAGE_KEEP_SPKG_BUILD" = "yes" ]; then
+    DELETE_TMP=0
+fi
 
 INSTALLED="$SAGE_PACKAGES/installed/"
 PKG_NAME=`echo "$1" | sed -e "s/\.spkg$//"`
```

?


---

Comment by mpatel created at 2010-08-06 22:37:39

There's a patch at #4949 that subsumes this and uses a better name than `SAGE_KEEP_SPKG_BUILD`.


---

Comment by jdemeyer created at 2013-05-24 12:22:21

Fixed by various patches to `sage-spkg`.


---

Comment by jdemeyer created at 2013-05-24 12:22:21

Resolution: worksforme
