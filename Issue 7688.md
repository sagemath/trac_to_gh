# Issue 7688: remove byte-compiled files from the sage source distribution

archive/issues_007688.json:
```json
{
    "body": "Assignee: tbd\n\nCC:  @ohanar\n\nThere are tons of Python byte-compiled files included in the Sage source distribution, all over the place.   I can't see why we include any of these.  We could (a) delete them all, and (b) complain to all relevant upstreams about them.  \n\nHere's a list:\n\n```\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_macros.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_parser.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_filters.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_ifcondition.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_security.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_inheritance.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_lexer.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/loaderres/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_streaming.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_syntax.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_undefined.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_loaders.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_forloop.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_i18n.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_tests.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_various.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_various.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_undefined.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_tests.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_syntax.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_streaming.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_security.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_parser.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_old_bugs.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_macros.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_lrucache.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_loaders.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_lexer.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_inheritance.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_imports.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_ifcondition.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_i18n.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_forloop.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_filters.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_ext.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_debug.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/loaderres/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/docs/jinjaext.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/src/numerical/slatec.lisp: Emacs v18 byte-compiled Lisp data\nsage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/src/sys-proclaim.lisp: Emacs v18 byte-compiled Lisp data\nsage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/share/affine/sys-proclaim.lisp: Emacs v18 byte-compiled Lisp data\nsage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/macro/latex.pyc: python 2.4 byte-compiled\nsage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/parser/inline_latex.pyc: python 2.4 byte-compiled\nsage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/parser/latex.pyc: python 2.4 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/numpydoc.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/docscrape.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/phantom_import.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/docscrape_sphinx.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/autosummary.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/only_directives.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/warnings.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/linecache.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/encodings/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/types.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/constants.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/sagenb-0.4.7/src/sagenb/data/jquery/plugins/jeditable/jquery.jeditable.mini.js: Emacs v18 byte-compiled Lisp data\nsage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/arpack.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/tests/test_arpack.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/info.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/sqlalchemy-0.4.6.p1/src/test/binary_data_one.dat: python 2.4 byte-compiled\nsage-4.3.rc0/spkg/standard/sqlalchemy-0.4.6.p1/src/test/binary_data_two.dat: python 2.4 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/action.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/enviroment.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/__init__.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/all.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/cython.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/gcc.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/filewalker.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/all.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/optionmanager.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/taskmanager.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compiler.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/config.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/dependencies.pyc: python 2.5 byte-compiled\nsage-4.3.rc0/spkg/standard/sage_scripts-4.3.rc0/ipython/ipy_user_conf.pyc: python 2.4 byte-compiled\n```\n\nIssue created by migration from https://trac.sagemath.org/ticket/7688\n\n",
    "created_at": "2009-12-15T19:34:22Z",
    "labels": [
        "component: distribution",
        "minor",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-5.4",
    "title": "remove byte-compiled files from the sage source distribution",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/7688",
    "user": "https://github.com/williamstein"
}
```
Assignee: tbd

CC:  @ohanar

There are tons of Python byte-compiled files included in the Sage source distribution, all over the place.   I can't see why we include any of these.  We could (a) delete them all, and (b) complain to all relevant upstreams about them.  

Here's a list:

```
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_macros.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_parser.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_filters.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_ifcondition.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_security.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_inheritance.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_lexer.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/loaderres/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_streaming.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_syntax.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_undefined.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_loaders.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_forloop.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_i18n.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_tests.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja-1.2.p0/src/tests/test_various.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_various.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_undefined.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_tests.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_syntax.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_streaming.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_security.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_parser.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_old_bugs.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_macros.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_lrucache.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_loaders.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_lexer.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_inheritance.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_imports.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_ifcondition.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_i18n.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_forloop.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_filters.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_ext.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/test_debug.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/tests/loaderres/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/jinja2-2.1.1.p0/src/docs/jinjaext.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/src/numerical/slatec.lisp: Emacs v18 byte-compiled Lisp data
sage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/src/sys-proclaim.lisp: Emacs v18 byte-compiled Lisp data
sage-4.3.rc0/spkg/standard/maxima-5.19.1.p2/src/share/affine/sys-proclaim.lisp: Emacs v18 byte-compiled Lisp data
sage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/macro/latex.pyc: python 2.4 byte-compiled
sage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/parser/inline_latex.pyc: python 2.4 byte-compiled
sage-4.3.rc0/spkg/standard/moin-1.5.7.p3/patches/parser/latex.pyc: python 2.4 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/numpydoc.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/docscrape.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/phantom_import.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/docscrape_sphinx.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/autosummary.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/numpy-1.3.0.p2/src/doc/sphinxext/only_directives.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/warnings.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/linecache.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python-2.6.2.p4/src/Lib/encodings/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/types.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/python_gnutls-1.1.4.p6/src/gnutls/library/constants.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/sagenb-0.4.7/src/sagenb/data/jquery/plugins/jeditable/jquery.jeditable.mini.js: Emacs v18 byte-compiled Lisp data
sage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/arpack.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/tests/test_arpack.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/info.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/scipy_sandbox-20071020.p4/arpack/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/sqlalchemy-0.4.6.p1/src/test/binary_data_one.dat: python 2.4 byte-compiled
sage-4.3.rc0/spkg/standard/sqlalchemy-0.4.6.p1/src/test/binary_data_two.dat: python 2.4 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/action.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/enviroment.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/__init__.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/all.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/cython.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compilers/gcc.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/filewalker.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/all.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/optionmanager.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/taskmanager.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/compiler.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/config.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/extcode-4.3.rc0/sagebuild/build/dependencies.pyc: python 2.5 byte-compiled
sage-4.3.rc0/spkg/standard/sage_scripts-4.3.rc0/ipython/ipy_user_conf.pyc: python 2.4 byte-compiled
```

Issue created by migration from https://trac.sagemath.org/ticket/7688





---

archive/issue_comments_065852.json:
```json
{
    "body": "Changing status from new to needs_review.",
    "created_at": "2012-10-05T09:30:02Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65852",
    "user": "https://github.com/jdemeyer"
}
```

Changing status from new to needs_review.



---

archive/issue_comments_065853.json:
```json
{
    "body": "Shouldn't we keep the DS_Store line for OSX? Or maybe replace it with something like\n\n```\n(^|/)\\.DS_Store$\n(^|/)\\._\\.DS_Store$\n```",
    "created_at": "2012-10-05T19:28:51Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65853",
    "user": "https://github.com/ohanar"
}
```

Shouldn't we keep the DS_Store line for OSX? Or maybe replace it with something like

```
(^|/)\.DS_Store$
(^|/)\._\.DS_Store$
```



---

archive/issue_comments_065854.json:
```json
{
    "body": "`devel/sage/.hgignore` has\n\n```\n(^|/)\\.DS_Store$\n```\nWould that be okay?",
    "created_at": "2012-10-05T19:34:43Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65854",
    "user": "https://github.com/jdemeyer"
}
```

`devel/sage/.hgignore` has

```
(^|/)\.DS_Store$
```
Would that be okay?



---

archive/issue_comments_065855.json:
```json
{
    "body": "Replying to [comment:4 ohanar]:\n> Shouldn't we keep the DS_Store line for OSX?\n\nI was thinking that DS_Store files shouldn't end up in the actual shipped spkgs.  But of course, `.hgignore` is also used for end-user installations.  So we should probably keep it indeed.",
    "created_at": "2012-10-05T19:36:01Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65855",
    "user": "https://github.com/jdemeyer"
}
```

Replying to [comment:4 ohanar]:
> Shouldn't we keep the DS_Store line for OSX?

I was thinking that DS_Store files shouldn't end up in the actual shipped spkgs.  But of course, `.hgignore` is also used for end-user installations.  So we should probably keep it indeed.



---

archive/issue_comments_065856.json:
```json
{
    "body": "Patch updated, with `.DS_Store` put back in `.hgignore`.",
    "created_at": "2012-10-08T08:17:35Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65856",
    "user": "https://github.com/jdemeyer"
}
```

Patch updated, with `.DS_Store` put back in `.hgignore`.



---

archive/issue_comments_065857.json:
```json
{
    "body": "Apply to EXTCODE",
    "created_at": "2012-10-08T08:18:54Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65857",
    "user": "https://github.com/jdemeyer"
}
```

Apply to EXTCODE



---

archive/issue_comments_065858.json:
```json
{
    "body": "Changing status from needs_review to positive_review.",
    "created_at": "2012-10-13T16:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65858",
    "user": "https://github.com/ohanar"
}
```

Changing status from needs_review to positive_review.



---

archive/issue_comments_065859.json:
```json
{
    "body": "Attachment [7688_extcode_pyc.patch](tarball://root/attachments/some-uuid/ticket7688/7688_extcode_pyc.patch) by @ohanar created at 2012-10-13 16:45:46\n\nOk, everything looks good to me.",
    "created_at": "2012-10-13T16:45:46Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65859",
    "user": "https://github.com/ohanar"
}
```

Attachment [7688_extcode_pyc.patch](tarball://root/attachments/some-uuid/ticket7688/7688_extcode_pyc.patch) by @ohanar created at 2012-10-13 16:45:46

Ok, everything looks good to me.



---

archive/issue_events_018365.json:
```json
{
    "actor": "https://github.com/jdemeyer",
    "created_at": "2012-10-14T18:55:53Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/7688#event-18365"
}
```



---

archive/issue_comments_065860.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2012-10-14T18:55:53Z",
    "issue": "https://github.com/sagemath/sagetest/issues/7688",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/7688#issuecomment-65860",
    "user": "https://github.com/jdemeyer"
}
```

Resolution: fixed
