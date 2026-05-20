text = "   Hi codegnan   "

print("Original text:", text)

print("zfill(30):",text.strip().zfill(30))
print("center(30,'*'):", text.strip().center(30, '*'))
print("ljust(30,'-'):", text.strip().ljust(30, '-'))
print("rjust(30,'-'):", text.strip().rjust(30, '-'))
