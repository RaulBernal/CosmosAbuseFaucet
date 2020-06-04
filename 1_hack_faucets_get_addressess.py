import json
import os
import time
from datetime import datetime

#Config

dst_chain_id = "staked-ibc-3"
json_file_wallets = dst_chain_id + "-wallets.json"
num_wallets= 2000


def create_wallets():
        file= open(json_file_wallets, "a+")
        file.write('[')
        file.close()
        for i in range(num_wallets):
                #create wallet in dst_chain
                print ("CREATING WALLETS IN: " + dst_chain_id)
                key_dst = dst_chain_id + "-wallet-" + str(i+1)
                command = "rly keys add " + dst_chain_id + " " + key_dst
                output = os.popen(command).read()
                print (output)
                chain_wallet = json.loads(output)
                address_src = chain_wallet['address']
                #faucet
                print("STEALING FROM FAUCET: " + dst_chain_id)
                command2 = "rly testnets request " + dst_chain_id + " " + key_dst
                output2 = os.popen(command2).read()
                print (output2)

                file= open(json_file_wallets, "a+")
                if i+1 == num_wallets:
                        file.write(output+"]")
                else:
                        file.write(output+',')
                file.close()

def get_coins():

        try: json_data=open(url)

        except:
                print ("Can not open file")
                result = 0
        else:
                chain = json.load(json_data)
                for lines in chain:
                        chain_id = lines.get('chain-id')
                        if chain_id != source_chain_id:
                                print ("GETTING COINS FROM: " + chain_id)
                                command = "rly testnets request " + chain_id
                                output = os.popen(command).read()
                                print (output)
                                file= open(log, "a+")
                                file.write(output)
                                file.close()

if __name__ == "__main__":
        create_wallets()
        print("Done!")
