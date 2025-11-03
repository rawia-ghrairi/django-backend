from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render, redirect, get_object_or_404

from .models import Project, Skills, History, Contact
from .serializers import ProjectSerializer, SkillsSerializer, HistorySerializer, ContactSerializer


# ------------------- PROJECT CRUD -------------------

@api_view(['GET', 'POST'])
def project_list(request):
    if request.method == 'GET':
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)

    if request.method == 'GET':
        serializer = ProjectSerializer(project)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = ProjectSerializer(project, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- SKILL CRUD -------------------

@api_view(['GET', 'POST'])
def skill_list(request):
    if request.method == 'GET':
        skills = Skills.objects.all()
        serializer = SkillsSerializer(skills, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = SkillsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def skill_detail(request, pk):
    skill = get_object_or_404(Skills, pk=pk)

    if request.method == 'GET':
        serializer = SkillsSerializer(skill)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SkillsSerializer(skill, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        skill.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- HISTORY CRUD -------------------
# ------------------- HISTORY CRUD -------------------
@api_view(['GET', 'POST'])
def history_list(request):
    if request.method == 'GET':
        histories = History.objects.all()
        serializer = HistorySerializer(histories, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
        serializer = HistorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def history_detail(request, pk):
    history = get_object_or_404(History, pk=pk)

    if request.method == 'GET':
        serializer = HistorySerializer(history)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = HistorySerializer(history, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        history.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ------------------- API pour React -------------------
@api_view(['POST'])
def api_create_contact(request):
    """Créer un contact depuis React via API"""
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ------------------- Backend Django -------------------
def contact_list(request):
    """Afficher tous les contacts côté backend"""
    contacts = Contact.objects.all()
    return render(request, 'listContact.html', {'contacts': contacts})
def delete_contact(request, pk):
    """Supprimer un contact depuis la page backend"""
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contact.delete()
        return redirect('listContact')
    return render(request, 'confirm_delete.html', {'contact': contact})