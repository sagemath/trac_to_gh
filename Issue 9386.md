# Issue 9386: sage-native-execute leaves traces of sage

Issue created by migration from Trac.

Original creator: nbruin

Original creation time: 2010-06-29 23:05:43

Assignee: tbd

CC:  iandrus leif vbraun

The following shows that `sage-native-execute` creates a very hostile environment for running python:

```
$ sage -sh

Starting subshell with Sage environment variables set.
Be sure to exit when you are done and do not do anything
with other copies of Sage!

Bypassing shell configuration files ...

> sage-native-execute sh

sh-3.2$ python
python: error while loading shared libraries: libpython2.6.so.1.0:
cannot open shared object file: No such file or directory
sh-3.2$ which python
/usr/local/sage/4.4.4/local/bin/python
sh-3.2$ /usr/bin/python
'import site' failed; use -v for traceback
Python 2.4.3 (#1, Jun 11 2009, 14:09:37)
[GCC 4.1.2 20080704 (Red Hat 4.1.2-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.

sh-3.2$ echo $PYTHONPATH
:/usr/local/sage/4.4.4/local/lib/python
sh-3.2$ echo $PYTHONHOME
/usr/local/sage/4.4.4/local
sh-3.2$ unset PYTHONPATH
sh-3.2$ unset PYTHONHOME
sh-3.2$ /usr/bin/python
Python 2.4.3 (#1, Jun 11 2009, 14:09:37)
[GCC 4.1.2 20080704 (Red Hat 4.1.2-44)] on linux2
Type "help", "copyright", "credits" or "license" for more information.
```

The problem is `python` refers to the sage python, because $PATH still has sage paths in it. This doesn't run because LD_LIBRARY_PATH does not point at sage library anymore

The system python `/usr/bin/python` doesn't run successfully either because PYTHONPATH and PYTHONHOME still point at sage locations.

This problem arose while trying to use the magma interface. My magma startup script uses python to resolve some paths, which didn't work anymore.

There are other traces left by sage-native-execute:


```
ECLDIR=/usr/local/sage/4.4.4/local/lib/ecl/
GP_DATA_DIR=/usr/local/sage/4.4.4/local/share/pari
GPDOCDIR=/usr/local/sage/4.4.4/local/share/pari/doc
GPHELP=/usr/local/sage/4.4.4/local/bin/gphelp
LD_LIBRARY_PATH=
LIBRARY_PATH=/usr/local/sage/4.4.4/local/lib/
PATH=/usr/local/sage/4.4.4:/usr/local/sage/4.4.4/local/bin:   #.....
PYTHONHOME=/usr/local/sage/4.4.4/local
PYTHONPATH=:/usr/local/sage/4.4.4/local/lib/python
SINGULAR_EXECUTABLE=/usr/local/sage/4.4.4/local/bin/Singular
SINGULARPATH=/usr/local/sage/4.4.4/local/share/singular
```


so I imagine local ecl, gp python, singular will all have problems.
I include LD_LIBRARY_PATH because that variable was originally undefined, not just empty. The variables PYTHONHOME and PYTHONPATH really need to be unset, not just emptied.


---

Comment by tmonteil created at 2015-02-08 17:31:53

New commits:


---

Comment by tmonteil created at 2015-02-08 17:31:53

Changing status from new to needs_review.


---

Comment by nbruin created at 2015-02-08 19:28:46

This goes a long way towards reconstructing the starting environment. The main thing I am worried about is that a lot of variables are "restored" by unsetting them, regardless of whether they had a previous value.That could break things.

That makes me wonder whether we should do something like the following at the start of sage:

```
SAGE_OLD_ENV=`env | base64`
```

and restore it by something like

```
{echo $SAGE_OLD_ENV | base64 > /tmp/temp_sage_env} ; . /tmp/temp_sage_env
```

This doesn't actually work, but I hope you get the idea. If we go this route we should probably make a python script "store_environment", and make `sage-native-execute` a python script that restores the environment. I'm not sure if there are some unexpected security concerns involved.

In fact, we should probably do this all on C-level with tiny programs, where we can use first the `extern char **environ` pointer to get the whole (pristine) environment, and later reconstruct it and use `execle` or similar to start the new process in the appropriately restored environment. The difficult part is finding an appropriate place to store the presage environment ...

I'd be fine with a more piecemeal solution as proposed here, because at least it will significantly improve the situation.


---

Comment by tmonteil created at 2015-02-08 20:06:01

I agree that once Sage exports a variable, we lose the information on whether it existed before (apart from `LD_LIBRARY_PATH` and `PATH` which have a hand-made specific workaround). This is already a problem with the `..._proxy` variables, or even `LC_ALL`. Instead of storing the whole environment on a central place, i was thinking of having a modified `export` function that applies to all Sage, that stores the previous value if it is not already stored (with a special flag to remember that the variable did no exist, which seems slightly different than being the empty string). So somehow, each export costs two exports, but it remains a local operation that passes the required info along subprocesses, so it is probably easier to maintain. Then, it suffices to copy-or-unset those values when `sage-native-execute` is called. I don't know which is best.


---

Comment by nbruin created at 2015-02-08 21:06:52

Replying to [comment:9 tmonteil]:
> Instead of storing the whole environment on a central place, i was thinking of having a modified `export` function that applies to all Sage, that stores the previous value if it is not already stored (with a special flag to remember that the variable did no exist, which seems slightly different than being the empty string)

*edit:* better to store the relevant variable names in a separate variable `SAGE_SAVED_ENVIRONMENT_VARIABLES`. Then you don't have to scan all of the environment, meaning that you only have to make your script robust against strings that the script is meant to see (environments can in principle contain arbitrary null-terminated strings) */edit*

The restoring bit could be easy:
 - scan the entire environment for variable names of the form `SAGE_OLD_<name>`. *edit:* rather, retrieve `<names>`s from `SAGE_SAVED_ENVIRONMENT_VARIABLES`. */edit* For each of those:
 - If the value of `SAGE_OLD_<name>` is of the form `+<value>` then set `<name>=<value>`
 - If the value is empty, unset `<name>`
 - If value is non-empty but does not start with +: error.
That's a simple loop you can execute in `sage-native-execute`.

The difficult part is ensuring all exports adhere to the standard imposed here. You could make a bash function that does this, but not all environment setting needs to happen by bash, and we might not have easy control over all environment setting instructions (chances are we do for all variables that matter, though. If we adjust sage-env, we're probably already good). An obvious advantage is that any non-cooperating environment clobbering will simply not be restored, which is not necessarily an error condition.

> it remains a local operation that passes the required info along subprocesses, so it is probably easier to maintain. Then, it suffices to copy-or-unset those values when `sage-native-execute` is called. I don't know which is best.

Agreed. Storing an environment in a temporary variable somewhere sounds awkward.


---

Comment by tmonteil created at 2015-02-08 21:56:35

On the Python side, i did the following short enumeration:


```
$ grep -R 'environ.*='
interfaces/qsieve.py~:    os.environ['TMPDIR'] = X
interfaces/qsieve.py:    os.environ['TMPDIR'] = X
interfaces/gp.py:os.environ["GPRC"] = os.path.join(SAGE_ETC, 'gprc.expect')
repl/notebook_ipython.py:            sage: os.environ['IPYTHONDIR'] = d
repl/notebook_ipython.py:            sage: os.environ['IPYTHONDIR'] = IPYTHONDIR
repl/notebook_ipython.py:            sage: os.environ['IPYTHONDIR'] = d
repl/notebook_ipython.py:            sage: os.environ['IPYTHONDIR'] = IPYTHONDIR
repl/attach.py:        sage: os.environ['SAGE_LOAD_ATTACH_PATH'] = '/veni/vidi:vici:'
repl/interpreter.py:            sage: os.environ['IPYTHONDIR'] = d
repl/interpreter.py:            sage: os.environ['IPYTHONDIR'] = IPYTHONDIR
env.py:        sage: os.environ['SAGE_FOO'] = 'foo'
Fichier binaire env.pyc concordant
doctest/forker.py:            sage: os.environ['SAGE_PEXPECT_LOG'] = "1"
doctest/forker.py:            sage: os.environ['SAGE_PEXPECT_LOG'] = "1"
geometry/polytope.py:    os.environ['PATH'] = '%s:'%path + os.environ['PATH']
dev/patch.py:                    os.environ['TZ'] = 'UTC'
dev/patch.py:                        os.environ['TZ'] = old_TZ
misc/cython.py:        sage: environ_parse('$SAGE_LOCAL') == SAGE_LOCAL
misc/cython.py:        sage: os.environ['DEFINE_THIS'] = 'hello'
```


So, this should not require much work to update, but perhaps there are other ways to modify an environment variable in Python ?


---

Comment by nbruin created at 2015-02-08 22:54:02

Replying to [comment:11 tmonteil]:
> So, this should not require much work to update, but perhaps there are other ways to modify an environment variable in Python ?

You don't really need to fix those in-situ. You just need to trigger saving the original value of the variables involved sage-env. I suspect that will be much more robust than trying to track down every site where the environment gets modified.


---

Comment by tmonteil created at 2015-02-09 01:30:49

After quite some work, the following seems to work (and let us love Python):


```

sage_export () {
    if [ $(echo "${SAGE_SAVED_ENVIRONMENT_VARIABLES}" | grep -c " ${1} ") = 0 ] ; then
        SAGE_SAVED_ENVIRONMENT_VARIABLES+=" ${1} "
        if [ -z "${!1+set}" ] ; then
            declare -g SAGE_SAVED_${1}='sage_unset'
        else
            declare -g SAGE_SAVED_${1}=${!1}
        fi
    fi
    declare -g ${1}=${2}
    export ${1}
    export SAGE_SAVED_${1}
    export SAGE_SAVED_ENVIRONMENT_VARIABLES
}


sage_clean () {
    for VARIABLE in ${SAGE_SAVED_ENVIRONMENT_VARIABLES} ; do
        declare SAGE_TMP_VAR_NAME=SAGE_SAVED_${VARIABLE}
        if [ "${!SAGE_TMP_VAR_NAME}" = 'sage_unset' ] ; then
            unset ${VARIABLE}
        else
            declare -g ${VARIABLE}=${!SAGE_TMP_VAR_NAME}
            export ${VARIABLE}
        fi
        unset ${SAGE_TMP_VAR_NAME}
    done
    unset SAGE_SAVED_ENVIRONMENT_VARIABLES
}

```



---

Comment by nbruin created at 2015-02-09 04:15:09

Ah good. Looks like we came up with about the same solution relatively independently. Some things:
 - it's nice if we can export variables and preserve their unset status. Then you can just do `sage_export UNSET_VARIABLE` and clobber it later (I did that by letting `sage_export` differentiate between 1 and 2 parameters)
 - you don't have to rely on a magic value to store whether or not a variable is unset: you can just unset the backup variable
 - bash does have local variables for functions.
 - you can avoid using grep.


---

Comment by nbruin created at 2015-02-09 04:15:57

sage export/restore environment variable facility


---

Comment by jdemeyer created at 2015-02-09 07:36:28

Changing status from needs_review to needs_work.


---

Attachment

_Unsetting_ `PATH`? Then nothing will work...


---

Comment by nbruin created at 2015-02-09 08:09:59

Replying to [comment:15 jdemeyer]:
> _Unsetting_ `PATH`? Then nothing will work...
Would you care to elaborate? If I do

```
$ . sage_restore.sh
$ sage_export PATH
$ PATH=bad_stuff:$PATH
$ sage_restore
```

I end up with my original path back, not with an unset path.

I fully expect that the script needs further tuning and probably lots of quotes in all kinds of places to catch all kinds of little quirks (it's scary to think that shell scripts are the weapon of choice for complicated configuration tasks), but I think the general mechanism is fine. Do you have better suggestions? I'm not married to my implementation. If you come up with something better I'm sure we'll be happy to adopt that.

However, if you're going to suggest to unset PATH then I don't think we'll be so eager, because indeed, I think if you do that, you'll break a lot.


---

Comment by jdemeyer created at 2015-02-09 09:16:24

I didn't look at your script, just the branch here. If a ticket gets set to "needs_review", it's assumed that the branch is what should be reviewed, not some random attachment to the ticket.


---

Comment by git created at 2015-02-10 02:45:47

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by nbruin created at 2015-02-10 02:48:19

Changing status from needs_work to needs_review.


---

Comment by nbruin created at 2015-02-10 02:48:19

I have tried to take the best ideas from both Thierry's and my implementation. Since `sage` itself is already a bash script, there seems no loss in using bashisms in our script, so `${!var}` is fine for dereferencing.

I've ensured what I thought are important variables in `sage-env` are now saved. If you want to see which are saved, do:

```
$ ./sage -sh -c 'echo $SAGE_ENVIRONMENT_VARIABLES'
:PATH:LIBRARY_PATH:CPATH:GP_DATA_DIR:GPHELP:GPDOCDIR:GIT_TEMPLATE_DIR:GIT_EXEC_PATH:SINGULARPATH:SINGULAR_EXECUTABLE:IPYTHONDIR:PYTHON_EGG_CACHE:PYTHONPATH:PYTHONHOME:LD_LIBRARY_PATH:MPLCONFIGDIR:R_HOME:R_PROFILE:MAXIMA_PREFIX:UNAME:CC:CPP:CXX:FC:F77:F90:F95:CCACHE_BASEDIR:ECLDIR:TERMINFO
```

We could "save" all the `SAGE_` variables as well, to ensure that `sage-native-execute` unsets those, but I would expect they would normally not get in the way.


---

Comment by git created at 2015-02-10 02:51:34

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by git created at 2015-02-10 02:54:20

Branch pushed to git repo; I updated commit sha1. This was a forced push. New commits:


---

Comment by jdemeyer created at 2015-02-11 13:38:29

I like the general approach but there is still a quoting issue, when replacing

```
var=`command`
```

by

```
sage_export var `command`
```


The simplest solution might be to replace

```
export var=`command`
```

by

```
sage_export var
var=`command`
```



---

Comment by nbruin created at 2015-02-11 16:16:19

Replying to [comment:23 jdemeyer]:
> I like the general approach but there is still a quoting issue
I don't immediately see what the issue is, but I believe you. I don't think that I met that particular issue in any of the replacements I made, but if it does occur somewhere, then

> The simplest solution might be to replace
> {{{
> export var=`command`
> }}}
> by
> {{{
> sage_export var
> var=`command`
> }}}
I agree with that approach. That was the main idea of allowing `sage_export` with a single argument (and I think I did run into some more complicated manipulations where I just decided to `sage_export` the variable beforehand and let the script do whatever it did before).

*edit:* Now I see where`#!sh` comes from: The `#!` is just a polite rendering of the adjective that is supposed to go in front of `sh`. 
For `sage_export a `echo 1 2 3`` we could do

```
    if (( $# > 1 )); then
        shift
        export $varname="$*"
```

but then, of course, `sage_export a 1 2 3` would do the same thing, presumably with the arguments `1 2 3` rather arbitrarily joined together with spaces (almost guaranteed to trip up environment variable use elsewhere). Perhaps an error if more than 2 arguments are given?


---

Comment by git created at 2015-02-14 22:06:07

Branch pushed to git repo; I updated commit sha1. New commits:


---

Comment by leif created at 2015-05-08 08:37:36

There are some typos:

"and its value and, if this hasn't been done before, its value"

s/sage-native execute/sage-native-execute/

`test` takes `=`, not `==`.

There are some other issues I can't all list right now... ;-)

But for example,

```sh
    #we need to test early that the first parameter is a valid identifier
    export "$varname" || return 1

```

should probably give a more explicit error message instead of just relying on bash's.




Otherwise, nice work.  Why not define `sage_restore()` in `sage-env`?

It could also be extended to restore individual variables (e.g. `sage_restore FOO` or `sage_restore FOO BAR BAZ`).


---

Comment by leif created at 2015-05-08 08:39:39

Replying to [comment:26 leif]:
> {{{
> #!sh
>     #we need to test early that the first parameter is a valid identifier
>     export "$varname" || return 1
> 
> }}}
> should probably give a more explicit error message instead of just relying on bash's.

And `exit 1` would be more appropriate there, I think.


---

Comment by leif created at 2015-05-08 09:42:26

Quoting and use of curly braces is inconsistent.  At some points, quoting isn't necessary, while for example in `[ -z ${!varname+x} ]` quoting would be necessary for portability.

There's also a wild mixture of bash constructs and non-bash constructs, such as `(( $# > 1 ))` instead of `[ $# -gt 1 ]`, while on the other hand e.g. `[ -z ... ]` is used instead of `[This is the Trac macro *-z ... * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#-z ... -macro)` (the latter is btw. safe w.r.t. zero arguments / empty variables).

In `[ "x$SAGE_ENVIRONMENT_VARIABLES" == "x${SAGE_ENVIRONMENT_VARIABLES/$varname}" ]`, using both "x" and quoting is superfluous , `[This is the Trac macro *$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/$varname} * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/$varname} -macro)` would suffice.

But more importantly, that check does not at all work with variable names like `CXX` and `CXXFLAGS`, i.e., when one name is a substring of other variable names.


---

Comment by leif created at 2015-05-08 09:42:26

Changing status from needs_review to needs_work.


---

Comment by leif created at 2015-05-09 08:10:50

Changing component from packages: standard to scripts.


---

Comment by nbruin created at 2015-05-09 17:27:00

Replying to [comment:26 leif]:

> Otherwise, nice work.  Why not define `sage_restore()` in `sage-env`?

because we need it (only) in `sage-native-execute`, which in principle could be executed quite frequently. Why source `sage-env` there for a routine that we only use in `sage-native-execute`? If this ever develops into a more generally used facility then, sure.

> It could also be extended to restore individual variables (e.g. `sage_restore FOO` or `sage_restore FOO BAR BAZ`).

which should be done if the need arises (would you prefer to do it now?)


---

Comment by nbruin created at 2015-05-09 17:37:07

Replying to [comment:28 leif]:
> [various sh/bash style comments]
Please fix! I will never be a reliable bash/sh programmer. If you have better knowledge on the pitfalls there please go ahead and make the changes. It'll be much faster than explaining to me which changes to make and then have to correct my incomplete fixes afterwards.

> But more importantly, that check does not at all work with variable names like `CXX` and `CXXFLAGS`, i.e., when one name is a substring of other variable names.

Oops ... The easiest fix for that is to ensure that `SAGE_SAVED_ENVIRONMENT_VARIABLES` both begins and ends with a `:` and use `[This is the Trac macro *$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/:$varname:} * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/:$varname:} -macro)`. Or do you see a serious flaw in that too?


---

Comment by leif created at 2015-05-09 19:29:06

Replying to [comment:30 nbruin]:
> Replying to [comment:26 leif]:
> 
> > Otherwise, nice work.  Why not define `sage_restore()` in `sage-env`?
> 
> because we need it (only) in `sage-native-execute`

Well, at the moment I think.  (I was also wondering whether people will find it at all if it's [just] defined in `sage-native-execute`.  Ok, a comment in `sage-env` refers to the latter.)




> which in principle could be executed quite frequently. Why source `sage-env` there for a routine that we only use in `sage-native-execute`? If this ever develops into a more generally used facility then, sure.

Every `sage-*` script in `local/bin/` (likewise, `src/bin/`) has (and must have) the Sage environment set up, i.e., is (directly or indirectly) called from a script that already sourced `sage-env`, so you of course don't have to `source sage-env` in `sage-native-execute` again.  (After all, if that wasn't the case, the function couldn't restore any environment variables because `sage-env` saves them.) 

The only thing we'd have to add is `export -f sage_restore`.




There's probably one problem already:  It at least used to be the case that `sage-env` must not use bashisms since it isn't (or wasn't) necessarily sourced by bash.  (IIRC in the top-level Makefile, which apparently is no longer the case, but also when starting a Sage subshell, maybe in more cases.)

If that's still a problem, we could "bypass" some things in case the shell isn't bash.
 



When or where is `sage-native-execute` executed frequently?




> > It could also be extended to restore individual variables (e.g. `sage_restore FOO` or `sage_restore FOO BAR BAZ`).
> 
> which should be done if the need arises (would you prefer to do it now?)

Just an idea, doesn't have to be implemented here.


---

Comment by leif created at 2015-05-09 19:40:58

Replying to [comment:31 nbruin]:
> Replying to [comment:28 leif]:
> > [various sh/bash style comments]
> Please fix! I will never be a reliable bash/sh programmer. If you have better knowledge on the pitfalls there please go ahead and make the changes. It'll be much faster than explaining to me which changes to make and then have to correct my incomplete fixes afterwards.

No problem, provided the source is "stable".

Not sure yet whether to make it "all bash" (e.g. `[This is the Trac macro *... * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#... -macro)` instead of `[ ... ]`, the former being safer and faster) or POSIX shell only.


---

Comment by leif created at 2015-05-09 19:49:02

Replying to [comment:31 nbruin]:
> Replying to [comment:28 leif]:
> > But more importantly, that check does not at all work with variable names like `CXX` and `CXXFLAGS`, i.e., when one name is a substring of other variable names.
> 
> Oops ... The easiest fix for that is to ensure that `SAGE_SAVED_ENVIRONMENT_VARIABLES` both begins and ends with a `:` and use `[This is the Trac macro *$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/:$varname:} * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#$SAGE_ENVIRONMENT_VARIABLES = ${SAGE_ENVIRONMENT_VARIABLES/:$varname:} -macro)`.

Good idea, probably using a different separator as well (to avoid confusion with typical `:`-lists).




> Or do you see a serious flaw in that too?

Not at first glance.


---

Comment by nbruin created at 2015-05-09 23:36:49

Replying to [comment:33 leif]:
> Not sure yet whether to make it "all bash" (e.g. `[This is the Trac macro *... * that was inherited from the migration](https://trac.sagemath.org/wiki/WikiMacros#... -macro)` instead of `[ ... ]`, the former being safer and faster) or POSIX shell only.

I tried staying with POSIX but it's a pain for this case, in particular because we need dereferencing of variables, which is easy in bash and painful in POSIX. I recall that the substring matching was also easier with bash.

The fact is that `sage` is already a bash script, so we lose no generality by using bash features here, so we might as well.

For separation: I figured `:` was pretty safe, since that's an insane character to put in a variable name. Another good separator is probably "=" or "$", since you _really_ need to go out of your way to put those in a variable name.

I was pretty happy with the state of the script, so I'm happy to not make changes to it.


---

Comment by nbruin created at 2015-05-10 03:52:03

Replying to [comment:32 leif]:
> The only thing we'd have to add is `export -f sage_restore`.

That's horrible! That stores the entire function in the environment. Every process spawned after sage-env was sourced would have that in its memory.

> When or where is `sage-native-execute` executed frequently?

OK, it's unlikely that a program that has such specific environment needs that it needs `sage-native-execute` would start up so quickly that some bash sourcing would be problematic.

However, I think there is something logically wrong with sourcing `sage-env`, which has all manner of side effects, in a script that is _designed_ to only run when `sage-env` has already run and whose sole purpose is undoing a lot of these side-effects.

The "proper" solution would probably be to have sage_export and sage_restore in yet another file and source that in sage-env. But probably adds considerable overhead (to any sourcing of sage-env).


---

Comment by nbruin created at 2015-05-20 04:27:50

OK, I'm holding off updating the branch here because leif expressed willingness to clean up the shell style of the code here. leif pointed out one actual deficiency (the substring problem), which I know how to correct. It looks like this ticket is a prereq (or at least should be) for #18438, so there's a little more urgency to resolving this ticket. Preferences on how to proceed?


---

Comment by vbraun created at 2015-05-20 07:00:28

The added `sage-system-python` script at #18438 should be good enough for that ticket, we could also just run with that until `sage-native-execute` works.
