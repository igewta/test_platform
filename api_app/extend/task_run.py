class 
if params != '':
			try:
				data = json.loads(params.replace("'", "\""))
			except :
				return resp_fail(f'参数：{params} 不是dict 格式')

		if header != '':
			try:
				head_json = json.loads(header.replace("'","\""))
			except :
				return resp_fail(f'header：{header} 不是dict 格式')

		if method == 'get':
			if params == '' and header == '' :
				r = requests.get(url)
			elif params == '' and header != '' :
				r = requests.get(url, headers=head_json)
			elif params != '' and header == '':
				r = requests.get(url, params = data)
			else:
				r = requests.get(url, params = data, headers=head_json)

		if method == 'post':
			if params == '':
				if header == '' :
					r = requests.post(url)
				else:
					r = requests.post(url, headers=head_json)
			else:
				if datatpye == 'form':
					if header == '':
						r = requests.post(url, data = data)
					else:
						r = requests.post(url, data = data, headers=head_json)
				if datatpye == 'json':
					if header == '':
						r = requests.post(url, json = data)
					else:
						r = requests.post(url, json = data, headers=head_json)