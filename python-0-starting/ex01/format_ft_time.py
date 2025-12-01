import time
from datetime import datetime


now = time.time()
print(f"Seconds  since January 1, 1970: {now:,.4f} or {now:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))