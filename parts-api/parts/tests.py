from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Part

class PartAPITests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.part = Part.objects.create(
            name="Original Part",
            sku="ORI123",
            description="Original description",
            weight_ounces=5,
            is_active=True
        )

    def test_create_part(self):
        url = reverse('part-list')
        data = {
            "name": "Test Part",
            "sku": "TEST001",
            "description": "A test part",
            "weight_ounces": 10,
            "is_active": True
        }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 2)

    def test_update_part(self):
        url = reverse('part-detail', args=[self.part.id])
        data = {
            "name": "Updated Part",
            "sku": "UPDATED123",
            "description": "Updated description",
            "weight_ounces": 15,
            "is_active": False
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_part = Part.objects.get(id=self.part.id)
        self.assertEqual(updated_part.name, "Updated Part")
        self.assertEqual(updated_part.is_active, False)

    def test_bulk_create_parts(self):
        url = reverse('part-bulk-create')
        data = [
            {
                "name": "Bulk 1",
                "sku": "BULK001",
                "description": "common energy module",
                "weight_ounces": 4,
                "is_active": True
            },
            {
                "name": "Bulk 2",
                "sku": "BULK002",
                "description": "common energy circuit",
                "weight_ounces": 7,
                "is_active": True
            }
        ]
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Part.objects.count(), 3)

    def test_bulk_delete_parts(self):
        p1 = Part.objects.create(name="To Delete 1", sku="DEL001", description="...", weight_ounces=2, is_active=True)
        p2 = Part.objects.create(name="To Delete 2", sku="DEL002", description="...", weight_ounces=3, is_active=False)

        url = reverse('part-bulk-delete')
        response = self.client.delete(url, data={"ids": [p1.id, p2.id]}, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Part.objects.filter(id__in=[p1.id, p2.id]).count(), 0)

    def test_top_words_endpoint(self):
        Part.objects.create(name="E1", sku="E1", description="energy energy circuit", weight_ounces=1, is_active=True)
        Part.objects.create(name="E2", sku="E2", description="module circuit energy", weight_ounces=1, is_active=True)

        url = reverse('part-top-words')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("energy", response.data)
        self.assertTrue(response.data["energy"] >= 3)
