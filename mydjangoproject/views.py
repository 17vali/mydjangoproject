from rest_framework.response import Response
from rest_framework.views import APIView

class indexAPIView(APIView):

	def get(self, request):
		urls = {
			'Admin':'/admin/',
			'Products':'products/',
			'Api':'/api/',
			}

		return Response(urls)
