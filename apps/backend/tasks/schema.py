import base64
import csv
import io
import json
import logging
import os
import random
import tempfile
import time
import uuid
from datetime import timedelta
from decimal import Decimal

import pandas as pd
from celery import shared_task
from django.core.files.base import ContentFile
from faker import Faker

from apps.backend.models.schema import DynamicSchema

logger = logging.getLogger(__name__)
fake = Faker()

FIELD_TYPE_MAPPING = {
    "CharField": lambda: fake.name(),
    "TextField": lambda: fake.text(),
    "IntegerField": lambda: random.randint(1, 1000),
    "FloatField": lambda: round(random.uniform(1.0, 1000.0), 2),
    "BooleanField": lambda: random.choice([True, False]),
    "DateField": lambda: fake.date_object().isoformat(),  # <-- converted
    "DateTimeField": lambda: fake.date_time().isoformat(),  # <-- converted
    "TimeField": lambda: fake.time_object().isoformat(),  # <-- converted
    "EmailField": lambda: fake.email(),
    "URLField": lambda: fake.url(),
    "SlugField": lambda: fake.slug(),
    "UUIDField": lambda: str(uuid.uuid4()),
    "ImageField": lambda: fake.image_url(),
    "FileField": lambda: fake.file_name(category="audio", extension="mp3"),
    "DecimalField": lambda: Decimal(str(round(random.uniform(1.0, 1000.0), 2))),
    "IPAddressField": lambda: fake.ipv4(),
    "GenericIPAddressField": lambda: fake.ipv6(),
    "PhoneNumberField": lambda: fake.phone_number(),
    "BinaryField": lambda: base64.b64encode(os.urandom(10)).decode("utf-8"),
    "DurationField": lambda: str(timedelta(seconds=random.randint(60, 3600))),
    "JSONField": lambda: {"key": fake.word(), "value": fake.random_int()},
    "SmallIntegerField": lambda: random.randint(-32768, 32767),
    "PositiveIntegerField": lambda: random.randint(0, 2147483647),
    "PositiveSmallIntegerField": lambda: random.randint(0, 32767),
    "BigIntegerField": lambda: random.randint(0, 9223372036854775807),
}


@shared_task
def process_schema_task(schema_id: int) -> None:
    """Generates fake data and saves it as CSV, JSON, and XLSX files."""
    time.sleep(0.3)

    try:
        schema = DynamicSchema.objects.get(id=schema_id)
    except DynamicSchema.DoesNotExist:
        logger.error(f"Schema with ID {schema_id} does not exist.")
        return

    fields = schema.config
    count = schema.count

    data = []
    for _ in range(count):
        item = {}
        for field in fields:
            field_name = field["name"]
            field_type = field["type"]
            item[field_name] = FIELD_TYPE_MAPPING.get(field_type, lambda: None)()
        data.append(item)

    # JSON file
    json_content = ContentFile(json.dumps(data, indent=4).encode("utf-8"))
    json_filename = f"schema_{schema_id}_{int(time.time())}.json"
    schema.json.save(json_filename, json_content)

    # CSV file
    csv_output = io.StringIO()
    csv_writer = csv.DictWriter(csv_output, fieldnames=[f["name"] for f in fields])
    csv_writer.writeheader()
    csv_writer.writerows(data)
    csv_content = ContentFile(csv_output.getvalue().encode("utf-8"))
    csv_filename = f"schema_{schema_id}_{int(time.time())}.csv"
    schema.csv.save(csv_filename, csv_content)

    # XLSX file
    df = pd.DataFrame(data)
    with tempfile.NamedTemporaryFile(suffix=".xlsx") as tmp:
        df.to_excel(tmp.name, index=False)
        tmp.seek(0)
        xlsx_content = ContentFile(tmp.read())
    xlsx_filename = f"schema_{schema_id}_{int(time.time())}.xlsx"
    schema.xlsx.save(xlsx_filename, xlsx_content)

    schema.is_active = True
    schema.save()
    logger.info(f"Schema {schema_id} processed and files saved.")
