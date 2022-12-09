# SageMath: upstream projects

Per [Wikipedia](https://en.wikipedia.org/wiki/Upstream_(software_development)), in software development, "upstream" refers to a direction toward the original authors or maintainers of software.

See [Surveying the mathematical software landscape](https://trac.sagemath.org/wiki/WikiStart#Surveyingthemathematicalsoftwarelandscape)

## Upstream projects

  * Many of the [packages in the SageMath distribution](https://doc.sagemath.org/html/en/reference/spkg/) are upstream packages for the SageMath library.
  * Used for the infrastructure:
    * [Trac](https://trac.edgewall.org)
    * [Askbot](https://askbot.com)
    * [Google groups](https://groups.google.com/)
    * [GitHub](https://github.com/)
    * [MoinMoin](https://moinmo.in)

## Upgrading and updating upstream packages

  * See task ticket [#33774](https://trac.sagemath.org/ticket/33774)
  * The Fedora people have a useful tool to track upstream version changes: https://release-monitoring.org/
  * [repology: sagemath_develop](https://repology.org/projects/?search=&maintainer=&category=&inrepo=sagemath_develop&notinrepo=&repos=&families=&repos_newest=&families_newest=&outdated=on) has much broader coverage.

## Sage trac tickets about upgrades, updates, packages

Here are some useful trac queries (final "e" omitted on purpose to also get final "ing").

  * [summary contains upgrad](https://trac.sagemath.org/query?summary=~upgrad&desc=1&order=status)
  * [summary contains updat](https://trac.sagemath.org/query?summary=~updat&desc=1&order=status)
  * [summary contains upgrad or updat](https://trac.sagemath.org/query?summary=~upgrad&or&summary=~updat&desc=1&order=status)
  * [summary contains packag](https://trac.sagemath.org/query?summary=~packag&desc=1&order=status)
  * [summary contains "upgrad" or "updat" or "packag"](https://trac.sagemath.org/query?summary=~upgrad&or&summary=~updat&or&summary=~packag&desc=1&order=status)

