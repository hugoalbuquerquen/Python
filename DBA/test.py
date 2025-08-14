import math

# Reorganize the data with days as rows instead of columns
vertical_data = [
    
    ["Day", "Focus", "Purpose", "Exercises / Notes"],
    ["Monday – Hard Boulders (Kilter 6B–7A)",
     "Power & Strength",
     "Power endurance, limit bouldering",
     "• Project 3–5 hard problems\n• 3–4 sets, 2–3 tries each\n• Rest 3–5 min\n• Steep, tension-focused"
     ],
    ["Tuesday – Full-Body Gym + Cardio",
     "Conditioning & Support",
     "Joint support, lower body strength, aerobic base",
     "🔹 Antagonists:\n• Face pulls, shoulder rotations, rows\n• Push-ups/chest press, core\n\n🔹 Legs:\n• Squats, leg press, calf raises\n• Glute bridges or ham curls\n\n🔹 Cardio:\n• 20–30 min treadmill, bike or rower\n• Keep HR ~120–140 bpm"
     ],
    ["Wednesday – Lead Climbing",
     "Endurance",
     "Route tactics, aerobic power",
     "• 4–6 routes (6B–7A)\n• Smooth clipping\n• 1–2 endurance laps at end"
     ],
    ["Thursday – Rest",
     "Recovery",
     "Tissue and CNS recovery",
     "• Light mobility or stretching if needed\n• Prioritize rest & nutrition"
     ],
    ["Friday – Spray Wall",
     "Aerobic Capacity",
     "Movement quality & forearm endurance",
     "• ARC: 15–20 min easy laps\n• 3–5 min intervals × 3–5 sets\n• Controlled, fluid movement"
     ],
    ["Saturday – Lead Climbing",
     "Endurance",
     "Repeat endurance and redpoint work",
     "• Repeat Wednesday structure\n• Try onsights or redpoints"
     ],
    ["Sunday – Rest or Light Day",
     "Optional Recovery",
     "Rehab or light aerobic support",
     "• Optional Zone 2 cardio (bike, row, jog)\n• Rehab, mobility, or core"
     ]
]

# Set column widths for vertical layout
col_widths_vert = [2.2 * 2.54, 1.2 * 2.54, 1.8 * 2.54, 6.0 * 2.54]

# Create table for vertical format
vertical_table = Table(vertical_data, colWidths=col_widths_vert, repeatRows=1)
vertical_table.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkblue),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
    ('VALIGN', (0, 0), (-1, -1), 'TOP'),
    ('FONTSIZE', (0, 0), (-1, -1), 8),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.grey),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.black),
    ('BACKGROUND', (0, 1), (-1, -1), colors.whitesmoke)
]))

# Generate the updated vertical PDF
vertical_pdf_path = "/mnt/data/Weekly_Climbing_Training_Plan.pdf"
doc = SimpleDocTemplate(vertical_pdf_path, pagesize=landscape(A4), rightMargin=20, leftMargin=20, topMargin=20, bottomMargin=20)
elements = [Paragraph("<b>Weekly Climbing Training Plan</b>", styles['Title']), Spacer(1, 12), vertical_table]
doc.build(elements)
vertical_pdf_path
