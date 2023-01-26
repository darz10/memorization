from .accounts import router as account_router
from .reminder import router as reminder_router


urlpatterns = account_router.urls + reminder_router.urls
