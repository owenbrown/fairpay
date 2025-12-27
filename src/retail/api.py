from datetime import datetime, timezone
from pathlib import Path

from django.http import HttpRequest
from ninja import File, Form, NinjaAPI
from ninja.files import UploadedFile

from .models import PriceTag, Receipt, StoreVisit

api = NinjaAPI()

IMAGE_STORAGE_DIR = Path.home() / "code/appdata/fairpay/images/pricetag"
RECEIPT_STORAGE_DIR = Path.home() / "code/appdata/fairpay/images/receipt"


@api.post("/pricetag")
def create_pricetag(
    request: HttpRequest,
    store_visit_id: int = Form(...),
    image: UploadedFile = File(...),
):
    if not request.user.is_authenticated:
        return 401, {"detail": "Authentication required"}

    store_visit = StoreVisit.objects.filter(
        id=store_visit_id,
        user=request.user,
    ).first()
    if not store_visit:
        return 404, {"detail": "Store visit not found"}

    IMAGE_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).isoformat()
    filename = f"{request.user.id}__{timestamp}"
    file_path = IMAGE_STORAGE_DIR / filename

    with file_path.open("wb") as output:
        for chunk in image.chunks():
            output.write(chunk)

    pricetag = PriceTag.objects.create(
        uploaded_by=request.user,
        image_storage_location=str(file_path),
        store_visit=store_visit,
    )

    return {
        "pricetag_id": pricetag.id,
        "pricetag_created_at": pricetag.created_at.isoformat(),
    }


@api.post("/receipt")
def create_receipt(
    request: HttpRequest,
    store_visit_id: int = Form(...),
    image: UploadedFile = File(...),
):
    if not request.user.is_authenticated:
        return 401, {"detail": "Authentication required"}

    store_visit = StoreVisit.objects.filter(
        id=store_visit_id,
        user=request.user,
    ).first()
    if not store_visit:
        return 404, {"detail": "Store visit not found"}

    RECEIPT_STORAGE_DIR.mkdir(parents=True, exist_ok=True)

    timestamp = datetime.now(timezone.utc).isoformat()
    filename = f"{request.user.id}__{timestamp}"
    file_path = RECEIPT_STORAGE_DIR / filename

    with file_path.open("wb") as output:
        for chunk in image.chunks():
            output.write(chunk)

    receipt = Receipt.objects.create(
        uploaded_by=request.user,
        image_storage_location=str(file_path),
        store_visit=store_visit,
    )

    return {
        "receipt_id": receipt.id,
        "receipt_created_at": receipt.created_at.isoformat(),
    }
