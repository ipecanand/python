*** Settings ***
Documentation  These are some API tests
Library  OperatingSystem
Library  String
Library  BuiltIn
Library  Process
Library  Collections
Library  E:\\robotframework\\pwms\\Resources\\PythonFile\\addstring.py
Library  E:\\robotframework\\pwms\\Resources\\PythonFile\\Flight.py  ${arg2}


# pybot -d results/Python tests/Python.robot

*** Variables ***
${stdout}
${arg1}=  SN0198
${arg2}=  AK1981
${Flight}=  Flight
${str1}=  how are you
${str2}=  i am good


*** Test Cases ***
Addition of Strings
    [Documentation]  We are combining two string together
    [Tags]  Add two string with passing two arguments
    joinString  ${str1}  ${str2}
Dictionary Script
    [Documentation]  this is Dictionary python script
    [Tags]  Python Smoke
    ${result}=  Run Process  python  E:\\robotframework\\pwms\\Resources\\PythonFile\\__pscript__.py
    # ${result}=  Run Process  python  C:\\Python27\\Lib\\site-packages\\__pscript__.py
    log  ${result}
    log  ${result.stdout}
valid number from addstring.py
    [Documentation]  this is Flight Class script which i called from addstring.py
    [Tags]  Python Smoke
    ${result}=  validnumber  ${arg1}
    log  ${result}
Flight Class Script From Flight.py
    # ${result}=  Run Process  python  E:\\robotframework\\pwms\\Resources\\PythonFile\\Flight.py  SN9877211
    # log  ${result.stdout}
    # ${Flight}=  number  SN22000
    # ${result}=  call method  ${flight}  number
    ${result}=  Flight.number
    log  ${result}
Add numbers with asseration From Flight.py
    ${Add_Result}=  Flight.addition
    log  ${Add_Result}
Multiply numbers with asseration From Flight.py
    ${Multiply_Result}=  Flight.multiplecation  2  4
    log  ${Multiply_Result}
Airthmatic operators from Flight.py
    ${AirthmaticOperatorsResult}=  Flight.airthmaticoperators  20  10
    log  ${AirthmaticOperatorsResult}
Assignment operators from Flight.py
    ${AssignmentOperatorsResult}=  Flight.assignmentoperators  10  20  30  40
    log  ${AssignmentOperatorsResult}
Bitwise operators from Flight.py
    ${BitWiseOperatorsResult}=  Flight.bitwiseoperator  6  2
    log  ${BitWiseOperatorsResult}
forloop series from Flight.py
    ${ForLoopResult}=  Flight.forloop  5
    log  ${ForLoopResult}
fibanaci series from Flight.py
    ${FibnaciResult}=  Flight.fibnaci  10
    log  ${FibnaciResult}


*** Keywords ***
joinString
    [Arguments]  ${str1}  ${str2}
    ${strResult}=  join_two_string  ${str1}  ${str2}
    log  ${strResult}
    should be equal  ${strResult}  how are you i am good
