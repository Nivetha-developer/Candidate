# candidate_app/views.py
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *
from  rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from django.views.decorators.csrf import csrf_protect


class CandidateListAPIView(APIView):
    def get(self, request):
        try:
            candidates = Candidatedirectory.objects.all()
            serializer = CandidateSerializer(candidates, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response(str(e), status=status.HTTP_400_BAD_REQUEST)

    @csrf_protect
    def post(self, request):
        serializer = CandidateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CandidateDetailAPIView(APIView):
    def get(self, request, pk):
        candidate = get_object_or_404(Candidatedirectory, pk=pk)
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data)

    def put(self, request, pk):
        candidate = get_object_or_404(Candidatedirectory, pk=pk)
        serializer = CandidateSerializer(candidate, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        candidate = get_object_or_404(Candidatedirectory, pk=pk)
        candidate.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



#Using Template
def candidate_list(request):
    candidates = Candidatedirectory.objects.all()
    return render(request, 'candidate_list.html', {'candidates': candidates})

def candidate_detail(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    return render(request, 'candidate_detail.html', {'candidate': candidate})

def candidate_new(request):
    if request.method == "POST":
        form = CandidateForm(request.POST)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.save()
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form = CandidateForm()
    return render(request, 'candidate_edit.html', {'form': form})

def candidate_edit(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    if request.method == "POST":
        form = CandidateForm(request.POST, instance=candidate)
        if form.is_valid():
            candidate = form.save(commit=False)
            candidate.save()
            return redirect('candidate_detail', pk=candidate.pk)
    else:
        form = CandidateForm(instance=candidate)
    return render(request, 'candidate_edit.html', {'form': form})

def candidate_delete(request, pk):
    candidate = get_object_or_404(Candidatedirectory, pk=pk)
    candidate.delete()
    return redirect('candidate_list')

from .models import *
# Eventdetails.objects.create(event_name ="event_name" )
# Jobrequisition.objects.create(job_title  ="job_title " )
# Persona.objects.create(persona_name ="Persona" )
# Screeningmode.objects.create(mode_name ="mode_name" )
# Gender.objects.create(gender_name ="gender_name" )
# Maritalstatus.objects.create(status_name ="status_name" )
# Employeedirectory.objects.create(employee_name ="employee_name" )
# City.objects.create(city_name ="city_name" )
# Educationlevel.objects.create(level_name   ="level_name  " )
# Educationqualification.objects.create(qualification_name  ="qualification_name " )
# Educationspecialization.objects.create(specialization_name  ="specialization_name " )
# Source.objects.create(source_name  ="source_name " )
# Sourcetype.objects.create(type_name   ="type_name  " )
# Reasonforchange.objects.create(reason_name  ="reason_name " )