from django.urls import path
from .views import ViewAllBalances

urlpatterns = {
	path('',ViewAllBalances.as_view())
}