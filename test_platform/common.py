from django.http import JsonResponse

def resp_success(message='请求成功',data=[]):
	content = {
		'success':'true',
		'message':message,
		'data':data,
		}
	return JsonResponse(content)

def resp_fail(message='请求失败'):
	content = {
		'success':'false',
		'message':message,
		}
	return JsonResponse(content)