# -*- coding: utf-8 -*-
"""
feedgen.version
~~~~~~~~~~~~~~~

:copyright: 2013-2018, Lars Kiesow <lkiesow@uos.de>
:copyright: 2026, Fabio Manganiello <fabio@manganiello.tech>

:license: FreeBSD and LGPL, see license.* for more details.

"""

"Version of feedgen2 represented as tuple"
version = (2, 0, 0)


"Version of feedgen2 represented as string"
version_str = ".".join([str(x) for x in version])

version_major = version[:1]
version_minor = version[:2]
version_full = version

version_major_str = ".".join([str(x) for x in version_major])
version_minor_str = ".".join([str(x) for x in version_minor])
version_full_str = ".".join([str(x) for x in version_full])
