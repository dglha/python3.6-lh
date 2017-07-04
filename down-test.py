from tqdm import tqdm
import time

for x in tqdm(range(1000)):
	time.sleep(0.005)

print("Download succesfully!")