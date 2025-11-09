import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def analyze_data(filename):
    data = []
    total_score = 0
    count = 0
    with open(filename, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            name = row['Name']
            score = int(row['Score'])
            data.append((name, score))
            total_score += score
            count += 1
    avg_score = total_score / count if count else 0
    return data, avg_score

def generate_pdf_report(data, avg_score, out_file):
    c = canvas.Canvas(out_file, pagesize=letter)
    c.setFont("Helvetica-Bold", 20)
    c.drawString(100, 750, "Student Score Report")
    c.setFont("Helvetica", 12)
    y = 700
    for name, score in data:
        c.drawString(100, y, f"{name}: {score}")
        y -= 20

    c.setFont("Helvetica-Bold", 14)
    c.drawString(100, y-10, f"Average Score: {avg_score:.2f}")
    c.save()

if __name__ == '__main__':
    data, avg_score = analyze_data("data.csv")
    generate_pdf_report(data, avg_score, "report.pdf")
    print("PDF report generated as report.pdf")
