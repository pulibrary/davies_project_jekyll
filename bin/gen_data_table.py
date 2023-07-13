from csv import DictReader, DictWriter


datafile = "../_data/alb1876.csv"

records = []
with open(datafile, encoding='utf-8') as f:
    reader = DictReader(f)
    fieldnames = reader.fieldnames
    print("<!DOCTYPE html>")
    print("<html>")
    print("<head>")
    print("<script src='https://ajax.googleapis.com/ajax/libs/jquery/3.6.4/jquery.min.js'></script>")
    print("<link rel='stylesheet' href='https://cdn.datatables.net/1.13.5/css/jquery.dataTables.css' />")
    print("<script src='https://cdn.datatables.net/1.13.5/js/jquery.dataTables.js'></script>")
    print("</head>")
    print("<body>")
    print("<table id='alb1876_data' width='75%'><thead><tr>")
    for name in fieldnames:
        print(f"<th>{name}</th>")
    print("</tr></thead>")
    print("<tbody>")
    for row in reader:
        print("<tr>")
        for field in fieldnames:
            print(f"<td>{row[field]}</td>")
        print("</tr>")
    print("</tbody></table>")
    print("<script>new DataTable('#alb1876_data');</script>")
    print("</html>")

