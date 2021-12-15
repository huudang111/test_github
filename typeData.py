def main():
	nhietdo()


def nhietdo():
	doc=input("nhap do c vao: ")
	if doc:
		doc=int(doc)
		dof= 9*doc/25 + 32
		print(f"do f là {dof}F")


if __name__ == "__main__":
	main()