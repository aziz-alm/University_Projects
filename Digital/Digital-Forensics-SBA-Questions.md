# Digital Forensics: Skills-Based Assessment (SBA)

**Subject:** Digital Forensics (UTS)  
**Time:** 60 minutes, pick any 3 out of 4 questions (10 pts each)

You are a forensics investigator working in a team investigating a suspect.

Full report with answers and screenshots: [SBA Report (PDF)](Abdulaziz-SBA-Report.pdf)

## Q1: Packet Capture Analysis (10 pts)

Examine the `OfficeWorks.pcapng` file using Wireshark (7,007 frames).

**a)** Use a filter to display only DNS responses. Locate the first IPv4 DNS response for `officeworks.com.au`. Take a screenshot showing Frame Number, query, and IPv4 addresses. (4 pts)

**b)** Locate the first IPv4 DNS response for `bazaarvoice`. What is the purpose of Bazaarvoice? What website is hosting it? (3 pts)

**c)** Locate the first IPv4 DNS response for `demdex`. What website is hosting it? (3 pts)

## Q2: File Metadata (10 pts)

**a)** Examine the corrupt `IMAG1672.jpg`. Use `xxd` to check the HEX header. Repair it using HxD. Examine the EXIF data and find where the photo was taken (hint: Sydney suburb). (3 pts)

**b)** Examine the corrupt `Evidence AIC.pdf`. Identify what is wrong with the HEX header and repair it. Show the metadata: Title, Author, PDF Producer, Application. (4 pts)

**c)** Describe `25 e2 e3 cf d3`. Is it ASCII? What is its purpose in a PDF file and where do you find it? (3 pts)

## Q3: Browser Files (10 pts)

Given a Chrome Browser task snapshot and the suspect's `Cookies` and `History` files:

**a)** Which website did the suspect visit? (1 pt)

**b)** What Google search term led to the website? (3 pts)

**c)** What did the suspect search for on the website? (3 pts)

**d)** Explain the use of the three tracking websites (ignore Google) in the Chrome subframes. (3 pts)

## Q4: Disk Imaging (10 pts)

**a)** What is a GUID and how do you tell the version? Use `diskpart` to list disks and display the GUID. (4 pts)

**b)** View the first two sectors of your disk using HxD. Is it BIOS or UEFI? What is the difference? (3 pts)

**c)** Use `fsstat` and `fls` on `C08InChp.dd`. Find the Volume Label, FAT table sizes, and three deleted files with their folders and inodes. (3 pts)
