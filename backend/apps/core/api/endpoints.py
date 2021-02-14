from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from apps.core.api.serializers import SolutionSerializer
from apps.core.models import Solution
from apps.services.solution_checker import SolutionCheckerAPI

api = SolutionCheckerAPI()


@api_view()
def ping(request):
    return Response("ok")


class SolutionList(generics.ListCreateAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer

    def create(self, request, *args, **kwargs):
        solution_serializer = self.serializer_class(data=request.data)

        if not solution_serializer.is_valid():
            return Response(data=solution_serializer.errors, status=HTTP_400_BAD_REQUEST)

        checker_id = api.submit_solution(solution_serializer.validated_data['code'])

        new_solution = solution_serializer.save(checker_identifier=checker_id)

        response_data = {
            'solution_id': new_solution.id,
            'status': new_solution.status,
        }

        return Response(data=response_data, status=HTTP_201_CREATED)


class SolutionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Solution.objects.all()
    serializer_class = SolutionSerializer


@api_view()
def get_last_user_solution(request):
    solution = Solution.objects.last()  # could be filtered by User, but we don't have user system in this test task

    solution_serializer = SolutionSerializer(instance=solution)

    return Response(data=solution_serializer.data)


@api_view()
def check_solution_status(request, solution_id):
    solution = Solution.objects.get(id=solution_id)

    solution_serializer = SolutionSerializer(instance=solution)

    return Response(data=solution_serializer.data)
