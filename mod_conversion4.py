# JTMS-14
# problem 8.4.py
# Abel Mengistu
# abmengistu@jacobs-university.de
def in2cm_table(startlength, stepsize, endlength):
    def converter(start):
       len_cm = (start * 2.54)
       return len_cm

    print("{:<5} {:>5}".format('inch', 'cm'))
    count = startlength
    while count <= endlength:
       print("{:<6} {:>6}".format(count, converter(count)))
       count += stepsize

def in2cm_html(startlength, stepsize,endlength):
    def converter(startlength):
       len_cm = (startlength * 2.54)
       return len_cm

    html = open('in2cm.html', 'w')
    ''' use markup language to define the layout  of the page
    Specify structure and content of the page with the text in "<>" '''
    html.write('<table>')
    html.write("<tr> <th> {:<10} </th> <th> {:>10} </th> </tr>, \n ".format('inch', 'cm'))

    count = startlength
    while count <= endlength:
        html.write("<tr> <td> {:<10} </td> <td> {:>10} </td> </tr>, \n ".format(count, converter(count)))
        count += stepsize
    html.write('</table>')
    html.close()