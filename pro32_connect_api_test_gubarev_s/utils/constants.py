BASE_URL = "https://getscreen.dev"
LOGIN_URL = f"{BASE_URL}/api/login"
PROFILE_UPDATE_URL = f"{BASE_URL}/api/dashboard/settings/account/update"
PROFILE_INFO_URL = f"{BASE_URL}/api/dashboard/settings/account"

headers = {
    'accept': '*/*',
    'accept-language': 'ru,en;q=0.9',
    'baggage': 'sentry-environment=production,sentry-release=1.123.1541,sentry-public_key=967773317b8139507b103b18d6840bfa,sentry-trace_id=f068832e760446f28016504e3ce0a2e3,sentry-sample_rate=1,sentry-sampled=true',
    'cache-control': 'no-cache',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': BASE_URL,
    'pragma': 'no-cache',
    'priority': 'u=1, i',
    'referer': f'{BASE_URL}/panel/login',
    'sec-ch-ua': '"Chromium";v="134", "Not:A-Brand";v="24", "YaBrowser";v="25.4", "Yowser";v="2.5"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sentry-trace': 'aa591bb2e15442d092c8bc5b8f729901-880398b1c6706b2a-1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 YaBrowser/25.4.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}
