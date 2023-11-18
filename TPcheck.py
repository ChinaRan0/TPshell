from pocs import construct_code_exec1
from pocs import construct_code_exec2
from pocs import construct_code_exec3
from pocs import construct_code_exec4
from pocs import construct_debug_rce
from pocs import invoke_func_code_exec
from pocs import lite_code_exec
from pocs import templalte_driver_rce
from pocs import session_inclde
import os
import concurrent.futures

def check_target(target):
    construct_code_exec1.check(target)
    construct_code_exec2.check(target)
    construct_code_exec3.check(target)
    construct_code_exec4.check(target)
    construct_debug_rce.check(target)
    invoke_func_code_exec.check(target)
    lite_code_exec.check(target)
    templalte_driver_rce.check(target)
    session_inclde.check(target)



if __name__ == "__main__":
    xianchengNUM = input("请输入线程数量:")
    print("请将目标放在target.txt")
    print("按回车开始检测目标")

    os.system("pause")

    with open("target.txt", 'r') as f:
        targets = f.read().splitlines()


    max_workers = int(xianchengNUM)

    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        executor.map(check_target, targets)
