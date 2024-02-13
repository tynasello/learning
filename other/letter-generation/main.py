import os
import subprocess


def load_latex_template():
    return r"""
        \documentclass[a4paper, 12pt]{letter}
        \setlength{\voffset}{-0.75in}

        \usepackage[scale=.8]{geometry}
        \usepackage{hyperref}
        \usepackage{xcolor}
        \hypersetup{
          colorlinks=true,
          urlcolor=black!70!black
        }

        \address
        {
            \href{https://tynasello.com}{tynasello.com},\\
            \href{mailto:tnasello@uwaterloo.ca}{tnasello@uwaterloo.ca},\\
            (123) 456-7890,\\
            \href{https://github.com/Tynasello}{github.com/tynasello},\\
            \href{https://www.linkedin.com/in/ty-nasello/}{linkedin.com/in/ty-nasello},\\
        }

        \newcommand{\getCompany}{%(company)s}
        \newcommand{\getRole}{%(role)s}


        \begin{document}
        \begin{letter}{\\}
        \opening{To the hiring manager at {\getCompany},}

        \vspace{0.5cm}

        Nam dui ligula, {\getRole} a, euismod sodales, sollicitudin vel, wisi. Morbi auctor lorem non justo. Nam lacus libero, pretium at, lobortis vitae, ultricies et, tellus. Donec aliquet, tortor sed accumsan bibendum, erat ligula aliquet magna, vitae ornare odio metus a mi. Morbi ac orci et nisl hendrerit mollis. Suspendisse ut massa. Cras nec ante. Pellentesque a nulla. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Aliquam tincidunt urna. Nulla ullamcorper vestibulum turpis. Pellentesque cursus luctus mauris. Nulla malesuada porttitor diam. Donec felis erat, congue non, volutpat at, tincidunt tristi-que, libero. Vivamus viverra fermentum felis. Donec nonummy pellentesque ante.

        Phasellus adipiscing semper elit. Proin fermentum massa ac quam. Sed diam turpis, molestie vitae, placerat a, molestie nec, leo. Maecenas lacinia. Nam ipsum ligula, eleifend at, accumsan nec, suscipit a, ipsum. Morbi blandit ligula feugiat magna. Nunc eleifend consequat lorem. Sed lacinia nulla vitae enim. Pellentesque tincidunt purus vel magna. Integer non enim. Praesent euismod nunc eu purus. Donec bibendum quam in tellus. Nullam cursus pulvinar lectus. Donec et mi. Nam vulputate metus eu enim. Vestibulum pellentesque felis eu massa. Quisque ullamcorper placerat ipsum. Cras nibh. Morbi vel justo vitae lacus tincidunt ultrices. Lorem ipsum dolor sit amet, consectetuer adipiscing elit. In hac habitasse platea dictumst.

        Integer tempus convallis augue. Etiam facilisis. Nunc elementum fermentum wisi. Aenean
        placerat. Ut imperdiet, enim sed gravida sollicitudin, felis odio placerat quam, ac pulvinar elit purus eget enim. Nunc vitae tortor. Proin tempus nibh sit amet nisl. Vivamus quis tortor vitae risus porta vehicula.

        \vspace{0.5cm}

        Sincerely, 

        Ty Nasello

        \end{letter}
        \end{document} """


def format_latex_template(template, role, company):
    return template % {"role": role, "company": company}


def read_lines(input):
    with open(input) as f:
        file_lines = f.readlines()

    placement_info = []

    for file_line in file_lines:
        seperated = file_line.split(";")
        seperated[-1] = seperated[-1].rstrip()
        placement_info.append(
            {
                "company": seperated[0],
                "role": seperated[1],
                "file_name": seperated[2]
                if len(placement_info) > 2 and seperated[2]
                else seperated[0] + " Cover Letter",
            }
        )

    return placement_info


def generate_pdf(template_file_path, pdf_destination_dir, placement_info):
    os.chdir(pdf_destination_dir)

    for placement in placement_info:
        company = placement["company"]
        role = placement["role"]
        file_name = placement["file_name"]

        with open("%s.tex" % file_name, "w") as f:
            f.write(format_latex_template(template_file_path, company, role))

        cmd = ["pdflatex", "-interaction", "nonstopmode", "%s.tex" % file_name]
        proc = subprocess.Popen(cmd)
        proc.communicate()

        retcode = proc.returncode
        if not retcode == 0:
            os.unlink("%s.pdf" % file_name)
            raise ValueError(
                "Error {} executing command: {}".format(retcode, " ".join(cmd))
            )

        os.unlink("%s.aux" % file_name)
        os.unlink("%s.out" % file_name)
        os.unlink("%s.tex" % file_name)
        os.unlink("%s.log" % file_name)


def main():
    input = "input.txt"
    pdf_destination_dir = "generated"

    template = load_latex_template()
    placement_info = read_lines(input)
    generate_pdf(template, pdf_destination_dir, placement_info)


if __name__ == "__main__":
    main()
