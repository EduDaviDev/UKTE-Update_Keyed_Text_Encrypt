ci = input("chave: ")
ci_bytes = ci.encode('utf-8')
ci_hex = ci_bytes.hex().upper()
c1 = int.from_bytes(ci_bytes, "big")

con = {
	"0":0, "1":1, "2":2, "3":3,
	"4":4, "5":5, "6":6, "7":7,
	"8":8, "9":9, "a":10, "b":11,
	"c":12, "d":13, "e":14, "f":15, 
}

ci_nums = [con[ci_hex[i].lower()] for i in range(len(ci_hex))]
c2_nums = [(ci_nums[i] * c1) for i in range(len(ci_nums))]
c2 = 0
for num in c2_nums:
	c2 += num

c3 = int(c2 / c1)

c4 = abs(int(int(c1 / c3) - c2))

cf = abs(int(
	abs(int(
		(c1 + c2)
		*
		(c3 + c4)
	))
	/
	c1
))

print(f"Chave FINAL: {cf}")
print(f"CI = {ci}")
print(f"C1 = {c1}")
print(f"C2 = {c2}")
print(f"C3 = {c3}")
print(f"C4 = {c4}")
print()

msg = input("Mensagem: ")
msgn = []

for c in msg:
	msgn.append((ord(c) * cf) + cf)

msgh = ""
for num in msgn:
	msgh = msgh + format(num, 'X')

bytes = b''
for num in msgn:
	bytes = bytes + num.to_bytes(max((num.bit_length() + 7) // 8, 1), "big")

msgo = bytes.decode('utf-8', errors='ignore')

print(f"Mensagem codificada: {msgo}")
print(f"HEX: {msgh}")
print(f"Bytes: {bytes}")
print(f"Números: {msgn}")