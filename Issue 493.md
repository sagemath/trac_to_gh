# Issue 493: gcc 4.3: LinBox package has broken NTL and givaro test

archive/issues_000493.json:
```json
{
    "body": "Assignee: mabshoff\n\nOkay, first off the current LinBox.spkg from 2.8.2 needs some cleanups because there are unneeded files in patches that are just copied over. That causes the \"NTL check for > 5\" to fail. The other problem appears to be that givaro as well as LinBox have different and probably incompatible gmp++.h header files. The current LinBox.spkg also abuses CFLAGS, CXXFLAGS and CPPFLAGS and that is due to some bugs in LinBox's config system. I have fixed the issue for GMP and will also fix the problem for Givaro and NTL. \n\nIn addition two build fixes (1 by Saunders, 1 by me) have been proposed and should make it into svn fairly soon. I am currently stuck with the following:\n\n\n```\n g++ -DHAVE_CONFIG_H -I. -I. -I../.. -I../.. -I. -O2 -\nDDISABLE_COMMENTATOR -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local//\ninclude -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local//include -MT\nlb-element.lo -MD -MP -MF .deps/lb-element.Tpo -c lb-element.C -o lb-\nelement.o\nIn file included from ./lb-domain-type.h:27,\n                 from ./lb-domain-functor.h:28,\n                 from ./lb-domain-function.h:28,\n                 from ./lb-element-data.h:31,\n                 from lb-element.C:28:\n../../linbox/field/PID-integer.h: In member function 'void\nLinBox::PID_integer::RationalReconstruction(LinBox::integer&,\nLinBox::integer&, const LinBox::integer&, const LinBox::integer&,\nconst LinBox::integer&, bool, bool) const':\n../../linbox/field/PID-integer.h:279: error: ISO C++ says that these\nare ambiguous, even though the worst conversion for the first is\nbetter than the worst conversion for the second:\n../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const\nInteger&, const Integer&)\n../../gmp++/gmp++_int.h:126: note: candidate 2: int\nInteger::operator>(long unsigned int) const\n../../linbox/field/PID-integer.h:279: error: ISO C++ says that these\nare ambiguous, even though the worst conversion for the first is\nbetter than the worst conversion for the second:\n../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const\nInteger&, const Integer&)\n../../gmp++/gmp++_int.h:125: note: candidate 2: int\nInteger::operator>(long int) const\n../../linbox/field/PID-integer.h:279: error: ISO C++ says that these\nare ambiguous, even though the worst conversion for the first is\nbetter than the worst conversion for the second:\n../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const\nInteger&, const Integer&)\n../../gmp++/gmp++_int.h:124: note: candidate 2: int\nInteger::operator>(int) const\nmake[3]: *** [lb-element.lo] Error 1\nmake[3]: Leaving directory `/tmp/Work2/linbox/linbox-r2798/interfaces/\ndriver'\n```\n\n\nAny ideas?\n\nCheers,\n\nMichael\n\nIssue created by migration from https://trac.sagemath.org/ticket/493\n\n",
    "created_at": "2007-08-26T19:38:27Z",
    "labels": [
        "component: packages: standard",
        "bug"
    ],
    "milestone": "https://github.com/sagemath/sagetest/milestones/sage-3.0",
    "title": "gcc 4.3: LinBox package has broken NTL and givaro test",
    "type": "issue",
    "url": "https://github.com/sagemath/sagetest/issues/493",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```
Assignee: mabshoff

Okay, first off the current LinBox.spkg from 2.8.2 needs some cleanups because there are unneeded files in patches that are just copied over. That causes the "NTL check for > 5" to fail. The other problem appears to be that givaro as well as LinBox have different and probably incompatible gmp++.h header files. The current LinBox.spkg also abuses CFLAGS, CXXFLAGS and CPPFLAGS and that is due to some bugs in LinBox's config system. I have fixed the issue for GMP and will also fix the problem for Givaro and NTL. 

In addition two build fixes (1 by Saunders, 1 by me) have been proposed and should make it into svn fairly soon. I am currently stuck with the following:


```
 g++ -DHAVE_CONFIG_H -I. -I. -I../.. -I../.. -I. -O2 -
DDISABLE_COMMENTATOR -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local//
include -I/tmp/Work2/sage-2.8.2-gcc4.3/sage-2.8.2/local//include -MT
lb-element.lo -MD -MP -MF .deps/lb-element.Tpo -c lb-element.C -o lb-
element.o
In file included from ./lb-domain-type.h:27,
                 from ./lb-domain-functor.h:28,
                 from ./lb-domain-function.h:28,
                 from ./lb-element-data.h:31,
                 from lb-element.C:28:
../../linbox/field/PID-integer.h: In member function 'void
LinBox::PID_integer::RationalReconstruction(LinBox::integer&,
LinBox::integer&, const LinBox::integer&, const LinBox::integer&,
const LinBox::integer&, bool, bool) const':
../../linbox/field/PID-integer.h:279: error: ISO C++ says that these
are ambiguous, even though the worst conversion for the first is
better than the worst conversion for the second:
../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const
Integer&, const Integer&)
../../gmp++/gmp++_int.h:126: note: candidate 2: int
Integer::operator>(long unsigned int) const
../../linbox/field/PID-integer.h:279: error: ISO C++ says that these
are ambiguous, even though the worst conversion for the first is
better than the worst conversion for the second:
../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const
Integer&, const Integer&)
../../gmp++/gmp++_int.h:125: note: candidate 2: int
Integer::operator>(long int) const
../../linbox/field/PID-integer.h:279: error: ISO C++ says that these
are ambiguous, even though the worst conversion for the first is
better than the worst conversion for the second:
../../gmp++/gmp++_int.inl:148: note: candidate 1: int operator>(const
Integer&, const Integer&)
../../gmp++/gmp++_int.h:124: note: candidate 2: int
Integer::operator>(int) const
make[3]: *** [lb-element.lo] Error 1
make[3]: Leaving directory `/tmp/Work2/linbox/linbox-r2798/interfaces/
driver'
```


Any ideas?

Cheers,

Michael

Issue created by migration from https://trac.sagemath.org/ticket/493





---

archive/issue_comments_002455.json:
```json
{
    "body": "Changing status from new to assigned.",
    "created_at": "2007-09-09T06:08:26Z",
    "issue": "https://github.com/sagemath/sagetest/issues/493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/493#issuecomment-2455",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Changing status from new to assigned.



---

archive/issue_comments_002456.json:
```json
{
    "body": "Resolution: fixed",
    "created_at": "2008-04-07T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/493#issuecomment-2456",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

Resolution: fixed



---

archive/issue_events_000524.json:
```json
{
    "actor": "mabshoff",
    "created_at": "2008-04-07T03:52:10Z",
    "event": "closed",
    "issue": "https://github.com/sagemath/sagetest/issues/493",
    "type": "issue_event",
    "url": "https://github.com/sagemath/sagetest/issues/493#event-524"
}
```



---

archive/issue_comments_002457.json:
```json
{
    "body": "This has been fixed in LinBox 1.1.5.\n\nCheers,\n\nMichael",
    "created_at": "2008-04-07T03:52:10Z",
    "issue": "https://github.com/sagemath/sagetest/issues/493",
    "type": "issue_comment",
    "url": "https://github.com/sagemath/sagetest/issues/493#issuecomment-2457",
    "user": "https://trac.sagemath.org/admin/accounts/users/mabshoff"
}
```

This has been fixed in LinBox 1.1.5.

Cheers,

Michael
