# Issue 4293: reload(sage.combinat.crystals)

Issue created by migration from Trac.

Original creator: nthiery

Original creation time: 2008-10-15 11:30:51

Assignee: was

I would love to have the following feature:

  reload(sage.combinat.crystals)

which would triggers an immediate reload recursively of all the files within the sage.combinat.crystals module.

For my personal debugging cycle, this would be more practical than attach:
 - I don't mind having to ask for the reload; actually having control over when the files is reloaded
   would be safer
 - I often modify many  files in a given module simultaneously, and not having to specify each file
   separately is handy
 - I prefer to just specify a module name rather than a file name

Thanks in advance!
