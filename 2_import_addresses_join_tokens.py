import json
import os
import pexpect  #pip3 install pexpect before run the first time
import sys
#Config
wallet_password = 'the encription password when create your first wallet: gaiacli keys add validator'
dst_chain_id = 'stacked-ibc-3'
json_file_wallets = dst_chain_id+'-wallets.json'
main_address = 'the first address you create'  #gaiacli keys add validator
amount = '990000stakedus' 

def import_wallets_tx():
	loops = 1
	try: json_data=open(json_file_wallets)
	except:
		print ("Can not open file")
		result = 0
	else:
		wallets = json.load(json_data)
		for lines in wallets:
			mnemonic = lines.get('mnemonic')
			address = lines.get('address')
			print ("IMPORTING: " + address)
			child = pexpect.spawn("gaiacli keys add node-" + str(loops) + " --recover")
			child.expect ("> Enter your bip39 mnemonic")
			child.sendline (mnemonic)
			child.expect ("passphrase:")
			child.sendline (wallet_password)
			child.interact()
			print("TX to main address: " + main_address)		
			child2 = pexpect.spawn('gaiacli tx send ' + address + ' ' + main_address + ' ' + amount + ' --gas auto -y')
			child2.expect ("Enter keyring passphrase:")
			child2.sendline (wallet_password)
			child2.expect ("Enter keyring passphrase:")
			child2.sendline (wallet_password)
			child2.interact()
			loops += 1

if __name__ == "__main__":
	import_wallets_tx()
	print("Done!")
