from datetime import datetime, timezone
from pathlib import Path

from django.http import HttpRequest
from ninja import File, NinjaAPI
from ninja.files import UploadedFile

from .models import PriceTag

api = NinjaAPI()

IMAGE_STORAGE_DIR = Path.home() / "code/appdata/fairpay/images/pricetag"


@api.post("/pricetag")
def create_pricetag(request: HttpRequest, image: UploadedFile = File(...)):
    if not request.user.is_authenticated:
        return 401, {"detail": "Authentication required"}

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
    )

    return {"pricetag_id": pricetag.id}
