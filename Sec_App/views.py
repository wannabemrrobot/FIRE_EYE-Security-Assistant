from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from .functions import greet,launcher,nmapScan,check,detect_csrf,curl
from .forms import getIp,getUrl
from .dos_function import perform_dos
from .classification import classifier
import random

current = ""
current_function = ""
@csrf_exempt
def get_response(request):
	print(request.body)

	response = {}

	if request.method == 'POST':
		global current
		global current_function
		chat_response = ""
		print("\nSTART CURRENT	:",current)
		data = request.body.decode('utf-8').replace('\0', '')
		print(data)
		data = data.lower()

		positive = ["yes","yep","s","yeah"]
		negative = ["no","nope","nah"]
		functions = ["CSRF Assessment", "Port Scanning", "DOS Assessment", "Host Discovery"]

		classified_text = classifier(data)
		print(classified_text)
		#chat_response = classified_text

		if current_function == "csrf":
			current_function = ""
			chat_response = detect_csrf(data)[0]
			return HttpResponse(chat_response)

		elif current_function == "ps":
			current_function = ""
			chat_response = nmapScan(data)[0]
			return HttpResponse(chat_response)

		elif current_function == "dos":
			current_function = ""
			chat_response = perform_dos(data)[0]
			return HttpResponse(chat_response)

		elif current_function == "host":
			current_function = ""
			chat_response = curl(data)
			return HttpResponse(chat_response)


		if (data in positive) and (current in functions):

			if current == "CSRF Assessment":
				chat_response = "Provide a valid URL for performing CSRF Assessment"
				current = ""
				current_function = "csrf"
				return HttpResponse(chat_response)

			elif current == "Port Scanning":
				chat_response = "Provide a valid URL or an IP address to perform Port Scan"
				current = ""
				current_function = "ps"
				return HttpResponse(chat_response)

			elif current == "DOS Assessment":
				chat_response = "Provide a valid URL to perform DOS Assessment"
				current = ""
				current_function = "dos"
				return HttpResponse(chat_response)

			elif current == "Host Discovery":
				chat_response = "Provide an URL for performing Host Discovery"
				current = ""
				current_function = "host"
				return HttpResponse(chat_response)

		elif (data in negative) and (current in functions):

			reply=["Okay","Alright","Cool","Alright, Do you want me to perform any other task?"]
			chat_response = reply[random.randint(0, (len(reply) - 1))]
			current = ""
			return HttpResponse(chat_response)

		elif classified_text in functions:
			current = classified_text
			chat_response = "Do you want to perform {}?".format(classified_text)
		else:
			chat_response = classified_text
		print("\nEND CURRENT:",current)

	else:
		response['error'] = 'no post data found'
	print(chat_response)

	#return HttpResponse(json.dumps(response),content_type="application/json")
	return HttpResponse(chat_response)
	#return HttpResponse(chat_response)

def home(request, template_name="home.html"):
	context = {'title': 'Security Assistant Chatbot Version 1.0'}
	return render(None,template_name, context)


def tools(request):
	return render(request,'tools.html')

@csrf_exempt
def port_scanning(request):
	ip = getIp(request.POST or None)

	if ip.is_valid():
		ip_address = ip.cleaned_data['ip']
		print(ip_address)
		if check(ip_address) ==1:
			ans = nmapScan(ip_address)[1]
			print(ans)
			context = {}
			context["response"] = ans
		else:
			return render(request,'port_scan.html',{'form':ip})
		return render(request,'port-scan-response.html', context)
	else:
		return render(request, 'port_scan.html',{'form': ip})


@csrf_exempt
def csrf_detection(request):

	url = getUrl(request.POST or None)
	if url.is_valid():
		input_url = url.cleaned_data['url']
		print(input_url)
		ans = detect_csrf(input_url)[1]
		print(ans)
		context = {}
		context["response"] = ans

		return render(request,'csrf-response.html', context)
	else:
		return render(request, 'csrf.html',{'form': url})


@csrf_exempt
def dos(request):

	url = getUrl(request.POST or None)
	if url.is_valid():
		input_url = url.cleaned_data['url']
		print(input_url)
		ans = perform_dos(input_url)[1]
		print("\n",ans)
		context = {}
		context["response"] = ans

		return render(request,'dos-response.html', context)
	else:
		return render(request, 'dos.html',{'form': url})


@csrf_exempt
def host_discovery(request):

	url = getUrl(request.POST or None)
	if url.is_valid():
		input_url = url.cleaned_data['url']
		print(input_url)
		ans = curl(input_url)
		print(ans)
		context = {}
		context["response"] = ans

		return render(request,'host-discovery-response.html', context)
	else:
		return render(request, 'host-discovery.html',{'form': url})

def envt(request):
    return HttpResponse("<h1> SAIRAM</h1>")

def base(request):
	return render(request,'base.html')