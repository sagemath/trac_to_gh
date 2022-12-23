# Issue 8303: Sage cannot work with files with spaces in their names

Issue created by migration from https://trac.sagemath.org/ticket/8303

Original creator: ddrake

Original creation time: 2010-02-19 02:32:06

Assignee: was

Keywords: spaces filenames

Scripts with spaces in their names defeat Sage:

```
$ sage "my script.sage" 
/opt/sage/local/bin/sage-sage: line 147: [: too many arguments
/opt/sage/local/bin/sage-sage: line 150: [: too many arguments
/opt/sage/local/bin/sage-sage: line 200: [: too many arguments
[...]
/opt/sage/local/bin/sage-sage: line 892: [: too many arguments
/opt/sage/local/bin/sage-preparse: File my is missing
/opt/sage/local/bin/sage-preparse: File script.sage is missing
python: can't open file 'my': [Errno 2] No such file or directory
```

Ticket #4354 claimed to fix this, but it's still broken on 4.3.2.


---

Comment by ddrake created at 2010-02-19 04:35:49

Changing assignee from was to ddrake.


---

Comment by ddrake created at 2010-02-19 04:35:49

I have the beginnings of patch, but I already know some of the problems going on here.

  * First, if $1 contains spaces, then whenever you do `if [ $1 = "blah" ]` the shell expands $1 into multiple words and the test gets confused. The script `sage-sage` is riddled with such things, which is the source of the "too many arguments" business above.

  * Second, the sage-sage script, if given non-option arguments (i.e., no -python, -preparse, etc) punts to the Python script sage-run. Inside sage-run, we have things like

```
 os.system('"$SAGE_LOCAL/bin/sage-python" %s.py %s'%(file[:-5], options))
```

where "options" contains all the arguments you originally passed to Sage. Unfortunately, when you do `os.system`, it seems to split words on all whitespace, which means at this point, we lose all information about command-line arguments with spaces in them.

It looks like we should be using subprocess.Popen (http://docs.python.org/library/subprocess.html#subprocess.Popen), which accepts a _list_ of arguments and hence can deal with spaces properly.


---

Comment by ddrake created at 2010-02-21 07:52:17

apply to sage_scripts spkg


---

Attachment

Patch up. Apply to sage_scripts spkg, or equivalently, to the repo in SAGE_ROOT/local/bin.

To test, try making a file with spaces in its name, and passing arguments with spaces in them. If the file is "script with spaces.sage" and it contains:

```
import sys
print integrate(x*cos(x)*sin(x), x)
print sys.argv
sys.exit(int(5))
```

then something like this should work properly:

```
$ sage "script with spaces.sage" "foo bar" arg2
-1/4*x*cos(2*x) + 1/8*sin(2*x)
['script with spaces.py', 'foo bar', 'arg2']
$ echo $?
5
```

I'd like to have the return code tested to make sure we don't get a regression on #2861.

Please test and review!


---

Comment by ddrake created at 2010-02-21 08:05:42

Changing status from new to needs_review.


---

Comment by ddrake created at 2010-02-21 08:18:43

Also, there is a script called sage-run2 in SAGE_ROOT/local/bin, which seems to me like abandoned cruft. There are no references to that file outside of the Mercurial repo store. It appears to be a script that allows you to sequentially run Sage on several files. I think that functionality would be easy to add to sage-run. Should we remove sage-run2 and put the functionality into sage-run?


---

Comment by ddrake created at 2010-02-23 13:10:19

Another point for testing: #4354 later got reverted (see changeset 1119:553a52746e3c in sage_scripts) because it interfered with -sdist; I tested this patch and it appears to cooperate with -sdist.


---

Comment by was created at 2010-04-28 03:41:08

Changing status from needs_review to positive_review.


---

Comment by was created at 2010-04-29 05:17:07

Resolution: fixed
