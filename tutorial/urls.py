from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings

from Account.views import (registration_view, logout_view, login_view, account_view, must_authenticate_view)

urlpatterns = [
	path('must_authenticate/', must_authenticate_view, name="home"),
    path('admin/', admin.site.urls),
    path('account/', account_view, name="account"),
    path('login/', login_view, name="login"),
    path('logout/', logout_view, name="logout"),
    path('must_authenticate/', must_authenticate_view, name="must_authenticate"),
    path('register/', registration_view, name="register"),
    path('blog/', include('Post.urls', 'post')),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
