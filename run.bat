pytest -v -s -m "regression" --html-report=./report/report.html --browser chrome
rem pytest -v -s -m "sanity" --html-report=./report/report.html --browser chrome
rem pytest -v -s -m "smoke" --html-report=./report/report.html --browser chrome
rem pytest -v -s -m "sanity and regression" --html-report=./report/report.html --browser chrome
rem pytest -v -s -m "sanity or regression" --html-report=./report/report.html --browser chrome