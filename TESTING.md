# Testing

> [!NOTE]
> Return back to the [README.md](README.md) file.

⚠️ INSTRUCTIONS ⚠️

In the following sections, you need to convince the assessors that you have conducted enough manual testing to legitimately believe that the site works well. Essentially, in this part, you should go over all of your project's features, and ensure that they all work as intended, with the project providing an easy and straightforward way for the users to achieve their goals.

⚠️ --- END --- ⚠️

## Code Validation

⚠️ INSTRUCTIONS ⚠️

Use the space below to discuss code validation for all of your own code files (*where applicable*). You are not required to validate external libraries/frameworks.

**MANDATORY**: You must provide a screenshot for each file you validate.

**PRO TIP**: Where possible, always validate the live URL pages/files, not your local code using copy/paste. There could be subtle/hidden differences.

⚠️ --- END --- ⚠️

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
| static | [carousel.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/components/carousel.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-carousel.png) | Notes (if applicable) |
| static | [cartBadge.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/components/cartBadge.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-cartBadge.png) | Notes (if applicable) |
| static | [filterPanel.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/components/filterPanel.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-filterPanel.png) | Notes (if applicable) |
| static | [main.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/main.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-main.png) | Notes (if applicable) |
| static | [checkout.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/pages/checkout.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-checkout.png) | Notes (if applicable) |
| static | [showroom.css](https://github.com/KC-85/Modern-Classics/blob/main/static/css/pages/showroom.css) | Link (if applicable) | ![screenshot](documentation/validation/css-static-showroom.png) | Notes (if applicable) |


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
| static | [carousel.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/components/carousel.js) | N/A | ![screenshot](documentation/validation/js-static-carousel.png) | Notes (if applicable) |
| static | [cartBadge.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/components/cartBadge.js) | N/A | ![screenshot](documentation/validation/js-static-cartBadge.png) | Notes (if applicable) |
| static | [filterPanel.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/components/filterPanel.js) | N/A | ![screenshot](documentation/validation/js-static-filterPanel.png) | Notes (if applicable) |
| static | [main.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/main.js) | N/A | ![screenshot](documentation/validation/js-static-main.png) | Notes (if applicable) |
| static | [carDetail.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/carDetail.js) | N/A | ![screenshot](documentation/validation/js-static-carDetail.png) | Notes (if applicable) |
| static | [checkout.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/checkout.js) | N/A | ![screenshot](documentation/validation/js-static-checkout.png) | Notes (if applicable) |
| static | [showroom.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/pages/showroom.js) | N/A | ![screenshot](documentation/validation/js-static-showroom.png) | Notes (if applicable) |
| static | [cartService.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/services/cartService.js) | N/A | ![screenshot](documentation/validation/js-static-cartService.png) | Notes (if applicable) |
| static | [orderService.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/services/orderService.js) | N/A | ![screenshot](documentation/validation/js-static-orderService.png) | Notes (if applicable) |
| static | [userService.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/services/userService.js) | N/A | ![screenshot](documentation/validation/js-static-userService.png) | Notes (if applicable) |
| static | [csrf.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/utils/csrf.js) | N/A | ![screenshot](documentation/validation/js-static-csrf.png) | Notes (if applicable) |
| static | [dom.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/utils/dom.js) | N/A | ![screenshot](documentation/validation/js-static-dom.png) | Notes (if applicable) |
| static | [events.js](https://github.com/KC-85/Modern-Classics/blob/main/static/js/utils/events.js) | N/A | ![screenshot](documentation/validation/js-static-events.png) | Notes (if applicable) |


### Python

⚠️ INSTRUCTIONS ⚠️

The [CI Python Linter](https://pep8ci.herokuapp.com) can be used two different ways.

- Copy/Paste your Python code directly into the linter.
- As an API, using the "raw" URL appended to the linter URL.
    - To find the "raw" URL, navigate to your file directly on the GitHub repo.
    - On that page, GitHub provides a button on the right called "Raw" that you can click.
    - From that new page, copy the full URL, and paste it after the CI Python Linter URL (with a `/` separator).

It's recommended to validate each file using the API URL. This will give you a custom URL which you can use on your testing documentation. It makes it easier to return back to a file for validating it again in the future. Use the steps above to generate your own custom URLs for each Python file.

**IMPORTANT**: `E501 line too long` errors

You must strive to fix all Python lines that are too long (>80 characters). In rare cases where you cannot break the lines [*without breaking the functionality*], adding "`  # noqa`" (*NO Quality Assurance*) to the end of those lines will ignore linting validation. Do not use "`  # noqa`" all over your project just to clear down validation errors! This can still cause a project to fail, for failing to fix actual PEP8 validation errors.

Sometimes variables can get too long, or excessive `if/else` conditional statements. These are acceptable instances to use the "`  # noqa`" comment.

When trying to fix "line too long" errors, try to avoid using `/` to split lines. A better approach would be to use any type of opening bracket, and hit `<Enter>` just after that. Any opening bracket type will work: `(`, `[`, `{`. By using an opening bracket, Python knows where to appropriately indent the next line of code, without having to *guess* for yourself and attempt to "tab" to the correct indentation level.

⚠️ --- END --- ⚠️

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
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/common/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/common/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/delivery/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/delivery/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/orders/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/orders/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/showroom/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/showroom/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/trailer/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/trailer/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| apps | [admin.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/admin.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/admin.py) | ![screenshot](documentation/validation/py-apps-admin.png) | Notes (if applicable) |
| apps | [forms.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/forms.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/forms.py) | ![screenshot](documentation/validation/py-apps-forms.png) | Notes (if applicable) |
| apps | [models.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/models.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/models.py) | ![screenshot](documentation/validation/py-apps-models.png) | Notes (if applicable) |
| apps | [serializers.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/serializers.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/serializers.py) | ![screenshot](documentation/validation/py-apps-serializers.png) | Notes (if applicable) |
| apps | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/urls.py) | ![screenshot](documentation/validation/py-apps-urls.png) | Notes (if applicable) |
| apps | [views.py](https://github.com/KC-85/Modern-Classics/blob/main/apps/users/views.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/apps/users/views.py) | ![screenshot](documentation/validation/py-apps-views.png) | Notes (if applicable) |
| core | [settings.py](https://github.com/KC-85/Modern-Classics/blob/main/core/settings.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/core/settings.py) | ![screenshot](documentation/validation/py-core-settings.png) | Notes (if applicable) |
| core | [urls.py](https://github.com/KC-85/Modern-Classics/blob/main/core/urls.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/core/urls.py) | ![screenshot](documentation/validation/py-core-urls.png) | Notes (if applicable) |
|  | [manage.py](https://github.com/KC-85/Modern-Classics/blob/main/manage.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/manage.py) | ![screenshot](documentation/validation/py--manage.png) | Notes (if applicable) |
| scripts | [import_test_data.py](https://github.com/KC-85/Modern-Classics/blob/main/scripts/import_test_data.py) | [PEP8 CI Link](https://pep8ci.herokuapp.com/https://raw.githubusercontent.com/KC-85/Modern-Classics/main/scripts/import_test_data.py) | ![screenshot](documentation/validation/py-scripts-import_test_data.png) | Notes (if applicable) |


## Responsiveness

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various device sizes.

The minimum requirement is to test the following 3 sizes:

- Mobile
- Tablet
- Desktop

**IMPORTANT**: You must provide screenshots of your results, to "prove" that you've actually tested them.

Using the [amiresponsive](http://ami.responsivedesign.is) mockup images (*or similar*) does not meet the requirements. Consider using some of the built-in device sizes from the Developer Tools.

If you have tested the project on your actual mobile phone or tablet, consider also including screenshots of these as well. It showcases a higher level of manual tests, and can be seen as a positive inclusion!

⚠️ --- END --- ⚠️

I've tested my deployed project to check for responsiveness issues.

| Page | Mobile | Tablet | Desktop | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/responsiveness/mobile-register.png) | ![screenshot](documentation/responsiveness/tablet-register.png) | ![screenshot](documentation/responsiveness/desktop-register.png) | Works as expected |
| Login | ![screenshot](documentation/responsiveness/mobile-login.png) | ![screenshot](documentation/responsiveness/tablet-login.png) | ![screenshot](documentation/responsiveness/desktop-login.png) | Works as expected |
| Profile | ![screenshot](documentation/responsiveness/mobile-profile.png) | ![screenshot](documentation/responsiveness/tablet-profile.png) | ![screenshot](documentation/responsiveness/desktop-profile.png) | Works as expected |
| Home | ![screenshot](documentation/responsiveness/mobile-home.png) | ![screenshot](documentation/responsiveness/tablet-home.png) | ![screenshot](documentation/responsiveness/desktop-home.png) | Works as expected |
| Products | ![screenshot](documentation/responsiveness/mobile-products.png) | ![screenshot](documentation/responsiveness/tablet-products.png) | ![screenshot](documentation/responsiveness/desktop-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/responsiveness/mobile-product-details.png) | ![screenshot](documentation/responsiveness/tablet-product-details.png) | ![screenshot](documentation/responsiveness/desktop-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/responsiveness/mobile-bag.png) | ![screenshot](documentation/responsiveness/tablet-bag.png) | ![screenshot](documentation/responsiveness/desktop-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/responsiveness/mobile-checkout.png) | ![screenshot](documentation/responsiveness/tablet-checkout.png) | ![screenshot](documentation/responsiveness/desktop-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/responsiveness/mobile-checkout-success.png) | ![screenshot](documentation/responsiveness/tablet-checkout-success.png) | ![screenshot](documentation/responsiveness/desktop-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/responsiveness/mobile-add-product.png) | ![screenshot](documentation/responsiveness/tablet-add-product.png) | ![screenshot](documentation/responsiveness/desktop-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/responsiveness/mobile-edit-product.png) | ![screenshot](documentation/responsiveness/tablet-edit-product.png) | ![screenshot](documentation/responsiveness/desktop-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/responsiveness/mobile-newsletter.png) | ![screenshot](documentation/responsiveness/tablet-newsletter.png) | ![screenshot](documentation/responsiveness/desktop-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/responsiveness/mobile-contact.png) | ![screenshot](documentation/responsiveness/tablet-contact.png) | ![screenshot](documentation/responsiveness/desktop-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/responsiveness/mobile-404.png) | ![screenshot](documentation/responsiveness/tablet-404.png) | ![screenshot](documentation/responsiveness/desktop-404.png) | Works as expected |

## Browser Compatibility

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site on various browsers. Consider testing at least 3 different browsers, if available on your system. You DO NOT need to use all of the browsers below, just pick any 3 (minimum).

Recommended browsers to consider:
- [Chrome](https://www.google.com/chrome)
- [Firefox (Developer Edition)](https://www.mozilla.org/firefox/developer)
- [Edge](https://www.microsoft.com/edge)
- [Safari](https://support.apple.com/downloads/safari)
- [Brave](https://brave.com/download)
- [Opera](https://www.opera.com/download)

**IMPORTANT**: You must provide screenshots of the browsers you've tested, to "prove" that you've actually tested them.

Please note, there are services out there that can test multiple browser compatibilities at the same time. Some of these are paid services, but some are free. If you use these, you must provide a link to the source used for attribution, and multiple screenshots of the results.

⚠️ --- END --- ⚠️

I've tested my deployed project on multiple browsers to check for compatibility issues.

| Page | Chrome | Firefox | Safari | Notes |
| --- | --- | --- | --- | --- |
| Register | ![screenshot](documentation/browsers/chrome-register.png) | ![screenshot](documentation/browsers/firefox-register.png) | ![screenshot](documentation/browsers/safari-register.png) | Works as expected |
| Login | ![screenshot](documentation/browsers/chrome-login.png) | ![screenshot](documentation/browsers/firefox-login.png) | ![screenshot](documentation/browsers/safari-login.png) | Works as expected |
| Profile | ![screenshot](documentation/browsers/chrome-profile.png) | ![screenshot](documentation/browsers/firefox-profile.png) | ![screenshot](documentation/browsers/safari-profile.png) | Works as expected |
| Home | ![screenshot](documentation/browsers/chrome-home.png) | ![screenshot](documentation/browsers/firefox-home.png) | ![screenshot](documentation/browsers/safari-home.png) | Works as expected |
| Products | ![screenshot](documentation/browsers/chrome-products.png) | ![screenshot](documentation/browsers/firefox-products.png) | ![screenshot](documentation/browsers/safari-products.png) | Works as expected |
| Product Details | ![screenshot](documentation/browsers/chrome-product-details.png) | ![screenshot](documentation/browsers/firefox-product-details.png) | ![screenshot](documentation/browsers/safari-product-details.png) | Works as expected |
| Bag | ![screenshot](documentation/browsers/chrome-bag.png) | ![screenshot](documentation/browsers/firefox-bag.png) | ![screenshot](documentation/browsers/safari-bag.png) | Works as expected |
| Checkout | ![screenshot](documentation/browsers/chrome-checkout.png) | ![screenshot](documentation/browsers/firefox-checkout.png) | ![screenshot](documentation/browsers/safari-checkout.png) | Works as expected |
| Checkout Success | ![screenshot](documentation/browsers/chrome-checkout-success.png) | ![screenshot](documentation/browsers/firefox-checkout-success.png) | ![screenshot](documentation/browsers/safari-checkout-success.png) | Works as expected |
| Add Product | ![screenshot](documentation/browsers/chrome-add-product.png) | ![screenshot](documentation/browsers/firefox-add-product.png) | ![screenshot](documentation/browsers/safari-add-product.png) | Works as expected |
| Edit Product | ![screenshot](documentation/browsers/chrome-edit-product.png) | ![screenshot](documentation/browsers/firefox-edit-product.png) | ![screenshot](documentation/browsers/safari-edit-product.png) | Works as expected |
| Newsletter | ![screenshot](documentation/browsers/chrome-newsletter.png) | ![screenshot](documentation/browsers/firefox-newsletter.png) | ![screenshot](documentation/browsers/safari-newsletter.png) | Works as expected |
| Contact | ![screenshot](documentation/browsers/chrome-contact.png) | ![screenshot](documentation/browsers/firefox-contact.png) | ![screenshot](documentation/browsers/safari-contact.png) | Works as expected |
| 404 | ![screenshot](documentation/browsers/chrome-404.png) | ![screenshot](documentation/browsers/firefox-404.png) | ![screenshot](documentation/browsers/safari-404.png) | Works as expected |

## Lighthouse Audit

⚠️ INSTRUCTIONS ⚠️

Use this space to discuss testing the live/deployed site's Lighthouse Audit reports. Avoid testing the local version (Gitpod/VSCode/etc.), as this can have knock-on effects for performance. If you don't have "Lighthouse" in your Developer Tools, it can be added as an [extension](https://chrome.google.com/webstore/detail/lighthouse/blipmdconlkpinefehnmjammfjpmpbjk).

Unless your project is a single-page application (SPA), you should test Lighthouse Audit results for all of your pages, for both *mobile* and *desktop*.

**IMPORTANT**: You must provide screenshots of the results, to "prove" that you've actually tested them.

⚠️ --- END --- ⚠️

I've tested my deployed project using the Lighthouse Audit tool to check for any major issues. Some warnings are outside of my control, and mobile results tend to be lower than desktop.

| Page | Mobile | Desktop |
| --- | --- | --- |
| Register | ![screenshot](documentation/lighthouse/mobile-register.png) | ![screenshot](documentation/lighthouse/desktop-register.png) |
| Login | ![screenshot](documentation/lighthouse/mobile-login.png) | ![screenshot](documentation/lighthouse/desktop-login.png) |
| Profile | ![screenshot](documentation/lighthouse/mobile-profile.png) | ![screenshot](documentation/lighthouse/desktop-profile.png) |
| Home | ![screenshot](documentation/lighthouse/mobile-home.png) | ![screenshot](documentation/lighthouse/desktop-home.png) |
| Products | ![screenshot](documentation/lighthouse/mobile-products.png) | ![screenshot](documentation/lighthouse/desktop-products.png) |
| Product Details | ![screenshot](documentation/lighthouse/mobile-product-details.png) | ![screenshot](documentation/lighthouse/desktop-product-details.png) |
| Bag | ![screenshot](documentation/lighthouse/mobile-bag.png) | ![screenshot](documentation/lighthouse/desktop-bag.png) |
| Checkout | ![screenshot](documentation/lighthouse/mobile-checkout.png) | ![screenshot](documentation/lighthouse/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/lighthouse/mobile-checkout-success.png) | ![screenshot](documentation/lighthouse/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/lighthouse/mobile-add-product.png) | ![screenshot](documentation/lighthouse/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/lighthouse/mobile-edit-product.png) | ![screenshot](documentation/lighthouse/desktop-edit-product.png) |
| Newsletter | ![screenshot](documentation/lighthouse/mobile-newsletter.png) | ![screenshot](documentation/lighthouse/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/lighthouse/mobile-contact.png) | ![screenshot](documentation/lighthouse/desktop-contact.png) |
| 404 | ![screenshot](documentation/lighthouse/mobile-404.png) | ![screenshot](documentation/lighthouse/desktop-404.png) |

## Defensive Programming

⚠️ INSTRUCTIONS ⚠️

Defensive programming (defensive design) is extremely important! When building projects that accept user inputs or forms, you should always test the level of security for each form field. Examples of this could include (but not limited to):

All Projects:

- Users cannot submit an empty form (add the `required` attribute)
- Users must enter valid field types (ensure the correct input `type=""` is used)
- Users cannot brute-force a URL to navigate to a restricted pages

Python Projects:

- Users cannot perform CRUD functionality if not authenticated (if login functionality exists)
- User-A should not be able to manipulate data belonging to User-B, or vice versa
- Non-Authenticated users should not be able to access pages that require authentication
- Standard users should not be able to access pages intended for superusers/admins

You'll want to test all functionality on your application, whether it's a standard form, or CRUD functionality, for data manipulation on a database. Try to access various pages on your site as different user types (User-A, User-B, guest user, admin, superuser). You should include any manual tests performed, and the expected results/outcome.

Testing should be replicable (can someone else replicate the same outcome?). Ideally, tests cases should focus on each individual section of every page on the website. Each test case should be specific, objective, and step-wise replicable.

Instead of adding a general overview saying that everything works fine, consider documenting tests on each element of the page (eg. button clicks, input box validation, navigation links, etc.) by testing them in their "happy flow", their "bad/exception flow", mentioning the expected and observed results, and drawing a parallel between them where applicable.

Consider using the following format for manual test cases:

- Expected Outcome / Test Performed / Result Received / Fixes Implemented

- **Expected**: "Feature is expected to do X when the user does Y."
- **Testing**: "Tested the feature by doing Y."
- (either) **Result**: "The feature behaved as expected, and it did Y."
- (or) **Result**: "The feature did not respond to A, B, or C."
- **Fix**: "I did Z to the code because something was missing."

Use the table below as a basic start, and expand on it using the logic above.

⚠️ --- END --- ⚠️

Defensive programming was manually tested with the below user acceptance testing:

| Page | Expectation | Test | Result | Screenshot |
| --- | --- | --- | --- | --- |
| Products | Feature is expected to allow users to browse products without registration. | Opened product pages as a guest user. | Products were fully accessible without requiring registration. | ![screenshot](documentation/defensive/products.png) |
| | Feature is expected to sort products by price and name. | Tested sorting options for price (low-to-high/high-to-low) and name (alphabetical). | Sorting worked correctly for all options. | ![screenshot](documentation/defensive/sorting.png) |
| | Feature is expected to filter products by category. | Applied category filters while browsing products. | Filters worked as expected, displaying only relevant products. | ![screenshot](documentation/defensive/filtering.png) |
| | Feature is expected to show detailed product information. | Clicked on individual products to view details. | Product details (description, price, image) were displayed correctly. | ![screenshot](documentation/defensive/product-details.png) |
| Shopping Cart | Feature is expected to allow customers to add items to the cart with quantity controls. | Added products to the cart and adjusted quantities. | Items were added successfully, and quantities updated as expected. | ![screenshot](documentation/defensive/add-to-cart.png) |
| | Feature is expected to allow customers to view and manage their cart. | Opened the cart page and edited cart contents. | Cart contents were displayed, updated, and removed correctly. | ![screenshot](documentation/defensive/manage-cart.png) |
| Checkout | Feature is expected to display cart items, grand total, and input fields for checkout. | Proceeded to checkout with items in the cart. | Checkout page displayed cart items, total, and input fields as expected. | ![screenshot](documentation/defensive/checkout.png) |
| | Feature is expected to allow secure payment via Stripe. | Entered valid card details using Stripe at checkout. | Payment was processed securely, and an order confirmation page was displayed. | ![screenshot](documentation/defensive/stripe-payment.png) |
| | Feature is expected to send a confirmation email after purchase. | Completed a purchase and checked email inbox. | Confirmation email was received with order details. | ![screenshot](documentation/defensive/confirmation-email.png) |
| | Feature is expected to display an order confirmation page with an order number. | Completed a purchase. | Order confirmation page displayed successfully with an order number. | ![screenshot](documentation/defensive/order-confirmation.png) |
| Account Management | Feature is expected to allow returning customers to log in and view past orders. | Logged in as a returning customer and accessed order history. | Past orders were displayed correctly in the account section. | ![screenshot](documentation/defensive/order-history.png) |
| | Feature is expected to remember the shipping address for returning customers. | Completed multiple checkouts as a returning customer. | Shipping address was pre-filled on subsequent purchases. | ![screenshot](documentation/defensive/saved-address.png) |
| Admin Features | Feature is expected to allow the site owner to create new products. | Created new products with valid data (name, price, description, image, category). | Products were added successfully and displayed on the site. | ![screenshot](documentation/defensive/create-product.png) |
| | Feature is expected to allow the site owner to update product details. | Edited product details as an admin user. | Product updates were saved and displayed correctly. | ![screenshot](documentation/defensive/update-product.png) |
| | Feature is expected to allow the site owner to delete products. | Deleted a product from the inventory. | Product was removed successfully from the site, after being prompted to confirm first. | ![screenshot](documentation/defensive/delete-product.png) |
| Orders | Feature is expected to allow the site owner to view all orders placed. | Accessed the orders dashboard as an admin user. | All orders were displayed correctly. | ![screenshot](documentation/defensive/view-orders.png) |
| Newsletter | Feature is expected to allow users to sign up for the newsletter. | Submitted valid email addresses for newsletter registration. | Email addresses were successfully added to the newsletter list. | ![screenshot](documentation/defensive/newsletter.png) |
| 404 Error Page | Feature is expected to display a 404 error page for non-existent pages. | Navigated to an invalid URL (e.g., `/test`). | A custom 404 error page was displayed as expected. | ![screenshot](documentation/defensive/404.png) |

## User Story Testing

⚠️ INSTRUCTIONS ⚠️

Testing User Stories is actually quite simple, once you've already got the stories defined on your README.

Most of your project's **Features** should already align with the **User Stories**, so this should be as simple as creating a table with the User Story, matching with the re-used screenshot from the respective Feature.

⚠️ --- END --- ⚠️

| Target | Expectation | Outcome | Screenshot |
| --- | --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. | ![screenshot](documentation/features/feature01.png) |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. | ![screenshot](documentation/features/feature02.png) |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. | ![screenshot](documentation/features/feature03.png) |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. | ![screenshot](documentation/features/feature04.png) |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. | ![screenshot](documentation/features/feature05.png) |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. | ![screenshot](documentation/features/feature06.png) |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. | ![screenshot](documentation/features/feature07.png) |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. | ![screenshot](documentation/features/feature08.png) |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. | ![screenshot](documentation/features/feature09.png) |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. | ![screenshot](documentation/features/feature10.png) |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. | ![screenshot](documentation/features/feature11.png) |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. | ![screenshot](documentation/features/feature12.png) |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. | ![screenshot](documentation/features/feature13.png) |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. | ![screenshot](documentation/features/feature14.png) |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. | ![screenshot](documentation/features/feature15.png) |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. | ![screenshot](documentation/features/feature16.png) |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. | ![screenshot](documentation/features/feature17.png) |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. | ![screenshot](documentation/features/feature18.png) |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. | ![screenshot](documentation/features/feature19.png) |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. | ![screenshot](documentation/features/feature20.png) |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. | ![screenshot](documentation/features/feature21.png) |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. | ![screenshot](documentation/features/feature22.png) |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. | ![screenshot](documentation/features/feature23.png) |

## Automated Testing

I have conducted a series of automated tests on my application.

> [!NOTE]
> I fully acknowledge and understand that, in a real-world scenario, an extensive set of additional tests would be more comprehensive.

### Python (Unit Testing)

⚠️ INSTRUCTIONS ⚠️

Adjust the code below (file names, function names, etc.) to match your own project files/folders. Use these notes loosely when documenting your own Python Unit tests, and remove/adjust where applicable.

⚠️ SAMPLE ⚠️

I have used Django's built-in unit testing framework to test the application functionality. In order to run the tests, I ran the following command in the terminal each time:

- `python3 manage.py test name-of-app`

To create the coverage report, I would then run the following commands:

- `pip3 install coverage`
- `pip3 freeze --local > requirements.txt`
- `coverage run --omit=*/site-packages/*,*/migrations/*,*/__init__.py,env.py,manage.py test`
- `coverage report`

To see the HTML version of the reports, and find out whether some pieces of code were missing, I ran the following commands:

- `coverage html`
- `python3 -m http.server`

Below are the results from the full coverage report on my application that I've tested:

![screenshot](documentation/automation/html-coverage.png)

#### Unit Test Issues

⚠️ INSTRUCTIONS ⚠️

Use this section to list any known issues you ran into while writing your Python unit tests. Remember to include screenshots (where possible), and a solution to the issue (if known). This can be used for both "fixed" and "unresolved" issues. Remove this sub-section entirely if you somehow didn't run into any issues while working with your tests.

⚠️ --- END --- ⚠️

## Bugs

⚠️ INSTRUCTIONS ⚠️

Nobody likes bugs,... except the assessors! Projects seem more suspicious if a student doesn't properly track their bugs. If you're about to submit your project without any bugs listed below, you should ask yourself why you're doing this course in the first place, if you're able to build this entire application without running into any bugs. The best thing you can do for any project is to document your bugs! Not only does it show the true stages of development, but think of it as breadcrumbs for yourself in the future, should you encounter the same/similar bug again, it acts as a gentle reminder on what you did to fix the bug.

If/when you encounter bugs during the development stages of your project, you should document them here, ideally with a screenshot explaining what the issue was, and what you did to fix the bug.

Alternatively, an improved way to manage bugs is to use the built-in **[Issues](https://www.github.com/KC-85/Modern-Classics/issues)** tracker on your GitHub repository. This can be found at the top of your repository, the tab called "Issues".

If using the Issues tracker for bug management, you can simplify the documentation process for testing. Issues allow you to directly paste screenshots into the issue page without having to first save the screenshot locally. You can add labels to your issues (e.g. `bug`), assign yourself as the owner, and add comments/updates as you progress with fixing the issue(s). Once you've solved the issue/bug, you should then "Close" it.

When showcasing your bug tracking for assessment, you can use the following examples below.

⚠️ --- END --- ⚠️

### Fixed Bugs

[![GitHub issue custom search](https://img.shields.io/github/issues-search?query=repo%3AKC-85%2FModern-Classics%20label%3Abug&label=bugs)](https://www.github.com/KC-85/Modern-Classics/issues?q=is%3Aissue+is%3Aclosed+label%3Abug)

I've used [GitHub Issues](https://www.github.com/KC-85/Modern-Classics/issues) to track and manage bugs and issues during the development stages of my project.

All previously closed/fixed bugs can be tracked [here](https://www.github.com/KC-85/Modern-Classics/issues?q=is%3Aissue+is%3Aclosed+label%3Abug).

![screenshot](documentation/bugs/gh-issues-closed.png)

### Unfixed Bugs

⚠️ INSTRUCTIONS ⚠️

You will need to mention any unfixed bugs and why they are not fixed upon submission of your project. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed. Where possible, you must fix all outstanding bugs, unless outside of your control.

If you've identified any unfixed bugs, no matter how small, be sure to list them here! It's better to be honest and list them, because if it's not documented and an assessor finds the issue, they need to know whether or not you're aware of them as well, and why you've not corrected/fixed them.

⚠️ --- END --- ⚠️

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
| The `-`/`+` quantity buttons work well on "product_details.html", but not on "bag.html". | ![screenshot](documentation/issues/quantity-buttons.png) |

> [!IMPORTANT]
> There are no remaining bugs that I am aware of, though, even after thorough testing, I cannot rule out the possibility.

