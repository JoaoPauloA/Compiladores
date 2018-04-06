import re

STATES = ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 
		'q9', 'q10', 'q11', 'q12', 'q13', 'q14', 'q15', 'q16', 'q17',
		'q18', 'q19', 'q20', 'q21', 'q22', 'q23', 'q24', 'q25', 'q26',
		'q27', 'q28', 'q29', 'q30', 'q31', 'q32', 'q33', 'q34', 'q35', 
		'q36', 'q37', 'q38', 'q39', 'q40', 'q41']

FINALS = ['q3','q8','q39','q13', 'q16', 'q22', 'q28', 'q33']

TOKENS = ['IF', 'THEN', 'WRITE', 'ELSE', 'END', 'REPEAT', 'REPEAT', 'UNTIL', 'READ']

TRANSITIONS = [('q0','$','q1'),('q0','$','q4'),('q0','$','q9'), ('q0','$','q14'), ('q0','$','q17'),
		('q0','$','q23'), ('q0','$','q29'), ('q0','$','q34'),
		('q1','i','q2'), ('q2','f','q3'), 
		('q4','t','q5'), ('q5','h','q6'),('q6','e','q7'),('q7','n','q8'),
		('q9','e','q10'), ('q10','l','q11'),('q11','s','q12'),('q12','e','q13'),
		('q14','e','q15'), ('q15','n','q40'), ('q40','d','q16'), 
		('q17','r','q18'), ('q18','e','q19'), ('q19','p','q20'), ('q20','e','q21'),('q21','a','q41'), ('q41','t','q22'),
		('q23','u','q24'),('q24','n','q25'),('q25','t','q26'),('q26','i','q27'),('q27','l','q28'),
		('q29','r','q30'), ('q30','e','q31'), ('q31','a','q32'),('q32','d','q33'),
		('q34','w','q35'),('q35','r','q36'), ('q36','i','q37'), ('q37','t','38'), ('q38','e','q39')]

SIGMA = ['a','d','e','f','h','i','l','n','p','r','s','t','u','w']

EMPTY = '$'

def edge(s, c):
    conj = set()
    for t in TRANSITIONS:
	if s == t[0] and t[1].find(c) != -1:
	   conj.add(t[2])
    return conj

def closure(s):
    clo = set()
    for t in TRANSITIONS:
	if t[0] == s:
	    clo = clo.union(edge(t[0],EMPTY))
	if clo == set():
		return [s]
	return clo

def DFAed(d, c):
	l = closure(d)
	lst = set()
	for j in l:
		p =  edge(j,c)
		if p != set():
			lst = lst.union(p)
					
	return lst



DFAstates = []
DFAtransitions = dict()

def get(c):
	if c == set():
		return False
	for a in DFAstates:
		if a == c:
			return True

	return False		


def NFA_DFA():
	DFAstates.append(set())
	DFAstates.append(closure('q0'))
	p = 1
	j = 0
	z = -1
	while j <= p:
		for c in SIGMA:
			s = set()
			for cj in DFAstates[j]:
				e = DFAed(cj, c)
				if len(e) != 0:
					s = s.union(e)
			if len(s)==0:
				continue
			z+=1
			if get(s):
				DFAtransitions[z] = (DFAstates[j], c, s)
			else:
				p+=1
				DFAstates.append(s)
				DFAtransitions[z] = (DFAstates[j], c, s) 
		j+=1

NFA_DFA()
print DFAtransitions
print '--------------------------------------------------------------'
print DFAstates
#DFAstates.append(closure('q0'))
#print get(closure('q0'))

