# Issue 7515: Improved deprecation and renaming of function and methods.

Issue created by migration from Trac.

Original creator: hivert

Original creation time: 2009-11-22 17:19:12

Assignee: hivert

CC:  combinat

Keywords: deprecation:

Along the cleanup of combinat, a lot of methods and function get renamed. It is painfull to write backward compatibility aliases.
The patch given here should make it easier. I take also the chance to add a version optional argument to `deprecation` to store and print in which version of sage the method/function was deprecated.

Here is an excerpt from the doc:

```
        sage: from sage.misc.misc import deprecated_function_alias
        sage: g = deprecated_function_alias(number_of_partitions,
        ...     'Sage Version 42.132, Release Date: 5123-04-01')
        sage: g(5)
        doctest:1: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) g is deprecated. Please use number_of_partitions instead.
        7
```

This also works for methods:

```
        sage: from sage.misc.misc import deprecated_method_alias
        sage: class cls(object):
        ...      def new_meth(self): return 42
        ...      old_meth = deprecated_method_alias(new_meth,
        ...            'Sage Version 42.132, Release Date: 5123-04-01')
        sage: cls().old_meth()
        doctest:...: DeprecationWarning: (Since Sage Version 42.132, Release Date: 5123-04-01) old_meth is deprecated. Please use new_meth instead.
        42
```




---

Comment by hivert created at 2009-11-22 17:23:25

Changing status from new to needs_review.


---

Comment by hivert created at 2009-11-23 09:49:24

Adressed William comments on sage-devel.


---

Attachment

Updated patch to remark on sage-devel (i.e. just put the version of deprecation, without the date). Reday for review.


---

Comment by ncohen created at 2009-11-30 12:00:20

Changing status from needs_review to positive_review.


---

Comment by ncohen created at 2009-11-30 12:00:20

No problem with this one... Extremely useful :-)

Do you think one should create a ticket saying "replace all the deprecation warning using deprecated_function_alias whenever possible" ?

Firsdt, it would shorten Sage's code, plus everybody would see this is how we should set functions as deprecated instead of using the old method... I "copy" things very often in Sage's code, and if I am not working around an example of this, you can be sure I'd do it the other way :-)

Positive review, thanks for your work !

Nathann


---

Comment by hivert created at 2009-11-30 12:19:24

Replying to [comment:4 ncohen]:
> No problem with this one... Extremely useful :-)
> 
> Do you think one should create a ticket saying "replace all the deprecation warning using deprecated_function_alias whenever possible" ?

This would be surely a good idea, but I'm not sure I wan't to volunteer to do this one right now. There are a lot of deprecated things in sage. Here is a rough evaluation:

```
tomahawk-*/devel/sage-main $ grep deprecat **/*.py **/*.pyx | wc
   1228   13940  168762
```

So I'm opening the ticket but I currently don't accept it.

Cheers,

Florent


---

Comment by ncohen created at 2009-11-30 12:21:28

Perhaps it is possible to script it in emacs.... :-)


---

Comment by mhansen created at 2009-12-01 03:53:49

Looks good to me.


---

Comment by mhansen created at 2009-12-01 03:53:49

Resolution: fixed
