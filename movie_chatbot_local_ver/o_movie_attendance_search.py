from bs4 import BeautifulSoup
import urllib.request as req
from urllib.request import Request, urlopen
# import requests


def movie_attendance_search(keyword):
    url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query="
    str_keyword = str(keyword.encode('utf-8'))[2:-1].replace('\\x', '%')
    plus = "+"
    total_attendance = "영화"
    str_total_attendance = str(total_attendance.encode('utf-8'))[2:-1].replace('\\x', '%')
    url = url + str_total_attendance + plus + str_keyword
    hdr = {'User-Agent': 'Mozilla/5.0'}
    requ = Request(url, headers=hdr)

    res = req.urlopen(requ)
    soup = BeautifulSoup(res, 'html.parser')
    people = soup.select_one("div > dl > dt#dss_h_movie_info_total_audience + dd > span")

    if people is None:
        print("해당 영화 '"+ keyword +"'에 대한 누적관객수 정보가 없습니다.")
    else:
        print("영화 '" + keyword + "'의 누적관객수 정보입니다. " + people.text)
