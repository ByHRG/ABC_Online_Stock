import httpx
import json


class ABCMART:

    def url_setting(self, url):
        return url.split("&")[0].split("prdtNo=")[-1]

    def login(self, input):
        #로그인 처리는 비밀입니다.
        return header

    def run(self, url):
        product_code = self.url_setting(data['url'])
        if "onthespot" in data['url']:
            url = "https://www.onthespot.co.kr/"
        elif "grandstage" in data['url']:
            url = "https://grandstage.a-rt.com/"
        else:
            url = "https://abcmart.a-rt.com/"
        output = {
            "Url": f'{url}product?prdtNo={product_code}',
            "Stock": {},
        }
        # url = f"{url}product/info?prdtNo=" + product_code

        header = self.login(data)
        req = httpx.get(f"https://abcmart.a-rt.c비밀APINo={product_code}", headers=header).json()
        size = req["productOption"][0]["optnName"]

        url = f"{url}cart비밀API?prdtNo={product_code}&orderQty=0&mmnyPrdtYn=Y&optnAddAmt=0&clickTabId=All&layerType=Cart&dailyDlvyYn=N&prdtOptnNo={size}"
        req = httpx.get(url, headers=header).json()["prdtOptList"]
        for i in req:
            data = {str(i["optnName"]): str(i["orderPsbltQty"])}
            output["Stock"].update(data)
        return output

data = {
    'url':'제품 URL',
    'id':'ABC계정',
    'pw': 'ABC암호'
}

print(json.dumps(ABCMART().run(data), ensure_ascii=False, indent=4))
