This project speeds up the process of writing cover letters and can automate the process of creating generic ones. Simply edit the file input.txt and provide the company names and job roles for which you want to create letters for. Each line in this file will be used as input to a LaTeX template (found at top of main script) which a PDF will be generated from.

In the file **input.txt**, provide inputs in the form **Company name;Job role;File name**. The company name will be used as the default file name if no input is provided for it. Run **main.py** and locate your generated PDFs in the **generated folder**.

## Installation

A TeX distribution is required to run this project. It provides all necessary LaTeX programs. You can find out what distribution to install through [TeX Live](https://tug.org/texlive/).

Install a suitable TeX distribution. I ran the following (on MacOS).

`brew install basictex`

Clone repository.

`git clone https://github.com/Tynasello/cover-letter-generation`

`cd cover-letter-generation`

Create a virtual environment.

`python -m venv .venv `

Activate virtual environment.

`source .venv/bin/activate`
