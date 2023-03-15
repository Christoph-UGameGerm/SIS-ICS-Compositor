import os

targetDir = input("Please drag and drop the ics folder exported and unzipped from SIS to this window\nPath: ")
while not os.path.isdir(targetDir):
    print("Path not exist.")
    targetDir = input("Please drag and drop the ics folder exported and unzipped from SIS to this window\nPath: ")
os.path.isdir(targetDir)
if os.path.exists(os.path.join(targetDir, "composite.ICS")):
    os.remove(os.path.join(targetDir, "composite.ICS"))
    print("Old composition detected and removed.")

icsFiles = []

for root, dirs, files in os.walk(targetDir):
    for name in files:
        icsFiles.append(name)

with open(os.path.join(targetDir, "composite.ICS"), "w", encoding="utf-8") as compositeICS:

    with open(os.path.join(targetDir, icsFiles[0]), "r", encoding="utf-8") as headICS:
        print("LeadingFile: " + name[15:-7])
        for line in headICS.read().split("\n"):
            if line == "X-MS-OLK-FORCEINSPECTOROPEN:TRUE":
                compositeICS.write("X-MS-OLK-FORCEINSPECTOROPEN:FALSE" + "\n")
                continue
            compositeICS.write(line + "\n")
            if line == "END:VEVENT":
                break

    for name in icsFiles[1:]:
        print("Compositing: " + name[15:-7])
        with open(os.path.join(targetDir, name), "r", encoding="utf-8") as sourceICS:
            flag = 0
            for line in sourceICS.read().split("\n"):
                if line == "BEGIN:VEVENT":
                    flag = 1
                if flag:
                    compositeICS.write(line + "\n")
                if line == "END:VEVENT":
                    flag = 0
    print("Compositing complete.")
    compositeICS.write("END:VCALENDAR")

print("Done.")    