

IpPort_list=[]
conf_uuid=[]
# load list
with open('socks4_proxies.txt') as f:
    for line in f:
        ip_port = line.strip().replace(":", " ")
        # IpPort_list.append(ip_port)

        with open("proxychains4.conf", "a") as myfile:
            myfile.write(ip_port)
            myfile.close()

import subprocess
subprocess.run(["proxychains -f proxychains4.conf curl https://challenge.uccuhacker.tw/nop.php?token=MzZ8a2RkY28=_f7d663f38bc772b661937cbdd3c4a7656393952c98745bfd5455eb6bc0be09d7"])


