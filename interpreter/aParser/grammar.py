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
	23 : ('Ex', [b'Or_l'], True),
	24 : ('Or_l', [b'Or_l', b'||', b'And_l'], True),
	25 : ('Or_l', [b'And_l'], True),
	26 : ('And_l', [b'And_l', b'&&', b'Not_l'], True),
	27 : ('And_l', [b'Not_l'], True),
	28 : ('Not_l', [b'!', b'Not_l'], True),
	29 : ('Not_l', [b'Lx'], True),
	30 : ('Lx', [b'Lx', b'Lo', b'Or_b'], True),
	31 : ('Lx', [b'Or_b'], True),
	32 : ('Lo', [b'<'], True),
	33 : ('Lo', [b'>'], True),
	34 : ('Lo', [b'<='], False),
	35 : ('Lo', [b'>='], True),
	36 : ('Lo', [b'=='], True),
	37 : ('Lo', [b'!='], True),
	38 : ('Or_b', [b'Or_b', b'|', b'Xor_b'], True),
	39 : ('Or_b', [b'Xor_b'], True),
	40 : ('Xor_b', [b'Xor_b', b'^', b'And_b'], True),
	41 : ('Xor_b', [b'And_b'], True),
	42 : ('And_b', [b'And_b', b'&', b'Shift'], True),
	43 : ('And_b', [b'Shift'], True),
	44 : ('Shift', [b'Shift', b'>>', b'Ax'], True),
	45 : ('Shift', [b'Shift', b'<<', b'Ax'], True),
	46 : ('Shift', [b'Ax'], True),
	47 : ('Ax', [b'Ax', b'+', b'Af'], True),
	48 : ('Ax', [b'Ax', b'-', b'Af'], True),
	49 : ('Ax', [b'Af'], True),
	50 : ('Af', [b'Af', b'*', b'Ap'], True),
	51 : ('Af', [b'Af', b'%', b'Ap'], True),
	52 : ('Af', [b'Af', b'/', b'Ap'], True),
	53 : ('Af', [b'Ap'], True),
	54 : ('Ap', [b'At', b'**', b'Ap'], True),
	55 : ('Ap', [b'At'], True),
	56 : ('At', [b'Si', b'NUMBER'], True),
	57 : ('At', [b'STRING'], True),
	58 : ('At', [b'Si', b'ID'], True),
	59 : ('At', [b'Si', b'(', b'Ex', b')'], False),
	60 : ('At', [b'poi(', b'Lla', b')'], False),
	61 : ('At', [b'list(', b'Par', b')'], False),
	62 : ('Par', [b'Ex', b'Pas'], False),
	63 : ('Par', [b'\xce\xb5'], False),
	64 : ('Pas', [b',', b'Ex', b'Pas'], False),
	65 : ('Pas', [b'\xce\xb5'], False),
	66 : ('Si', [b'Si', b'+'], True),
	67 : ('Si', [b'Si', b'-'], True),
	68 : ('Si', [b'Si', b'~'], True),
	69 : ('Si', [b'\xce\xb5'], True),
	70 : ('Dc', [b'drone', b'(', b'STRING', b',', b'Lla', b')'], False),
	71 : ('Lla', [b'Ex', b',', b'Ex', b',', b'Ex'], False),
	72 : ('Fun', [b'move_to', b'(', b'ID', b',', b'Lla', b')'], False),
	73 : ('Fun', [b'rotate', b'(', b'ID', b',', b'Lla', b')'], False),
	74 : ('Fun', [b'print', b'(', b'Ex', b')'], False),
	75 : ('Ctrl', [b'For'], False),
	76 : ('Ctrl', [b'While'], False),
	77 : ('Ctrl', [b'If'], False),
	78 : ('For', [b'for', b'(', b'ID', b':', b'Ex', b',', b'Ex', b',', b'Ex', b')', b'{', b'Sx', b'}'], False),
	79 : ('While', [b'while', b'(', b'Ex', b')', b'{', b'Sx', b'}'], False),
	80 : ('If', [b'if', b'(', b'Ex', b')', b'{', b'Sx', b'}', b'El'], False),
	81 : ('El', [b'else', b'{', b'Sx', b'}'], False),
	82 : ('El', [b'elif', b'(', b'Ex', b')', b'{', b'Sx', b'}', b'El'], False),
	83 : ('El', [b'\xce\xb5'], False),
}
