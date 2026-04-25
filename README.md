# [Modern-Classics](https://modern-classics-b10468fd6f55.herokuapp.com)

Developer: Kristian Cross ([KC-85](https://www.github.com/KC-85))

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics)

Modern Classics is a full-stack Django e-commerce platform focused on classic car sales. The application allows visitors to browse a curated showroom, filter and search listings, add cars to a cart, and complete checkout using Stripe.

The project is aimed at enthusiast buyers who want a clean browsing experience and secure purchase flow, and at site administrators who need manageable inventory and order workflows. Admin users can manage stock and delivery options, while authenticated customers can track their orders and maintain profile data.

This repository contains both customer-facing functionality (showroom, cart, checkout, FAQ/contact/newsletter) and operational functionality (admin CRUD, delivery configuration, webhook payment updates, SEO pages such as robots and sitemap).

![screenshot](documentation/mockup.png)

source: [Modern-Classics amiresponsive](https://ui.dev/amiresponsive?url=https://modern-classics-b10468fd6f55.herokuapp.com)

## UX

### The 5 Planes of UX

#### 1. Strategy

**Purpose**
- Provide a seamless and intuitive e-commerce experience for customers to browse, filter, and purchase products.
- Empower site owners to manage the store's inventory and customer orders efficiently.

**Primary User Needs**
- Guest users need to browse products and checkout with ease.
- Registered customers need a streamlined shopping experience with account and order history features.
- Site owners need robust tools for inventory and order management.

**Business Goals**
- Drive sales by providing a user-friendly shopping experience.
- Build customer loyalty through personalized and efficient account features.
- Maintain an organized and up-to-date store inventory.

#### 2. Scope

**[Features](#features)** (see below)

**Content Requirements**
- Product details, including name, price, description, category, and images.
- Clear prompts and instructions for browsing, filtering, and purchasing.
- Order details, confirmation pages, and email notifications.
- Secure payment processing using Stripe.
- Payment success emails sent to users.
- 404 page for lost users.

#### 3. Structure

**Information Architecture**
- **Navigation Menu**:
  - Links to Home, Products, Cart, Newsletter, and Account sections.
- **Hierarchy**:
  - Prominent product categories and filters for easy navigation.
  - Cart and checkout options displayed prominently for convenience.

**User Flow**
1. Guest user browses the store → filters and sorts products by category, price, or name.
2. Guest user adds items to the cart → proceeds to checkout.
3. Guest user creates an account or logs in during checkout → completes purchase.
4. Returning customers log in → view past orders and track purchase history.
5. Site owners manage inventory → add, update, or delete products and categories.
6. Users signup to the newsletter → potentially receive advanced notice of upcoming sales.

#### 4. Skeleton

**[Wireframes](#wireframes)** (see below)

#### 5. Surface

**Visual Design Elements**
- **[Colours](#colour-scheme)** (see below)
- **[Typography](#typography)** (see below)

### Colour Scheme

I used [coolors.co](https://coolors.co/f6f8fb-ffffff-0f1827-1b2a44) to generate my color palette.

- `#000000` primary text.
- `#3772FF` primary highlights.
- `#DF2935` secondary text.
- `#FDCA40` secondary highlights.

![screenshot](documentation/coolors.png)

### Typography

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.
- [Lato](https://fonts.google.com/specimen/Lato) was used for all other secondary text.
- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## Wireframes

To follow best practice, wireframes were developed for mobile, tablet, and desktop sizes.
I've used [Balsamiq](https://balsamiq.com/wireframes) to design my site wireframes.

| Page | Mobile | Tablet | Desktop |
| --- | --- | --- | --- |
| Register | ![screenshot](documentation/wireframes/mobile-register.png) | ![screenshot](documentation/wireframes/tablet-register.png) | ![screenshot](documentation/wireframes/desktop-register.png) |
| Login | ![screenshot](documentation/wireframes/mobile-login.png) | ![screenshot](documentation/wireframes/tablet-login.png) | ![screenshot](documentation/wireframes/desktop-login.png) |
| Profile | ![screenshot](documentation/wireframes/mobile-profile.png) | ![screenshot](documentation/wireframes/tablet-profile.png) | ![screenshot](documentation/wireframes/desktop-profile.png) |
| Showroom | ![screenshot](documentation/wireframes/mobile-showroom.png) | ![screenshot](documentation/wireframes/tablet-showroom.png) | ![screenshot](documentation/wireframes/desktop-showroom.png) |
| Product Details | ![screenshot](documentation/wireframes/mobile-product-details.png) | ![screenshot](documentation/wireframes/tablet-product-details.png) | ![screenshot](documentation/wireframes/desktop-product-details.png) |
| Bag | ![screenshot](documentation/wireframes/mobile-bag.png) | ![screenshot](documentation/wireframes/tablet-bag.png) | ![screenshot](documentation/wireframes/desktop-bag.png) |
| Checkout | ![screenshot](documentation/wireframes/mobile-checkout.png) | ![screenshot](documentation/wireframes/tablet-checkout.png) | ![screenshot](documentation/wireframes/desktop-checkout.png) |
| Checkout Success | ![screenshot](documentation/wireframes/mobile-checkout-success.png) | ![screenshot](documentation/wireframes/tablet-checkout-success.png) | ![screenshot](documentation/wireframes/desktop-checkout-success.png) |
| Add Product | ![screenshot](documentation/wireframes/mobile-add-product.png) | ![screenshot](documentation/wireframes/tablet-add-product.png) | ![screenshot](documentation/wireframes/desktop-add-product.png) |
| Edit Product | ![screenshot](documentation/wireframes/mobile-edit-product.png) | ![screenshot](documentation/wireframes/tablet-edit-product.png) | ![screenshot](documentation/wireframes/desktop-edit-product.png) |
| Newsletter | ![screenshot](documentation/wireframes/mobile-newsletter.png) | ![screenshot](documentation/wireframes/tablet-newsletter.png) | ![screenshot](documentation/wireframes/desktop-newsletter.png) |
| Contact | ![screenshot](documentation/wireframes/mobile-contact.png) | ![screenshot](documentation/wireframes/tablet-contact.png) | ![screenshot](documentation/wireframes/desktop-contact.png) |
| 404 | ![screenshot](documentation/wireframes/mobile-404.png) | ![screenshot](documentation/wireframes/tablet-404.png) | ![screenshot](documentation/wireframes/desktop-404.png) |

## User Stories

| Target | Expectation | Outcome |
| --- | --- | --- |
| As a guest user | I would like to browse products without needing to register | so that I can shop freely before deciding to create an account. |
| As a guest user | I would like to be prompted to create an account or log in at checkout | so that I can complete my purchase and track my order history. |
| As a user | I would like to sign up to the site's newsletter | so that I can stay up to date with any upcoming sales or promotions. |
| As a customer | I would like to browse various product categories (clothing, toys, jewelry, kitchen gadgets, etc.) | so that I can easily find what I'm looking for. |
| As a customer | I would like to sort products by price (low-to-high/high-to-low) and name (alphabetical) | so that I can quickly organize items in a way that suits my shopping style. |
| As a customer | I would like to filter products by category | so that I can narrow down the products to the types I am most interested in. |
| As a customer | I would like to click on individual products to view more details (description, price, image, etc.) | so that I can make an informed decision about my purchase. |
| As a customer | I would like to add items to my shopping cart using quantity increment/decrement buttons | so that I can adjust how many units of a product I want before checkout. |
| As a customer | I would like to view and manage my shopping cart | so that I can review, add, or remove items before proceeding to checkout. |
| As a customer | I would like to adjust the quantity of items in my cart | so that I can modify my purchase preferences without leaving the cart. |
| As a customer | I would like to remove items from my cart | so that I can remove products I no longer wish to buy. |
| As a customer | I would like to proceed to checkout where I see my cart items, grand total, and input my name, email, shipping address, and card details | so that I can complete my purchase. |
| As a customer | I would like to receive a confirmation email after my purchase | so that I can have a record of my transaction and order details. |
| As a customer | I would like to see an order confirmation page with a checkout order number after completing my purchase | so that I know my order has been successfully placed. |
| As a customer | I would like to securely enter my card details using Stripe at checkout | so that I can feel confident my payment information is protected. |
| As a returning customer | I would like to be able to log in and view my past orders | so that I can track my previous purchases and order history. |
| As a returning customer | I would like the checkout process to remember my shipping address | so that future purchases are quicker and easier. |
| As a site owner | I would like to create new products with a name, description, price, images, and category | so that I can add additional items to the store inventory. |
| As a site owner | I would like to update product details (name, price, description, image, category) at any time | so that I can keep my product listings accurate and up to date. |
| As a site owner | I would like to delete products that are no longer available or relevant | so that I can maintain a clean and accurate inventory. |
| As a site owner | I would like to view all orders placed on the website | so that I can track and manage customer purchases. |
| As a site owner | I would like to manage product categories | so that I can ensure items are correctly organized and easy for customers to find. |
| As a user | I would like to see a 404 error page if I get lost | so that it's obvious that I've stumbled upon a page that doesn't exist. |

## Features

### Existing Features

| Feature | Notes | Screenshot |
| --- | --- | --- |
| Register | Authentication is handled by allauth, allowing users to register accounts. | ![screenshot](documentation/features/register.png) |
| Login | Authentication is handled by allauth, allowing users to log in to their existing accounts. | ![screenshot](documentation/features/login.png) |
| Logout | Authentication is handled by allauth, allowing users to log out of their accounts. | ![screenshot](documentation/features/logout.png) |
| Product List | Users can browse all available products with sorting, filtering by categories, and search functionality. | ![screenshot](documentation/features/product-list.png) |
| Product Details | Displays detailed information about a selected product, including its name, description, price, an image, and available sizes. | ![screenshot](documentation/features/product-details.png) |
| Add to Bag | Users can add items to their shopping bag, with support for selecting different sizes if applicable. | ![screenshot](documentation/features/add-to-bag.png) |
| View Bag | Users can view the contents of their shopping bag, adjust quantities, or remove items. | ![screenshot](documentation/features/view-bag.png) |
| Checkout | Users can proceed to checkout, where they provide their delivery details and payment information using Stripe integration. | ![screenshot](documentation/features/checkout.png) |
| Order Confirmation | Users receive an on-screen and email confirmation with details of their purchase. | ![screenshot](documentation/features/order-confirmation.png) |
| Profile Management | Users can manage their profile information, including their default delivery address and order history. | ![screenshot](documentation/features/profile-management.png) |
| Order History | Users can view their past orders and access details of each order, including products purchased and the delivery status. | ![screenshot](documentation/features/order-history.png) |
| Product Management | Superusers can add, edit, and delete products from the site via a CRUD interface. | ![screenshot](documentation/features/product-management.png) |
| Newsletter | Users can register their email address to receive newsletters from the site. Currently, this only stores the email in the database. | ![screenshot](documentation/features/newsletter.png) |
| Contact | Users can submit a message via the contact form, which stores their name, email, and message in the database. | ![screenshot](documentation/features/contact.png) |
| FAQs | Admins can manage frequently asked questions, which are displayed on the site for users. | ![screenshot](documentation/features/faqs.png) |
| User Feedback | Clear and concise Django messages are used to provide feedback to users when interacting with various features (e.g., adding products to the bag, checking out, etc.). | ![screenshot](documentation/features/user-feedback.png) |
| Heroku Deployment | The site is deployed to Heroku, making it accessible online for users. | ![screenshot](documentation/features/heroku.png) |
| SEO | SEO optimization with a sitemap.xml, robots.txt, and appropriate meta tags to improve search engine visibility. | ![screenshot](documentation/features/seo.png) |
| Marketing | Social media presence is available in the footer using external links, as well as a Facebook Marketplace wireframe in the README for future integrations. | ![screenshot](documentation/features/marketing.png) |
| 404 | The 404 error page will indicate when a user has navigated to a page that doesn't exist, replacing the default Heroku 404 page with one that ties into the site's look and feel. | ![screenshot](documentation/features/404.png) |

### Future Features

- **Product Reviews & Ratings**: Allow customers to leave reviews and rate products, with admin moderation. Display average ratings and review counts on product pages.
- **Wishlist Functionality**: Enable users to save products to a personal wishlist for future purchases. Notify users if wishlist items go on sale or are back in stock.
- **Product Recommendations**: Implement a "Customers who bought this also bought" or "You might also like" feature to suggest related products.
- **Live Chat Support**: Provide real-time customer support through an integrated live chat or chatbot.
- **Abandoned Cart Recovery**: Automatically send emails to users who add items to their cart but don't complete the purchase, offering discounts or reminders.
- **Discount Codes and Vouchers**: Allow the admin to create discount codes or vouchers for promotions and marketing campaigns.
- **Loyalty Program**: Introduce a points-based loyalty system where customers earn points for purchases, which can be redeemed for discounts.
- **Product Inventory Alerts**: Notify customers when out-of-stock items are back in stock, or when low inventory is approaching.
- **Multi-Currency and Multi-Language Support**: Expand the application to support multiple currencies and languages to reach a global audience.
- **Product Bundles**: Offer discounted product bundles (e.g., buy 3 for the price of 2) or custom product kits.
- **Social Media Integration**: Enable users to share products directly to social media platforms or implement a social login for quick account creation.
- **Shipping Tracking Integration**: Provide real-time shipping updates and tracking information directly within the user’s order history.
- **Advanced Analytics Dashboard for Admin**: Offer an in-depth dashboard that displays sales trends, popular products, customer behavior, and more.
- **Subscription-Based Products**: Allow users to subscribe to certain products (e.g., monthly deliveries of consumables like coffee or skincare products).
- **Product Video Demos**: Support product videos to better showcase features, especially for high-tech or complex items.
- **Mobile App**: Develop a mobile app for iOS and Android, providing users with a more optimized shopping experience on mobile devices.

## Tools & Technologies

| Tool / Tech | Use |
| --- | --- |
| [![badge](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://markdown.2bn.dev) | Generate README and TESTING templates. |
| [![badge](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) | Version control. (`git add`, `git commit`, `git push`) |
| [![badge](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) | Secure online code storage. |
| [![badge](https://img.shields.io/badge/VSCode-grey?logo=htmx&logoColor=007ACC)](https://code.visualstudio.com) | Local IDE for development. |
| [![badge](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) | Main site content and layout. |
| [![badge](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) | Design and layout. |
| [![badge](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) | User interaction on the site. |
| [![badge](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) | Back-end programming language. |
| [![badge](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) | Hosting the deployed back-end site. |
| [![badge](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) | Front-end CSS framework for modern responsiveness and pre-built components. |
| [![badge](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) | Python framework for the site. |
| [![badge](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) | Relational database management. |
| [![badge](https://img.shields.io/badge/Cloudinary-grey?logo=cloudinary&logoColor=3448C5)](https://cloudinary.com) | Online static file storage. |
| [![badge](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) | Serving static files with Heroku. |
| [![badge](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) | Online secure payments of e-commerce products/services. |
| [![badge](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) | Sending emails in my application. |
| [![badge](https://img.shields.io/badge/ChatGPT-grey?logo=openai&logoColor=75A99C)](https://chat.openai.com) | Help debug, troubleshoot, and explain things. |
| [![badge](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://mermaid.live) | Generate an interactive diagram for the data/schema. |
| [![badge](https://img.shields.io/badge/W3Schools-grey?logo=w3schools&logoColor=04AA6D)](https://www.w3schools.com) | Tutorials/Reference Guide |

## Database Design

### Data Model

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models. Understanding the relationships between different tables can save time later in the project.

![screenshot](documentation/erd.png)

I have used `Mermaid` to generate an interactive ERD of my project.

```mermaid
erDiagram
    CUSTOMUSER {
        BigInt id PK
        varchar username
        varchar email
        varchar password
        varchar first_name
        varchar last_name
        varchar phone_number
        date    date_of_birth
        varchar address_line1
        varchar address_line2
        varchar city
        varchar postal_code
        varchar country
        varchar profile_image
        datetime date_joined
    }
    CUSTOMUSER ||--o{ CART            : owns
    CUSTOMUSER ||--o{ ORDERS_ORDER    : places

    %% Showroom (Cars)
    CARMAKE {
        BigInt id PK
        varchar name
    }
    CARMODEL {
        BigInt id PK
        BigInt make_id FK
        varchar name
    }
    CAR {
        BigInt id PK
        BigInt make_id FK
        BigInt model_id FK
        int    year
        text   specifications
        varchar performance
        varchar condition
        varchar image
        decimal price
        datetime created_at
        datetime updated_at
        varchar slug
    }
    CARMAKE ||--o{ CARMODEL : has
    CARMODEL ||--o{ CAR      : has

    %% Cart / Trailer
    CART {
        BigInt id PK
        BigInt user_id FK
        datetime created_at
    }
    CARTITEM {
        BigInt id PK
        BigInt cart_id FK
        BigInt car_id FK
        int     quantity
    }
    CART ||--o{ CARTITEM : contains
    CAR  ||--o{ CARTITEM : referenced_by

    %% Orders & Checkout
    ORDERS_ORDER {
        BigInt id PK
        BigInt user_id FK
        numeric total_amount
        varchar status
        varchar stripe_session_id
        datetime created_at
        datetime updated_at
    }
    ORDERS_ORDERITEM {
        BigInt id PK
        BigInt order_id FK
        BigInt car_id FK
        int      quantity
        decimal  price
    }
    CART   ||--o{ ORDERS_ORDER    : converted_to
    ORDERS_ORDER ||--o{ ORDERS_ORDERITEM : includes
    CAR    ||--o{ ORDERS_ORDERITEM : referenced_by

    %% Delivery
    DELIVERYOPTION {
        BigInt id PK
        varchar name
        decimal fee
        text    description
    }
    ORDERDELIVERY {
        BigInt id PK
        BigInt order_id FK
        BigInt option_id FK
        varchar tracking_id
        datetime shipped_at
    }
    DELIVERYOPTION ||--o{ ORDERDELIVERY : available_choice
    ORDERS_ORDER   ||--o{ ORDERDELIVERY : ships_via

    %% Common (misc)
    COMMON_NEWSLETTER {
        BigInt id PK
        varchar email
    }
    COMMON_CONTACT {
        BigInt id PK
        varchar name
        varchar email
        text    message
        datetime date_sent
    }
    COMMON_FAQ {
        BigInt id PK
        varchar question
        text    answer
    }
```

source: [Mermaid](https://mermaid.live/edit#pako:eNqVVcFu2zAM_RVD57RIHLdpfRs6DBg2bB2GXYYAhmIxjlBZcimqqdvk3yfbSVPHceP5kBh8TyRFPtKvLDUCWMwAP0ueIc_nOvDPHwsYvDbv1SM1BVIE998OpieO6Ypj4DxV8xy6CORcqq654NauDYoG2c71IeQ9mqVUMDCygCV3ipJiZTQk2uULwH6WJQSghAuBYO1kKDHsJ5JZ68Rgkkoq-1mpcfojvDCWqiac8YDliXoFm83FxWbTql0crLhNfEX2xDtOkBksB1b1dC-XKEELVSYH-C0TH1m4lAb6tw_uXFCCZ_K3tynKgqTRB2RhjKrvZ-UL2INdQCpzroICZQpdM3KSOuuG9WAGicN3Kq1NzW_PNauam82hrHGwAGV0Zr0g9tyfKAYPkKm4vfJdOqWS_5uvD8ehJabWsV4dfqzzs3N1dp6OJ0T4ypLMoX7pNlOAkk-ApZ8LS124KScZ4qoL-g2nxTFYy82gzKTmKlnw7OQdZAFJIY-3Vt3o71LDV4L8TMMr06Pjmlp13KemvBPpnRxn99afRn618k8lsddlO6NmG-Rcl6fy3R3ZK7tfyTtie890yT9gbRUQDdb-Owm_3ebOaOKD18mg0ag7nHv1daf6y6dfAyM9OrDtbVS75dqu94O2ZSOWA_rgwn9Ta7dzRivwKbLYvwqOD3M21xWPOzK_S52ymNDBiLmikvvuK8ziJVfWWwuuWfzKnlk8jSaXN9ez8HoyHc_C8TiajVjJ4ovp5XUUTqMovLqdXd2Et-FsO2Ivxngfk8vxZBpGkT_m_zxW-_tbY01QNC5b7YJt_wE0ZoQj)

I have used `pygraphviz` and `django-extensions` to auto-generate an ERD.

The steps taken were as follows:
- In the terminal: `sudo apt update`
- then: `sudo apt-get install python3-dev graphviz libgraphviz-dev pkg-config`
- then type `Y` to proceed
- then: `pip3 install django-extensions pygraphviz`
- in my `settings.py` file, I added the following to my `INSTALLED_APPS`:
```python
INSTALLED_APPS = [
    ...
    'django_extensions',
    ...
]
```
- back in the terminal: `python3 manage.py graph_models -a -o erd.png`
- drag the new `erd.png` file into my `documentation/` folder
- removed `'django_extensions',` from my `INSTALLED_APPS`
- finally, in the terminal: `pip3 uninstall django-extensions pygraphviz -y`

![screenshot](documentation/advanced-erd.png)

source: [medium.com](https://medium.com/@yathomasi1/1-using-django-extensions-to-visualize-the-database-diagram-in-django-application-c5fa7e710e16)

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://www.github.com/KC-85/Modern-Classics/projects) served as an Agile tool for this project. Through it, EPICs, User Stories, issues/bugs, and Milestone tasks were planned, then subsequently tracked on a regular basis using the Kanban project board.

![screenshot](documentation/gh-projects.png)

### GitHub Issues

[GitHub Issues](https://www.github.com/KC-85/Modern-Classics/issues) served as an another Agile tool. There, I managed my User Stories and Milestone tasks, and tracked any issues/bugs.

| Link | Screenshot |
| --- | --- |
| [![GitHub issues](https://img.shields.io/github/issues/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics/issues) | ![screenshot](documentation/gh-issues-open.png) |
| [![GitHub closed issues](https://img.shields.io/github/issues-closed/KC-85/Modern-Classics)](https://www.github.com/KC-85/Modern-Classics/issues?q=is%3Aissue+is%3Aclosed) | ![screenshot](documentation/gh-issues-closed.png) |

### MoSCoW Prioritization

I've decomposed my Epics into User Stories for prioritizing and implementing them. Using this approach, I was able to apply "MoSCoW" prioritization and labels to my User Stories within the Issues tab.

- **Must Have**: guaranteed to be delivered - required to Pass the project (*max ~60% of stories*)
- **Should Have**: adds significant value, but not vital (*~20% of stories*)
- **Could Have**: has small impact if left out (*the rest ~20% of stories*)
- **Won't Have**: not a priority for this iteration - future features

## Ecommerce Business Model

Modern Classics follows a **B2C (Business to Consumer)** model. The core transaction is a single-customer purchase of a listed classic car through the website checkout flow.

### Commercial Intent

- Convert showroom browsing into completed Stripe-backed purchases.
- Build buyer trust through transparent listing details and secure payment handling.
- Increase repeat engagement through account history and email communications.

### Revenue Model

- Primary revenue comes from direct vehicle sales.
- No subscription model is used; transactions are one-off purchases.

### Marketing & Retention Channels

- **Newsletter signup** is used for audience retention and announcement campaigns.
- **SEO pages** (sitemap/robots + metadata) support organic discovery.
- **Social presence** and external channels are used to drive qualified traffic to listings.

### Audience

- Individual buyers searching for curated classic vehicles.
- Enthusiasts who prefer a streamlined online purchasing process with clear inventory visibility.

## SEO & Marketing

### Keywords

I've identified some appropriate keywords to align with my site, that should help users when searching online to find my page easily from a search engine. This included a series of the following keyword types:

- Short-tail (head terms) keywords
- Long-tail keywords

I've also played around with [Word Tracker](https://www.wordtracker.com) a bit to check the frequency of some of my site's primary keywords (only until the free trial expired).

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file. This was generated using my deployed site URL: https://modern-classics-b10468fd6f55.herokuapp.com

After it finished crawling the entire site, it created a [sitemap.xml](sitemap.xml), which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level. Inside, I've included the default settings:

```txt
User-agent: *
Disallow:
Sitemap: https://modern-classics-b10468fd6f55.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales. Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account using the [Balsamiq template](https://code-institute-org.github.io/5P-Assessments-Handbook/files/Facebook_Mockups.zip) provided by Code Institute.

![screenshot](documentation/mockup-facebook.png)

### Newsletter Marketing

I have incorporated a newsletter sign-up form in the application so users can register their email address for updates.

Current implementation uses a Django `Newsletter` model to store subscriptions directly in the project database.

Future enhancement path: integrate transactional or campaign email delivery (for example via Mailchimp or a custom send pipeline) when newsletter automation is required.

## Testing

> [!NOTE]
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://modern-classics-b10468fd6f55.herokuapp.com).

### Heroku Deployment

This project is deployed to Heroku using Gunicorn and PostgreSQL.

Deployment summary:

1. Create a new Heroku app.
2. Connect the GitHub repository to the app (or deploy via Heroku CLI).
3. Set required config vars (see below).
4. Deploy `main`.
5. Run migrations on the deployed app.

Required deployment files:

- [requirements.txt](requirements.txt)
- [Procfile](Procfile)

Current Procfile process:

- `web: python manage.py collectstatic --noinput && gunicorn core.wsgi --log-file -`

### Required Heroku Config Vars

Set the following values in Heroku app settings:

- `SECRET_KEY`
- `DATABASE_URL`
- `ALLOWED_HOSTS`
- `CSRF_TRUSTED_ORIGINS`
- `CLOUDINARY_CLOUD_NAME`
- `CLOUDINARY_API_KEY`
- `CLOUDINARY_API_SECRET`
- `STRIPE_SECRET_KEY`
- `STRIPE_PUBLISHABLE_KEY`
- `STRIPE_WEBHOOK_SECRET`
- `ENVIRONMENT` (`production` on Heroku)

If email sending is enabled in production, also set:

- `EMAIL_HOST_USER`
- `EMAIL_HOST_PASSWORD`

### Post-Deployment Checks

After deployment, verify:

- Home, showroom, and auth routes load correctly.
- Stripe checkout flow completes and updates order status.
- `robots.txt` and `sitemap.xml` are reachable.
- Static assets load without 404s.

### Cloudinary API

This project uses the [Cloudinary API](https://cloudinary.com) to store media assets online, due to the fact that Heroku doesn't persist this type of data.

To obtain your own Cloudinary API key, create an account and log in.

- For "Primary Interest", you can choose **Programmable Media for image and video API**.
- *Optional*: edit your assigned cloud name to something more memorable.
- On your Cloudinary Dashboard, you can copy your **API Environment Variable**.
- Be sure to remove the leading `CLOUDINARY_URL=` as part of the API **value**; this is the **key**.
    - `cloudinary://123456789012345:AbCdEfGhIjKlMnOpQrStuVwXyZa@1a2b3c4d5)`
- This will go into your own `env.py` file, and Heroku Config Vars, using the **key** of `CLOUDINARY_URL`.

### PostgreSQL

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net) for the Relational Database with Django.

> [!CAUTION]
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Submitted my email address to the CI PostgreSQL Database link above.
- An email was sent to me with my new Postgres Database.
- The Database connection string will resemble something like this:
    - `postgres://<db_username>:<db_password>@<db_host_url>/<db_name>`
- You can use the above URL with Django by setting `DATABASE_URL` locally and in Heroku config vars.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
    - `STRIPE_PUBLISHABLE_KEY` = Publishable Key (starts with **pk**)
    - `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://modern-classics-b10468fd6f55.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
    - `STRIPE_WEBHOOK_SECRET` = Signing secret (starts with **wh**)

### Yahoo API

This project uses [Yahoo](https://mail.yahoo.com) to handle sending emails to users for purchase order confirmations.

Once you've created a Yahoo account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Yahoo Mail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Yahoo Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (*verify your password and account*)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords** (*search for it at the top, if not*).
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
    - Any custom name, such as "Django" or `Modern-Classics`
- You'll be provided with a 16-character password (API key).
    - Save this somewhere locally, as you cannot access this key again later!
    - If your 16-character password contains *spaces*, make sure to remove them entirely.
    - `EMAIL_HOST_PASS` = user's 16-character API key
    - `EMAIL_HOST_USER` = user's own personal Gmail/Yahoo email address

### WhiteNoise

This project uses the [WhiteNoise](https://whitenoise.readthedocs.io/en/latest/) to aid with static files temporarily hosted on the live Heroku site.

To include WhiteNoise in your own projects:

- Install the latest WhiteNoise package:
    - `pip install whitenoise`
- Update the `requirements.txt` file with the newly installed package:
    - `pip freeze --local > requirements.txt`
- Edit your `settings.py` file and add WhiteNoise to the `MIDDLEWARE` list, above all other middleware (apart from Django’s "SecurityMiddleware"):

```python
# settings.py

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # any additional middleware
]
```


### Local Development

This project can be cloned or forked in order to make a local copy on your own system.

Recommended local setup:

```bash
python3.12 -m venv venv
source venv/bin/activate
pip3/pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser
python3 manage.py runserver
```

Local environment variables should be provided via `.env` (loaded by `python-dotenv`) and should mirror required config vars used in deployment.

If you'd like to backup your database models, use the following command for each model you'd like to create a fixture for:

- `python3 manage.py dumpdata your-model > your-model.json`
- *repeat this action for each model you wish to backup*
- **NOTE**: You should never make a backup of the default *admin* or *users* data with confidential information.

#### Cloning

You can clone the repository by following these steps:

1. Go to the [GitHub repository](https://www.github.com/KC-85/Modern-Classics).
2. Locate and click on the green "Code" button at the very top, above the commits and files.
3. Select whether you prefer to clone using "HTTPS", "SSH", or "GitHub CLI", and click the "copy" button to copy the URL to your clipboard.
4. Open "Git Bash" or "Terminal".
5. Change the current working directory to the location where you want the cloned directory.
6. In your IDE Terminal, type the following command to clone the repository:
	- `git clone https://www.github.com/KC-85/Modern-Classics.git`
7. Press "Enter" to create your local clone.

Alternatively, if using Gitpod, you can click below to create your own workspace using this repository.

[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#https://www.github.com/KC-85/Modern-Classics)

**Please Note**: in order to directly open the project in Gitpod, you should have the browser extension installed. A tutorial on how to do that can be found [here](https://www.gitpod.io/docs/configure/user-settings/browser-extension).

#### Forking

By forking the GitHub Repository, you make a copy of the original repository on our GitHub account to view and/or make changes without affecting the original owner's repository. You can fork this repository by using the following steps:

1. Log in to GitHub and locate the [GitHub Repository](https://www.github.com/KC-85/Modern-Classics).
2. At the top of the Repository, just below the "Settings" button on the menu, locate and click the "Fork" Button.
3. Once clicked, you should now have a copy of the original repository in your own GitHub account!

### Local VS Deployment

There are no remaining major differences between the local version when compared to the deployed version online.

## Credits

### Content

| Source | Notes |
| --- | --- |
| [Chris Beams](https://chris.beams.io/posts/git-commit) | "How to Write a Git Commit Message" |
| [Bootstrap](https://getbootstrap.com) | Various components / responsive front-end framework |
| [AWS S3](https://aws.amazon.com/s3) | Cloud storage for static/media files |
| [Whitenoise](https://whitenoise.readthedocs.io) | Static file service |
| [Stripe](https://docs.stripe.com/payments/elements) | Online payment services |
| [Gmail API](https://developers.google.com/gmail/api/guides) | Sending payment confirmation emails |
| [Python Tutor](https://pythontutor.com) | Additional Python help |
| [ChatGPT](https://chatgpt.com) | Help with code logic and explanations |

### Media

| Source | Notes |
| --- | --- |
| [favicon.io](https://favicon.io) | Generating the favicon |
| [Font Awesome](https://fontawesome.com) | Icons used throughout the site |
| [Pexels](https://images.pexels.com/photos/416160/pexels-photo-416160.jpeg) | Hero image |
| [Wallhere](https://c.wallhere.com/images/9c/c8/da4b4009f070c8e1dfee43d25f99-2318808.jpg!d) | Background wallpaper |
| [Pixabay](https://cdn.pixabay.com/photo/2017/09/04/16/58/passport-2714675_1280.jpg) | Background wallpaper |
| [DALL-E 3](https://openai.com/index/dall-e-3) | AI generated artwork |
| [TinyPNG](https://tinypng.com) | Compressing images < 5MB |
| [CompressPNG](https://compresspng.com) | Compressing images > 5MB |
| [CloudConvert](https://cloudconvert.com/webp-converter) | Converting images to `.webp` |

### Acknowledgements

- I would like to thank my Code Institute mentor, [Tim Nelson](https://www.github.com/TravelTimN) for the support throughout the development of this project.
- I would like to thank the [Code Institute](https://codeinstitute.net) Tutor Team for their assistance with troubleshooting and debugging some project issues.
- I would like to thank the [Code Institute Discord community](https://discord.gg/codeinstitute) for the moral support; it kept me going during periods of self doubt and impostor syndrome.
- I would like to thank my friends & family, for believing in me, and allowing me to make this transition into software development.
- I would like to thank my employer, for supporting me in my career development change towards becoming a software developer.

