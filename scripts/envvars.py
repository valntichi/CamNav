import os


if "DEBUSSY" not in os.environ:
    # os.environ["DEBUSSY"] = "1"
    print "Not present"

if "BT_ENVIRONMENT" not in os.environ:
    os.environ["BT_ENVIRONMENT"] = "sandbox"
if "BT_MERCHANT_ID" not in os.environ:
    os.environ["BT_MERCHANT_ID"] = "d6hqgmhcykpd4s5m"
if "BT_PUBLIC_KEY" not in os.environ:
    os.environ["BT_PUBLIC_KEY"] = "t88bv49fx3gd5m8x"
if "BT_PRIVATE_KEY" not in os.environ:
    os.environ["BT_PRIVATE_KEY"] = "e4cd88b05f74ed6cd8bd82a60d34f230"

for a in os.environ:
    print  a, '=', os.getenv(a)
