### About
Solution (Page Object Model) for review from  [Stepik course](https://stepik.org/lesson/201964/step/15?unit=176022) 
### Requirements
Python 3.9+
[Chromediver](https://chromedriver.chromium.org/downloads)/[Firefoxdriver](https://github.com/mozilla/geckodriver/releases)
### Install
1. Сlone the repository and go to your local copy;
2. Download your driver or move to the root of the project;
3. Create virtual environment: `python -m venv {your env}`;
4. Activate your environment:
* Linux/Mac OS:
`source {path to proj}/bin/activate`;
* Windows OS:
PowerShell:`{your env}/bin/Activate.ps1`;
CMD:`{your env}/Scripts/activate.bat`;
5. Install dependencies:
`pip install -r requirements.txt`;
6. Run tests: 
`pytest -v --tb=line --language=en -m need_review`;