# Issue 8594: allow printing of floating point numbers with locale-dependent decimal separators

Issue created by migration from https://trac.sagemath.org/ticket/8594

Original creator: ddrake

Original creation time: 2010-03-24 02:06:27

Assignee: was

Keywords: i18n

Some people would like floats to print with a comma for the decimal separator: 3,14159 for pi and so on. We should make this possible. Ideally Sage would check the user's locale or have a command to set the default printing style. Python seems to have a bit of support for this, maybe: http://docs.python.org/library/string.html#format-specification-mini-language

This ticket is prompted by http://groups.google.com/group/sage-support/browse_thread/thread/f2f2277a407b7d21 

More info: http://en.wikipedia.org/wiki/Decimal_separator

Since commas and dots are a very important part of Python syntax, I'm not sure we should try to change *input* of floating point numbers, but I think it's reasonable to have this support for output.


---

Comment by @Kreijstal created at 2021-06-21 19:30:36

Has this been solved? I have this issue too.
