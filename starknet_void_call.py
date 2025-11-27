import requests, time

def void_call():
    print("Starknet — A Void Call Just Echoed Through the Cairo Void")
    seen = set()
    while True:
        r = requests.get("https://api.starkscan.co/v0/transactions?limit=40")
        for tx in r.json().get("data", []):
            h = tx["tx_hash"]
            if h in seen: continue
            seen.add(h)

            # Detect self-destruct / account suicide on Starknet
            if tx.get("entry_point_selector") != "0x0289d5": continue
            if "remove" not in tx.get("calldata", [""])[0]: continue

            contract = tx["contract_address"]
            print(f"THE VOID JUST SWALLOWED A SOUL\n"
                  f"Account {contract[:14]}... executed self-destruct\n"
                  f"Hash: {h}\n"
                  f"Block: {tx['block_number']}\n"
                  f"https://starkscan.co/tx/{h}\n"
                  f"→ This Cairo contract chose permanent oblivion\n"
                  f"→ No recovery. No resurrection. Only silence.\n"
                  f"→ In Starknet, even death is provable.\n"
                  f"{'○   ●   ○   ●'*25}\n")
        time.sleep(1.6)

if __name__ == "__main__":
    void_call()
