from client import HelpdeskWorkflowClient

def main():
    client = HelpdeskWorkflowClient()
    res = client.handle_reset(user_id='usr_77', service='VPN')
    print(f"Result for status: {res['status']}")

if __name__ == "__main__":
    main()
