grammar = {
	0 : ('Sx', [b'A_aug', b';', b'Sx'], False),
	1 : ('Sx', [b'A_sim', b';', b'Sx'], False),
	2 : ('Sx', [b'A_aug', b';'], False),
	3 : ('Sx', [b'A_sim', b';'], False),
	4 : ('Sx', [b'A_dro', b';'], False),
	5 : ('Sx', [b'Ctrl', b'Sx'], False),
	6 : ('Sx', [b'Ctrl'], False),
	7 : ('Sx', [b'Fun', b'Sx'], False),
	8 : ('Sx', [b'Fun'], False),
	9 : ('A_aug', [b'ID', b'Ao', b'Ex'], False),
	10 : ('A_sim', [b'ID', b'=', b'Ex'], False),
	11 : ('A_sim', [b'ID', b'=', b'Dc'], False),
	12 : ('Ao', [b'+='], False),
	13 : ('Ao', [b'-='], False),
	14 : ('Ao', [b'*='], False),
	15 : ('Ao', [b'/='], False),
	16 : ('Ao', [b'%='], False),
	17 : ('Ao', [b'>>='], False),
	18 : ('Ao', [b'<<='], False),
	19 : ('Ao', [b'&='], False),
	20 : ('Ao', [b'|='], False),
	21 : ('Ao', [b'^='], False),
	22 : ('Ao', [b'**='], False),
	23 : ('Ex', [b'Or_l'], False),
	24 : ('Or_l', [b'Or_l', b'||', b'And_l'], False),
	25 : ('Or_l', [b'And_l'], False),
	26 : ('And_l', [b'And_l', b'&&', b'Not_l'], False),
	27 : ('And_l', [b'Not_l'], False),
	28 : ('Not_l', [b'!', b'Not_l'], False),
	29 : ('Not_l', [b'Lx'], False),
	30 : ('Lx', [b'Lx', b'Lo', b'Or_b'], False),
	31 : ('Lx', [b'Or_b'], False),
	32 : ('Lo', [b'<'], False),
	33 : ('Lo', [b'>'], False),
	34 : ('Lo', [b'<='], False),
	35 : ('Lo', [b'>='], False),
	36 : ('Lo', [b'=='], False),
	37 : ('Lo', [b'!='], False),
	38 : ('Or_b', [b'Or_b', b'|', b'Xor_b'], False),
	39 : ('Or_b', [b'Xor_b'], False),
	40 : ('Xor_b', [b'Xor_b', b'^', b'And_b'], False),
	41 : ('Xor_b', [b'And_b'], False),
	42 : ('And_b', [b'And_b', b'&', b'Shift'], False),
	43 : ('And_b', [b'Shift'], False),
	44 : ('Shift', [b'Shift', b'>>', b'Ax'], False),
	45 : ('Shift', [b'Shift', b'<<', b'Ax'], False),
	46 : ('Shift', [b'Ax'], False),
	47 : ('Ax', [b'Ax', b'+', b'Af'], False),
	48 : ('Ax', [b'Ax', b'-', b'Af'], False),
	49 : ('Ax', [b'Af'], False),
	50 : ('Af', [b'Af', b'*', b'Ap'], False),
	51 : ('Af', [b'Af', b'%', b'Ap'], False),
	52 : ('Af', [b'Af', b'/', b'Ap'], False),
	53 : ('Af', [b'Ap'], False),
	54 : ('Ap', [b'At', b'**', b'Ap'], False),
	55 : ('Ap', [b'At'], False),
	56 : ('At', [b'Si', b'NUMBER'], False),
	57 : ('At', [b'STRING'], False),
	58 : ('At', [b'Si', b'ID'], False),
	59 : ('At', [b'Si', b'(', b'Ex', b')'], False),
	60 : ('At', [b'poi(', b'Lla', b')'], False),
	61 : ('At', [b'list(', b'Par', b')'], False),
	62 : ('Par', [b'Ex', b'Pas'], False),
	63 : ('Par', [b'\xce\xb5'], False),
	64 : ('Pas', [b',', b'Ex', b'Pas'], False),
	65 : ('Pas', [b'\xce\xb5'], False),
	66 : ('Si', [b'Si', b'+'], False),
	67 : ('Si', [b'Si', b'-'], False),
	68 : ('Si', [b'Si', b'~'], False),
	69 : ('Si', [b'\xce\xb5'], False),
	70 : ('Dc', [b'drone', b'(', b'STRING', b',', b'Lla', b')'], False),
	71 : ('Lla', [b'Ex', b',', b'Ex', b',', b'Ex'], False),
	72 : ('Fun', [b'move_to', b'(', b'ID', b',', b'Lla', b')'], False),
	73 : ('Fun', [b'rotate', b'(', b'ID', b',', b'Lla', b')'], False),
	74 : ('Ctrl', [b'For'], False),
	75 : ('Ctrl', [b'While'], False),
	76 : ('Ctrl', [b'If'], False),
	77 : ('For', [b'for', b'(', b'ID', b':', b'Ex', b',', b'Ex', b')', b'{', b'Sx', b'}'], False),
	78 : ('While', [b'while', b'(', b'Ex', b')', b'{', b'Sx', b'}'], False),
	79 : ('If', [b'if', b'(', b'Ex', b')', b'{', b'Sx', b'}', b'El'], False),
	80 : ('El', [b'else', b'{', b'Sx', b'}'], False),
	81 : ('El', [b'elif', b'(', b'Ex', b')', b'{', b'Sx', b'}', b'El'], False),
	82 : ('El', [b'\xce\xb5'], False),
}
