import concurrent.futures
import requests
import argparse
import sys

def check_proxy(proxy, url, timeout):
    try:
        response = requests.get(url, proxies={"http": proxy, "https": proxy}, timeout=timeout)
        if response.status_code == 200:
            print(proxy)
    except:
        pass

def main():
    parser = argparse.ArgumentParser(description="Proxy checker script.")
    parser.add_argument(
        "--url",
        type=str,
        default="https://google.com",
        help="The URL to check proxies against (default: https://google.com).",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=1,
        help="Timeout for proxy check in seconds (default: 1).",
    )
    parser.add_argument(
        "--threads",
        type=int,
        default=100,
        help="Number of threads to use (default: 100).",
    )
    args = parser.parse_args()

    # Read proxies from stdin
    proxies = [line.rstrip() for line in sys.stdin]

    # Run checks with ThreadPoolExecutor
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.threads) as executor:
        results = [executor.submit(check_proxy, proxy, args.url, args.timeout) for proxy in proxies]

        for future in concurrent.futures.as_completed(results):
            result = future.result()
            if result is not None:
                print(result)

if __name__ == "__main__":
    main()
