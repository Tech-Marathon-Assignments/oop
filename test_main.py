from main import main

# Test case 1:
# Input:
# company_list = [
# 	Company("Amazon", 1994),
# 	Company("Apple", 1976),
# 	Company("Facebook", 2004),
# 	Company("Google", 1998),
# 	Company("Microsoft", 1975),
# ]
# Output:
# Name: Amazon
# Founded Year: 1994
# Name: Apple
# Founded Year: 1976
# Name: Facebook
# Founded Year: 2004
# Name: Google
# Founded Year: 1998
# Name: Microsoft
# Founded Year: 1975

def test_main_testcase_1(capfd):
    main(company_list = [
    	Company("Amazon", 1994),
    	Company("Apple", 1976),
    	Company("Facebook", 2004),
    	Company("Google", 1998),
    	Company("Microsoft", 1975)
    ])
    out, err = capfd.readouterr()
    assert out == """Name: Amazon
Founded Year: 1994
Name: Apple
Founded Year: 1976
Name: Facebook
Founded Year: 2004
Name: Google
Founded Year: 1998
Name: Microsoft
Founded Year: 1975
"""

# Test case 2:
# Input:
# company_list = [
# 	Company("Amazon", 1994),
# 	Company("Apple", 1976),
# 	Company("Facebook", 2004),
# 	Company("Google", 1998),
# 	Company("Microsoft", 1975),
# ]
# Output:
# Name: Amazon
# Founded Year: 1994
# Name: Apple
# Founded Year: 1976
# Name: Google
# Founded Year: 1998
# Name: Microsoft
# Founded Year: 1975

def test_main_testcase_2(capfd):
    main(company_list = [
    	Company("Amazon", 1994),
    	Company("Apple", 1976),
    	Company("Google", 1998),
    	Company("Microsoft", 1975)
    ])
    out, err = capfd.readouterr()
    assert out == """Name: Amazon
Founded Year: 1994
Name: Apple
Founded Year: 1976
Name: Google
Founded Year: 1998
Name: Microsoft
Founded Year: 1975
"""

# Test case 3:
# Input:
# company_list = [
# 	Company("Amazon", 1994),
# 	Company("Apple", 1976),
# 	Company("Facebook", 2004),
# 	Company("Google", 1998),
# 	Company("Microsoft", 1975),
# ]
# Output:
# Name: Amazon
# Founded Year: 1994
# Name: Apple
# Founded Year: 1976
# Name: Google
# Founded Year: 1998
# Name: Microsoft
# Founded Year: 1975
# Name: Tesla
# Founded Year: 2003


def test_main_testcase_3(capfd):
    main(company_list = [
    	Company("Amazon", 1994),
    	Company("Apple", 1976),
    	Company("Google", 1998),
    	Company("Microsoft", 1975),
        Company("Tesla", 2003)
    ])
    out, err = capfd.readouterr()
    assert out == """Name: Amazon
Founded Year: 1994
Name: Apple
Founded Year: 1976
Name: Google
Founded Year: 1998
Name: Microsoft
Founded Year: 1975
Name: Tesla
Founded Year: 2003
"""
