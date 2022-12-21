# Issue 7653: Ensure that C++ libraries linked are ISO standard with commerical compilers

Issue created by migration from Trac.

Original creator: drkirkby

Original creation time: 2009-12-10 16:35:09

Assignee: GeorgSWeber

CC:  dimpase

Several C++ compilers from commercial vendors (Sun and HP being two examples I am aware of), created C++ libraries based on an older version of the C++ standard. This is incompatible with the current standard, so both HP and Sun ship two libraries - one for backward compatibility, the other which implements the last ISO standard, but at the expense of backward compatibility. 

In contrast, g++ only uses on library. 

Sun take their usual attitude of ensuring Solaris is backward compatible, so by default their C++ compiler uses a library which does not conform to the latest C++ standard. Alexander Dreyer has found that the magic switch to get Sun Studio to use the latest C++ library is 


```
-library=stlport4
```


Further details can be found on the Sun web site at 

http://developers.sun.com/solaris/articles/cmp_stlport_libCstd.html

Looking at the HP C++ compiler for HP-UX, I see that it too has two C++ libraries - one for backward compatibility, one for latest C++ conformance. 

http://docs.hp.com/en/14487/faq.htm

Like the Sun compiler, the HP compiler defaults to an older C++ library standard. The option to enable the latest standard is


```
-AA
```


In both cases, the same library must be used for all objects - you can't mix them. 

Hence at some point, all code in Sage that uses C++ must have the appropriate option to C++ compiler to use the latest libraries, if it is to be built with Sun Studio or any other compiler which ships with two libraries. 

I would invisage creating individual trac tickets for each package which uses C++. The sensible option it to add this flag to a CXXFLAGS and hope all packages respect CXXFLAGS. In practice, this will not happen, so many will require changes to ensure they do respect flags from a global CXX flags. 



---

Comment by mkoeppe created at 2020-04-25 02:55:44

Changing status from new to needs_review.


---

Comment by mkoeppe created at 2020-04-25 02:55:44

outdated, should be closed


---

Comment by dimpase created at 2020-04-26 08:31:56

Changing status from needs_review to positive_review.


---

Comment by chapoton created at 2020-05-31 12:30:59

Resolution: invalid
