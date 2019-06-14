import csv


with open('Προγραμμα.csv', 'r', newline='') as ifp, open('Schedule.csv', 'w', newline='')as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    header = next(reader)
    for i, row in enumerate(reader, start=1):
        for col, value in zip(header, row):
            if col == 'Ώρα':
                new_value = value.split('-')
                writer.writerow([i, 'Ώρα Έναρξης', new_value[0]])
                writer.writerow([i, 'Ώρα Λήξης', new_value[1]])
            else:
                writer.writerow([i, col, value])\


with open('Schedule.csv',  'r', newline='') as ifp, open('New_Schedule.csv', 'w', newline='') as ofp:
        reader = csv.reader(ifp)
        writer = csv.writer(ofp)

        for s, p, o in reader:
            new_s, new_o = 'b:' + s, o
            if p in ['Μάθημα', 'Αίθουσα', 'Διδάσκων']:
                new_o = 'u:' + o
            else:
                new_o = 'l:' + o
            writer.writerow([new_s, p, new_o])




with open('New_Schedule.csv',  'r', newline='') as ifp, open('Schedule_uri.csv', 'w', newline='') as ofp:
    reader = csv.reader(ifp)
    writer = csv.writer(ofp)
    for row in reader:
        s = row[0]
        p = "http://host/sw/p15verg/myvocab#" + row[1]
        o = row[2]

        if o.startswith('u:'):
            o = 'http://host/sw/p15verg/resource/'

            for i in row[2][2:]:
                if i == " ":
                    o += "%20"
                elif i != "l":
                    o += i



        writer.writerow([s, p, o])


with open('Schedule_uri.csv',  'r', newline='') as ifp, open('Schedule_rdf.nt', 'w') as ofp:
        reader = csv.reader(ifp)

        for s, p, o in reader:
            new_s = f'_:b{s[2:]}'
            new_p = f'<{p}>'
            if o[:2] == 'l:':
                new_o = o[2:]
                if 'Ώρα' in p:
                    new_o += ':00'
                new_o = f'"{new_o}"'
            else:
                new_o = f'<{o}>'
            ofp.write(' '.join([new_s, new_p, new_o]) + ' .\n')