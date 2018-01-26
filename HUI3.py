# Multi-Attribute Health Status Classification System: Health Utilities Index Mark 3 (HUI3)
# Problem 1: Implement the HUI3 instrument .
# The user will specify the level of 8 attributes in HUI3 instrument and gets the corresponding health score.
C1 = 1.371
C2 = 0.371
SingCoefficients = {'Vision':	    [1,	0.95, 0.73,	0.59, 0.38, 0],
                    'Hearing':	    [1,	0.86, 0.71,	0.48, 0.32,	0],
                    'Speech':	    [1,	0.82, 0.67,	0.41, 0],
                    'Ambulation':   [1, 0.83, 0.67, 0.36, 0.16, 0],
                    'Dexterity':    [1, 0.88, 0.73, 0.45, 0.2, 0],
                    'Emotion':	    [1,	0.91, 0.73, 0.33, 0],
                    'Cognition':    [1, 0.86, 0.92, 0.7,  0.32, 0],
                    'Pain':	        [1,	0.92, 0.77,	0.48, 0]}

MultCoefficients = {'Vision':	    [1, 0.98, 0.89, 0.84, 0.75,	0.61],
                    'Hearing':	    [1, 0.95, 0.89, 0.80, 0.74,	0.61],
                    'Speech':	    [1,	0.94, 0.89,	0.81, 0.68],
                    'Ambulation':   [1, 0.93, 0.86, 0.73, 0.65, 0.58],
                    'Dexterity':    [1, 0.95, 0.88, 0.76, 0.65, 0.56],
                    'Emotion':	    [1,	0.95, 0.85, 0.64, 0.46],
                    'Cognition':    [1, 0.92, 0.95, 0.83, 0.60, 0.42],
                    'Pain':	        [1,	0.96, 0.90,	0.77, 0.55]}


def get_score(Vision, Hearing, Speech, Ambulation, Dexterity, Emotion, Cognition, Pain):
    """
    :param Vision
    :param Hearing
    :param Speech
    :param Ambulation
    :param Dexterity
    :param Emotion
    :param Cognition
    :param Pain
    :return: Score: utility score of chronic health status where dead has a utility of 0.00 and healthy has a utility of 1.00.
    """

    # ensure the entered health dimension levels are acceptable
    if not (Vision in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Vision level can take only 1, 2, 3, 4, 5 or 6')
    if not (Hearing in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Hearing level can take only 1, 2, 3, 4, 5 or 6')
    if not (Speech in [1, 2, 3, 4, 5]):
        raise ValueError('Speech level can take only 1, 2, 3, 4 or 5')
    if not (Ambulation in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Ambulation level can take only 1, 2, 3, 4, 5 or 6')
    if not (Dexterity in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Dexterity level can take only 1, 2, 3, 4, 5 or 6')
    if not (Emotion in [1, 2, 3, 4, 5]):
        raise ValueError('Emotion level can take only 1, 2, 3, 4 or 5')
    if not (Cognition in [1, 2, 3, 4, 5, 6]):
        raise ValueError('Cognition level can take only 1, 2, 3, 4, 5 or 6')
    if not (Pain in [1, 2, 3, 4, 5]):
        raise ValueError('Pain level can take only 1, 2, 3, 4, 5')

    count = 0
    for num in [Vision, Hearing, Speech, Ambulation, Dexterity, Emotion, Cognition, Pain]:
        if num == 1:
            count += 1


    if  count >= 7:
        print("HUI3 Single-Attribute Utility Function")
        score=1
        score *= SingCoefficients['Vision'][Vision - 1]
        score *= SingCoefficients['Hearing'][Hearing - 1]
        score *= SingCoefficients['Speech'][Speech - 1]
        score *= SingCoefficients['Ambulation'][Ambulation - 1]
        score *= SingCoefficients['Dexterity'][Dexterity - 1]
        score *= SingCoefficients['Emotion'][Emotion - 1]
        score *= SingCoefficients['Cognition'][Cognition - 1]
        score *= SingCoefficients['Pain'][Pain - 1]
    else:
        print("HUI3 Multi-Attribute Utility Function")
        score = C1
        score *= MultCoefficients['Vision'][Vision - 1]
        score *= MultCoefficients['Hearing'][Hearing - 1]
        score *= MultCoefficients['Speech'][Speech - 1]
        score *= MultCoefficients['Ambulation'][Ambulation - 1]
        score *= MultCoefficients['Dexterity'][Dexterity - 1]
        score *= MultCoefficients['Emotion'][Emotion - 1]
        score *= MultCoefficients['Cognition'][Cognition - 1]
        score *= MultCoefficients['Pain'][Pain - 1]
        score -= C2
    return score


print("Score for ", [2, 1, 1, 2, 1, 2, 1, 3])
print(get_score(2, 1, 1, 2, 1, 2, 1, 3))

print("Score for ", [1, 1, 1, 1, 1, 2, 1, 1])
print(get_score(1, 1, 1, 1, 1, 2, 1, 1))