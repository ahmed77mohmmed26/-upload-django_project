from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin,
    UserPassesTestMixin
)

from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView
)

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import DeleviryInformation
from .serializers import DeliverySerializer


# =========================
# CLASS-BASED VIEWS (CBV)
# =========================

# LIST VIEW (كل المستخدمين المسجلين فقط)
class HomeView(LoginRequiredMixin, ListView):
    model = DeleviryInformation
    template_name = 'delevery/home.html'
    context_object_name = 'deliveries'


# =========================
# CREATE VIEW (Staff + Admin فقط)
# =========================
class AddDeliveryView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = DeleviryInformation
    template_name = 'delevery/add.html'
    fields = ['name', 'age', 'gender', 'city', 'description']
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_staff or self.request.user.is_superuser


# =========================
# UPDATE VIEW (Staff + Admin فقط)
# =========================
class EditDeliveryView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = DeleviryInformation
    template_name = 'delevery/edit.html'
    fields = ['name', 'age', 'gender', 'city', 'description']
    success_url = reverse_lazy('home')

    permission_required = 'deleviry.change_deleviryinformation'


# =========================
# DELETE VIEW (Admin فقط)
# =========================
class DeleteDeliveryView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = DeleviryInformation
    template_name = 'delevery/delete.html'
    success_url = reverse_lazy('home')

    def test_func(self):
        return self.request.user.is_superuser


# =========================
# API VIEW (DRF)
# =========================
@api_view(['GET'])
def delivery_api(request):
    deliveries = DeleviryInformation.objects.all()
    serializer = DeliverySerializer(deliveries, many=True)
    return Response(serializer.data)