from datetime import datetime
import jinja2
import os
import json
import requests
import webbrowser
import keyboard

default_path = os.path.join(os.getcwd(), 'static')
file_name = 'example.html'

example_logo_b64 = "iVBORw0KGgoAAAANSUhEUgAAADIAAAAyCAYAAAAeP4ixAAAAAXNSR0IArs4c6QAABWtJREFUaEPdmXtMm1UUwA/0a3mVV8ECfTmGToVNnTAXH+Ph5ky2BF3icM5El5m4SeQx0LkHSBEGOIc8lhD/AJVlilvmXFxMNMssC0zDJBGSzSxBYbw7HgM6Xpa2x3zDQmm/0u9+vdUgf/Lde875nce959x6wf/kz+vf5tge54P7koIgtWaYqm6qwlw55Zu3wnHbOn/wy+ihrpe6QGcwbXlR+FCEGG4bzLDqaD91vdQFcoE05shxY7TvvU9vnx6GL1pmqOulLtAeJHezFItfki38OzKjRzYBMOYqDUm/exRE7gfPdB/XNNsa5Yn6YOV7FKSzWIFRwcwS565IkJmTGrRPkRUH8vnrMty1QeqQ6isOxFCpRrHIMXPXFw0U3hwyaUmL2dV6j9XIdLUGvTik1zUb4J0z49T1Uhdo9RxXfbDfpv6yQPi7fdT1UhNYlRaMWWcnFuQ5A2FhPFEn1EBYAyer1Li2YDDl1rip0VlqseuKvx+HYz8YqOqmKux6fhTGyMWQfWYUilJDIdDPm7NGzRYEaVYvVd1UhT0VLTb8lBMVyFo/OmmGMKnI6WGzpUJvutppFLs6jfh+pwrCKl2uNmyNMpoRgrPpReU/A2GhtlbqoelPIxUbqAix9TTfiLB7TGaEQEpRoQrypIbRXnlPUcA3r9l1+08PQz2F+YQqSP0bMkxLcOyvlgNDBPDPdH/0pQoyWaVBEfeJu2yQPr1igAPn3GtbqIE8rmR0vxxSJJOkFc2BixrIRIUKJYyAcPxDc61rFpI+GRJsj+CNtt584REfvJAeITQYC/vc6cGogCzXV5HQ3Rw0wvoSvSCbBG2yNe7HTDkmPjj/1GP/1z06B/eHkXUhQqPiFsiacG9te4HK6b2hPNwT99sR5Q15oPOeyx6+pWsWkgXUilsgdyvVyHCMs6xxzR0z8Hz1sFdcBNPWmqd4jHeKIYCfgHtFMMhyl58FEQIyFxvCsXIV+kr4n2i7a4fg2/ZZItuIFlu9KpNAbH+55oYzL2+r1oOuY7EZ3LiK0TXm8r9jpo0WCMslG4cFgQwdV6GzoUk/YYLovAEHucMnVCj14R8V0qInBklQM7qmg9zeRUTwt0kp24hFSiG5q1Sj41srcfk9hZ3jwPvZiBiEnctF3tzb9tYPQ0Or85f26/mRGCOX8GJ5rW4IzrfxrxMikKdXM9rLB7jb9BmjBWQu8loVAjs6ijTn+ZCUXxqDvO/u8raP90JWeceHClSFLn2UthoVfbgnRT8Jja6MNFSoUczMq2XfuAKc1M3Jy+Nw8AL/lxYiEGfT3++DRojn2VpkPSfFsh3zv5fcNpggIojbMblnR6CmaZq3fbwXsoqdgZCcMOEBold7y5RfsfK+vDYJr8T7A8MxxGz6qK+wtc/imWLnApmds0BoDtmZb5XDOuBSlhyffcCxVyNxDusUtyOS0TACtT/zT4GIQNHeWyXKuovtU5BWO+pV8XII7k8KWlJaY1NmUBwi+8GUCGS6Wo1edk/spJ47lhqMW2P9YEPZfLte+mIQZm8JWQKyrnAg5Y8Rk8uDw3YTEcipPWG4Mz5giVJSkJpdIZj+9eJ8fmqPDHfGLz5YdI3OQax2kMgu4tTiKnhSEIeZpUSJ1jbfvtl0dZQLjgi78dFIRttydPFSdBfEmq7ss9DqI/zuIi5A4hCyQravleC5fZH35CWeGGj8tduUQuI969qF/gsB4gr6d3eOmRuEyBGUWlZFT6gY7dX3FQV3psygJDxhrDIupt+Hmx/2hTUf9Kb0jbvuCpaDFBQRW4F9pUpM/Fj/Zucd82ek3uwvU6JQJ9jrchuEFZigFutae+eI0mtTjARpvcS7lVqk3vf0+r8BUtLbQhgk6wQAAAAASUVORK5CYII="

example_header = { 
    "Company" : "MyCompany",
    "Logo" : example_logo_b64,
    "Mail" : "AnyCompany@hotmail.com",
    "Id" : "20300000009",
    "Street" : "Fleet street",
    "City" : "Iowa",
    "PostCode" : "2978",
    "Telephone" : "+5493464520203",
    "BillNo" : "0",
    "Client" : "John Doe",
}

# Detail, Cant, Price
example_sells =  [
    ["Computer", 1, 1500],
    ["Telephone", 2, 1000],
    ["Chair", 12, 450],
    ["Gaming set", 1, 12000],
    ["headphone", 2, 300],
    ["Calculator", 1, 340]
]

def generate_bill(header:dict = example_header,
                  sells: list = example_sells,
                  path: str = default_path ,
                  filename: str = file_name,
                  open_on_chrome: bool = False) -> None:
    
    path_to_save = os.path.join(path, filename)
    with open(path_to_save, 'w+') as f:
        date = datetime.now()
        date = str(date.day) + '-' + str(date.month) + '-' + str(date.year)
        company = header["Company"]
        logo = header["Logo"]
        mail = header["Mail"]
        id = header["Id"]
        street = header["Street"]
        city = header["City"]
        post_code = header["PostCode"]
        tel = header["Telephone"]
        billno = header["BillNo"]
        client = header["Client"]
        
        header_ = f"<p style=\"text-align: center;\"><img src=\"data:image/png;base64,{logo} \" alt=\"Xd\" /></p> \n \
            <table style=\"width: 506.688px; margin-left: auto; margin-right: auto;\"> \n \
            <tbody> \n \
            <tr style=\"height: 18px;\"> \n \
            <td style=\"width: 279px; height: 18px;\"><strong>{company}</strong></td> \n \
            <td style=\"width: 229.688px; height: 18px;\"><strong>Factura No: {billno}</strong></td> \n \
            </tr> \n \
            <tr style=\"height: 18px;\"> \n \
            <td style=\"width: 279px; height: 18px;\"><strong>{mail}</strong></td> \n \
            <td style=\"width: 229.688px; height: 18px;\"><strong>Cliente: {client}</strong></td> \n \
            </tr> \n \
            <tr style=\"height: 18px;\"> \n \
            <td style=\"width: 279px; height: 18px;\"><strong>DNI: {id}</strong></td> \n \
            <td style=\"width: 229.688px; height: 18px;\"><strong>Fecha:{date};</strong></td> \n \
            </tr> \n \
            <tr style=\"height: 18px;\"> \n \
            <td style=\"width: 279px; height: 18px;\"><strong>{street}</strong></td> \n \
            <td style=\"width: 229.688px; height: 18px;\">&nbsp;</td> \n \
            </tr> \n \
            <tr style=\"height: 25.75px;\"> \n \
            <td style=\"width: 279px; height: 25.75px;\"><strong>{city}, {post_code}</strong></td> \n \
            <td style=\"width: 229.688px; height: 25.75px;\">&nbsp;</td> \n \
            </tr> \n \
            </tbody> \n \
            </table> \n \
            <hr />\n \
            <h4 style=\"text-align: center;\"><span style=\"text-decoration: underline;\">Presupuesto:</span></h4>\n"
            
        f.write("<html><style> \n \
                table \{ \n \
                border-collapse: collapse; \n \
                margin: 25px 0; \n \
                font-size: 0.9em; \n \
                font-family: sans-serif;  \n \
                min-width: 400px;  \n \
                box-shadow: 0 0 20px rgba(0, 0, 0, 0.15);\}  \n \
                </style>")
        
        f.write(header_)
        f.write("<table class=\"styled-table\"; style=\"width: 800; margin-left: auto; margin-right: auto;\" border=\"1\"><tbody>")
        f.write("<tr> \n \
                <td style=\"width: 605.969px; text-align: center;\">Detalle</td> \n \
                <td style=\"width: 10px; text-align: center;\">Cant.</td> \n \
                <td style=\"width: 177px; text-align: center;\">Precio Unidad</td> \n \
                <td style=\"width: 67px; text-align: center;\">Total</td> \n \
                </tr>")
        
        total = 0
        for product in sells.copy():
            detalle = product[0]
            cant = product[1]
            price = product[2]
            total_ = price * cant
            
            total += total_
            product_ = f"<tr> \n \
                <td style=\"width: 605.969px; text-align: center;\">{detalle}</td> \n \
                <td style=\"width: 10px; text-align: center;\">{cant}</td> \n \
                <td style=\"width: 177px; text-align: center;\">{price}</td> \n \
                <td style=\"width: 67px; text-align: center;\">{total_}</td> \n \
                </tr>"
            f.write(product_)
        
        f.write(f"</tbody>\n \
                </table> \n \
                <h3 style=\"text-align: right;\">SubTotal = {total}&emsp;&emsp;&emsp;</h3></html>")
        f.close()
        
        if open_on_chrome:
            webbrowser.open('file://' + path_to_save)
            try:
                keyboard.press_and_release('control + p')
            except:
                pass
generate_bill(open_on_chrome=True)