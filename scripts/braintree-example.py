import braintree

braintree.Configuration.configure(braintree.Environment.Sandbox,
                                  merchant_id="d6hqgmhcykpd4s5m",
                                  public_key="t88bv49fx3gd5m8x",
                                  private_key="e4cd88b05f74ed6cd8bd82a60d34f230")


print "client token=", braintree.ClientToken.generate()