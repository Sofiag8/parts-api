import os
import sys
import django

sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'parts_api.settings')

django.setup()

from parts.models import Part

Part.objects.create(name="Heavy coil", sku="SDJDDH8223DHJ", description="Tightly wound nickel-gravy alloy spring", weight_ounces=22, is_active=True)
Part.objects.create(name="Reverse lever", sku="DCMM39823DSJD", description="Attached to provide inverse leverage", weight_ounces=9, is_active=False)
Part.objects.create(name="Macrochip", sku="OWDD823011DJSD", description="Used for heavy-load computing", weight_ounces=2, is_active=True)

print("Database populated with initial data.")
