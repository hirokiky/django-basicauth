================
django-basicauth
================

Basic auth utilities for Django.

Requires
========

Tested under...

* Python

  * 3.6
  * 3.7
  * 3.8
  * 3.9

* Django

  * 2.2
  * 3.0
  * 3.1

Installation
============

::

    pip install django-basicauth


Usage
=====

.. code-block:: python

    from basicauth.decorators import basic_auth_required

    @basic_auth_required
    def myview(request):
        ...

or by a middleware.

.. code-block:: python

    MIDDLEWARE = (
        'basicauth.middleware.BasicAuthMiddleware',
        ...
    )


Basic Auth for specific requests only
-------------------------------------

To apply basic auth for specific requests,
Use ``target_test`` argument.

In the below code, anonymous users will be required Basic Auth
Authenticated users can pass it without `Basic ...` header.

.. code-block:: python

    from basicauth.decorators import basic_auth_required

    @basic_auth_required(
        target_test=lambda request: not request.user.is_authenticated
    )
    def myview(request):
        ...

``target_test`` accepts ``typing.Callable[[HttpRequest], bool]``,
and if the callable returns ``True``, Basic Auth will be required.

Applying decorator to CBVs
==========================

To apply ``@basic_auth_required`` decorator to Class Based Views,
use ``django.utils.decorators.method_decorator``.

.. code-block:: python

    from django.utils.decorators import method_decorator
    from basicauth.decorators import basic_auth_required

    @method_decorator(basic_auth_required, name='dispatch')
    class YourView(TemplateView):
        template_name = "my-template.html"

Settings
========

* ``BASICAUTH_USERS`` (required): Dictionary including keys as username and values as passwords.
* ``BASICAUTH_REALM``: realm string, default is "Secure resource".
* ``BASICAUTH_DISABLE``: Disable all of barriers by this library.
