import requests
import json
import os

def fetch_and_save():
    api_token = 'a5c609ce7e4b4bf787745e6f0b044d11'
    url = 'https://api.football-data.org/v4/matches'
    headers = {'X-Auth-Token': api_token}

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()

        # حفظ البيانات في ملف json
        with open('matches.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print("تم تحديث البيانات بنجاح!")
    except Exception as e:
        print(f"حدث خطأ: {e}")

if __name__ == "__main__":
    fetch_and_save()
