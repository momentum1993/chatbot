import xml.etree.ElementTree as ET
import urllib.request


def actor_name_search(keyword):
    # KMDB- 영화목록 url
    url = "http://api.koreafilm.or.kr/openapi-data2/wisenut/search_api/search_xml.jsp?collection=kmdb_new&ServiceKey="
    key = "키 발급해야한다"
    url = url + key

    # 입력받은 line을 utf-8로 변형
    utfLine = str(keyword.encode('utf-8'))[2:-1].replace('\\x', '%')

    # 사용자 입력 + 영화목록 url
    # 제작년도 기준으로 정렬
    newLine = url+"&actor="+utfLine+"&startCount=0&listCount=100&sort=prodYear,1"
    print(newLine)
    # xml 탐색 부분.
    try:
        tree = ET.ElementTree(file=urllib.request.urlopen(newLine))
    except:
        newLine = url + "&actor=" + utfLine + "&startCount=0&sort=prodYear,1"
        tree = ET.ElementTree(file=urllib.request.urlopen(newLine))
    root = tree.getroot()  # root 노드

    if int(root[2].attrib.get('TotalCount')) == 0:
        print("배우 '"+keyword+"'에 대한 검색정보가 없습니다.")
    else:
        for i in range(0, int(root[2].attrib.get('TotalCount'))):  # 모든 제목 출력
            print(str(i+1)+".", root[2][i][3].text)