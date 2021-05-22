from django.urls import path
from django.views.generic import TemplateView
from main import views

app_name = 'main'

urlpatterns = [

    path('', TemplateView.as_view(template_name="home.html"), name='home'),
    path('about-us/', TemplateView.as_view(template_name="about_us.html"), name='about_us'),
	path('contact-us/', views.ContactUsView.as_view(), name="contact_us"),
	path('products/<str:tag>/', views.ProductListView.as_view(), name='products'),
	path('product/<slug:slug>/', views.ProductDetailView.as_view(), name="product")
]