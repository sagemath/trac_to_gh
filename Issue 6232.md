# Issue 6232: Consider CADO-NFS for inclusion

Issue created by migration from Trac.

Original creator: malb

Original creation time: 2009-06-06 12:48:45

Assignee: malb

CC:  zimmerma leif wbhart jpflori lorenz

Keywords: linear algebra, factoring, number theory

CADO-NFS is an implementation of the number field sieve:


```
CADO is sponsored by the French Research Agency (ANR).
It started in 2008 for 3 years. It involves 3 teams: CACAO (INRIA Nancy), TANC (INRIA Saclay), and Gerald Tenenbaum’s team (IECN Nancy). 

Objectives:
 * better understand how the Number Field Sieve works
 * publish a state-of-the art implementation, not to break new
   records, but to routinely factor numbers of 155 digits
 * use that code base to try new ideas and/or new algorithms
```


http://webloria.loria.fr/~zimmerma/talks/cado.pdf

The Block-Wiedemann in CADO-NSF might be of independent interest.


---

Comment by malb created at 2010-07-21 16:07:52

I vote for closing this ticket, no point in having it around since no motion to actually include it is happening.


---

Comment by zimmerma created at 2011-11-01 09:31:57

We just released version 1.1 of CADO-NFS, see http://cado-nfs.gforge.inria.fr/

Paul


---

Comment by zimmerma created at 2011-11-01 09:34:40

see also #5310: both msieve and cado-nfs implement the number field sieve.


---

Comment by jdemeyer created at 2014-11-13 14:08:01

Changing component from packages: standard to packages: optional.


---

Comment by zimmerma created at 2015-06-03 11:28:20

I use this ticket to report an issue related to CADO-NFS. I'm not sure the problem is due to Sage. I could open a separate ticket if needed.

The issue is the following. Some colleague wrote the following Sage code to call CADO-NFS
from Sage:

```
import subprocess
def my_exec_factor(nbr):
    cmd = ['/tmp/cado-nfs-1.1/factor.sh', str(nbr)]
    process = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        print "Output :"
        print output
        raise subprocess.CalledProcessError(retcode, cmd)
    return output

res=my_exec_factor(90377629292003121684002147101760858109247336549001090677693)

r=[]
for i in res.splitlines()[-6].split(' '):
    r.append(Integer(i))
print r
```

When used with CADO-NFS 1.1, this code works fine.

However with CADO-NFS 2.1.1 it fails:

```
sage: %runfile /tmp/garambois.sage
Output :
(debug mode, temporary files will be kept in /tmp/cado.mru0w9AeIM)
Fatal Python error: Py_Initialize: Unable to get the locale encoding
  File "/usr/local/sage-6.0-x86_64-Linux/local/lib/python/encodings/__init__.py", line 123
    raise CodecRegistryError,\
                            ^
SyntaxError: invalid syntax

Current thread 0x00002b81297f1700 (most recent call first):
/tmp/cado-nfs-2.1.1/factor.sh: line 242: 13296 Aborted                 "${TIMEOUT[`@`]}" $PYTHON $cadofactor "$t/param" N=$n tasks.execpath="$bindir" tasks.threads=$cores tasks.workdir="$t" slaves.hostnames="$hostnames" slaves.nrclients=$slaves slaves.scriptpath="$scriptpath" "$server_address" slaves.basepath="$t/client/" "$`@`"
FAILED ; data left in /tmp/cado.mru0w9AeIM

---------------------------------------------------------------------------
CalledProcessError                        Traceback (most recent call last)
<ipython-input-1-cf20ddc02bb1> in <module>()
----> 1 get_ipython().magic(u'runfile /tmp/garambois.sage')

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/IPython/core/interactiveshell.pyc in magic(self, arg_s)
   2134         magic_name, _, magic_arg_s = arg_s.partition(' ')
   2135         magic_name = magic_name.lstrip(prefilter.ESC_MAGIC)
-> 2136         return self.run_line_magic(magic_name, magic_arg_s)
   2137 
   2138     #-------------------------------------------------------------------------

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/IPython/core/interactiveshell.pyc in run_line_magic(self, magic_name, line)
   2060                 args.append(sys._getframe(stack_depth).f_locals)
   2061             with self.builtin_trap:
-> 2062                 result = fn(*args)
   2063             return result
   2064 

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/misc/sage_extension.pyc in runfile(self, s)

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/IPython/core/magic.pyc in <lambda>(f, *a, **k)
    189     # but it's overkill for just that one bit of state.
    190     def magic_deco(arg):
--> 191         call = lambda f, *a, **k: f(*a, **k)
    192 
    193         if callable(arg):

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/misc/sage_extension.pyc in runfile(self, s)
     77         """
     78         from sage.misc.preparser import load_wrap
---> 79         return self.shell.ex(load_wrap(s, attach=False))
     80 
     81     `@`line_magic

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/IPython/core/interactiveshell.pyc in ex(self, cmd)
   2382         """Execute a normal python statement in user namespace."""
   2383         with self.builtin_trap:
-> 2384             exec cmd in self.user_global_ns, self.user_ns
   2385 
   2386     def ev(self, expr):

<string> in <module>()

/usr/local/sage-6.0-x86_64-Linux/local/lib/python2.7/site-packages/sage/misc/preparser.pyc in load(filename, globals, attach)
   1770             # Preparse in memory only for speed.
   1771             exec_file_is(fpath)
-> 1772             exec preparse_file(open(fpath).read()) + "\n" in globals
   1773     elif fpath.endswith('.spyx') or fpath.endswith('.pyx'):
   1774         exec_file_is(fpath)

<string> in <module>()

<string> in my_exec_factor(nbr)

CalledProcessError: Command '['/tmp/cado-nfs-2.1.1/factor.sh', '90377629292003121684002147101760858109247336549001090677693']' returned non-zero exit status 134
```

My guess is that there is an interaction between the version of Python used by CADO-NFS 2.1.1 (Python 3) and the one used by Sage (Python 2.7). (Note that CADO-NFS 1.1 did not use Python but Perl instead.)

Can anybody reproduce that problem? Any idea how to solve it?

Paul


---

Comment by zimmerma created at 2015-06-03 12:00:38

by the way the above code, if we manage to make it work with recent versions of CADO-NFS, might be useful to factor large integers from within Sage.

Paul


---

Comment by zimmerma created at 2015-06-03 15:03:53

thanks to Alexander Kruppa, the solution is to undefine the environment variables PYTHONHOME and PYTHONPATH:

```
import subprocess, os
def my_exec_factor(nbr):
    cmd = ['/tmp/cado-nfs-2.1.1/factor.sh', str(nbr)]
    my_env = os.environ
    if my_env.has_key("PYTHONHOME"):
       my_env.pop("PYTHONHOME")
    if my_env.has_key("PYTHONPATH"):
       my_env.pop("PYTHONPATH")
    process = subprocess.Popen(cmd, stderr=subprocess.STDOUT, stdout=subprocess.PIPE, env=my_env)
    output, unused_err = process.communicate()
    retcode = process.poll()
    if retcode:
        print "Output :"
        print output
        raise subprocess.CalledProcessError(retcode, cmd)
    return output
```



---

Comment by zimmerma created at 2015-06-04 09:53:54

in addition, one should unset PATH:

```
    if my_env.has_key("PATH"):
       my_env.pop("PATH")
```

and replace `res.splitlines()[-6]` by `res.splitlines()[-2]` for CADO-NFS 2.1.1.

Paul


---

Comment by zimmerma created at 2017-01-17 09:28:55

fixed typo in description (CADO-NSF -> CADO-NFS)


---

Comment by @sheerluck created at 2021-11-21 11:20:33

I have no access to https://gitlab.inria.fr/cado-nfs/cado-nfs/-/issues but I want to report this: 


```
$ cado-nfs.py 10000000000000000000009070000000000000000000063
RuntimeError: no parameter file found for c47 (tried c47, c45)
```

after mixing up `factor/params.c30` and `factor/params.c60` into `factor/params.c45`:

```
$ cado-nfs.py 10000000000000000000009070000000000000000000063
Info:root: Using default parameter file /usr/share/cado-nfs-3.0.0/factor/params.c45
...
10000000000000000000009 1000000000000000000000007
```



---

Comment by thome created at 2021-11-22 03:07:36

Hi Andrew,

> I have no access to ​https://gitlab.inria.fr/cado-nfs/cado-nfs/-/issues

The relevant bit of info is https://sympa.inria.fr/sympa/arc/cado-nfs/2020-10/msg00006.html (the link was dead for yet another fallout of this infrastructure change, sorry for that). TL;DR: send me an e-mail, I'll happily open you an account.

As regards your feature request: the number field sieve as a factoring algorithm does not really make sense for numbers that small. You would be much better off trying to use another piece of code to factor 45-digit integers (check out yafu, for example). This is the reason why we didn't care to write parameter files for these sizes.

The reason for the existence of the 30-digit file is different: it's used for continuous integration.

If you really really want to factor a 45-digit number with NFS, the approach that you have taken is the right one: interpolate between nearby parameter files. A first working guess is unlikely to be "optimal", but again, there's zero chance that NFS is "optimal" in this size range anyway. (patches with contributed parameter files are welcome, of course!)


---

Comment by zimmerma created at 2021-11-22 09:04:16

as said by Emmanuel, feel free to contribute the params.c45 file.
