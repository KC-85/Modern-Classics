from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from apps.common.models import Newsletter, FAQ

User = get_user_model()


class NavigationDiscoverabilityTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="nav-user",
            email="nav@example.com",
            password="pass12345",
        )

    def test_guest_navigation_shows_common_resource_links(self):
        resp = self.client.get(reverse("showroom:car_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, reverse("common:faq_list"))
        self.assertContains(resp, reverse("common:contact"))
        self.assertContains(resp, reverse("common:newsletter"))

    def test_authenticated_navigation_still_shows_common_resource_links(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse("showroom:car_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, reverse("common:faq_list"))
        self.assertContains(resp, reverse("common:contact"))
        self.assertContains(resp, reverse("common:newsletter"))

    def test_layout_has_external_link_with_rel_attributes(self):
        resp = self.client.get(reverse("showroom:car_list"))
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, 'target="_blank"', html=False)
        self.assertContains(resp, 'rel="noopener noreferrer"', html=False)


class HomeViewAccessTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="home-user",
            email="home@example.com",
            password="pass12345",
        )

    def test_guest_sees_hero_page(self):
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/hero.html")

    def test_authenticated_user_redirects_to_showroom(self):
        self.client.force_login(self.user)
        resp = self.client.get(reverse("home"))
        self.assertRedirects(resp, reverse("showroom:car_list"))

    def test_user_sees_hero_after_logout(self):
        self.client.force_login(self.user)
        self.client.logout()
        resp = self.client.get(reverse("home"))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, "home/hero.html")


class NewsletterSignupViewTests(TestCase):
    def test_get_renders_form(self):
        url = reverse("common:newsletter")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertContains(resp, "Newsletter")

    def test_post_valid_redirects_to_success_and_creates_record(self):
        url = reverse("common:newsletter")
        resp = self.client.post(
            url, {"email": "ok@example.com", "consent": True})
        self.assertRedirects(resp, reverse("common:newsletter_success"))
        self.assertTrue(Newsletter.objects.filter(
            email="ok@example.com").exists())

    def test_post_duplicate_stays_on_form_with_error(self):
        Newsletter.objects.create(email="dupe@example.com")
        url = reverse("common:newsletter")
        resp = self.client.post(
            url, {"email": "dupe@example.com", "consent": True})
        # Expect form to re-render (200) with an error message you add in the view
        self.assertEqual(resp.status_code, 200)
        # Match your view’s error text exactly:
        self.assertContains(resp, "already subscribed",
                            status_code=200, html=False)


class NewsletterSuccessViewTests(TestCase):
    def test_success_page_renders(self):
        url = reverse("common:newsletter_success")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        # Your template shows “You’re subscribed!”
        text = resp.content.decode()
        self.assertTrue(
            ("You're subscribed!" in text) or (
                "You&#x27;re subscribed!" in text),
            "Success copy not found"
        )


class FAQCrudViewTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(
            username="faq-user",
            email="faq-user@example.com",
            password="pass12345",
        )
        cls.superuser = User.objects.create_superuser(
            username="faq-admin",
            email="faq-admin@example.com",
            password="admin12345",
        )
        cls.faq = FAQ.objects.create(
            question="How do I buy a car?",
            answer="Sign in and checkout.",
            order=1,
        )

    def test_superuser_can_create_faq(self):
        self.client.force_login(self.superuser)
        resp = self.client.post(
            reverse("common:faq_create"),
            {"question": "Test Q", "answer": "Test A", "order": 2},
        )
        self.assertRedirects(resp, reverse("common:faq_list"))
        self.assertTrue(FAQ.objects.filter(question="Test Q").exists())

    def test_superuser_can_edit_faq(self):
        self.client.force_login(self.superuser)
        resp = self.client.post(
            reverse("common:faq_edit", kwargs={"pk": self.faq.pk}),
            {"question": "Updated Q", "answer": "Updated A", "order": 1},
        )
        self.assertRedirects(resp, reverse("common:faq_list"))
        self.faq.refresh_from_db()
        self.assertEqual(self.faq.question, "Updated Q")

    def test_superuser_can_delete_faq(self):
        self.client.force_login(self.superuser)
        resp = self.client.post(reverse("common:faq_delete", kwargs={"pk": self.faq.pk}))
        self.assertRedirects(resp, reverse("common:faq_list"))
        self.assertFalse(FAQ.objects.filter(pk=self.faq.pk).exists())

    def test_non_superuser_cannot_access_faq_crud_views(self):
        self.client.force_login(self.user)
        create_resp = self.client.get(reverse("common:faq_create"))
        edit_resp = self.client.get(reverse("common:faq_edit", kwargs={"pk": self.faq.pk}))
        delete_resp = self.client.get(reverse("common:faq_delete", kwargs={"pk": self.faq.pk}))

        self.assertEqual(create_resp.status_code, 302)
        self.assertEqual(edit_resp.status_code, 302)
        self.assertEqual(delete_resp.status_code, 302)
