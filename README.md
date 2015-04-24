# Camel_SNAKE-kebab

[![Build Status](https://travis-ci.org/t6/camel_snake_kebab.svg?branch=master)](https://travis-ci.org/t6/camel_snake_kebab)

A Python library for word case conversions.

This library is a port of the
[Clojure library](https://github.com/qerub/camel-snake-kebab) with the
same name by @qerub.

It is available on PyPI and can be installed with

```bash
pip install --user camel_snake_kebab
```

It was tested with Python 2.7 and Python 3.4.

## Examples

```python
>>> from camel_snake_kebab import *
>>> CamelCase('flux-capacitor')
'FluxCapacitor'
>>> SCREAMING_SNAKE_CASE('I am constant')
'I_AM_CONSTANT'
>>> kebab_case('object_id')
'object-id'
>>> HTTP_Header_Case('x-ssl-cipher')
'X-SSL-Cipher'
>>> dot_case('JAVA_VERSION')
'java.version'
>>> Dot_Case('JAVA_VERSION')
'Java.Version'
```

## Available Conversion Functions

* `PascalCase` aka `CamelCase`
* `camelCase`
* `SCREAMING_SNAKE_CASE`
* `Snake_case`
* `snake_case`
* `kebab_case`
* `Camel_Snake_Case`
* `HTTP-Header-Case`
* `dot_case`
* `Dot_Case`

You should be able to figure out all what all of them do.

## Further Reading

See the homepage for the Clojure library at
https://github.com/qerub/camel-snake-kebab for more information.

## License

Copyright (C) 2015 Tobias Kortkamp
Copyright (C) 2012-2014 Christoffer Sawicki, ToBeReplaced & Brendan Bates

Distributed under the Eclipse Public License v1.0 (see
[epl-v10.html](epl-v10.html)).
