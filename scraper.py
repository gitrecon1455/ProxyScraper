import requests
from bs4 import BeautifulSoup
import json
import re
from urllib.parse import unquote


# def hidemy_name():
#     try:
#         headers = {
#             'cookie': 't=293933193; cf_chl_2=3922b2357e82aa5; cf_clearance=8VyslhUAl1awezSMpGamCbUUFK5GXPZBYT_biJCNupE-1674515463-0-150',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
#         }
#
#         url = 'https://hidemy.name/en/proxy-list/?type=hs#list'
#
#         response = requests.get(url, headers=headers)
#
#         if response.status_code == 200:
#             soup = BeautifulSoup(response.text, 'html.parser')
#             pagination = soup.find(class_="pagination")
#             ul = pagination.find("ul")
#
#             li = ul.find_all('li')
#             end_page = li[-2].text # will print the 2nd last li element
#
#             for i in range(1, int(end_page)+1):
#                 furl = f'https://hidemy.name/en/proxy-list/?type=hs&start={i*64}#list'
#                 response = requests.get(furl, headers=headers)
#
#                 soup = BeautifulSoup(response.text, 'html.parser')
#                 tbody = soup.find("tbody")
#                 tr = tbody.find("tr")
#                 ip = tr.find_all("td")[0].text
#                 port = tr.find_all("td")[1].text
#                 print(f"{ip}:{port}")
#     except:
#         pass
# hidemy_name()


def free_proxy_list():
    urls = ["https://free-proxy-list.net",
            "https://sslproxies.org",
            "https://free-proxy-list.net/uk-proxy.html",
            "https://us-proxy.org"]

    for url in urls:
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            tbody = soup.find("tbody")
            tr = tbody.find_all("tr")

            for td in tr:
                tds = td.find_all("td")
                ip = tds[0].text
                port = tds[1].text

                proxy = f"{ip}:{port}"
                with open("http_proxies.txt", "a") as f:
                    f.write(proxy + "\n")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

        except Exception as e:
            print(e)
free_proxy_list()


# def freeproxylists():
#     headers = {
#         'cookie': 'hl=en; userno=20230124-001857; from=google; refdomain=www.google.com; visited=2023%2F01%2F26%2014%3A30%3A04; pv=30',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
#     }
#
#     url = 'https://www.freeproxylists.net/?page=1'
#
#     response = requests.get(url, headers=headers)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     for trs in soup.find_all(class_="Odd"):
#
#         ut = unquote(trs)
#         print(ut)
# # freeproxylists()


def openproxy():
    url = "https://openproxy.space/list/http"

    try:
        response = requests.get(url)

        # Use regular expression to find IP addresses and ports
        proxys = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b', response.text)

        # Print the matches
        for proxy in proxys:
            with open("http_proxies.txt", "a") as f:
                f.write(proxy + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
openproxy()


def proxies():
    url = "https://sunny9577.github.io/proxy-scraper/proxies.json"
    try:
        response = requests.get(url)
        data = json.loads(response.text)

        for proxy in data:
            with open("http_proxies.txt", "a") as f:
                f.write(proxy["ip"] + ":" + proxy["port"] + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
proxies()


def proxyscrape():
    url = "https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all"
    try:
        response = requests.get(url)

        proxies = response.text
        proxy = '\n'.join(line for line in proxies.splitlines() if line.strip())
        with open("http_proxies.txt", "a") as f:
            f.write(proxy)

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
proxyscrape()


# working but taking too much time
# def freeproxy():
#     for page in range(1, 560):
#         url = f"https://www.freeproxy.world/?type=http&anonymity=&country=&speed=&port=&page={page}"
#
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         ips = []
#         ports = []
#         for ips_tag in soup.find_all(class_="show-ip-div"):
#             ips.append(ips_tag.text.split()[0])
#
#         for link in soup.find_all('a', href=True):
#             if "/?port" in link['href']:
#                 ports.append(link['href'].split("=")[-1])
#         if ips and ports:
#             for i, p in zip(ips, ports):
#                 print(f"{i}:{p}")
#                 with open("http_proxies.txt", "a") as f:
#                     f.write(f"{i}:{p}" + "\n")
# freeproxy()


def spys_me():
    url = "https://spys.me/proxy.txt"
    try:
        response = requests.get(url)

        proxys = re.findall(r'\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b', response.text)
        for proxy in proxys:
            with open("http_proxies.txt", "a") as f:
                f.write(proxy + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
spys_me()


# def proxy_list():
#     url2 = "https://www.proxy-list.download/proxylist.txt"
#     response2 = requests.get(url2).text
#     website_output2 = "\n".join(response2.split("\n")[2:])
#
#     url3 = "https://raw.githubusercontent.com/hendrikbgr/Free-Proxy-Repo/master/proxy_list.txt"
#     response3 = requests.get(url3).text
#     website_output3 = "\n".join(response3.split("\n")[:-1])
#     print(website_output2, website_output3)
#
#     urls = ["https://www.proxy-list.download/api/v2/get?l=en&t=http", "https://www.proxy-list.download/api/v2/get?l=en&t=https"]
#     for url in urls:
#         response = requests.get(url)
#         data = json.loads(response.text)
#
#         for proxy in data["LISTA"]:
#             print(proxy["IP"] + ":" + proxy["PORT"])
# proxy_list()


# def proxynova():
#     try:
#         url = "https://proxylist.to/http"
#
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         cls = soup.find_all(class_="prx_tr")
#
#         for cl in cls:
#             ip = cl.find(class_="t_ip").text
#             port = cl.find(class_="t_port").text
#             print(f"{ip}:{port}")
#     except Exception as e:
#         print(e)
# # proxynova()


# def proxylist():
#     url = "https://paste.fo/top"
#
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     tds = soup.find_all("td")
#
#     for td in tds:
#         links = td.find_all("a", href=True)
#         for link in links:
#             if "user" not in link["href"]:
#                 urls = "https://paste.fo" + link["href"]
#
#                 response = requests.get(urls).text
#
#                 proxies = response.split("\n")
#                 for proxy in proxies:
#                     match = re.search(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b",proxy)
#                     if match:
#                         print(match.group())
# # proxylist()


def niek():
    url = "https://niek.github.io/free-proxy-list"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')

        tbody = soup.find("tbody")
        tr = tbody.find_all("tr")

        for td in tr:
            tds = td.find_all("td")
            proxy = tds[2].text
            with open("http_proxies.txt", "a") as f:
                f.write(proxy + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
niek()


def github():
    urls = ["https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt",
            "https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/http.txt",
            "https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/https.txt",
            "https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/http.txt",
            "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt",
            "https://raw.githubusercontent.com/resource-collector/proxylist/results/all/http.proxy.txt",
            "https://raw.githubusercontent.com/resource-collector/proxylist/results/all/https.proxy.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-http.txt",
            "https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies-https.txt",
            "https://raw.githubusercontent.com/saisuiu/Lionkings-Http-Proxys-Proxies/main/free.txt",
            "https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt"]

    for url in urls:
        try:
            response = requests.get(url).text

            proxies = response.split("\n")
            for proxy in proxies:
                match = re.search(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b", proxy)
                if match:
                    with open("http_proxies.txt", "a") as f:
                        f.write(match.group() + "\n")

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

        except Exception as e:
            print(e)
github()


# def proxy_daily():
#     try:
#         url = "https://proxy-daily.com"
#
#         response = requests.get(url)
#         soup = BeautifulSoup(response.text, 'html.parser')
#
#         data = soup.find_all(class_="centeredProxyList")[1].text
#         website_output = "\n".join(data.split("\n")[:-1])
#         print(website_output)
#     except Exception as e:
#         print(e)
# proxy_daily()


def proxy11():
    url = "https://proxy11.com"
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        tbody = soup.find("tbody")
        tr = tbody.find_all("tr")

        for td in tr:
            tds = td.find_all("td")
            ip = tds[0].text
            port = tds[1].text
            with open("http_proxies.txt", "a") as f:
                f.write(f"{ip}:{port}" + "\n")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing {url}: {e}")

    except Exception as e:
        print(e)
proxy11()


def proxylists():
    urls = ["http://www.proxylists.net/http_highanon.txt",
            "https://ab57.ru/downloads/proxylist.txt",
            "https://multiproxy.org/txt_all/proxy.txt",
            "http://rootjazz.com/proxies/proxies.txt",
            "https://www.proxyscan.io/api/proxy?format=txt&ping=500&limit=10000&type=http,https"]
    for url in urls:
        try:
            response = requests.get(url).text
            website_output = "\n".join(response.split("\n")[:-1])
            proxy = '\n'.join(line for line in website_output.splitlines() if line.strip())
            with open("http_proxies.txt", "a") as f:
                f.write(proxy)

        except requests.exceptions.RequestException as e:
            print(f"Error accessing {url}: {e}")

        except Exception as e:
            print(e)
proxylists()


# working but taking too much time
# def proxyhub():
#     for x in range(1, int(100)+1):
#         headers = {
#             'cookie': f'page={x}; anonymity=all',
#             'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'
#         }
#
#         urls = ["https://proxyhub.me/en/all-http-proxy-list.html",
#                 "https://proxyhub.me/en/all-https-proxy-list.html"]
#
#         for url in urls:
#             try:
#                 response = requests.get(url, headers=headers)
#                 soup = BeautifulSoup(response.text, 'html.parser')
#
#                 tbody = soup.find("tbody")
#                 tr = tbody.find_all("tr")
#
#                 for td in tr:
#                     tds = td.find_all("td")
#                     ip = tds[0].text
#                     port = tds[1].text
#                     print(f"{ip}:{port}")
#
#             except requests.exceptions.RequestException as e:
#                 print(f"Error accessing {url}: {e}")
#
#             except Exception as e:
#                 print(e)
# proxyhub()


# def proxylist4all():
#     url = "https://www.proxylist4all.com"
#
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     # tbody = soup.find("tbody")
#     # tr = tbody.find_all("tr")
#     print(soup)
#
#     # for td in tr:
#     #     tds = td.find_all("td")
#     #     ip = tds[0].text
#     #     port = tds[1].text
#     #     print(f"{ip}:{port}")
# proxylist4all()


# def checkerproxy():
#     url = "https://checkerproxy.net/getAllProxy"
#
#     response = requests.get(url)
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     links = soup.find_all('a', href=True)
#
#     for link in links:
#         if "archive" in link["href"]:
#             url2 = "https://checkerproxy.net" + link['href']
#             response2 = requests.get(url2)
#             soup = BeautifulSoup(response2.text, 'html.parser')
# checkerproxy()


# working but taking too much time
# def proxylist_geonode():
#     for x in range(1, 21):
#         url = f"https://proxylist.geonode.com/api/proxy-list?limit=500&page={x}&sort_by=lastChecked&sort_type=desc"
#
#         try:
#             response = requests.get(url)
#             data = json.loads(response.text)
#
#             for proxy in data["data"]:
#                 print(proxy["ip"] + ":" + proxy["port"])
#
#         except requests.exceptions.RequestException as e:
#             print(f"Error accessing {url}: {e}")
#
#         except Exception as e:
#             print(e)
# proxylist_geonode()