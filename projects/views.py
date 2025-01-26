from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action

from .models import Todos
from .serializers import TodoSerializer  # Assuming you have a TodoSerializer instead of SampleSerializer
from bson import ObjectId

class TodoViewSet(viewsets.ViewSet):
    
    lookup_value_regex = '[0-9a-fA-F]{24}'  # Add this line to match ObjectId pattern


    # List all todos
    def list(self, request):
        print(request);
        todos = Todos.objects.all()
        serializer = TodoSerializer(todos, many=True)
        return Response(serializer.data)

    # Create a new todo
    def create(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Retrieve a specific todo

    def retrieve(self, request, pk=None):
        try:
            todo = Todos.objects.get(_id=ObjectId(pk))
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except (Todos.DoesNotExist, InvalidId):
            return Response(
                {"error": "Todo not found"}, 
                status=status.HTTP_404_NOT_FOUND
            )

    # Update a todo with query parameters

    @action(detail=True, methods=['put'])
    def todo_update(self, request, pk=None):
        try:
            # Use _id and ObjectId for MongoDB
            todo = Todos.objects.get(_id=ObjectId(pk))
        except (Todos.DoesNotExist, InvalidId):
            return Response(
                {"error": "Todo not found or invalid ID"}, 
                status=status.HTTP_404_NOT_FOUND
            )

        # Get data from query parameters if available, else fallback to the request body
        name = request.query_params.get('name', request.data.get('name', todo.name))
        description = request.query_params.get('description', request.data.get('description', todo.description))
        project = request.query_params.get('project', request.data.get('project', todo.project))
        status_value = request.query_params.get('status', request.data.get('status', todo.status))

        # Validate status value against choices
        valid_statuses = ['pending', 'in_progress', 'completed']
        if status_value not in valid_statuses:
            return Response(
                {"error": f"Invalid status. Must be one of: {', '.join(valid_statuses)}"}, 
                status=status.HTTP_400_BAD_REQUEST
            )

        # Update the todo instance
        todo.name = name
        todo.description = description
        todo.project = project
        todo.status = status_value

        # If you're using assigned_users, uncomment and modify these lines
        # assigned_users = request.query_params.get('assigned_users', request.data.get('assigned_users', []))
        # if assigned_users:
        #     # Convert string of comma-separated values to list if needed
        #     if isinstance(assigned_users, str):
        #         assigned_users = [user.strip() for user in assigned_users.split(',')]
        #     todo.assigned_users.set(assigned_users)

        try:
            # Save the updated todo
            todo.save()
            
            # Serialize the updated todo
            serializer = TodoSerializer(todo)
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
    # Delete a todo
    def destroy(self, request, pk=None):
        try:
            todo = Todos.objects.get(pk=pk)
        except Todos.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
            
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
