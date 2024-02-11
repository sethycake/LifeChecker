import socket
import pystyle
from pystyle import Colors, Colorate
import requests

print(Colorate.Vertical(Colors.blue_to_cyan,'''                                 ('-.                    ('-. .-.   ('-.             .-. .-')     ('-.  _  .-')   
                              _(  OO)                  ( OO )  / _(  OO)            \  ( OO )  _(  OO)( \( -O )  
 ,--.      ,-.-')    ,------.(,------.         .-----. ,--. ,--.(,------.   .-----. ,--. ,--. (,------.,------.  
 |  |.-')  |  |OO)('-| _.---' |  .---'        '  .--./ |  | |  | |  .---'  '  .--./ |  .'   /  |  .---'|   /`. ' 
 |  | OO ) |  |  \(OO|(_\     |  |            |  |('-. |   .|  | |  |      |  |('-. |      /,  |  |    |  /  | | 
 |  |`-' | |  |(_//  |  '--. (|  '--.        /_) |OO  )|       |(|  '--.  /_) |OO  )|     ' _)(|  '--. |  |_.' | 
(|  '---.',|  |_.'\_)|  .--'  |  .--'        ||  |`-'| |  .-.  | |  .--'  ||  |`-'| |  .   \   |  .--' |  .  '.' 
 |      |(_|  |     \|  |_)   |  `---.      (_'  '--'\ |  | |  | |  `---.(_'  '--'\ |  |\   \  |  `---.|  |\  \  
 `------'  `--'      `--'     `------'         `-----' `--' `--' `------'   `-----' `--' '--'  `------'`--' '--' 
»-----------------------------------------------•--------------------------------------------------------------«
  {1}IP INFO                                                                  {3}WEBSITE IP CHECKER 
  {2}HOST CHECKER                                                             {4}Credits '''))

choice = input(Colorate.Vertical(Colors.blue_to_cyan,''' 
  -o>'''))


def life():
 print(Colorate.Vertical(Colors.blue_to_cyan,'''
                         

                                ('-.                    ('-. .-.   ('-.             .-. .-')     ('-.  _  .-')   
                              _(  OO)                  ( OO )  / _(  OO)            \  ( OO )  _(  OO)( \( -O )  
 ,--.      ,-.-')    ,------.(,------.         .-----. ,--. ,--.(,------.   .-----. ,--. ,--. (,------.,------.  
 |  |.-')  |  |OO)('-| _.---' |  .---'        '  .--./ |  | |  | |  .---'  '  .--./ |  .'   /  |  .---'|   /`. ' 
 |  | OO ) |  |  \(OO|(_\     |  |            |  |('-. |   .|  | |  |      |  |('-. |      /,  |  |    |  /  | | 
 |  |`-' | |  |(_//  |  '--. (|  '--.        /_) |OO  )|       |(|  '--.  /_) |OO  )|     ' _)(|  '--. |  |_.' | 
(|  '---.',|  |_.'\_)|  .--'  |  .--'        ||  |`-'| |  .-.  | |  .--'  ||  |`-'| |  .   \   |  .--' |  .  '.' 
 |      |(_|  |     \|  |_)   |  `---.      (_'  '--'\ |  | |  | |  `---.(_'  '--'\ |  |\   \  |  `---.|  |\  \  
 `------'  `--'      `--'     `------'         `-----' `--' `--' `------'   `-----' `--' '--'  `------'`--' '--' 
»-----------------------------------------------•--------------------------------------------------------------«
  {1}IP INFO                                                                  {3}WEBSITE IP CHECKER 
  {2}HOST CHECKER                                                             {4}Credits                        '''))
 choice = input(Colorate.Vertical(Colors.blue_to_cyan,''' o> '''))





def opt_1():

 def get_ip_info_with_coordinates(ip_address):
     url = f"http://ipinfo.io/{ip_address}/json"
     response = requests.get(url)
     
     if response.status_code == 200:
         data = response.json()
         return data
     else:
         return None
 ip_address = input(Colorate.Horizontal(Colors.blue_to_cyan,''' Ip address ->'''))
 ip_info = get_ip_info_with_coordinates(ip_address)

 if ip_info:
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Coordinates: {ip_info.get('loc', 'N/A')}'''))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Hostname: {ip_info.get('hostname', 'N/A')}'''))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' City: {ip_info.get('city', 'N/A')}'''))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Region: {ip_info.get('region', 'N/A')}'''))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Country: {ip_info.get('country', 'N/A')}'''))
    print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Organization: {ip_info.get('org', 'N/A')}'''))
 else:
     print(Colorate.Horizontal(Colors.blue_to_cyan,f''' Unable to retrieve information for IP address: {ip_address}'''))
     input(Colorate.Horizontal(Colors.blue_to_cyan,''' Press enter to leave'''))
if choice == "1":
   opt_1()

  




 
def opt_4():
  print(Colorate.Horizontal(Colors.blue_to_cyan, '''Made by Primex '''))
  print(Colorate.Horizontal(Colors.blue_to_cyan, '''Check out our tool, ImportMonster: https://discord.gg/3batENggTz '''))
  choice = input(Colorate.Horizontal(Colors.blue_to_cyan, '''Send any letter to continue> '''))





   


def opt_2():
 def is_host_reachable(host, port):
     try:
         socket_obj = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
         socket_obj.settimeout(5)
         socket_obj.connect((host, port))

         return True
     except (socket.timeout, ConnectionRefusedError):
         return False
     finally:
         socket_obj.close()

 if __name__ == "__main__":
     host = input(Colorate.Horizontal(Colors.blue_to_cyan,''' Enter the host or IP address to check: '''))
     port = int(input(Colorate.Horizontal(Colors.blue_to_cyan,''' Enter the port to check: ''')))
 
     if is_host_reachable(host, port):
         print(Colorate.Horizontal(Colors.blue_to_cyan,f''' {host}:{port} is reachable.'''))
         input(Colorate.Horizontal(Colors.blue_to_cyan,''' Press enter to leave... '''))
         
     else:
         print(Colorate.Horizontal(Colors.blue_to_cyan,f''' {host}:{port} is not reachable.'''))
         input(Colorate.Horizontal(Colors.blue_to_cyan,''' Press enter to leave... '''))

def opt_3():
 def get_ip_address(url):
     try:
         ip_address = socket.gethostbyname(url)
         return ip_address
     except socket.gaierror:
         return "Unable to resolve the host."

 if __name__ == "__main__":
     website_url = input(Colorate.Horizontal(Colors.blue_to_cyan,'''Enter the website URL to check its IP address:'''))
 
     ip_address = get_ip_address(website_url)
     print(Colorate.Horizontal(Colors.blue_to_red,f'''The IP address of <{website_url}> is <{ip_address}>'''))
     input(Colorate.Horizontal(Colors.blue_to_cyan,''' Press enter to leave...'''))



if choice == "1":
    opt_1()       
if choice == "4":
    opt_4()

if choice == "2":
   opt_2()
if choice == "3":
   opt_3()

else:
  exit