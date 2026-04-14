from django.db import migrations


def seed_faq_data(apps, schema_editor):
    FAQ = apps.get_model("common", "FAQ")

    # Do not overwrite/admin-edit existing records.
    if FAQ.objects.exists():
        return

    faq_rows = [
        {"question": "Do I need an account to buy a car?", "answer": "Yes. Anyone can browse, but you must sign in or sign up to add to cart and checkout.", "order": 10},
        {"question": "How do I create an account?", "answer": "Click Sign Up in the header, enter your details, and confirm via email.", "order": 20},
        {"question": "I forgot my password-what now?", "answer": "Use Login -> Forgot Password to reset securely via email.", "order": 30},
        {"question": "How do I filter or sort cars?", "answer": "Use the search box and Sort dropdown on the Showroom page.", "order": 40},
        {"question": "Are the photos accurate?", "answer": "Photos are optimized for fast loading and represent the actual vehicle.", "order": 50},
        {"question": "A car I saw now says SOLD-what happened?", "answer": "Vehicles can sell quickly. If a listing shows SOLD, it is no longer available.", "order": 60},
        {"question": "Are prices final?", "answer": "Prices shown are the asking price. Delivery fees appear at checkout when applicable.", "order": 70},
        {"question": "Do prices include tax/VAT?", "answer": "If applicable, tax appears in checkout. Contact support for invoice requests.", "order": 80},
        {"question": "What payment methods are accepted?", "answer": "Major cards are accepted via Stripe.", "order": 90},
        {"question": "Is payment secure?", "answer": "Yes. Stripe uses TLS encryption and PCI-compliant infrastructure.", "order": 100},
        {"question": "Where can I view my orders?", "answer": "Go to My Orders in the header while signed in.", "order": 110},
        {"question": "Do you offer delivery?", "answer": "Yes. Delivery options and costs appear at checkout.", "order": 120},
        {"question": "Can I cancel or edit an order?", "answer": "Contact support as soon as possible. Some cancellations may not be possible once processing starts.", "order": 130},
        {"question": "What is your return policy?", "answer": "Vehicle returns are limited and only possible under specific conditions.", "order": 140},
        {"question": "Do cars come with service history and documents?", "answer": "Each listing notes included documentation such as records, MOT, and manuals.", "order": 150},
        {"question": "How is condition graded?", "answer": "Condition is shown with standardized categories such as Excellent, Good, and Fair.", "order": 160},
        {"question": "I am not receiving emails (signup/reset/receipt).", "answer": "Check spam/junk and safe-sender rules. Contact support if messages still do not arrive.", "order": 170},
        {"question": "How do I contact you?", "answer": "Use the Contact page and include your order number for urgent issues.", "order": 180},
    ]

    FAQ.objects.bulk_create([FAQ(**row) for row in faq_rows])


class Migration(migrations.Migration):

    dependencies = [
        ("common", "0001_initial"),
    ]

    operations = [
        migrations.RunPython(seed_faq_data, migrations.RunPython.noop),
    ]
