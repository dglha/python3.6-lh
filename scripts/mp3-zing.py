# encoding:UTF-8

import urllib2
from StringIO import StringIO
import gzip
import re
import json


def get_content_from_url_gzip(input_url):
    try:
        req = urllib2.Request(input_url, headers={'User-Agent': 'Mozilla/5.0'})
        req.add_header('Accept-encoding', 'gzip')
        response = urllib2.urlopen(req)
        if response.info().get('Content-Encoding') == 'gzip':
            buf = StringIO(response.read())
            f = gzip.GzipFile(fileobj=buf)
            content = f.read()

        return content
    except:
        return ''


def detect_data_xml(content):
    try:
        url_json = ""
        reg = re.compile('(data-xml=")(.*?)("></div>)')
        if reg.search(content):
            url_json = reg.search(content).group(2)

        url_json = "http://mp3.zing.vn" + url_json
        return url_json
    except Exception as e:
        print
        str(e)
        return ''


def get_url_mp3_from_json(input_json):
    item = {}
    url_mp3 = input_json["data"][0]["source_list"][0]
    song_name = input_json["data"][0]["name"]
    item["download_link"] = url_mp3
    item["song_name"] = song_name
    return item


def down_load_file_from_url(url, file_name):
    mp3file = urllib2.urlopen(url)
    with open(file_name, 'wb') as output:
        output.write(mp3file.read())


def download_mp3_from_url(url):
    content = get_content_from_url_gzip(url)
    url_json = detect_data_xml(content)
    content_url_json = get_content_from_url_gzip(url_json)
    json_object = json.loads(content_url_json)
    mp3_item = get_url_mp3_from_json(json_object)

    url_download = mp3_item["download_link"]
    file_name = mp3_item["song_name"] + ".mp3"

    down_load_file_from_url(url_download, file_name)


if __name__ == "__main__":
    download_mp3_from_url("http://mp3.zing.vn/bai-hat/Noi-Nay-Co-Anh-Son-Tung-M-TP/ZW79ZBE8.html")
