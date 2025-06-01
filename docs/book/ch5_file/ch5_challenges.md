---
title: Challenges
---
# Challenge



### Challenge 1
Open a file and splitting by newlines:
<details><summary>Respond:</summary>
```Python
with open("out.txt") as f:
    data = f.read().splitlines()
    print ("h\n")
```
</details>

### Challenge 2
Open a file a print out all lines starting with a pattern:

<details><summary>Respond:</summary>
```Python
with open("test.fasta") as f:
   for line in f:
       if line.startswith(">"):
           print line,
```
</details>