from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from catalog.models import Topic, Newspaper


class ModelsTests(TestCase):
    def test_topic_str(self):
        topic = Topic.objects.create(name="Drama", )

        self.assertEqual(
            str(topic),
            f"{topic.name}",
        )

    def test_redactor_str(self):
        redactor = get_user_model().objects.create(
            username="test",
            password="test12345",
            first_name="Test first",
            last_name="Test last",
        )

        self.assertEqual(
            str(redactor),
            f"{redactor.username} ({redactor.first_name} {redactor.last_name})"
        )

    def test_newspaper_str(self):
        topic = Topic.objects.create(name="Drama")
        newspaper = Newspaper.objects.create(
            title="Test",
            topic=topic
        )

        self.assertEqual(str(newspaper), f"{newspaper.title}")


class NewspaperSearchTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            "test",
            "password123",
        )
        self.client.force_login(self.user)

    def test_of_searching_newspapers(self) -> None:
        response = self.client.get(
            reverse("catalog:newspaper-list") + "?title=m"
        )

        self.assertEqual(
            list(response.context["newspaper_list"]),
            list(Newspaper.objects.filter(title__icontains="m")),
        )


TOPIC_URL = reverse("catalog:topic-list")


class PublicTopicFormatTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_required(self):
        res = self.client.get(TOPIC_URL)

        self.assertNotEqual(res.status_code, 200)


class PrivateTopicFormatTests(TestCase):
    def setUp(self) -> None:
        self.user = get_user_model().objects.create_user(
            "test3",
            "password123444",
        )
        self.client.force_login(self.user)  # Тут мы логинимся

    def test_retrieve_topic(self):
        Topic.objects.create(name="Politicsss")

        response = self.client.get(TOPIC_URL)
        topics = Topic.objects.all()

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            list(response.context["topic_list"]),
            list(topics)
        )
        self.assertTemplateUsed(response, "catalog/topic_list.html")
