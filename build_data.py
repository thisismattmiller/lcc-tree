from pymarc import MARCReader
import glob
import multiprocessing
import tqdm
import json

# pip3 install pymarc tqdm

path = './*.mrc'

def process_file(f):

	results = {}

	with open(f, 'rb') as fh:

		reader = MARCReader(fh)	

		# try:
		for record in reader:			
			if '050' in record:
				if 'a' in record['050']:
					# might want to change this stuff, 

					# take the first set of codes before a "."
					lcc = record['050']['a'].split('.')[0]

					# take whatever is first if there is a space
					lcc = lcc.split(' ')[0]


					if lcc not in results:
						results[lcc] = 0
					results[lcc]+=1
		# except:
		# 	print("error reading record in ", f)


	return results


if __name__ == '__main__':

	work = list(glob.glob(path))

	the_pool = multiprocessing.Pool(multiprocessing.cpu_count())

	all_results = {}

	for one_file_results in tqdm.tqdm(the_pool.imap_unordered(process_file, work), total=len(work)):  
		
		for k in one_file_results:

			if k not in all_results:
				all_results[k] =one_file_results[k]
			else:
				all_results[k] = all_results[k] + one_file_results[k]
	
	
		json.dump(all_results,open('lcc_count.json','w'),indent=2)

	the_pool.close()
	the_pool.join()

