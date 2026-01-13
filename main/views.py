from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import CreateAPIView
from django.shortcuts import get_object_or_404

from .models import JobOpening, JobDetail, ContactMessage
from .serializers import JobOpeningSerializer, JobDetailSerializer,ContactMessageSerializer

class JobOpeningListAPIView(APIView):
    def get(self, request):
        queryset = JobOpening.objects.filter(is_active=True)

        location = request.query_params.get("location")
        function = request.query_params.get("function")

        if location:
            queryset = queryset.filter(location__name__iexact=location)

        if function:
            queryset = queryset.filter(function__name__iexact=function)

        serializer = JobOpeningSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class JobDetailAPIView(APIView):
    def get(self, request, job_id):
        job_detail = get_object_or_404(JobDetail, job__id=job_id)
        serializer = JobDetailSerializer(job_detail)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

class ContactMessageCreateAPIView(CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"message": "Your message has been sent successfully."},
            status=status.HTTP_201_CREATED
        )
