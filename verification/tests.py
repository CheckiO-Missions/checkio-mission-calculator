"""
TESTS is a dict with all of your tests.
Keys for this will be the categories' names.
Each test is a dict with
    "input" -- input data for a user function
    "answer" -- your right answer
    "explanation" -- not necessarily a key, it's used for an additional info in animation.
"""


TESTS = {
    "Basics": [
        {
            "input": ["12"],
            "answer": "12",
            "explanation": "you see what you enter"
        },
        {
            "input": ["12+"],
            "answer": "12",
            "explanation": "you see what you enter, one (+) doesn't change anything"
        },
        {
            "input": ["12+15"],
            "answer": "15",
            "explanation": "last entered number, since the operation is not finished"
        },
        {
            "input": ["12+15="],
            "answer": "27",
            "explanation": "12 + 15 = 27"
        },
        {
            "input": ["12+15+"],
            "answer": "27",
            "explanation": "12 + 15 = 27 (+) requires a previous calculation to be calculated"
        },
        {
            "input": ["12+15+3"],
            "answer": "3",
            "explanation": "last entered number, since the operation is not finished"
        },
        {
            "input": ["3+="],
            "answer": "6",
            "explanation": "3+= is the same as 3+3="
        },
        {
            "input": ["3+2=="],
            "answer": "7",
            "explanation": "repeating =, means repeating previous operation"
        },
        {
            "input": ["3+-2="],
            "answer": "1",
            "explanation": "- replaces + so 3+-2 become 3-2"
        },
        {
            "input": ["78-="],
            "answer": "0",
            "explanation": "78-78=0"
        },
        {
            "input": ["3+2-="],
            "answer": "0",
            "explanation": "2 + 3 - 5 = 0"
        },
        {
            "input": ["+-=12="],
            "answer": "12",
            "explanation": "all of the operations, in the beginning, are ignored"
        },
        {
            "input": ["2+3=+7="],
            "answer": "12",
            "explanation": "2+3+7=12"
        },
        {
            "input": ["2+3=7+7="],
            "answer": "14",
            "explanation": "2+3 will be overwiten by the next operation"
        },
        {
            "input": ["90000+10000="],
            "answer": "error",
            "explanation": "too many digits in the result"
        },
        {
            "input": ["90000+10000-10000="],
            "answer": "error",
            "explanation": "any operation after error doesn't fix the error"
        },
        {
            "input": ["90000+10000-10000"],
            "answer": "10000",
            "explanation": "last entered number is shown even with error"
        },
        {
            "input": ["123456789"],
            "answer": "12345",
            "explanation": "only first 5 digits are shown"
        },
        {
            "input": ["123456789+5="],
            "answer": "12350",
            "explanation": "12345 + 5 = 12350. Only first 5 digits are used in the operation"
        },
        {
            "input": ["5+123456789"],
            "answer": "12345",
            "explanation": "12345 as is was the last number entered"
        },
    ],
    "Extra": [
        {
            "input": ["134+56+-+9="],
            "answer": "199",
        },
    ]
}
