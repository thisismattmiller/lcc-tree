import json

import re


lcc_data = json.load(open('lcc.json'))
lcc_reg = re.compile(r'([A-Z]+)([0-9]+)')

hierarchy = {
  'A':{'code':'A', 'subject':'General Works','count':0,'children':{}},
  'B':{'code':'B', 'subject':'Philosophy, Psychology, Religion','count':0,'children':{}},
  'C':{'code':'C', 'subject':'Auxiliary Sciences of History (General)','count':0,'children':{}},
  'D':{'code':'D', 'subject':'World History (except American History)','count':0,'children':{}},
  'E':{'code':'E', 'subject':'American History','count':0,'children':{}},
  'F':{'code':'F', 'subject':'Local History of the United States and British, Dutch, French, and Latin America','count':0,'children':{}},
  'G':{'code':'G', 'subject':'Geography, Anthropology, Recreation','count':0,'children':{}},
  'H':{'code':'H', 'subject':'Social Sciences','count':0,'children':{}},
  'J':{'code':'J', 'subject':'Political Science','count':0,'children':{}},
  'K':{'code':'K', 'subject':'Law','count':0,'children':{}},
  'L':{'code':'L', 'subject':'Education','count':0,'children':{}},
  'M':{'code':'M', 'subject':'Music','count':0,'children':{}},
  'N':{'code':'N', 'subject':'Fine Arts','count':0,'children':{}},
  'P':{'code':'P', 'subject':'Language and Literature','count':0,'children':{}},
  'Q':{'code':'Q', 'subject':'Science','count':0,'children':{}},
  'R':{'code':'R', 'subject':'Medicine','count':0,'children':{}},
  'S':{'code':'S', 'subject':'Agriculture','count':0,'children':{}},
  'T':{'code':'T', 'subject':'Technology','count':0,'children':{}},
  'U':{'code':'U', 'subject':'Military Science','count':0,'children':{}},
  'V':{'code':'V', 'subject':'Naval Science','count':0,'children':{}},
  'Z':{'code':'Z', 'subject':'Bibliography, Library Science','count':0,'children':{}}
}

lcc_counts = json.load(open('lcc_count.json'))

for lcc_key in lcc_counts:

	cl = lcc_reg.search(lcc_key)
	if cl != None:
		
		alpha = cl.group(1)
		num = int(cl.group(2))

		if alpha in lcc_data:
			options = []
			for a in lcc_data[alpha]:
				if num >= a['start'] and num <= a['stop']:

					options.append(a)


			if len(options) > 0:
					
				# print(len(options))
				a = options[0]
				for aa in options:
					if len(aa['parents']) > len(a['parents']):
						a = aa

				# find the top lvl
				top = a['prefix'][0]
				last_parent = hierarchy[top]['children']
				hierarchy[top]['count']+=lcc_counts[lcc_key]
				for p in a['parents']:
					if p not in last_parent:

						for x in lcc_data:
							for xx in lcc_data[x]:
								if p == xx['id']:

									label = xx['subject']

						last_parent[p] = {'code':p, 'subject':label,'count':0,'children':{}}

					last_parent[p]['count']+=lcc_counts[lcc_key]

					last_parent = last_parent[p]['children']

				if a['id'] not in last_parent:
					last_parent[a['id']] = {'code':a['id'], 'subject':a['subject'],'count':0,'children':{}}

				last_parent[a['id']]['count']+=lcc_counts[lcc_key]



listbased = {
	"name": "root",
 	"children": [],
 	'value':0
}

for l1 in hierarchy:
	l1item = {'name':hierarchy[l1]['subject'], 'code': hierarchy[l1]['code'], 'value': hierarchy[l1]['count'], 'children':[]}


	# children = listbased[l1]['children']

	listbased['children'].append(l1item)

	listbased['value'] = listbased['value'] +  l1item['value']

	for l2 in hierarchy[l1]['children']:

		l2item = {'name':hierarchy[l1]['children'][l2]['subject'], 'code': hierarchy[l1]['children'][l2]['code'], 'value': hierarchy[l1]['children'][l2]['count'], 'children':[]}

		l1item['children'].append(l2item)


		for l3 in hierarchy[l1]['children'][l2]['children']:

			l3item = {'name':hierarchy[l1]['children'][l2]['children'][l3]['subject'], 'code':  hierarchy[l1]['children'][l2]['children'][l3]['code'] , 'value': hierarchy[l1]['children'][l2]['children'][l3]['count'], 'children':[]}

			l2item['children'].append(l3item)


			for l4 in hierarchy[l1]['children'][l2]['children'][l3]['children']:

				l4item = {'name':hierarchy[l1]['children'][l2]['children'][l3]['children'][l4]['subject'], 'code': hierarchy[l1]['children'][l2]['children'][l3]['children'][l4]['code'],  'value': hierarchy[l1]['children'][l2]['children'][l3]['children'][l4]['count'], 'children':[]}

				l3item['children'].append(l4item)


json.dump(hierarchy,open('hierarchy.json','w'),indent=2)
json.dump(listbased,open('listhierarchy.json','w'),indent=2)
