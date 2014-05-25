import re

class IgnoreCsrfMiddleware(object):
	def process_request(self,request,**kwargs):
		if re.match(r'^/ueditor/.*$',request.path):
			request.csrf_processing_done=True
			return None

