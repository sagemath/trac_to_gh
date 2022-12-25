# Issue 6550: We need to be able to save itermediate files - particulary for ATLAS

archive/issues_006550.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @nexttime @qed777\n\nWhen ATLAS builds, it goes through a lengthly tuning process (taking 8.5 hours on 't2'). That could be shorted, by saving architectural defaults, but that needs the temporary files. \n \nSetting \n\n```\nDELETE_TMP=0\n```\n\non line 76 of $SAGE_ROOT/local/bin/sage-spkg causes a syntax error. \n\nWe need way to do this. Preferably from an environment variable. \n\nIn theory, if the line is changed to:\n\n```\nDELETE_TMP=\"${REMOVE_TMP:-1}\"\n```\n\nthen setting the environment variable REMOVE_TMP to 0 would make DELETE_TMP change from 1 to 0. Otherwise, it would default to 1.\n\nBut all I get are syntax errors. \n\nTo me, this is an important enhancement if we want to reduce the build time of Sage on 't2'\n\nDave \n\nIssue created by migration from https://trac.sagemath.org/ticket/6550\n\n",
    "created_at": "2009-07-17T18:01:54Z",
    "labels": [
        "component: algebra"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-duplicate/invalid/wontfix",
    "title": "We need to be able to save itermediate files - particulary for ATLAS",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/6550",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```
Assignee: tbd

CC:  @nexttime @qed777

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

Issue created by migration from https://trac.sagemath.org/ticket/6550





---

archive/issue_comments_053305.json:
```json
{
    "body": "Which syntax errors do you get exactly?\n\nSetting DELETE_TMP=0 and then running `./sage -f zlib-1.2.3.p4` works fine for me here (linux, bash 3.2.39) and leaves the build directory intact.\n\n-Willem Jan",
    "created_at": "2009-07-17T18:30:52Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53305",
    "user": "https://github.com/wjp"
}
```

Which syntax errors do you get exactly?

Setting DELETE_TMP=0 and then running `./sage -f zlib-1.2.3.p4` works fine for me here (linux, bash 3.2.39) and leaves the build directory intact.

-Willem Jan



---

archive/issue_comments_053306.json:
```json
{
    "body": "I'll run this later today (its one minute past midnight here), but I understood that if DELETE_TMP was changed on line 76, to 0, then all intermediate files would be retained. Changing that line 76 causes a syntax error report. I'll run it later and shoe you the output. \n\nDave",
    "created_at": "2009-07-17T23:03:41Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53306",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'll run this later today (its one minute past midnight here), but I understood that if DELETE_TMP was changed on line 76, to 0, then all intermediate files would be retained. Changing that line 76 causes a syntax error report. I'll run it later and shoe you the output. 

Dave



---

archive/issue_comments_053307.json:
```json
{
    "body": "Changing assignee from tbd to drkirkby.",
    "created_at": "2009-07-17T23:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53307",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing assignee from tbd to drkirkby.



---

archive/issue_comments_053308.json:
```json
{
    "body": "Changing component from algebra to build.",
    "created_at": "2009-07-17T23:04:03Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53308",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

Changing component from algebra to build.



---

archive/issue_comments_053309.json:
```json
{
    "body": "It seems if I only change DELETE_TMP to 0, then it does work. But any attempt I have made to get the code to behave in the way an environment variable is set, just fails miserably. This is despite the fact that a bit of code that changes the value of DELETE_TMP outwide of Sage works fine. \n\nAlso, I note from that script that the -m option is supposed to be used to save temp files, which is what william told me. But it only works for one file. \n\nI wrote a small script (see below) which sets the variable DELETE_TMP to 0 or 1 in exactly the same way as in the script inside $SAGE_ROOT/local/bin/sage-spkg However, the setting is done depending on the value of an environment variable.  (I've tried simpler version too, but whatever I try, I can't seem to get something that allows an environment variable to decide if temporary files are kept or not. \n\n```\nkirkby@t2:[~] $ ./testprog\nTMPVAR=1\nDELETE_TMP=1\nDELETE_TMP is one\nkirkby@t2:[~] $ export DELETE_TMP_FILES=0\nkirkby@t2:[~] $ ./testprog\nTMPVAR=0\nDELETE_TMP=0\nDELETE_TMP is zero\nkirkby@t2:[~] $ export DELETE_TMP_FILES=1\nkirkby@t2:[~] $ ./testprog\nTMPVAR=1\nDELETE_TMP=1\nDELETE_TMP is one\nkirkby@t2:[~] $ unset DELETE_TMP_FILES\nkirkby@t2:[~] $ ./testprog\nTMPVAR=1\nDELETE_TMP=1\nDELETE_TMP is one\n```\nHere's the code which generates this. \n\n```/bin/sh\nTMPVAR=\"${DELETE_TMP_FILES-1}\"\necho \"TMPVAR=$TMPVAR\"\n\nif [ \"x$TMPVAR\" = \"x0\" ] ; then\n   DELETE_TMP=0\nelif [ \"x$TMPVAR\" = \"x1\" ] ; then\n   DELETE_TMP=1\nelse\n   echo \"Error in enviroment variable DELETE_TMP_FILES.\"\n   echo \"The enviroment variable DELETE_TMP_FILES should be set to 0 to keep the temporary files, or 1 to delete them. By default they are deleted\"\n   exit\nfi\necho \"DELETE_TMP=$DELETE_TMP\"\n\nif [ $DELETE_TMP -eq  1 ] ; then\n  echo \"DELETE_TMP is one\"\nfi\n\n\nif [ $DELETE_TMP -eq 0  ] ; then\n  echo \"DELETE_TMP is zero\"\nfi\n\n```",
    "created_at": "2009-07-19T15:09:50Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53309",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

It seems if I only change DELETE_TMP to 0, then it does work. But any attempt I have made to get the code to behave in the way an environment variable is set, just fails miserably. This is despite the fact that a bit of code that changes the value of DELETE_TMP outwide of Sage works fine. 

Also, I note from that script that the -m option is supposed to be used to save temp files, which is what william told me. But it only works for one file. 

I wrote a small script (see below) which sets the variable DELETE_TMP to 0 or 1 in exactly the same way as in the script inside $SAGE_ROOT/local/bin/sage-spkg However, the setting is done depending on the value of an environment variable.  (I've tried simpler version too, but whatever I try, I can't seem to get something that allows an environment variable to decide if temporary files are kept or not. 

```
kirkby@t2:[~] $ ./testprog
TMPVAR=1
DELETE_TMP=1
DELETE_TMP is one
kirkby@t2:[~] $ export DELETE_TMP_FILES=0
kirkby@t2:[~] $ ./testprog
TMPVAR=0
DELETE_TMP=0
DELETE_TMP is zero
kirkby@t2:[~] $ export DELETE_TMP_FILES=1
kirkby@t2:[~] $ ./testprog
TMPVAR=1
DELETE_TMP=1
DELETE_TMP is one
kirkby@t2:[~] $ unset DELETE_TMP_FILES
kirkby@t2:[~] $ ./testprog
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

archive/issue_comments_053310.json:
```json
{
    "body": "I'm wondering if either of you guys have a clue how to solve this. It seems a trivial problem, but I just can't get it to work. \n\nI can see it is going to be needed soon for debugging on Solaris, as deleting all the source files makes debugging much harder, as the debugger does not have the source code.",
    "created_at": "2010-08-03T02:44:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53310",
    "user": "https://trac.sagemath.org/admin/accounts/users/drkirkby"
}
```

I'm wondering if either of you guys have a clue how to solve this. It seems a trivial problem, but I just can't get it to work. 

I can see it is going to be needed soon for debugging on Solaris, as deleting all the source files makes debugging much harder, as the debugger does not have the source code.



---

archive/issue_comments_053311.json:
```json
{
    "body": "What happens with\n\n```diff\ndiff --git a/sage-spkg b/sage-spkg\n--- a/sage-spkg\n+++ b/sage-spkg\n@@ -84,6 +84,9 @@ if [ $1 = '-s' -o $1 = '-m' ]; then\n     DELETE_TMP=0\n     shift\n fi\n+if [ \"$SAGE_KEEP_SPKG_BUILD\" = \"yes\" ]; then\n+    DELETE_TMP=0\n+fi\n \n INSTALLED=\"$SAGE_PACKAGES/installed/\"\n PKG_NAME=`echo \"$1\" | sed -e \"s/\\.spkg$//\"`\n```\n?",
    "created_at": "2010-08-03T04:19:16Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53311",
    "user": "https://github.com/qed777"
}
```

What happens with

```diff
diff --git a/sage-spkg b/sage-spkg
--- a/sage-spkg
+++ b/sage-spkg
@@ -84,6 +84,9 @@ if [ $1 = '-s' -o $1 = '-m' ]; then
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

archive/issue_comments_053312.json:
```json
{
    "body": "There's a patch at #4949 that subsumes this and uses a better name than `SAGE_KEEP_SPKG_BUILD`.",
    "created_at": "2010-08-06T22:37:39Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53312",
    "user": "https://github.com/qed777"
}
```

There's a patch at #4949 that subsumes this and uses a better name than `SAGE_KEEP_SPKG_BUILD`.



---

archive/issue_comments_053313.json:
```json
{
    "body": "Fixed by various patches to `sage-spkg`.",
    "created_at": "2013-05-24T12:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53313",
    "user": "https://github.com/jdemeyer"
}
```

Fixed by various patches to `sage-spkg`.



---

archive/issue_comments_053314.json:
```json
{
    "body": "Resolution: worksforme",
    "created_at": "2013-05-24T12:22:21Z",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/6550#issuecomment-53314",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: worksforme



---

archive/issue_events_015448.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-24T12:22:21Z",
    "event": "milestoned",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "milestone": "sage-duplicate/invalid/wontfix",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6550#event-15448"
}
```



---

archive/issue_events_015449.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2013-05-24T12:22:21Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/6550",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/6550#event-15449"
}
```
