import ntplib
import time

def get_time_string():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')
        return time.ctime(response.tx_time)
    except Exception:
        return time.ctime()

def sntp_client():
    print("SNTP Time Synchronization")
    print(f"Time received from server: {get_time_string()}")

if __name__ == '__main__':
    sntp_client()