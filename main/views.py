
import re
import json
import requests
from random import randint
from bs4 import BeautifulSoup
from collections import Counter
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt



CODE = "QWDCR4"
PHONE = "+71111111111"
TEST_URL = "freestylo.ru"


@csrf_exempt
def login(request):

    if request.method == "GET":
        get_to_dict = dict(request.GET.lists())
        if "phone" in get_to_dict:
            phone = request.GET['phone']
            phone_check = re.match(r'^(8|7)?\d{10}$', str(phone))
            if phone_check:
                phone_checking_code = randint(100000, 999999)
                return JsonResponse({"code": phone_checking_code})
            else:
                return JsonResponse({"status": f"Incorrect request, {phone} - is incorrect number format. Enter number in 7or8XXXXXXXXXX format"})
        else:
            return JsonResponse({"status": "Incorrect request, you need to use 'phone' in params"})
    
    if request.method == "POST":
        status_incorrect_request = {"status": "Incorrect request"}
        if request.POST:
            request_to_dict = dict(request.POST.lists())
        else: 
            request_body = request.body
            request_body_decoded = request_body.decode() 
            try:
                request_to_dict = json.loads(request_body_decoded)
            except:
                return JsonResponse(status_incorrect_request)
        if "phone" in request_to_dict and "code" in request_to_dict:
            phone = ''.join(request_to_dict['phone'])
            code = ''.join(request_to_dict['code'])

            if phone == PHONE and code == CODE: 
                return JsonResponse({"status": "OK"})
            else:
                return JsonResponse({"status": "Fail"})
        else:
            return JsonResponse({"status": "Incorrect request, you need to use 'phone' and 'code' in your request params"})
    else:
        return JsonResponse({"status":"Incorrect request, you need to use GET or POST method"})


def tags_counter(link):
    link_str = ''.join(link)
    if not link_str.startswith('http'):
        link_str = f"http://{link_str}"
    requests_get = requests.get(link_str)
    soup = BeautifulSoup(requests_get.text, "html.parser")
    tag = [tag.name for tag in soup.find_all()]
    return Counter(tag)
 

def get_structure(request):

    if request.method == "GET":
        if request.GET:
            get_queryset_dict = dict(request.GET.lists())
            if "link" in get_queryset_dict and "tags" in get_queryset_dict:
                tags_counted = tags_counter(get_queryset_dict['link'])
                seclected_tag_list = [i.split(",") for i in get_queryset_dict['tags']]
                seclected_tag_dict = {}
                for tag in seclected_tag_list[0]: 
                    seclected_tag_dict[tag] = tags_counted[tag] 
                return JsonResponse(seclected_tag_dict)            
            elif "link" in get_queryset_dict:
                all_tags_counted = tags_counter(get_queryset_dict['link'])
                return JsonResponse(all_tags_counted)
            else:             
                return JsonResponse({"status": "Incorrect request, you need to use 'link' and 'tags' in params"})
        else: 
            all_tags_counted = tags_counter(TEST_URL)
            return JsonResponse(all_tags_counted)
    else:
        return JsonResponse({"status": "Incorrect request, you need to use GET method"})


@csrf_exempt
def check_structure(request):

    if request.method == "POST":
        request_body = request.body
        request_body_decoded = request_body.decode()
        json_to_dict = json.loads(request_body_decoded)
        if "link" in request_body_decoded:          
            tags_counted = tags_counter(json_to_dict['link'])

            dict_tag_counter_output = dict(tags_counted)
            dict_tag_counter_input = json_to_dict['structure']

            set_tag_counter_output = set(dict_tag_counter_output.items())
            set_tag_counter_input = set(dict_tag_counter_input.items())
            difference = dict(set_tag_counter_input.difference(set_tag_counter_output))
            if not difference:
                return JsonResponse({"is_correct": True})
            else:
                return JsonResponse({"is_correct": False, "difference": difference})
    else:
        return JsonResponse({"status": "Incorrect request, you need to use GET method"})
