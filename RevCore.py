from com_win import gathering_info
import  com_gen
from com_linux import gathering

gt = gathering_info()
gen = com_gen
gl = gathering()

sandbox = 0
if gen.command() == "Windows":
    print(gen.release())
    print(gt)

if gen.check_cpu()["count"] == 0.0:
    sandbox += 1

if gen.check_cpu()["percent"] == 0:
    sandbox += 1

if len(gen.check_drive()) < 2:
    sandbox += 1

if gen.check_battery() == "None":
    sandbox += 1

if gen.c_drive() < 4:
    sandbox += 1

print(gen.check_id())
print(gen.system_information())
print(gen.check_ip())

percent = int((sandbox / 5) * 100)
print(f"{percent}% possibility for sandbox")



