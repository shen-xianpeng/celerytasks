from app import accept_argument

big_data = "A" * 1024 * 1024 * 8

accept_argument.delay(big_data)
accept_argument.delay(big_data)