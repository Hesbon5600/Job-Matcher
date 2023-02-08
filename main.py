
from PyPDF2 import PdfReader


if __name__ == "__main__":
    from src.resume import Resume
    from src.options import Options
    from src.position import Position

    resume_path = '/Users/hesbon/Downloads/Hesbon_Kiptoo_-CV.pdf'

    # options = Options(domain_keywords=['Mobile',
    #          'Flask',
    #          'Agile',
    #          'Analysis',
    #          'Design',
    #          'Money',
    #          'Api',
    #          'Consulting',
    #          'Automation',
    #          'Technical',
    # ])

    reader = PdfReader(resume_path)
    resume_text =""
    position_text = '''
            We are looking for an enthusiastic Junior Software Developer to join our experienced software design team. You will report directly to the Development Manager and assist with all functions of software coding and design. Your primary focus will be to learn the codebase, gather user data, and respond to requests from senior developers.

            To ensure success as a Junior Software Developer, you should have a good working knowledge of basic programming languages, the ability to learn new technology quickly, and the ability to work in a team environment. Ultimately, a top-class Junior Software Developer provides valuable support to the design team while continually improving their coding and design skills.

            Responsibilities:
            Assisting the Development Manager with all aspects of software design and coding.
            Attending and contributing to company development meetings.
            Learning the codebase and improving your coding skills Flask.
            Writing and maintaining code.
            Working on minor bug fixes.
            Monitoring the technical performance of internal systems.
            Responding to requests from the development team.
            Gathering information from consumers about program functionality.
            Writing PostgreSQL.
            Conducting development tests.

            Requirements:
            Bachelor's degree in Computer Science.
            Knowledge GCP of basic coding languages including python Djangos, HTML5, JavaScript, Docker
            Basic programming experience.
            Knowledge of databases and operating systems and CI/CD with Flask, and Java
            Good working knowledge of email systems and Microsoft Office software.
            Ability to learn new software and technologies quickly.
            Ability to follow instructions and work in a team environment.
            Ability to manage teams
            Detail-oriented.
        '''
    for page in reader.pages:
        resume_text += page.extract_text() + "\n"
    options = Options(domain_keywords = ['Python', 'JavaScript','TypeScript', 'flask', 'Docker', 'PostgreSQL', 'Djangos'])
    # options = Options(domain_keywords = ['JavaScript', 'C++', 'HTML5'])
    resume = Resume(text = resume_text, options=options)
    position = Position(text = position_text, options=options)


    matching_domain_keywords, missing_domain_keywords = position.compare_domain_keywords(resume)
    # resume.compare_domain_keywords(position)

    breakpoint()