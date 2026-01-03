#!/usr/bin/env python3
"""
Script to generate PSIOP one-pager PDF using ReportLab
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import cm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

def generate_onepager():
    # Create the PDF
    doc = SimpleDocTemplate("static/PSIOP_OnePager.pdf", pagesize=A4, 
                           rightMargin=2*cm, leftMargin=2*cm, 
                           topMargin=2*cm, bottomMargin=2*cm)
    
    # Define styles
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=12,
        alignment=1,  # Center alignment
        textColor=colors.HexColor('#0064c8')
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        spaceAfter=20,
        alignment=1,  # Center alignment
        textColor=colors.grey
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=14,
        spaceBefore=12,
        spaceAfter=6,
        textColor=colors.black
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=6,
        textColor=colors.HexColor('#323232')
    )
    
    bullet_style = ParagraphStyle(
        'CustomBullet',
        parent=styles['Normal'],
        fontSize=11,
        spaceAfter=3,
        leftIndent=20,
        bulletIndent=10,
        textColor=colors.HexColor('#323232')
    )
    
    disclaimer_style = ParagraphStyle(
        'Disclaimer',
        parent=styles['Normal'],
        fontSize=9,
        spaceAfter=12,
        textColor=colors.grey,
        leftIndent=10,
        rightIndent=10
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=12,
        alignment=1,
        textColor=colors.HexColor('#0064c8'),
        fontName='Helvetica-Bold'
    )
    
    # Build the document content
    story = []
    
    # Title and subtitle
    story.append(Paragraph("PSIOP", title_style))
    story.append(Paragraph("Персональный нейроинтерфейс для медитации, фокуса и диалогов", subtitle_style))
    story.append(Spacer(1, 12))
    
    # What is PSIOP
    story.append(Paragraph("Что такое PSIOP?", heading_style))
    story.append(Paragraph("Замкнутый контур обратной связи: ЭЭГ-обруч считывает сигналы мозга и сердечный ритм, ИИ анализирует ваше состояние и даёт персональные рекомендации, вы отмечаете результаты — система становится точнее.", normal_style))
    story.append(Spacer(1, 8))
    
    # Three modes
    story.append(Paragraph("Три режима работы:", heading_style))
    story.append(Paragraph("• Медитация — глубокие сессии с дыхательными подсказками и адаптивной музыкой", bullet_style))
    story.append(Paragraph("• Фокус и продуктивность — мониторинг усталости, стресса, определение часов максимальной продуктивности", bullet_style))
    story.append(Paragraph("• EQ-коуч — анализ речи в реальном времени, предупреждение эскалации в диалогах", bullet_style))
    story.append(Spacer(1, 8))
    
    # Target audience
    story.append(Paragraph("Для кого создан PSIOP:", heading_style))
    story.append(Paragraph("• Медитирующие — объективная обратная связь по качеству практики", bullet_style))
    story.append(Paragraph("• Специалисты с высокой нагрузкой — управление фокусом, предотвращение выгорания", bullet_style))
    story.append(Paragraph("• Команды и пары — снижение конфликтности в диалогах", bullet_style))
    story.append(Spacer(1, 8))
    
    # How it works
    story.append(Paragraph("Как работает:", heading_style))
    story.append(Paragraph("• Считывание ЭЭГ-сигналов и частоты сердцебиения", bullet_style))
    story.append(Paragraph("• Предобработка и фильтрация данных", bullet_style))
    story.append(Paragraph("• ИИ-анализ состояния и формирование рекомендаций", bullet_style))
    story.append(Paragraph("• Обратная связь от пользователя для персонализации", bullet_style))
    story.append(Spacer(1, 8))
    
    # Privacy and security
    story.append(Paragraph("Безопасность и приватность:", heading_style))
    story.append(Paragraph("• Шифрование данных при передаче и хранении", bullet_style))
    story.append(Paragraph("• Псевдонимные идентификаторы вместо реальных имён", bullet_style))
    story.append(Paragraph("• Возможность удаления истории по запросу", bullet_style))
    story.append(Paragraph("• Часть анализа выполняется локально на устройстве", bullet_style))
    story.append(Spacer(1, 15))
    
    # Disclaimer
    story.append(Paragraph("<b>Важно:</b> PSIOP не является медицинским устройством и не заменяет консультацию врача или психотерапевта. Это инструмент для самонаблюдения и развития навыков саморегуляции.", disclaimer_style))
    story.append(Spacer(1, 15))
    
    # Contact info
    story.append(Paragraph("Свяжитесь с нами для участия в программе раннего доступа", contact_style))
    
    # Build PDF
    doc.build(story)

if __name__ == "__main__":
    generate_onepager()
    print("One-pager PDF generated successfully!")