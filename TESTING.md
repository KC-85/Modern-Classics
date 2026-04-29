# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

This document records manual and automated validation carried out on the deployed application and the local test environment.

Testing focus areas:

- Core e-commerce flow (cart, checkout, payment state updates, order history)
- Access control (guest vs authenticated vs superuser behavior)
- SEO endpoints (robots and sitemap)
- Form validation and defensive behavior

## Code Validation

Validation was completed for project-owned code only (not third-party/vendor assets). Screenshots are referenced in the tables below.

### HTML

⚠️ INSTRUCTIONS ⚠️

1. [*recommended*] If you are using the live deployed site URLs, validate using this link: https://validator.w3.org/#validate_by_uri
2. Otherwise, if you are copying/pasting your HTML code manually, use this link: https://validator.w3.org/#validate_by_input

It's recommended to validate the live pages (all of them) using the deployed URL. This will give you a custom URL as well, which you can use below on your testing documentation. It makes it easier to return back to a page for validating it again in the future. The URL will look something like this:

- https://validator.w3.org/nu/?doc=https://KC-85.github.io/Modern-Classics/index.html

⚠️ --- END --- ⚠️

🛑 IMPORTANT 🛑

RE: Python/Jinja syntax in HTML

Python projects that use Jinja syntax, such as `{% for loops %}`, `{% url 'home' %}`, and `{{ variable|filter }}` will not validate properly if you're copying/pasting into the HTML validator.

In order to properly validate these types of files, it's recommended to [validate by uri](https://validator.w3.org/#validate_by_uri) from the deployed Heroku pages.

Unfortunately, pages that require a user to be "logged-in" and authenticated (CRUD functionality) will not work using this method, due to the fact that the HTML Validator (W3C) doesn't have access to login to an account on your project. In order to properly validate HTML pages with Jinja syntax for authenticated pages, follow these steps:

- Navigate to the deployed pages which require authentication.
- Right-click anywhere on the page, and select **View Page Source** (usually `CTRL+U` or `⌘+U` on Mac).
- This will display the entire "compiled" code, without any Jinja syntax.
- Copy everything, and use the [validate by input](https://validator.w3.org/#validate_by_input) method.
- Repeat this process for every page that requires a user to be logged-in/authenticated (e.g.: CRUD functionality).

🛑 ---- END --- 🛑

I have used the recommended [HTML W3C Validator](https://validator.w3.org) to validate all of my HTML files.



### CSS

⚠️ INSTRUCTIONS ⚠️

1. [*recommended*] If you are using the live deployed site, use this link: https://jigsaw.w3.org/css-validator/#validate_by_uri
2. If you are copying/pasting your CSS code, use this link: https://jigsaw.w3.org/css-validator/#validate_by_input

It's recommended to validate the live site for your primary CSS file on the deployed URL. This will give you a custom URL as well, which you can use below on your testing documentation. It makes it easier to return back to a page for validating it again in the future. The URL will look something like this:

- https://jigsaw.w3.org/css-validator/validator?uri=https://modern-classics-b10468fd6f55.herokuapp.com

If you have additional/multiple CSS files, then individual "[validation by input](https://jigsaw.w3.org/css-validator/#validate_by_input)" is recommended for the extra CSS files.

**IMPORTANT**: Third-Party tools

If you're using external libraries/frameworks (e.g: Bootstrap, Materialize, Font Awesome, etc.), then sometimes the tool will attempt to also validate these, even though it's not part of your own actual code that you wrote. You are not required to validate the external libraries or frameworks!

⚠️ --- END --- ⚠️

I have used the recommended [CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator) to validate all of my CSS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| static | [hero.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/components/hero.css) | Link (if applicable) | ![screenshot](documentation/validation/css/css-carousel-hero.png) | Notes (if applicable) |
| static | [main.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/main.css) | Link (if applicable) | ![screenshot](documentation/validation//css/css-main.png) | Notes (if applicable) |
| static | [checkout.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/pages/checkout.css) | Link (if applicable) | ![screenshot](documentation/validation/css/css-checkout.png) | Notes (if applicable) |
| static | [showroom.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/pages/showroom.css) | Link (if applicable) | ![screenshot](documentation/validation/css/css-showroom.png) | Notes (if applicable) |


### JavaScript

⚠️ INSTRUCTIONS ⚠️

If using modern JavaScript (ES6) methods, then make sure to include the following line at the very top of every single JavaScript file in your project (this should remain in your files for submission as well):

`/* jshint esversion: 11 */`

If you are also including jQuery (`$`), then the updated format will be:

`/* jshint esversion: 11, jquery: true */`

This allows the JShint validator to recognize modern ES6 methods, such as: `let`, `const`, `template literals`, `arrow functions (=>)`, etc.

**IMPORTANT**: External resources

Sometimes we'll write JavaScript that imports variables from other files, such as "an array of questions" from `questions.js`, which are used within the main `script.js` file elsewhere. If that's the case, the JShint validation tool doesn't know how to recognize "unused variables" that would normally be imported locally when running your own project. These warnings are acceptable, so showcase on your screenshot(s).

The same thing applies when using external libraries such as Stripe, Leaflet, Bootstrap, Materialize, etc. To instantiate these components, we need to use their respective declarator. Again, the JShint validation tool would flag these as "undefined/unused variables". These warnings are acceptable, so showcase on your screenshot(s).

⚠️ --- END --- ⚠️

I have used the recommended [JShint Validator](https://jshint.com) to validate all of my JS files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
|  | [babel.config.js](https://github.com/KC-85/Modern-Classics/blob/main/babel.config.js) |  | ![screenshot](documentation/validation/js--babel.config.png) | ⚠️ Notes (if applicable) |
|  | [jest.config.js](https://github.com/KC-85/Modern-Classics/blob/main/jest.config.js) |  | ![screenshot](documentation/validation/js--jest.config.png) | ⚠️ Notes (if applicable) |
| static | [cartBadge.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/components/cartBadge.js) |  | ![screenshot](documentation/validation/js/static-cartBadge.png) | ⚠️ Notes (if applicable) |
| static | [main.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/main.js) |  | ![screenshot](documentation/validation/js/static-main.png) | ⚠️ Notes (if applicable) |
| static | [carDetail.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/carDetail.js) |  | ![screenshot](documentation/validation/js/static-carDetail.png) | ⚠️ Notes (if applicable) |
| static | [hero.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/hero.js) |  | ![screenshot](documentation/validation/js/static-hero.png) | ⚠️ Notes (if applicable) |
| static | [showroom.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/showroom.js) |  | ![screenshot](documentation/validation/js/static-showroom.png) | ⚠️ Notes (if applicable) |
| static | [cartService.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/services/cartService.js) |  | ![screenshot](documentation/validation/js/static-cartService.png) | ⚠️ Notes (if applicable) |
| static | [csrf.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/utils/csrf.js) |  | ![screenshot](documentation/validation/js/static-csrf.png) | ⚠️ Notes (if applicable) |
| static | [dom.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/utils/dom.js) |  | ![screenshot](documentation/validation/js/static-dom.png) | ⚠️ Notes (if applicable) |
| static | [cardetail.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/cardetail.test.js) |  | ![screenshot](documentation/validation/js/static-cardetail.test.png) | ⚠️ Notes (if applicable) |
| static | [cartbadge.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/cartbadge.test.js) |  | ![screenshot](documentation/validation/js/static-cartbadge.test.png) | ⚠️ Notes (if applicable) |
| static | [cartservice.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/cartservice.test.js) |  | ![screenshot](documentation/validation/js/static-cartservice.test.png) | ⚠️ Notes (if applicable) |
| static | [csrf.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/csrf.test.js) |  | ![screenshot](documentation/validation/js/static-csrf.test.png) | ⚠️ Notes (if applicable) |
| static | [dom.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/dom.test.js) |  | ![screenshot](documentation/validation/js/static-dom.test.png) | ⚠️ Notes (if applicable) |
| static | [hero.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/hero.test.js) |  | ![screenshot](documentation/validation/js/static-hero.test.png) | ⚠️ Notes (if applicable) |
| static | [main.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/main.test.js) |  | ![screenshot](documentation/validation/js/static-main.test.png) | ⚠️ Notes (if applicable) |
| static | [showroom.test.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js_tests/showroom.test.js) |  | ![screenshot](documentation/validation/js/static-showroom.test.png) | ⚠️ Notes (if applicable) |


### Python

🛑 IMPORTANT 🛑

**IMPORTANT**: Django settings

The Django `settings.py` file comes with 4 lines that are quite long, and will throw the `E501 line too long` error. This is default behavior, but can be fixed by adding the "`  # noqa`" comment at the end of those lines.

```python
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",  # noqa
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",  # noqa
    },
]
```

**IMPORTANT**: *migration* and *pycache* files

You do not have to validate files from the `migrations/` or `pycache/` folders! Ignore these `.py` files, and validate just the files that you've created or modified.

🛑 --- END --- 🛑

I have used the recommended [PEP8 CI Python Linter](https://pep8ci.herokuapp.com) to validate all of my Python files.

| Directory | File | URL | Screenshot | Notes |
| --- | --- | --- | --- | --- |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/admin.py) | ![screenshot](documentation/validation//python/py-apps-user-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/forms.py) | ![screenshot](documentation/validation//python/py-apps-user-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/models.py) | ![screenshot](documentation/validation/python/py-apps-user-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/urls.py) | ![screenshot](documentation/validation/python/py-apps-user-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/views.py) | ![screenshot](documentation/validation/python/py-apps-user-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/admin.py) | ![screenshot](documentation/validation/python/py-apps-checkout-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/forms.py) | ![screenshot](documentation/validation/python/py-apps-checkout-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/models.py) | ![screenshot](documentation/validation//python/py-apps-checkout-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/urls.py) | ![screenshot](documentation/validation/python/py-apps-checkout-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/views.py) | ![screenshot](documentation/validation/python/py-apps-checkout-views.png) | Notes (if applicable) |
| apps | [utils.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/utils.py) | ![screenshot](documentation/validation/python/py-apps-checkout-utils.png) | Notes (if applicable) |
| apps | [webhook_handler.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/webhook_handler.py) | ![screenshot](documentation/validation/python/py-apps-checkout-wh-handler.png) | Notes (if applicable) |
| apps | [webhooks.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/checkout/webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/checkout/webhooks.py) | ![screenshot](documentation/validation/python/py-apps-checkout-webhooks.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/admin.py) | ![screenshot](documentation/validation/python/py-apps-common-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/forms.py) | ![screenshot](documentation/validation/python/py-apps-common-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/models.py) | ![screenshot](documentation/validation/python/py-apps-common-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/urls.py) | ![screenshot](documentation/validation/python/py-apps-common-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/views.py) | ![screenshot](documentation/validation/python/py-apps-common-views.png) | Notes (if applicable) |
| apps | [auth_mixins.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/auth_mixins.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/auth_mixins.py) | ![screenshot](documentation/validation/python/py-apps-common-authmixins.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/admin.py) | ![screenshot](documentation/validation/python/py-apps-showroom-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/forms.py) | ![screenshot](documentation/validation/python/py-apps-showroom-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/models.py) | ![screenshot](documentation/validation/python/py-apps-showroom-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/urls.py) | ![screenshot](documentation/validation/python/py-apps-showroom-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/views.py) | ![screenshot](documentation/validation/python/py-apps-showroom-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/admin.py) | ![screenshot](documentation/validation/python/py-apps-trailer-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/forms.py) | ![screenshot](documentation/validation/python/py-apps-trailer-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/models.py) | ![screenshot](documentation/validation/python/py-apps-trailer-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/urls.py) | ![screenshot](documentation/validation/python/py-apps-trailer-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/views.py) | ![screenshot](documentation/validation/python/py-apps-trailer-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/admin.py) | ![screenshot](documentation/validation/python/py-apps-delivery-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/forms.py) | ![screenshot](documentation/validation/python/py-apps-delivery-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/models.py) | ![screenshot](documentation/validation/python/py-apps-delivery-models.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/urls.py) | ![screenshot](documentation/validation/python/py-apps-delivery-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/views.py) | ![screenshot](documentation/validation/python/py-apps-delivery-views.png) | Notes (if applicable) |
| core | [settings.py](https://github.com/KC-85/Modern-Classics/blob/main/core/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/core/settings.py) | ![screenshot](documentation/validation/python/py-core-settings.png) | Notes (if applicable) |
| core | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/core/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/core/urls.py) | ![screenshot](documentation/validation/python/py-core-urls.png) | Notes (if applicable) |
| core | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/core/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/core/views.py) | ![screenshot](documentation/validation/python/py-core-views.png) | Notes (if applicable) |
|  | [manage.py](https://github.com/KC-85/Modern-Classics/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/manage.py) | ![screenshot](documentation/validation/python/py--manage.png) | Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_utils.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_utils.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_utils.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_utils.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_webhook_handler.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_webhook_handler.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_webhook_handler.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_webhook_handler.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_webhooks.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/checkout/test_webhooks.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/checkout/test_webhooks.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_webhooks.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/common/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/common/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views-common.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/delivery/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/delivery/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views-delivery.png) | ⚠️ Notes (if applicable) |
| unit_tests | [helper.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/helper.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/helper.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_helper.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/showroom/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/showroom/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views-showroom.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/trailer/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/trailer/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views-trailer.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_admin.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_admin.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_admin-users.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_apps.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_apps.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_apps.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_apps-users.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_forms.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_forms.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_forms-users.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_models.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_models.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_models-users.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_urls.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_urls.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_urls-users.png) | ⚠️ Notes (if applicable) |
| unit_tests | [test_views.py](https://github.com/KC-85/Modern-Classics/blob/main/unit_tests/users/test_views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/unit_tests/users/test_views.py) | ![screenshot](documentation/validation/python/py-unit_tests-test_views-users.png) | ⚠️ Notes (if applicable) |


## Responsiveness

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Hero | ![screenshot](documentation/responsiveness/mobile-hero.png) | ![screenshot](documentation/responsiveness/tablet-hero.png) | ![screenshot](documentation/responsiveness/desktop-hero.png) | Works as expected |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Showroom | ![screenshot](documentation/responsiveness/mobile-showroom.png) | ![screenshot](documentation/responsiveness/tablet-showroom.png) | ![screenshot](documentation/responsiveness/desktop-showroom.png) | Works as expected |
| Car Details | ![screenshot](documentation/responsiveness/mobile-car-details.png) | ![screenshot](documentation/responsiveness/tablet-car-details.png) | ![screenshot](documentation/responsiveness/desktop-car-details.png) | Works as expected |
| Cart | ![screenshot](documentation/responsiveness/mobile-cart.png) | ![screenshot](documentation/responsiveness/tablet-cart.png) | ![screenshot](documentation/responsiveness/desktop-cart.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Car | ![screenshot](documentation/responsiveness/mobile-add-car.png) | ![screenshot](documentation/responsiveness/tablet-add-car.png) | ![screenshot](documentation/responsiveness/desktop-add-car.png) | Works as expected |
| Edit Car | ![screenshot](documentation/responsiveness/mobile-edit-car.png) | ![screenshot](documentation/responsiveness/tablet-edit-car.png) | ![screenshot](documentation/responsiveness/desktop-edit-car.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/brave-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/brave-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/brave-profile.png) | Works as expected |
| Showroom | ![screenshot](documentation/browsers/chrome-showroom.png) | ![screenshot](documentation/browsers/firefox-showroom.png) | ![screenshot](documentation/browsers/brave-showroom.png) | Works as expected |
| Car Details | ![screenshot](documentation/browsers/chrome-car-details.png) | ![screenshot](documentation/browsers/firefox-car-details.png) | ![screenshot](documentation/browsers/brave-car-details.png) | Works as expected |
| Cart | ![screenshot](documentation/browsers/chrome-cart.png) | ![screenshot](documentation/browsers/firefox-cart.png) | ![screenshot](documentation/browsers/brave-cart.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/brave-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/brave-checkout-success.png) | Works as expected |
| Add car | ![screenshot](documentation/browsers/chrome-add-car.png) | ![screenshot](documentation/browsers/firefox-add-car.png) | ![screenshot](documentation/browsers/brave-add-car.png) | Works as expected |
| Edit Car | ![screenshot](documentation/browsers/chrome-edit-car.png) | ![screenshot](documentation/browsers/firefox-edit-car.png) | ![screenshot](documentation/browsers/brave-edit-car.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/firefox-newsletter.png) | ![screenshot](documentation/browsers/brave-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/brave-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/brave-404.png) | Works as expected |

## Lighthouse Audit

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Showroom | ![screenshot](documentation/lighthouse/mobile-showroom.png) | ![screenshot](documentation/lighthouse/desktop-showroom.png) |
| Car Detail | ![screenshot](documentation/lighthouse/mobile-car-detail.png) | ![screenshot](documentation/lighthouse/desktop-car-detail.png) |
| Cart | ![screenshot](documentation/lighthouse/mobile-cart.png) | ![screenshot](documentation/lighthouse/desktop-cart.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Car | ![screenshot](documentation/lighthouse/mobile-add-car.png) | ![screenshot](documentation/lighthouse/desktop-add-car.png) |
| Edit Car | ![screenshot](documentation/lighthouse/mobile-edit-car.png) | ![screenshot](documentation/lighthouse/desktop-edit-car.png) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Cars | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/cars.png) |
| Sorting| Feature is expected to sort products by price . | Tested sorting options for price (low-to-high/high-to-low). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| Filtering | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| Product Details | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Add to Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| Manage Cart | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| Stripe Payment| Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| Order Confirmation | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| Saved Address | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/admin-add-car.png) |
| Admin Features | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/admin-edit-car.png) |
| Admin Features | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/admin-delete-car.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can browse freely before deciding to create an account. | ![screenshot](documentation/features/us01.png) |
| As a guest user | I would like to be prompted to create an account or log in at add to cart | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/us02.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/us03.png) |
| As a customer | I would like to browse various product categories (make, model etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/us04.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low/newest) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/us05.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/us06.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/us07.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/us08.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/us09.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/us10.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/us11.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/us12.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/us13.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/us14.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/us15.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/us16.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/us17.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/us18.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/us19.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/us20.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/us21.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

I used Django's built-in test runner and the app-level unit test suites in [unit_tests](unit_tests/).

Primary command used during this assessment phase:

- `python3 manage.py test`

Current result:

- Full suite passes locally (`Exit Code: 0`) after Tier 1 to Tier 4 fixes.
- Key regressions were added around checkout payment status transitions, webhook idempotency, delivery-option access control, and navigation discoverability.

Coverage reporting commands used:

- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,manage.py -m django test`
- `coverage report`
- `coverage html`

Below are the latest coverage artifacts:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

- Initial environment issue: virtual environment created with Python 3.14 caused dependency install failures (notably psycopg2 wheel/build path).
- Resolution: recreated virtual environment with Python 3.12 (matching [.python-version](.python-version)), reinstalled requirements, reran suite successfully.
- One test expectation update was required after payment and access-control hardening: denial responses can be `302` or `403` depending on decorator/redirect behavior.

## Bugs

Bug tracking is managed through [GitHub Issues](https://www.github.com/KC-85/Modern-Classics/issues) using labels and close-state history for reproducible audit trails.

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AKC-85%2FModern-Classics%20label%3Abug&label=bugs)](https://www.github.com/KC-85/Modern-Classics/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/KC-85/Modern-Classics/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/KC-85/Modern-Classics/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

[![GitHub issues](https://img.shields.io/github/issues/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics/issues)

Any remaining open issues can be tracked [here](https://www.github.com/KC-85/Modern-Classics/issues).

![screenshot](documentation/bugs/gh-issues-open.png)

### Known Issues

| Issue | Screenshot |
| --- | --- |
| On devices smaller than 375px, the page starts to have horizontal `overflow-x` scrolling. | ![screenshot](documentation/issues/overflow.png) |
| When validating HTML with a semantic `<section>` element, the validator warns about lacking a header `h2-h6`. This is acceptable. | ![screenshot](documentation/issues/section-header.png) |
| Validation errors on "signup.html" coming from the Django Allauth package. | ![screenshot](documentation/issues/allauth.png) |
| With a known order-number, users can brute-force "checkout_success.html" and see potentially sensitive information. | ![screenshot](documentation/issues/checkout-success.png) |
| If a product is in your bag/cart, but then gets deleted from the database, it throws errors from the session storage memory. | ![screenshot](documentation/issues/session-storage.png) |


> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

