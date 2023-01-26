from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime, timedelta
from apps.users.models import User
from apps.boards.models import Board

class UserGenderStatisticView(APIView):
    """
    유저의 남녀 수를 확인합니다.
    """
    def get(self, request):
        male_cnt = User.objects.filter(gender="Male").count()
        female_cnt = User.objects.filter(gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)

class UserAgeStatisticView(APIView):
    """
    유저의 (국제기준) 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                User.objects
                .filter(birth_date__range=[datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31,23,59,59)])
                .distinct()
                .count()
            )
            if i == 0:
                age_key = '10대 미만 유저 수'
            else:
                age_key = str(i * 10) + '대 유저 수'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)


class BoardGenderStatisticView(APIView):
    """
    게시판에서 남녀의 분포를 확인합니다.
    """
    def get(self, request):
        male_cnt = Board.objects.filter(user__gender="Male").count()
        female_cnt = Board.objects.filter(user__gender="Female").count()
        return Response({"male_count": male_cnt, "female_count": female_cnt}, status=status.HTTP_200_OK)


class BoardAgeStatisticView(APIView):
    """
    게시판에서의 나이대 분포를 확인합니다.
    """
    def get(self, request):
        result = {}
        this_year=datetime.today().year
        for i in range(10):
            age_num = (
                Board.objects.select_related("user")
                .filter(user__birth_date__range=[datetime(this_year-((i+1)*10)+1,1,1), datetime(this_year - (i*10),12,31,23,59,59)])
                .distinct()
                .values_list("user")
                .count()
            )
            if i == 0:
                age_key = '10대 미만 유저 게시물 수'
            else:
                age_key = str(i * 10) + '대 유저 게시물 수'

            result[age_key] = age_num

        return Response({"result": result}, status=status.HTTP_200_OK)