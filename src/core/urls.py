from django.urls import path

from core.views import (
    home,
    error_400,
    error_404,
    error_403,
    error_429,
    error_500,
    error_503,
)


app_name = "core"

urlpatterns = [
    path("", home, name="index")
]

handler400 = error_400
handler403 = error_403
handler404 = error_404
handler429 = error_429
handler500 = error_500
handler503 = error_503
