# Issue 1198: scipy-20071020 fails to build

Issue created by migration from https://trac.sagemath.org/ticket/1198

Original creator: mabshoff

Original creation time: 2007-11-18 06:40:34

Assignee: jkantor


```
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/local/lib/python2.5/site-packages/numpy/distutils/command/config.py", line 28, in finalize_options
    f = self.distribution.get_command_obj('config_fc')
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/local/lib/python2.5/distutils/dist.py", line 863, in get_command_obj
    if not cmd_obj and create:
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/local/lib/python2.5/distutils/cmd.py", line 105, in __getattr__
    if attr == 'dry_run':
RuntimeError: maximum recursion depth exceeded in cmp
Error building scipy.

real    0m2.319s
user    0m0.440s
sys     0m0.152s
sage: An error occurred while installing scipy-20071020
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/spkg/build/scipy-20071020 and type 'make'.
Instead type "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/sage -sh"
in order to set all environment variables correctly, then cd to
/tmp/Work-mabshoff/release-cycles/sage-2.8.13-build/spkg/build/scipy-20071020
(When you are done debugging, you can type "exit" to leave the
```


Cheers,

Michael


---

Comment by mabshoff created at 2007-11-18 06:50:42

hmm, scipy-20070817 also fails to build with the same error with 2.8.13.alpha0. So something else is broken somehow.

Cheers,

Michael


---

Comment by mabshoff created at 2007-11-18 09:38:06

There is a persistent build failure on sage.math, even from a fresh build:

```
Finished extraction
****************************************************
Host system
uname -a:
Linux sage 2.6.18-4-amd64 #1 SMP Fri May 4 00:37:33 UTC 2007 x86_64 GNU/Linux
****************************************************
****************************************************
GCC Version
gcc -v
Using built-in specs.
Target: x86_64-linux-gnu
Configured with: ../src/configure -v --enable-languages=c,c++,fortran,objc,obj-c++,treelang --prefix=/usr --enable-shared --with-system-zlib --libexecdir=/usr/lib --without-included-gettext --enable-threads=posix --enable-nls --program-suffix=-4.1 --enable-__cxa_atexit --enable-clocale=gnu --enable-libstdcxx-debug --enable-mpfr --enable-checking=release x86_64-linux-gnu
Thread model: posix
gcc version 4.1.2 20061115 (prerelease) (Debian 4.1.1-21)
****************************************************
Using g95mkl_info:
  libraries mkl,vml,guide not found in /lib
  NOT AVAILABLE

fftw3_info:
  libraries fftw3 not found in /lib
  fftw3 not found
  NOT AVAILABLE

fftw2_info:
  libraries rfftw,fftw not found in /lib
  fftw2 not found
  NOT AVAILABLE

dfftw_info:
  libraries drfftw,dfftw not found in /lib
  dfftw not found
  NOT AVAILABLE

djbfft_info:
  NOT AVAILABLE

blas_opt_info:
blas_mkl_info:
  libraries mkl,vml,guide not found in /lib
  NOT AVAILABLE

atlas_blas_threads_info:
Setting PTATLAS=ATLAS
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries ptf77blas,ptcblas,atlas not found in /lib
  NOT AVAILABLE

atlas_blas_info:
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries f77blas,cblas,atlas not found in /lib
  NOT AVAILABLE

/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/system_info.py:1314: UserWarning: 
    Atlas (http://math-atlas.sourceforge.net/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [atlas]) or by setting
    the ATLAS environment variable.
  warnings.warn(AtlasNotFoundError.__doc__)
blas_info:
  libraries blas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries blas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  FOUND:
    libraries = ['blas']
    library_dirs = ['/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib']
    language = f77

  FOUND:
    libraries = ['blas']
    library_dirs = ['/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib']
    define_macros = [('NO_ATLAS_INFO', 1)]
    language = f77

lapack_opt_info:
lapack_mkl_info:
  NOT AVAILABLE

atlas_threads_info:
Setting PTATLAS=ATLAS
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries ptf77blas,ptcblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries ptf77blas,ptcblas,atlas not found in /lib
  libraries lapack_atlas not found in /lib
numpy.distutils.system_info.atlas_threads_info
  NOT AVAILABLE

atlas_info:
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  libraries f77blas,cblas,atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries lapack_atlas not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib
  libraries f77blas,cblas,atlas not found in /lib
  libraries lapack_atlas not found in /lib
numpy.distutils.system_info.atlas_info
  NOT AVAILABLE

/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/system_info.py:1221: UserWarning: 
    Atlas (http://math-atlas.sourceforge.net/) libraries not found.
    Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [atlas]) or by setting
    the ATLAS environment variable.
  warnings.warn(AtlasNotFoundError.__doc__)
lapack_info:
  libraries lapack not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local
  libraries lapack not found in /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/include
  FOUND:
    libraries = ['lapack']
    library_dirs = ['/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib']
    language = f77

  FOUND:
    libraries = ['lapack', 'blas']
    library_dirs = ['/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib']
    define_macros = [('NO_ATLAS_INFO', 1)]
    language = f77

non-existing path in 'scipy/linsolve': 'tests'
umfpack_info:
Disabled umfpack_info: (UMFPACK is None)
/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/system_info.py:403: UserWarning: 
    UMFPACK sparse solver (http://www.cise.ufl.edu/research/sparse/umfpack/)
    not found. Directories to search for the libraries can be specified in the
    numpy/distutils/site.cfg file (section [umfpack]) or by setting
    the UMFPACK environment variable.
  warnings.warn(self.notfounderror.__doc__)
  NOT AVAILABLE

running build
running config_cc
unifing config_cc, config, build_clib, build_ext, build commands --compiler options
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
[cut 180 lines of the same]
unifing config_fc, config, build_clib, build_ext, build commands --fcompiler options
Traceback (most recent call last):
  File "setup.py", line 53, in <module>
    setup_package()
  File "setup.py", line 45, in setup_package
    configuration=configuration )
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/core.py", line 173, in setup
    return old_setup(**new_attr)
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/core.py", line 151, in setup
    dist.run_commands()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/dist.py", line 974, in run_commands
    self.run_command(cmd)
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/dist.py", line 994, in run_command
    cmd_obj.run()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/command/build.py", line 112, in run
    self.run_command(cmd_name)
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 333, in run_command
    self.distribution.run_command(command)
[cut 1900 lines of the same]
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 319, in get_finalized_command
    cmd_obj.ensure_finalized()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 117, in ensure_finalized
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/command/config.py", line 30, in finalize_options
    ('fcompiler', 'fcompiler'))
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 305, in set_undefined_options
    src_cmd_obj.ensure_finalized()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 117, in ensure_finalized
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/command/config_compiler.py", line 61, in finalize_options
    config = self.get_finalized_command('config')
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 319, in get_finalized_command
    cmd_obj.ensure_finalized()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 117, in ensure_finalized
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/command/config.py", line 30, in finalize_options
    ('fcompiler', 'fcompiler'))
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 305, in set_undefined_options
    src_cmd_obj.ensure_finalized()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 117, in ensure_finalized
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/command/config_compiler.py", line 61, in finalize_options
    config = self.get_finalized_command('config')
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 319, in get_finalized_command
    cmd_obj.ensure_finalized()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 117, in ensure_finalized
    self.finalize_options()
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/site-packages/numpy/distutils/command/config.py", line 28, in finalize_options
    f = self.distribution.get_command_obj('config_fc')
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/dist.py", line 863, in get_command_obj
    if not cmd_obj and create:
  File "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/local/lib/python2.5/distutils/cmd.py", line 105, in __getattr__
    if attr == 'dry_run':
RuntimeError: maximum recursion depth exceeded in cmp
Error building scipy.

real	0m2.739s
user	0m0.412s
sys	0m0.172s
sage: An error occurred while installing scipy-20071020
Please email sage-devel http://groups.google.com/group/sage-devel
explaining the problem and send the relevant part of
of /tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/install.log.  Describe your computer, operating system, etc.
If you want to try to fix the problem, yourself *don't* just cd to
/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/spkg/build/scipy-20071020 and type 'make'.
Instead type "/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/sage -sh"
in order to set all environment variables correctly, then cd to
/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/spkg/build/scipy-20071020
(When you are done debugging, you can type "exit" to leave the
subshell.)
make[1]: *** [installed/scipy-20071020] Error 1
make[1]: Leaving directory `/tmp/Work-mabshoff/release-cycles/sage-2.8.13-alpha0/spkg'

real	0m9.790s
user	0m5.800s
sys	0m1.728s
```

After this the build is FUBAR and even the old scipy no longer builds.

Cheers,

Michael


---

Comment by jkantor created at 2007-11-18 20:49:52

Something was going on with files from older numpy versions persisting and screwing up the scipy build. The solution is to rm -rf the numpy directory in site-packages
before a newer version of numpy is built.

The numpy script is supposed to do this before it builds but it was doing

rm -rf $SAGE_LOCAL/local/lib/python2.5/site-package/numpy 

instead of

rm -rf $SAGE_LOCAL/lib/python2.5/site-packages/numpy

so this wasn't happening.

If the old numpy is correctly deleted, the new one and scipy build fine (for me at least)

New numpy and scipy packages to fix that problem and include the version number in
the file name.

http://sage.math.washington.edu/home/jkantor/spkgs/scipy-20071020-0.6.spkg http://sage.math.washington.edu/home/jkantor/spkgs/numpy-20071020-1.0.3.1.spkg


---

Comment by mabshoff created at 2007-11-18 23:21:35

Merged in 2.8.13.alpha1.

The new numpy and scipy spkgs now build for me on sage.math on a fresh 2.8.13.alpha0. 

Great job Josh,

Michael


---

Comment by mabshoff created at 2007-11-18 23:21:35

Resolution: fixed
