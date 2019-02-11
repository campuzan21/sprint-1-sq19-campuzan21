from django.shortcuts import render
from django.http import HttpResponse
import requests, time



https://selfserve-db.up.edu/prd/bwckschd.p_get_crse_unsec?term_in=201903&sel_subj=dummy&sel_day=dummy&sel_schd=dummy&sel_insm=dummy&sel_camp=dummy&sel_levl=dummy&sel_sess=dummy&sel_instr=dummy&sel_ptrm=dummy&sel_attr=dummy&sel_subj=CS&sel_crse=&sel_title=&sel_schd=%25&sel_from_cred=&sel_to_cred=&sel_levl=%25&sel_dunt_unit=&sel_dunt_code=MTHS&sel_instr=%25&begin_hh=0&begin_mi=0&begin_ap=a&end_hh=0&end_mi=0&end_ap=a





paramslist = {
              "term_in": "201903", 
              "sel_subj": ["CS","%"],
              "sel_day": "dummy",
              "sel_schd": ["dummy","%"],
              "sel_insm": "dummy", 
              "sel_camp": "dummy", 
              "sel_levl": ["dummy","%"], 
              "sel_sess": "dummy", 
              "sel_instr": "dummy",
              "sel_ptrm": "dummy",
              "sel_attr": "dummy", 
              "sel_crse:": "", 
              "sel_title": "", 
              "sel_to_cred": "", 
              "sel_from_cred": "",
              "sel_dunt_unit": "", 
              "sel_dunt_code": "MTHS", 
              "end_mi": "0", 
              "end_hh": "0", 
              "end_ap": "a", 
              "begin_mi": "0",
              "begin_hh": "0", 
              "begin_ap": "a"
              }


def getCourses(params):
	mysession = requests.session()
	url1 = 'https://selfserve-db.up.edu/prd/bwckschd.p_disp_dyn_sched'
	#https://selfserve-db.up.edu/prd/bwckgens.p_proc_term_date
	url2 = 'https://selfserve-db.up.edu/prd/bwckschd.p_get_crse_unsec'
	header = {'Accept-Encoding': 'gzip, deflate, sdch',
				'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
				'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:60.0) Gecko/20100101 Firefox/60.'}
	
	#return mysession.post(url1, headers = header, params = {"p_calling_proc": "bwckschd.p_disp_dyn_sched", "p_term": "201903"})
	#time.sleep(5)
	return mysession.post(url2, headers = header, params=paramslist)
	
def index(request):
	return HttpResponse(getCourses(paramslist))
