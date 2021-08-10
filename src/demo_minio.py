import threading
import os
import time
import subprocess

# export MINIO_ROOT_USER=minio_credential MINIO_ROOT_PASSWORD=minio_credential
os.putenv("MINIO_ROOT_USER", "minio_credential")
os.putenv("MINIO_ROOT_PASSWORD", "minio_credential")


def start_minio():
    os.system('minio server --console-address ":9001" /Users/zheng/Desktop/minio_data')


def stop_minio():
    print("add alias")
    subprocess.run(
        "mc alias set myminio http://localhost:9000 minio_credential minio_credential", shell=True
    )
    print("shutting")
    subprocess.run("mc admin service stop myminio", shell=True)
    print("finished")


x = threading.Thread(target=start_minio, daemon=True)
x.start()

i = 0
while i < 5:
    time.sleep(5)
    print(i)
    i += 1

stop_minio()
