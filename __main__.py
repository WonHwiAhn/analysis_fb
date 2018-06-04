import collection
import analyze
import visualize

if __name__ == '__main__':
    items = [
        {'pagename': 'jtbcnews', 'since': '2018-05-01', 'until': '2018-05-31'},
        {'pagename': 'chosun', 'since': '2018-05-01', 'until': '2018-05-31'}
    ]

    # collection
    for item in items:
        resultfile = collection.crawling(**item)
        item['resultfile'] = resultfile


    # analyze 파일을 읽어서 분석
    for item in items:
        print(item['resultfile'])

    # visualization

