import ntplib
import time

def sntp_client():
    try:
        client = ntplib.NTPClient()
        response = client.request('pool.ntp.org')

        # convert incoming timestamp into readable date and time
        print(f"Time received from server: {time.ctime(response.tx_time)}")
    
    except Exception as e:
        print(f"Time information can not be received. Details: {e}")

if __name__ == '__main__':
    sntp_client()