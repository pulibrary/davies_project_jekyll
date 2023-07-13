from csv import DictReader, DictWriter


datafile = "../_data/alb1876.csv"

with open(datafile, encoding='utf-8') as f:
    reader = DictReader(f)
    fieldnames = reader.fieldnames
    fieldnames.remove('card_image')

    print("---")
    print("layout: data_table")
    print("title: Library Data")
    print("---")
    print("")
    print("<table id='alb1876_data'>\n<thead>\n<tr>")
    for name in fieldnames:
        print(f"<th>{name}</th>")
    print("</tr>\n</thead>")
    print("<tbody>")
    for row in reader:
        print("<tr>")
        for field in fieldnames:
            print(f"<td>{row[field]}</td>")
        print("</tr>")
    print("</tbody>\n</table>")
    print("<script>new DataTable('#alb1876_data');</script>")


