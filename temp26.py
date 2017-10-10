# 윈도우 시스템 명령을 사용하기 위해 os , 시간을 알기 위해 time
import os
import time

# 윈도우 OS 를 기준으로 프로그램
source = ['"C:\\Dev"', 'C:\\Code']
target_dir = 'D:\\Backup'

# os.sep 는 "\\" 이고, '%Y%m%d%H%M%S' 는 '연도+월+일+시간+분+초'
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

# 만약 백업파일을 저장할 디렉토리가 없으면 디렉토리를 만든다.
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

# 명령창(cmd) 에서 zip 명령을 수행하기 위한 문자열
# -r 은 하위 디렉토리까지 포함하는 옵션
zip_command = "zip -r {0} {1}".format(target, ' '.join(source))

# 백업을 수행
print("Zip command is:")
print(zip_command)
print("Running:")

if os.system(zip_command)==0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')
