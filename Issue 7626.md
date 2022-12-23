# Issue 7626: delete PBUILD code in local/bin/sage-sage script

Issue created by migration from https://trac.sagemath.org/ticket/7626

Original creator: was

Original creation time: 2009-12-08 19:22:39

Assignee: GeorgSWeber

I noticed code like this in the sage-sage script:

```
 		    if [ "$SAGE_PBUILD" == "yes" ]; then 
 		        echo 'Pbuild is currently broken -- defaulting to serial build.' 
 		        # if [ "$@" ]; then 
 		        #     ln -snf "$SAGE_ROOT"/devel/sage-"$@" "$SAGE_ROOT"/devel/sage 
 		        # fi 
 		        # time python "$SAGE_ROOT"/devel/sage/build.py -b 
 		        sage-build "$@" 
```


Not only is SAGE_PBUILD "broken", it has long since been replaced by something better.  So we should just delete this stuff from sage-sage.


---

Comment by jdemeyer created at 2012-03-06 09:20:55

This is already deleted some time ago.


---

Comment by jdemeyer created at 2012-03-06 09:20:55

Resolution: worksforme
