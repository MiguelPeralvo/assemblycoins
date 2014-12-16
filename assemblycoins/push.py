import transactions


def send_btc(from_addr, from_private, destination_address, btc_value):
     fee=os.environ['STANDARD_BTC_FEE']

     tx=transactions.make_raw_transaction(public_address,amount,destination, fee)
     try:
         tx2=transactions.sign_tx(tx, private_key)
     except:
         tx2=''
     tx3=transactions.pushtx(tx2)
     print "SENT BTC"
     print tx3
