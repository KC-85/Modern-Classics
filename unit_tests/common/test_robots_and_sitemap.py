from django.test import TestCase
from django.urls import reverse


class RobotsAndSitemapTests(TestCase):
    def test_robots_txt_is_plain_text_and_mentions_sitemap(self):
        resp = self.client.get("/robots.txt")
        self.assertEqual(resp.status_code, 200)
        self.assertIn("text/plain", resp["Content-Type"])
        self.assertIn("Sitemap:", resp.content.decode())

    def test_sitemap_xml_has_urlset(self):
        # Name your URL `name="sitemap"` in core/urls.py
        resp = self.client.get(reverse("sitemap"))
        self.assertEqual(resp.status_code, 200)
        body = resp.content.decode()
        self.assertIn("<urlset", body)
        self.assertIn("</urlset>", body)
